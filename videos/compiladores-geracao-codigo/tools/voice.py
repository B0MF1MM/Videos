"""Narração local com Piper pt_BR (via sherpa-onnx) + tempos por frase.

Uso: python3 -I tools/voice.py <dir-do-modelo-piper> [ids de cena...]
Lê SCRIPT.txt, gera assets/voice/<NN>.wav (44.1 kHz mono) e tools/timing.json
com o início de cada frase ("cue") e tempos aproximados por palavra para as legendas.
"""
import glob, json, os, re, subprocess, sys
import numpy as np
import sherpa_onnx
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = sys.argv[1]
ONLY = set(sys.argv[2:])
SR = 22050
GAP = 0.32      # silêncio entre frases
LEAD = 0.15     # silêncio no início da cena
SPEED = 1.06


def parse(path):
    scenes = []
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m = re.match(r"^# (\d\d-[\w-]+)\s*$", line)
        if m:
            scenes.append({"id": m.group(1), "segs": []})
            continue
        m = re.match(r"^([a-z]): (.+)$", line)
        if m and scenes:
            cap, _, say = m.group(2).partition(" || ")
            scenes[-1]["segs"].append({"cue": m.group(1), "cap": cap.strip(), "say": (say or cap).strip()})
    return scenes


def voiced_bounds(x):
    env = np.abs(x)
    win = int(SR * 0.02)
    e = np.convolve(env, np.ones(win) / win, mode="same")
    idx = np.where(e > 0.02 * e.max())[0]
    if not len(idx):
        return 0, len(x)
    return idx[0], idx[-1]


model = glob.glob(os.path.join(MODEL_DIR, "*.onnx"))[0]
tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(
    model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(
            model=model, tokens=os.path.join(MODEL_DIR, "tokens.txt"),
            data_dir=os.path.join(MODEL_DIR, "espeak-ng-data"),
            noise_scale=0.667, noise_scale_w=0.8, length_scale=1.0),
        num_threads=8),
    max_num_sentences=1))

scenes = parse(os.path.join(ROOT, "SCRIPT.txt"))
tpath = os.path.join(ROOT, "tools", "timing.json")
timing = json.load(open(tpath)) if os.path.exists(tpath) else {}

for sc in scenes:
    if ONLY and sc["id"] not in ONLY:
        continue
    pieces = [np.zeros(int(SR * LEAD), dtype=np.float32)]
    t = LEAD
    cues, words = {}, []
    for seg in sc["segs"]:
        a = tts.generate(seg["say"], sid=0, speed=SPEED)
        x = np.asarray(a.samples, dtype=np.float32)
        s0, s1 = voiced_bounds(x)
        x = x[max(0, s0 - int(SR * 0.03)): s1 + int(SR * 0.06)]
        dur = len(x) / SR
        cues[seg["cue"]] = round(t, 3)
        # palavras da legenda: tempo proporcional ao tamanho (aproximação)
        ws = seg["cap"].split()
        weights = [len(w) + 2 for w in ws]
        tot = float(sum(weights))
        acc = 0.0
        for w, wt in zip(ws, weights):
            st = t + dur * acc / tot
            acc += wt
            words.append({"text": w, "start": round(st, 3), "end": round(t + dur * acc / tot, 3), "cue": seg["cue"]})
        pieces.append(x)
        pieces.append(np.zeros(int(SR * GAP), dtype=np.float32))
        t += dur + GAP
    y = np.concatenate(pieces[:-1])
    peak = np.abs(y).max()
    y = y / peak * 0.89
    num = sc["id"][:2]
    tmp = os.path.join(ROOT, "tools", "_tmp.wav")
    sf.write(tmp, y, SR)
    out = os.path.join(ROOT, "assets", "voice", num + ".wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-ar", "44100", "-ac", "1", out], check=True)
    os.remove(tmp)
    timing[sc["id"]] = {"voice": "assets/voice/%s.wav" % num, "duration": round(len(y) / SR, 3), "cues": cues, "words": words}
    print(sc["id"], timing[sc["id"]]["duration"], cues)

json.dump(timing, open(tpath, "w"), ensure_ascii=False, indent=1)
