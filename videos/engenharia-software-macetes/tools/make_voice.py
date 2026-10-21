"""Gera a narração (assets/voice/NN.wav) e as marcações de palavra em audio_meta.json.

Provedores:
  piper  — local (sherpa-onnx + modelo vits-piper-pt_BR-faber-medium do GitHub k2-fsa/sherpa-onnx, tag tts-models)
  gemini — Gemini TTS (precisa de GEMINI_API_KEY no ambiente)

Uso:
  python3 -I tools/make_voice.py . piper  <dir-do-modelo-piper> [speed] [ids]
  python3 -I tools/make_voice.py . gemini <voz, ex: Charon>     [modelo, padrão gemini-3.8-flash-tts] [ids]

Depois: python3 -I tools/gen_frames.py .  (re-sincroniza as animações com a nova fala), e o fluxo
sync-durations → captions → assemble-index → transitions (ver tools/README.md).
"""
import sys, re, json, os, io, time, subprocess, base64, urllib.request, urllib.error
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lines import LINES, SPOKEN

proj, provider = sys.argv[1], sys.argv[2]
arg3 = sys.argv[3] if len(sys.argv) > 3 else None
arg4 = sys.argv[4] if len(sys.argv) > 4 else None
only = set(sys.argv[5].split(",")) if len(sys.argv) > 5 else None
TMP = os.path.join(proj, ".hyperframes", "voice-tmp"); os.makedirs(TMP, exist_ok=True)


def syl(w):
    return max(1, len(re.findall(r"[aeiouáéíóúâêôãõày]+", w.lower())))


def trim(a, sr, thr=0.01):
    idx = np.where(np.abs(a) > thr)[0]
    return a[:0] if len(idx) == 0 else a[max(0, idx[0] - int(0.01 * sr)): idx[-1] + int(0.03 * sr)]


def spread(disp, t0, dur):
    """Distribute a sentence's words over [t0, t0+dur] by syllables, leaving room after commas."""
    wts = [syl(SPOKEN.get(w, w)) + (0.9 if w.endswith(",") else 0) for w in disp]
    tot = sum(wts); cur = t0; out = []
    for w, wt in zip(disp, wts):
        span = dur * wt / tot
        pause = dur * 0.9 / tot if w.endswith(",") else 0
        out.append({"text": w, "start": round(cur, 3), "end": round(cur + span - pause, 3)})
        cur += span
    return out


def sentences(text):
    return [s for s in re.split(r"(?<=[.?!:])\s+", text) if s.strip()]


if provider == "piper":
    import sherpa_onnx
    model_dir = arg3; speed = float(arg4 or 1.07)
    name = model_dir.rstrip("/").split("vits-piper-")[1]
    tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=f"{model_dir}/{name}.onnx", tokens=f"{model_dir}/tokens.txt",
                                                   data_dir=f"{model_dir}/espeak-ng-data"), num_threads=4)))
    SR = tts.sample_rate

    def synth_line(text):
        chunks = [np.zeros(int(0.08 * SR), dtype=np.float32)]; words = []; t = 0.08
        for s in sentences(text):
            disp = s.split()
            a = trim(np.array(tts.generate(" ".join(SPOKEN.get(w, w) for w in disp), sid=0, speed=speed).samples, dtype=np.float32), SR)
            words += spread(disp, t, len(a) / SR)
            chunks.append(a); t += len(a) / SR
            gap = 0.32 if s.endswith((".", "?", "!")) else 0.18
            chunks.append(np.zeros(int(gap * SR), dtype=np.float32)); t += gap
        return np.concatenate(chunks), SR, words

elif provider == "gemini":
    KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not KEY:
        sys.exit("GEMINI_API_KEY não está definida")
    voice = arg3 or "Charon"; model = arg4 or "gemini-3.8-flash-tts"

    def synth_line(text):
        spoken = " ".join(SPOKEN.get(w, w) for w in text.split())
        body = {"contents": [{"parts": [{"text": spoken}]}],
                "generationConfig": {"responseModalities": ["AUDIO"],
                                     "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
        # the key goes in the query string: header auth is refused for some key types
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={KEY}"
        for attempt in range(6):
            try:
                req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
                r = json.load(urllib.request.urlopen(req, timeout=180))
                if "content" in r["candidates"][0]: break
                if attempt == 5: raise RuntimeError(f"sem áudio: {r['candidates'][0].get('finishReason')}")
            except urllib.error.HTTPError as e:
                # 403/429 show up transiently under the free tier's per-minute limit
                if e.code not in (403, 429, 500, 503) or attempt == 5: raise
            time.sleep(20 * (attempt + 1))
        part = r["candidates"][0]["content"]["parts"][0]["inlineData"]
        raw = base64.b64decode(part["data"])
        if raw[:4] == b"RIFF":  # 3.8 returns a complete WAV
            a, sr = sf.read(io.BytesIO(raw), dtype="float32")
            if a.ndim > 1: a = a.mean(axis=1)
        else:  # older models: raw 16-bit PCM
            sr = int(re.search(r"rate=(\d+)", part.get("mimeType", "rate=24000")).group(1))
            a = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
        a = np.concatenate([np.zeros(int(0.08 * sr), dtype=np.float32), trim(a, sr)])
        # sentence boundaries = the longest silences, in order; words spread inside each sentence
        ss = sentences(text); env = np.abs(a); hop = int(0.01 * sr)
        quiet = np.array([env[i:i + hop].max() < 0.02 for i in range(0, len(a) - hop, hop)])
        gaps = []; i = 0
        while i < len(quiet):
            if quiet[i]:
                j = i
                while j < len(quiet) and quiet[j]: j += 1
                if j - i >= 15 and i > 10: gaps.append(((j - i), i * 0.01, j * 0.01))
                i = j
            else:
                i += 1
        cut = sorted(sorted(gaps, reverse=True)[:len(ss) - 1], key=lambda g: g[1])
        bounds = [0.08] + [g[1] for g in cut] if len(cut) == len(ss) - 1 else None
        ends = [g[1] for g in cut] + [len(a) / sr] if bounds else None
        starts = [0.08] + [g[2] for g in cut] if bounds else None
        words = []
        if bounds:
            for s, t0, t1 in zip(ss, starts, ends): words += spread(s.split(), t0, t1 - t0)
        else:
            words = spread(text.split(), 0.08, len(a) / sr - 0.08)
        return a, sr, words
else:
    sys.exit("provider: piper | gemini")

meta_path = os.path.join(proj, "audio_meta.json")
meta = json.load(open(meta_path))
voices = {v["frame"]: v for v in meta["voices"]}
for (lid, slug, title, text) in LINES:
    if only and lid not in only: continue
    audio, sr, words = synth_line(text)
    tmp = os.path.join(TMP, f"{lid}.wav"); sf.write(tmp, audio, sr)
    out = os.path.join(proj, "assets/voice", f"{lid}.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "44100", "-ac", "1", out], check=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout)
    voices[int(lid)] = {"frame": int(lid), "path": f"assets/voice/{lid}.wav", "duration_s": round(d, 3),
                        "words": [{"id": f"w{i}", **w} for i, w in enumerate(words)]}
    print(lid, round(d, 2), "s", flush=True)
    meta["voices"] = [voices[k] for k in sorted(voices)]
    json.dump(meta, open(meta_path, "w"), ensure_ascii=False, indent=2)  # after every line, so a failure can resume
print("total", round(sum(v["duration_s"] for v in meta["voices"]), 1))
