"""Re-estima as marcações de palavra de assets/voice/NN.wav sem modelo de fala.

Detecta as pausas reais do áudio e as alinha (programação dinâmica, em ordem) às fronteiras de
pontuação do texto (vírgula, dois-pontos, ponto). Entre duas âncoras, as palavras são distribuídas
pelas sílabas. Uso: python3 -I tools/realign.py . [ids]
"""
import sys, os, re, json
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lines import LINES, SPOKEN

PUNCT_W = {",": 1.2, ":": 1.8, ";": 1.8, ".": 2.4, "?": 2.4, "!": 2.4}


def syl(w):
    return max(1, len(re.findall(r"[aeiouáéíóúâêôãõày]+", w.lower())))


def pauses(a, sr, min_len=0.11):
    hop = int(0.01 * sr)
    rms = np.array([np.sqrt(np.mean(a[i:i + hop] ** 2)) for i in range(0, len(a) - hop, hop)])
    thr = max(0.006, 0.08 * np.percentile(rms, 95))
    quiet = rms < thr
    voiced = np.where(~quiet)[0]
    s0, s1 = voiced[0] * 0.01, (voiced[-1] + 1) * 0.01
    out = []; i = voiced[0]
    while i <= voiced[-1]:
        if quiet[i]:
            j = i
            while quiet[j]: j += 1
            if (j - i) * 0.01 >= min_len: out.append((i * 0.01, j * 0.01))
            i = j
        else:
            i += 1
    return s0, s1, out


def align(text, a, sr):
    words = text.split()
    s0, s1, ps = pauses(a, sr)
    w = [syl(SPOKEN.get(x, x)) for x in words]
    bnd = [i for i, x in enumerate(words[:-1]) if x[-1] in PUNCT_W]
    # expected time of each boundary: syllables plus a pause allowance per punctuation mark
    tot = sum(w) + sum(PUNCT_W[words[i][-1]] for i in bnd)
    exp = []; acc = 0
    for i, x in enumerate(words[:-1]):
        acc += w[i]
        if i in bnd:
            exp.append(s0 + (s1 - s0) * (acc + PUNCT_W[x[-1]] / 2) / tot)
            acc += PUNCT_W[x[-1]]
    nb, npz = len(bnd), len(ps)
    INF = 1e9
    C = np.full((nb + 1, npz + 1), INF); B = {}
    C[0][0] = 0
    for j in range(nb + 1):
        for k in range(npz + 1):
            if C[j][k] >= INF: continue
            if j < nb:  # boundary without a detected pause
                c = C[j][k] + 0.5
                if c < C[j + 1][k]: C[j + 1][k] = c; B[(j + 1, k)] = (j, k, None)
            if k < npz:  # pause inside a phrase (breath, emphasis)
                L = ps[k][1] - ps[k][0]
                c = C[j][k] + 0.25 + 1.5 * L
                if c < C[j][k + 1]: C[j][k + 1] = c; B[(j, k + 1)] = (j, k, None)
            if j < nb and k < npz:
                mid = (ps[k][0] + ps[k][1]) / 2
                L = ps[k][1] - ps[k][0]
                c = C[j][k] + abs(exp[j] - mid) - 0.4 * L
                if c < C[j + 1][k + 1]: C[j + 1][k + 1] = c; B[(j + 1, k + 1)] = (j, k, k)
    j, k = nb, npz; match = {}
    while (j, k) != (0, 0):
        pj, pk, m = B[(j, k)]
        if m is not None: match[bnd[pj]] = ps[m]
        j, k = pj, pk
    # anchors: (word index range, time range) segments
    segs = []; start_i = 0; t = s0
    for i in sorted(match):
        segs.append((start_i, i, t, match[i][0])); start_i = i + 1; t = match[i][1]
    segs.append((start_i, len(words) - 1, t, s1))
    out = []
    for (i0, i1, t0, t1) in segs:
        ww = w[i0:i1 + 1]; tw = sum(ww) + sum(0.8 for x in words[i0:i1] if x[-1] in PUNCT_W)
        cur = t0
        for i in range(i0, i1 + 1):
            span = (t1 - t0) * w[i] / tw
            out.append({"text": words[i], "start": round(cur, 3), "end": round(cur + span, 3)})
            cur += span
            if i < i1 and words[i][-1] in PUNCT_W: cur += (t1 - t0) * 0.8 / tw
    return out, len(match), nb


if __name__ == "__main__":
    proj = sys.argv[1]
    only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    mp = os.path.join(proj, "audio_meta.json"); meta = json.load(open(mp))
    vs = {v["frame"]: v for v in meta["voices"]}
    for (lid, slug, title, text) in LINES:
        if only and lid not in only: continue
        a, sr = sf.read(os.path.join(proj, "assets/voice", f"{lid}.wav"), dtype="float32")
        if a.ndim > 1: a = a.mean(axis=1)
        words, m, nb = align(text, a, sr)
        vs[int(lid)]["words"] = [{"id": f"w{i}", **x} for i, x in enumerate(words)]
        vs[int(lid)]["duration_s"] = round(len(a) / sr, 3)
        print(lid, f"{m}/{nb} pontuações ancoradas", flush=True)
    meta["voices"] = [vs[k] for k in sorted(vs)]
    json.dump(meta, open(mp, "w"), ensure_ascii=False, indent=2)
