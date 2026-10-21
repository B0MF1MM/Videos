#!/usr/bin/env python3
"""Edit de highlight de Valorant sincronizado com a batida.

Uso: python3 render.py <pasta_dos_clipes> <musica.mp3> <saida.mp4> [--preview]

Toda a montagem (cortes, rampas de velocidade, abates, letra) vem de edit.json.
"""
import json, math, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1280, 720, 30
OUT_W, OUT_H = 1920, 1080
FONT = os.path.join(HERE, 'assets', 'Anton-Regular.ttf')

cfg = json.load(open(os.path.join(HERE, 'edit.json'), encoding='utf-8'))
clip_dir, music, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
preview = '--preview' in sys.argv
BEAT = 60 / cfg['bpm']
DROP = cfg['drop']
SEGS = cfg['segments']
KILLS = cfg['kills']
DUR = SEGS[-1]['end']
CUTS = [s['start'] for s in SEGS[1:]]
rng = np.random.default_rng(7)


def clip_path(key):
    name = cfg['clips'][key]
    for f in os.listdir(clip_dir):
        if f.endswith(name):
            return os.path.join(clip_dir, f)
    raise FileNotFoundError(name)


def src_time(seg, t):
    a = seg['anchors']
    if t <= a[0][0]:
        return a[0][1] + (t - a[0][0])
    for (m0, s0), (m1, s1) in zip(a, a[1:]):
        if t <= m1:
            return s0 + (s1 - s0) * (t - m0) / (m1 - m0)
    return a[-1][1] + (t - a[-1][0])


class Source:
    """Decodifica o trecho do clipe usado por um segmento e entrega quadros com blend (câmera lenta suave)."""

    def __init__(self, seg):
        path = clip_path(seg['clip'])
        ts = [src_time(seg, seg['start'] + i / FPS) for i in range(int(round((seg['end'] - seg['start']) * FPS)) + 1)]
        self.t0 = max(0.0, min(ts) - 0.1)
        t1 = max(ts) + 0.1
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{self.t0:.3f}', '-i', path, '-t', f'{t1 - self.t0:.3f}',
                              '-vf', f'scale={W}:{H}:flags=lanczos', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True, check=True).stdout
        self.frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
        fr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=r_frame_rate',
                             '-of', 'csv=p=0', path], capture_output=True, text=True).stdout.strip().split('/')
        self.fps = float(fr[0]) / float(fr[1])

    def get(self, s):
        x = (s - self.t0) * self.fps
        i = int(np.clip(math.floor(x), 0, len(self.frames) - 1))
        j = min(i + 1, len(self.frames) - 1)
        f = x - math.floor(x)
        a = self.frames[i].astype(np.float32) / 255
        if f < 0.05 or i == j:
            return a
        return a * (1 - f) + self.frames[j].astype(np.float32) / 255 * f


# ---------- grade ----------
def grade(img, t):
    if t < DROP:
        # frio, azul/ciano, levemente dessaturado (como o começo da referência)
        g = img.mean(2, keepdims=True)
        img = g + (img - g) * 0.8
        img = img * np.array([0.88, 1.0, 1.12], np.float32) + np.array([0.0, 0.01, 0.03], np.float32)
        img = np.clip((img - 0.5) * 1.12 + 0.5, 0, 1)
    else:
        # quente, rosa/magenta saturado depois do drop
        g = img.mean(2, keepdims=True)
        img = g + (img - g) * 1.2
        img = img * np.array([1.05, 0.97, 1.04], np.float32) + np.array([0.01, 0.0, 0.015], np.float32)
        img = np.clip((img - 0.5) * 1.18 + 0.5, 0, 1)
        bright = np.clip(img - 0.62, 0, 1)
        bloom = cv2.GaussianBlur(bright, (0, 0), 18)
        img = img + bloom * np.array([0.9, 0.6, 0.85], np.float32)
    return np.clip(img, 0, 1)


# ---------- curvas de impacto ----------
KICKS = []
k = DROP
while k < DUR:
    KICKS.append(k)
    k += BEAT


def impact(t):
    """zoom extra, tremida, rgb split e flash em cada abate; pulso leve em cada batida."""
    z = sh = rgb = fl = 0.0
    for kt in KILLS:
        d = t - kt
        if 0 <= d < 0.6:
            e = math.exp(-d / 0.11)
            z += 0.13 * e
            sh += 22 * math.exp(-d / 0.16)
            rgb += 9 * e
            fl += (0.85 if kt == DROP else 0.35) * math.exp(-d / 0.07)
    if t >= DROP:
        for kt in KICKS:
            d = t - kt
            if 0 <= d < 0.3:
                z += 0.03 * math.exp(-d / 0.08)
                rgb += 2.5 * math.exp(-d / 0.08)
    # subida antes do drop: zoom crescente + tremida
    if DROP - 0.95 <= t < DROP:
        p = (t - (DROP - 0.95)) / 0.95
        z += 0.22 * p ** 2
        sh += 10 * p ** 2
        rgb += 6 * p ** 2
    return z, sh, rgb, fl


def camera(img, z, sh):
    dx, dy = (rng.uniform(-1, 1, 2) * sh) if sh > 0.3 else (0, 0)
    s = 1 + z
    M = np.float32([[s, 0, (1 - s) * W / 2 + dx], [0, s, (1 - s) * H / 2 + dy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def rgb_split(img, d):
    if d < 0.5:
        return img
    d = int(round(d))
    out = img.copy()
    out[:, d:, 0] = img[:, :-d, 0]
    out[:, :-d, 2] = img[:, d:, 2]
    return out


def whip(img, t):
    """transição de chicote: borrão direcional forte perto de cada corte."""
    best = None
    for i, c in enumerate(CUTS):
        d = t - c
        if -3 / FPS <= d < 3 / FPS:
            best = (d, i)
    if best is None:
        return img
    d, i = best
    amt = 1 - abs(d) / (3 / FPS)
    L = int(10 + 110 * amt)
    vertical = i % 2 == 1
    k = np.zeros((L, L), np.float32)
    if vertical:
        k[:, L // 2] = 1 / L
    else:
        k[L // 2, :] = 1 / L
    out = cv2.filter2D(img, -1, k, borderType=cv2.BORDER_REFLECT)
    shift = int((-1 if d < 0 else 1) * 160 * amt) * (-1 if i % 4 >= 2 else 1)
    M = np.float32([[1, 0, 0 if vertical else shift], [0, 1, shift if vertical else 0]])
    return cv2.warpAffine(out, M, (W, H), borderMode=cv2.BORDER_REFLECT)


# ---------- texto ----------
_fonts = {}


def font(sz):
    if sz not in _fonts:
        _fonts[sz] = ImageFont.truetype(FONT, sz)
    return _fonts[sz]


def text_layer(word_list, size, tracking=0, pop=None):
    """renderiza palavras centralizadas em RGBA float; pop=(índice, escala) faz a palavra nova 'saltar'."""
    f = font(size)
    widths = [f.getlength(w) + tracking * len(w) for w in word_list]
    space = size * 0.28
    total = sum(widths) + space * (len(word_list) - 1)
    layer = Image.new('L', (W, size * 2), 0)
    d = ImageDraw.Draw(layer)
    base = size * 1.45
    x = (W - total) / 2
    for idx, (w, wd) in enumerate(zip(word_list, widths)):
        sc = pop[1] if pop and pop[0] == idx else 1.0
        if sc != 1.0:
            # palavra nova cresce a partir do próprio centro, sem empurrar as vizinhas
            d.text((x + wd / 2, base - size * 0.5 * (1 - sc)), w, font=font(max(8, int(size * sc))),
                   fill=int(255 * min(1.0, 2.2 - sc)), anchor='ms')
        else:
            cx = x
            for ch in w:
                d.text((cx, base), ch, font=f, fill=255, anchor='ls')
                cx += f.getlength(ch) + tracking
        x += wd + space
    return np.asarray(layer, np.float32) / 255


def composite_text(img, mask, y, glow_rgb, alpha=1.0, glow=1.0):
    h = mask.shape[0]
    y0 = int(y - h / 2)
    a0, a1 = max(0, y0), min(H, y0 + h)
    m = mask[a0 - y0:a1 - y0] * alpha
    g = cv2.GaussianBlur(m, (0, 0), 9) * 1.6 * glow
    region = img[a0:a1]
    region += g[..., None] * np.array(glow_rgb, np.float32)
    region[:] = region * (1 - m[..., None]) + m[..., None] * 1.0
    img[a0:a1] = np.clip(region, 0, 1)


def perspective(mask, angle_deg, tilt=0.0):
    """inclinação 3D simples (rotação no eixo Y) da camada de texto."""
    h, w = mask.shape
    a = math.radians(angle_deg)
    f = w * 1.2
    def proj(x, y):
        X = (x - w / 2) * math.cos(a)
        Z = (x - w / 2) * math.sin(a)
        s = f / (f + Z)
        return w / 2 + X * s, h / 2 + (y - h / 2) * s + tilt * (x - w / 2)
    src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst = np.float32([proj(0, 0), proj(w, 0), proj(w, h), proj(0, h)])
    return cv2.warpPerspective(mask, cv2.getPerspectiveTransform(src, dst), (w, h))


LY = cfg['lyrics']
for i, l in enumerate(LY):
    l['end'] = LY[i + 1]['t'] if i + 1 < len(LY) else DUR
    words = l['text'].split()
    l['words'] = words
    span = (l['end'] - l['t']) * 0.7
    step = BEAT / 2
    l['wt'] = [l['t'] + round(span * j / max(1, len(words)) / step) * step for j in range(len(words))]


def draw_text(img, t):
    for l in LY:
        if not (l['t'] <= t < l['end']):
            continue
        hook = l.get('hook')
        post = t >= DROP
        glow_col = (1.0, 0.25, 0.6) if post else (0.25, 0.7, 1.0)
        # legenda palavra por palavra
        shown = [w for w, wt in zip(l['words'], l['wt']) if t >= wt]
        if shown:
            last_t = l['wt'][len(shown) - 1]
            dt = t - last_t
            sc = 1 + 0.3 * math.exp(-dt / 0.05) if dt < 0.2 else 1.0
            size = 62 if post else 54
            y = 600 if not hook else 640
            fade = min(1.0, (l['end'] - t) / 0.08)
            m = text_layer(shown, size, tracking=2, pop=(len(shown) - 1, sc))
            composite_text(img, m, y, glow_col, alpha=fade)
        # palavra-tema grande em 3D (como o "UNTOUCHABLE" da referência)
        if hook:
            p = (t - l['t']) / (l['end'] - l['t'])
            n = len(hook)
            reveal = max(1, min(n, int(n * min(1.0, p / 0.55)) + 1))
            txt = hook[:reveal]
            track = int(6 + 26 * p)
            m = text_layer([txt], 128, tracking=track)
            ang = -28 + 40 * p
            m = perspective(m, ang, tilt=0.04 * math.sin(p * 3))
            out_fade = min(1.0, (l['end'] - t) / 0.1)
            composite_text(img, m, H / 2 - 30, glow_col, alpha=0.95 * out_fade, glow=1.4)
        break


def letterbox(img, t):
    for s in SEGS:
        lb = s.get('letterbox')
        if lb and lb[0] <= t < lb[1] + 0.12:
            p = min(1.0, (t - lb[0]) / 0.15) if t < lb[1] else max(0.0, 1 - (t - lb[1]) / 0.12)
            bar = int(95 * p)
            img[:bar] = 0
            img[H - bar:] = 0
            g = img.mean(2, keepdims=True)
            img[:] = g + (img - g) * (1 - 0.55 * p)
    return img


VIG = None


def vignette(img):
    global VIG
    if VIG is None:
        y, x = np.mgrid[0:H, 0:W]
        r = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H / 2) / (H / 2)) ** 2)
        VIG = np.clip(1 - 0.35 * np.clip(r - 0.55, 0, 1) ** 1.5, 0, 1).astype(np.float32)[..., None]
    return img * VIG


def render_video(tmp_video):
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', f'scale={OUT_W}:{OUT_H}:flags=lanczos,unsharp=5:5:0.4',
                            '-c:v', 'libx264', '-preset', 'ultrafast' if preview else 'medium', '-crf', '18',
                            '-pix_fmt', 'yuv420p', tmp_video], stdin=subprocess.PIPE)
    nframes = int(round(DUR * FPS))
    seg_i, src = -1, None
    for fi in range(nframes):
        t = fi / FPS
        while seg_i + 1 < len(SEGS) and t >= SEGS[seg_i + 1]['start']:
            seg_i += 1
            src = Source(SEGS[seg_i])
            print(f'segmento {seg_i + 1}/{len(SEGS)} ({SEGS[seg_i]["clip"]})', flush=True)
        seg = SEGS[seg_i]
        img = src.get(src_time(seg, t))
        img = grade(img, t)
        z, sh, rgb, fl = impact(t)
        img = camera(img, z, sh)
        img = whip(img, t)
        img = rgb_split(img, rgb)
        img = letterbox(img, t)
        img = vignette(img)
        draw_text(img, t)
        if fl > 0:
            img = img + fl * (1 - img)
        if t < 0.5:
            img = img * (t / 0.5)
        if t > DUR - 0.6:
            img = img * max(0.0, (DUR - t) / 0.6)
        enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
    enc.stdin.close()
    enc.wait()


def render_audio(tmp_audio):
    """música + tiro/som de abate original de cada jogada, alinhados no tempo da música."""
    inputs = ['-i', music]
    filt = ['[0:a]aresample=48000,volume=1.0,afade=t=out:st=%.2f:d=0.6[m]' % (DUR - 0.6)]
    labels = ['[m]']
    for i, g in enumerate(cfg['game_audio']):
        inputs += ['-ss', f'{max(0, g["src"] - 0.05):.3f}', '-t', '0.7', '-i', clip_path(g['clip'])]
        delay = int(max(0, g['at'] - 0.05) * 1000)
        filt.append(f'[{i + 1}:a]aresample=48000,volume=0.55,afade=t=out:st=0.45:d=0.25,adelay={delay}|{delay}[g{i}]')
        labels.append(f'[g{i}]')
    filt.append(''.join(labels) + f'amix=inputs={len(labels)}:normalize=0,atrim=0:{DUR},alimiter=limit=0.95[a]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(filt), '-map', '[a]',
                    '-c:a', 'aac', '-b:a', '256k', tmp_audio], check=True)


if __name__ == '__main__':
    tv, ta = out_path + '.v.mp4', out_path + '.a.m4a'
    render_audio(ta)
    render_video(tv)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tv, '-i', ta, '-c', 'copy', '-shortest',
                    '-movflags', '+faststart', out_path], check=True)
    os.remove(tv)
    os.remove(ta)
    print('ok ->', out_path)
