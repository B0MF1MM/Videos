#!/usr/bin/env python3
"""Edit de highlight de Valorant sincronizado com a batida (v2).

Uso: python3 render.py <pasta_dos_clipes> <musica.mp3> <saida.mp4> [--preview] [--from T --to T]

Toda a montagem (cortes, rampas de velocidade, abates, letra, transições) vem de edit.json.
Efeitos:
  - câmera lenta com interpolação por optical flow (estilo Twixtor)
  - motion blur pelo movimento real da imagem (estilo RSMB)
  - partículas: faíscas e brasas nos abates, poeira/brasas ambientes, texto que se desfaz em partículas
  - onda de choque com refração, zoom radial, impact frames invertidos, glitch
  - texto 3D atrás do cenário usando profundidade estimada pelo MiDaS
  - flares anamórficos, bloom, light leaks, linhas de velocidade, granulação de filme
"""
import json, math, os, subprocess, sys, urllib.request
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1280, 720, 30
OUT_W, OUT_H = 1920, 1080
CX, CY = W / 2, H / 2
FONT = os.path.join(HERE, 'assets', 'Anton-Regular.ttf')
MIDAS = os.path.join(HERE, 'assets', 'models', 'midas_small.onnx')
MIDAS_URL = 'https://github.com/isl-org/MiDaS/releases/download/v2_1/model-small.onnx'

cfg = json.load(open(os.path.join(HERE, 'edit.json'), encoding='utf-8'))
args = sys.argv[1:]
clip_dir, music, out_path = args[0], args[1], args[2]
preview = '--preview' in args
T_FROM = float(args[args.index('--from') + 1]) if '--from' in args else 0.0
T_TO = float(args[args.index('--to') + 1]) if '--to' in args else None
BEAT = 60 / cfg['bpm']
DROP = cfg['drop']
SEGS = cfg['segments']
KILLS = cfg['kills']
IMPACTS = cfg.get('impact_frames', [])
DUR = SEGS[-1]['end']
CUTS = [s['start'] for s in SEGS[1:]]
TRANS = cfg.get('transitions', ['whip'] * len(CUTS))
rng = np.random.default_rng(7)

GX, GY = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
RAD = np.sqrt((GX - CX) ** 2 + (GY - CY) ** 2)
ANG_X, ANG_Y = (GX - CX) / (RAD + 1e-3), (GY - CY) / (RAD + 1e-3)


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


def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


# ================= fonte de vídeo com optical flow =================
DIS = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)


class Source:
    def __init__(self, seg):
        path = clip_path(seg['clip'])
        n = int(round((seg['end'] - seg['start']) * FPS)) + 2
        ts = [src_time(seg, seg['start'] + i / FPS) for i in range(n)]
        self.t0 = max(0.0, min(ts) - 0.15)
        t1 = max(ts) + 0.15
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{self.t0:.3f}', '-i', path, '-t', f'{t1 - self.t0:.3f}',
                              '-vf', f'scale={W}:{H}:flags=lanczos', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True, check=True).stdout
        self.frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
        fr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=r_frame_rate',
                             '-of', 'csv=p=0', path], capture_output=True, text=True).stdout.strip().split('/')
        self.fps = float(fr[0]) / float(fr[1])
        self.flows = {}

    def flow(self, i, j):
        """fluxo i->j em resolução cheia (calculado em meia resolução)."""
        if (i, j) not in self.flows:
            a = cv2.cvtColor(cv2.resize(self.frames[i], (W // 2, H // 2)), cv2.COLOR_RGB2GRAY)
            b = cv2.cvtColor(cv2.resize(self.frames[j], (W // 2, H // 2)), cv2.COLOR_RGB2GRAY)
            f = DIS.calc(a, b, None)
            self.flows[(i, j)] = cv2.resize(f, (W, H)) * 2
        return self.flows[(i, j)]

    def get(self, s, rate):
        """quadro no tempo s; interpola com optical flow e aplica motion blur proporcional à velocidade."""
        x = (s - self.t0) * self.fps
        last = len(self.frames) - 1
        i = int(np.clip(math.floor(x), 0, last - 1))
        j = i + 1
        f = float(np.clip(x - i, 0, 1))
        A = self.frames[i].astype(np.float32) / 255
        B = self.frames[j].astype(np.float32) / 255
        fab = self.flow(i, j)
        if f < 0.04:
            img = A
        elif f > 0.96:
            img = B
        else:
            fba = self.flow(j, i)
            wa = cv2.remap(A, GX + f * fba[..., 0], GY + f * fba[..., 1], cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
            wb = cv2.remap(B, GX + (1 - f) * fab[..., 0], GY + (1 - f) * fab[..., 1], cv2.INTER_LINEAR,
                           borderMode=cv2.BORDER_REFLECT)
            img = wa * (1 - f) + wb * f
        # motion blur: obturador de 180° no tempo de saída
        shutter = 0.5 * rate
        mag = np.abs(fab).mean() * shutter
        if mag > 1.2:
            n = int(min(10, 3 + mag / 3))
            acc = np.zeros_like(img)
            for k in range(n):
                o = (k / (n - 1) - 0.5) * shutter
                acc += cv2.remap(img, GX - o * fab[..., 0], GY - o * fab[..., 1], cv2.INTER_LINEAR,
                                 borderMode=cv2.BORDER_REFLECT)
            img = acc / n
        return img


# ================= profundidade (MiDaS) =================
_midas = None
_depth_ema = None


def depth(img):
    """mapa de profundidade relativo 0..1 (1 = perto), suavizado no tempo."""
    global _midas, _depth_ema
    if _midas is None:
        import onnxruntime as ort
        if not os.path.exists(MIDAS):
            os.makedirs(os.path.dirname(MIDAS), exist_ok=True)
            urllib.request.urlretrieve(MIDAS_URL, MIDAS)
        _midas = ort.InferenceSession(MIDAS, providers=['CPUExecutionProvider'])
    x = cv2.resize(img, (256, 256))
    x = (x - np.array([0.485, 0.456, 0.406], np.float32)) / np.array([0.229, 0.224, 0.225], np.float32)
    d = _midas.run(None, {_midas.get_inputs()[0].name: x.transpose(2, 0, 1)[None].astype(np.float32)})[0][0]
    d = (d - np.percentile(d, 2)) / (np.percentile(d, 98) - np.percentile(d, 2) + 1e-6)
    d = cv2.resize(np.clip(d, 0, 1), (W, H))
    _depth_ema = d if _depth_ema is None else _depth_ema * 0.5 + d * 0.5
    return _depth_ema


# ================= grade / luz =================
def grade(img, t):
    g = img.mean(2, keepdims=True)
    if t < DROP:
        img = g + (img - g) * 0.78
        img = img * np.array([0.86, 1.0, 1.14], np.float32) + np.array([0.0, 0.01, 0.035], np.float32)
        img = np.clip((img - 0.5) * 1.14 + 0.5, 0, 1)
    else:
        img = g + (img - g) * 1.25
        img = img * np.array([1.04, 0.97, 1.04], np.float32) + np.array([0.012, 0.0, 0.02], np.float32)
        img = np.clip((img - 0.5) * 1.28 + 0.5, 0, 1)
        # sombras puxadas para roxo/azul, altas para rosa (split toning)
        lum = img.mean(2, keepdims=True)
        img = img + (1 - lum) * np.array([0.0, -0.01, 0.04], np.float32) + lum * np.array([0.03, 0.0, 0.01], np.float32)
    return np.clip(img, 0, 1)


def bloom_and_streaks(img, t):
    small = cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
    lum = small.max(2)
    hl = np.clip((lum - 0.8) * 4, 0, 1)[..., None] * small
    bloom = cv2.GaussianBlur(hl, (0, 0), 6) * 0.55 + cv2.GaussianBlur(hl, (0, 0), 16) * 0.45
    streak = cv2.blur(np.clip((lum - 0.88) * 8, 0, 1), (81, 1))
    streak = cv2.blur(streak, (41, 1))
    tint = np.array([1.0, 0.35, 0.85] if t >= DROP else [0.35, 0.75, 1.0], np.float32)
    add = bloom + streak[..., None] * tint * 2.2
    return np.clip(img + cv2.resize(add, (W, H)), 0, 1.4)


# ================= curvas de impacto =================
KICKS = []
_k = DROP
while _k < DUR:
    KICKS.append(_k)
    _k += BEAT


def impact(t):
    z = sh = rgb = fl = rot = 0.0
    for kt in KILLS:
        d = t - kt
        if 0 <= d < 0.7:
            e = math.exp(-d / 0.11)
            z += 0.14 * e
            sh += 26 * math.exp(-d / 0.15)
            rot += 1.6 * math.exp(-d / 0.15)
            rgb += 11 * e
            fl += (0.9 if kt == DROP else 0.4) * math.exp(-d / 0.06)
        elif -0.12 <= d < 0:   # puxada para dentro um instante antes do tiro
            z -= 0.04 * (1 + d / 0.12)
    if t >= DROP:
        for kt in KICKS:
            d = t - kt
            if 0 <= d < 0.3:
                z += 0.035 * math.exp(-d / 0.07)
                rgb += 3 * math.exp(-d / 0.07)
    for a, b in ((DROP - 0.95, DROP), (13.95, 14.63)):
        if a <= t < b:
            p = (t - a) / (b - a)
            z += 0.24 * p ** 2
            sh += 9 * p ** 2
            rgb += 7 * p ** 2
    return z, sh, rgb, fl, rot


def camera(img, z, sh, rot):
    if sh > 0.3:
        dx, dy = rng.uniform(-1, 1, 2) * sh
        ang = rng.uniform(-1, 1) * rot
    else:
        dx = dy = ang = 0.0
    M = cv2.getRotationMatrix2D((CX, CY), ang, 1 + z)
    M[0, 2] += dx
    M[1, 2] += dy
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def rgb_split(img, d):
    if d < 0.6:
        return img
    # aberração cromática radial (mais forte nas bordas)
    s = d / 600
    out = img.copy()
    out[..., 0] = cv2.remap(img[..., 0], CX + (GX - CX) * (1 + s), CY + (GY - CY) * (1 + s), cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_REFLECT)
    out[..., 2] = cv2.remap(img[..., 2], CX + (GX - CX) * (1 - s), CY + (GY - CY) * (1 - s), cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_REFLECT)
    return out


def radial_blur(img, strength, n=8):
    if strength < 0.005:
        return img
    acc = np.zeros_like(img)
    for k in range(n):
        s = 1 + strength * k / (n - 1)
        M = np.float32([[s, 0, (1 - s) * CX], [0, s, (1 - s) * CY]])
        acc += cv2.warpAffine(img, M, (W, H), borderMode=cv2.BORDER_REFLECT)
    return acc / n


def shockwave(img, t):
    for kt in KILLS:
        d = t - kt
        if 0 <= d < 0.5:
            r = 80 + d * 2400
            wdt = 70 + d * 120
            amp = 26 * (1 - d / 0.5) ** 1.5 * (1.6 if kt == DROP else 1.0)
            x = (RAD - r) / wdt
            prof = np.where(np.abs(x) < 1, np.sin(x * math.pi) * (1 - np.abs(x)), 0).astype(np.float32)
            disp = prof * amp
            img = cv2.remap(img, GX - ANG_X * disp, GY - ANG_Y * disp, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
            img = img + (np.abs(prof) * 0.12 * (1 - d / 0.5))[..., None]
    return img


def transition(img, t):
    for i, c in enumerate(CUTS):
        d = t - c
        if not (-4 / FPS <= d < 4 / FPS):
            continue
        amt = 1 - abs(d) / (4 / FPS)
        kind = TRANS[i % len(TRANS)]
        if kind == 'whip':
            L = int(10 + 140 * amt)
            k = np.zeros((L, L), np.float32)
            vertical = i % 2 == 1
            if vertical:
                k[:, L // 2] = 1 / L
            else:
                k[L // 2, :] = 1 / L
            img = cv2.filter2D(img, -1, k, borderType=cv2.BORDER_REFLECT)
            shift = (-1 if d < 0 else 1) * 220 * amt
            M = np.float32([[1, 0, 0 if vertical else shift], [0, 1, shift if vertical else 0]])
            img = cv2.warpAffine(img, M, (W, H), borderMode=cv2.BORDER_REFLECT)
        elif kind == 'zoom':
            # sai crescendo, entra vindo de dentro
            s = 1 + 0.35 * amt if d < 0 else 1 + 0.25 * amt
            M = np.float32([[s, 0, (1 - s) * CX], [0, s, (1 - s) * CY]])
            img = cv2.warpAffine(img, M, (W, H), borderMode=cv2.BORDER_REFLECT)
            img = radial_blur(img, 0.45 * amt)
            img = img + 0.25 * amt
        elif kind == 'glitch':
            g = np.random.default_rng(int(t * 1000))
            out = img.copy()
            y = 0
            while y < H:
                hgt = int(g.integers(8, 70))
                off = int(g.normal(0, 90 * amt))
                out[y:y + hgt] = np.roll(img[y:y + hgt], off, axis=1)
                y += hgt
            sft = int(24 * amt)
            if sft:
                out[..., 0] = np.roll(out[..., 0], sft, axis=1)
                out[..., 2] = np.roll(out[..., 2], -sft, axis=1)
            # blocos digitais
            for _ in range(int(14 * amt)):
                bx, by = int(g.integers(0, W - 160)), int(g.integers(0, H - 60))
                bw, bh = int(g.integers(30, 160)), int(g.integers(10, 50))
                out[by:by + bh, bx:bx + bw] = out[by:by + bh, bx:bx + bw].mean((0, 1)) * g.uniform(0.6, 1.6)
            img = out
    return img


def impact_frame(img, t):
    for it in IMPACTS:
        k = int(round((t - it) * FPS))
        if k == 0:
            g = np.clip(img, 0, 1).mean(2)
            inv = np.clip((1 - g - 0.5) * 3 + 0.5, 0, 1)
            return np.stack([inv, inv * 0.85, inv * 0.95], -1)
        if k == 1:
            g = np.clip(img, 0, 1).mean(2)
            th = (g > 0.45).astype(np.float32)
            col = np.array([1.0, 0.2, 0.55] if it >= DROP else [0.3, 0.7, 1.0], np.float32)
            return th[..., None] * np.ones(3, np.float32) * 0.95 + (1 - th[..., None]) * col * 0.15
    return img


# ================= partículas =================
class Particles:
    def __init__(self):
        self.p = np.zeros((0, 2), np.float32)
        self.v = np.zeros((0, 2), np.float32)
        self.life = np.zeros(0, np.float32)
        self.max = np.zeros(0, np.float32)
        self.size = np.zeros(0, np.float32)
        self.col = np.zeros((0, 3), np.float32)
        self.kind = np.zeros(0, np.int8)   # 0 faísca (risco), 1 brasa (ponto suave), 2 poeira
        self.drag = np.zeros(0, np.float32)
        self.grav = np.zeros(0, np.float32)

    def emit(self, pos, vel, life, size, col, kind, drag, grav):
        n = len(pos)
        if n == 0:
            return
        self.p = np.vstack([self.p, pos]).astype(np.float32)
        self.v = np.vstack([self.v, vel]).astype(np.float32)
        self.life = np.concatenate([self.life, life]).astype(np.float32)
        self.max = np.concatenate([self.max, life]).astype(np.float32)
        self.size = np.concatenate([self.size, size]).astype(np.float32)
        self.col = np.vstack([self.col, col]).astype(np.float32)
        self.kind = np.concatenate([self.kind, np.full(n, kind, np.int8)])
        self.drag = np.concatenate([self.drag, np.full(n, drag, np.float32)])
        self.grav = np.concatenate([self.grav, np.full(n, grav, np.float32)])

    def burst(self, x, y, n_spark, n_ember, palette, speed=1.0):
        a = rng.uniform(0, 2 * math.pi, n_spark)
        s = rng.uniform(350, 1700, n_spark) * speed
        self.emit(np.c_[x + rng.normal(0, 6, n_spark), y + rng.normal(0, 6, n_spark)],
                  np.c_[np.cos(a) * s, np.sin(a) * s], rng.uniform(0.25, 0.7, n_spark),
                  rng.uniform(1.0, 2.6, n_spark), palette[rng.integers(0, len(palette), n_spark)], 0, 3.2, 900)
        a = rng.uniform(0, 2 * math.pi, n_ember)
        s = rng.uniform(80, 520, n_ember) * speed
        self.emit(np.c_[x + rng.normal(0, 20, n_ember), y + rng.normal(0, 20, n_ember)],
                  np.c_[np.cos(a) * s, np.sin(a) * s - 120], rng.uniform(0.6, 1.6, n_ember),
                  rng.uniform(2.0, 5.5, n_ember), palette[rng.integers(0, len(palette), n_ember)], 1, 1.8, -60)

    def from_mask(self, mask, n, palette):
        """desfaz um texto em partículas (máscara em coordenadas de tela)."""
        ys, xs = np.nonzero(mask > 0.5)
        if len(xs) == 0:
            return
        idx = rng.choice(len(xs), min(n, len(xs)), replace=False)
        px = xs[idx].astype(np.float32)
        py = ys[idx].astype(np.float32)
        vx = (px - CX) * rng.uniform(0.3, 1.1, len(idx)) + rng.normal(0, 60, len(idx))
        vy = rng.uniform(-260, -40, len(idx))
        self.emit(np.c_[px, py], np.c_[vx, vy], rng.uniform(0.5, 1.3, len(idx)), rng.uniform(1.4, 3.2, len(idx)),
                  palette[rng.integers(0, len(palette), len(idx))], 2, 1.2, -40)

    def ambient(self, t, dt):
        if t < DROP:
            n = rng.poisson(14 * dt)
            pal = np.array([[0.6, 0.85, 1.0], [0.8, 0.95, 1.0]], np.float32)
            self.emit(np.c_[rng.uniform(0, W, n), rng.uniform(0, H, n)], np.c_[rng.normal(0, 15, n), rng.uniform(-40, -10, n)],
                      rng.uniform(1.5, 3, n), rng.uniform(1.0, 2.2, n), pal[rng.integers(0, 2, n)], 2, 0.2, 0)
        else:
            n = rng.poisson(34 * dt)
            pal = np.array([[1.0, 0.45, 0.75], [1.0, 0.7, 0.4], [1.0, 0.9, 0.95]], np.float32)
            self.emit(np.c_[rng.uniform(0, W, n), np.full(n, H + 10.0)], np.c_[rng.normal(0, 30, n), rng.uniform(-260, -90, n)],
                      rng.uniform(1.2, 2.8, n), rng.uniform(1.5, 4.0, n), pal[rng.integers(0, 3, n)], 1, 0.3, -20)

    def step(self, dt):
        if not len(self.life):
            return
        self.v *= np.exp(-self.drag * dt)[:, None]
        self.v[:, 1] += self.grav * dt
        sway = (self.kind > 0) * np.sin(self.life * 7 + self.p[:, 0] * 0.02) * 30
        self.p += self.v * dt
        self.p[:, 0] += sway * dt
        self.life -= dt
        keep = (self.life > 0) & (self.p[:, 0] > -50) & (self.p[:, 0] < W + 50) & (self.p[:, 1] > -80) & (self.p[:, 1] < H + 80)
        for k in ('p', 'v', 'life', 'max', 'size', 'col', 'kind', 'drag', 'grav'):
            setattr(self, k, getattr(self, k)[keep])

    def render(self, beat_boost=0.0):
        canvas = np.zeros((H, W, 3), np.float32)
        if not len(self.life):
            return canvas
        a = np.clip(self.life / self.max, 0, 1)
        flick = 0.75 + 0.25 * np.sin(self.life * 40 + self.p[:, 1])
        for i in range(len(self.life)):
            c = tuple(float(v) for v in self.col[i] * a[i] * (1 + beat_boost) * (flick[i] if self.kind[i] else 1))
            x, y = self.p[i]
            if self.kind[i] == 0:
                tail = self.v[i] * 0.022
                cv2.line(canvas, (int(x * 4), int(y * 4)), (int((x - tail[0]) * 4), int((y - tail[1]) * 4)), c,
                         max(1, int(self.size[i])), cv2.LINE_AA, shift=2)
            else:
                cv2.circle(canvas, (int(x * 4), int(y * 4)), max(4, int(self.size[i] * 4 * (0.5 + 0.5 * a[i]))), c, -1,
                           cv2.LINE_AA, shift=2)
        small = cv2.resize(canvas, (W // 2, H // 2), interpolation=cv2.INTER_AREA)
        glow = cv2.resize(cv2.GaussianBlur(small, (0, 0), 5), (W, H)) * 2.2
        return canvas * 1.1 + glow


PARTS = Particles()
SPARK_PRE = np.array([[0.7, 0.9, 1.0], [1.0, 1.0, 1.0], [0.4, 0.8, 1.0]], np.float32)
SPARK_POST = np.array([[1.0, 0.85, 0.6], [1.0, 1.0, 1.0], [1.0, 0.35, 0.7], [1.0, 0.55, 0.3]], np.float32)


# ================= texto =================
_fonts = {}


def font(sz):
    if sz not in _fonts:
        _fonts[sz] = ImageFont.truetype(FONT, sz)
    return _fonts[sz]


def text_layer(word_list, size, tracking=0, pop=None, cw=W):
    f = font(size)
    widths = [f.getlength(w) + tracking * len(w) for w in word_list]
    space = size * 0.28
    total = sum(widths) + space * (len(word_list) - 1)
    layer = Image.new('L', (cw, size * 2), 0)
    d = ImageDraw.Draw(layer)
    base = size * 1.45
    x = (cw - total) / 2
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


def place(mask, y):
    """converte a camada de texto em máscara de tela cheia."""
    full = np.zeros((H, W), np.float32)
    h = mask.shape[0]
    y0 = int(y - h / 2)
    a0, a1 = max(0, y0), min(H, y0 + h)
    full[a0:a1] = mask[a0 - y0:a1 - y0]
    return full


def composite(img, m, glow_rgb, alpha=1.0, glow=1.0, fill=(1, 1, 1)):
    m = m * alpha
    g = cv2.GaussianBlur(m, (0, 0), 10) * 1.7 * glow + cv2.GaussianBlur(m, (0, 0), 3) * 0.6 * glow
    img += g[..., None] * np.array(glow_rgb, np.float32)
    img[:] = img * (1 - m[..., None]) + m[..., None] * np.array(fill, np.float32)


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
for _i, _l in enumerate(LY):
    _l['end'] = LY[_i + 1]['t'] if _i + 1 < len(LY) else DUR
    _l['words'] = _l['text'].split()
    _span = (_l['end'] - _l['t']) * 0.7
    _l['wt'] = [_l['t'] + round(_span * j / max(1, len(_l['words'])) / (BEAT / 2)) * (BEAT / 2)
                for j in range(len(_l['words']))]
    _l['dissolved'] = False
    _l.setdefault('hook_end', _l['end'])
HOOK_DISSOLVE = 0.28


def hook_mask(l, t):
    hook = l['hook']
    p = (t - l['t']) / (l['hook_end'] - l['t'])
    n = len(hook)
    reveal = max(1, min(n, int(n * min(1.0, p / 0.5)) + 1))
    m = text_layer([hook[:reveal]], 140, tracking=int(4 + 22 * p), cw=2 * W)
    m = perspective(m, -30 + 44 * p, tilt=0.025 * math.sin(p * 3))[:, W // 2:W // 2 + W]
    return place(m, H / 2 - 20)


def draw_hook(img, t):
    for l in LY:
        if not (l.get('hook') and l['t'] <= t < l['hook_end']):
            continue
        post = t >= DROP
        glow_col = (1.0, 0.25, 0.65) if post else (0.25, 0.7, 1.0)
        m = hook_mask(l, t)
        diss_t = l['hook_end'] - HOOK_DISSOLVE
        if t >= diss_t:
            if not l['dissolved']:
                PARTS.from_mask(m, 1500, SPARK_POST if post else SPARK_PRE)
                l['dissolved'] = True
            m = m * max(0.0, 1 - (t - diss_t) / 0.12)
        # texto passa por trás do que está perto da câmera (arma, anel da mira, parede)
        dep = depth(np.clip(img, 0, 1))
        behind = np.median(dep[m > 0.5]) if (m > 0.5).any() else 0.5
        occ = np.clip((dep - (behind + 0.3)) / 0.1, 0, 1)
        m = m * (1 - cv2.GaussianBlur(occ, (0, 0), 3))
        composite(img, m, glow_col, alpha=0.97, glow=1.5)
        return


def draw_caption(img, t):
    for l in LY:
        if not (l['t'] <= t < l['end']) or not l['words']:
            continue
        post = t >= DROP
        shown = [w for w, wt in zip(l['words'], l['wt']) if t >= wt]
        if not shown:
            return
        dt = t - l['wt'][len(shown) - 1]
        sc = 1 + 0.3 * math.exp(-dt / 0.05) if dt < 0.2 else 1.0
        size = 60 if post else 52
        y = 640 if l.get('hook') else 605
        fade = min(1.0, (l['end'] - t) / 0.08)
        m = place(text_layer(shown, size, tracking=2, pop=(len(shown) - 1, sc)), y)
        jit = int(round(rng.uniform(-1, 1) * 3 * math.exp(-dt / 0.08))) if dt < 0.3 else 0
        m = np.roll(m, jit, axis=1)
        shadow = cv2.GaussianBlur(np.roll(np.roll(m, 4, axis=0), 4, axis=1), (0, 0), 4)
        img *= (1 - shadow[..., None] * 0.55 * fade)
        composite(img, m, (1.0, 0.3, 0.65) if post else (0.25, 0.7, 1.0), alpha=fade)
        return


# ================= overlays =================
RISERS = ((DROP - 0.95, DROP), (13.95, 14.63))


def speed_lines(img, t):
    for a, b in RISERS:
        if a <= t < b:
            p = (t - a) / (b - a)
            g = np.random.default_rng(int(t * FPS))
            lay = np.zeros((H, W), np.float32)
            for _ in range(int(30 + 90 * p)):
                ang = g.uniform(0, 2 * math.pi)
                r0 = g.uniform(260, 420) * (1.25 - 0.5 * p)
                r1 = r0 + g.uniform(200, 700)
                cv2.line(lay, (int(CX + math.cos(ang) * r0), int(CY + math.sin(ang) * r0)),
                         (int(CX + math.cos(ang) * r1), int(CY + math.sin(ang) * r1)), float(g.uniform(0.4, 1.0)),
                         int(g.integers(1, 4)), cv2.LINE_AA)
            img += cv2.GaussianBlur(lay, (0, 0), 1.2)[..., None] * 0.55 * p
    return img


def light_leak(img, t):
    amt = 0.0
    for c in CUTS + [DROP]:
        d = t - c
        if -0.15 <= d < 0.35:
            amt = max(amt, math.exp(-abs(d) / 0.12))
    if amt < 0.02:
        return img
    lw, lh = 64, 36
    yy, xx = np.mgrid[0:lh, 0:lw].astype(np.float32)
    ph = t * 3.0
    b1 = np.exp(-(((xx - (10 + 40 * (0.5 + 0.5 * math.sin(ph)))) / 18) ** 2 + ((yy - 8) / 14) ** 2))
    b2 = np.exp(-(((xx - (55 - 30 * (0.5 + 0.5 * math.cos(ph * 1.3)))) / 22) ** 2 + ((yy - 30) / 16) ** 2))
    col1 = np.array([1.0, 0.5, 0.2] if t >= DROP else [0.3, 0.6, 1.0], np.float32)
    col2 = np.array([1.0, 0.2, 0.6] if t >= DROP else [0.6, 0.9, 1.0], np.float32)
    leak = cv2.resize(b1[..., None] * col1 + b2[..., None] * col2, (W, H), interpolation=cv2.INTER_CUBIC)
    return 1 - (1 - np.clip(img, 0, 1)) * (1 - leak * 0.7 * amt)


def letterbox(img, t):
    for s in SEGS:
        lb = s.get('letterbox')
        if lb and lb[0] <= t < lb[1] + 0.12:
            p = smooth((t - lb[0]) / 0.18) if t < lb[1] else max(0.0, 1 - (t - lb[1]) / 0.12)
            bar = int(100 * p)
            g = img.mean(2, keepdims=True)
            img = g + (img - g) * (1 - 0.6 * p)
            img[:bar] = 0
            img[H - bar:] = 0
    return img


VIG = np.clip(1 - 0.42 * np.clip(np.sqrt(((GX - CX) / CX) ** 2 + ((GY - CY) / CY) ** 2) - 0.5, 0, 1) ** 1.4, 0, 1)[..., None]
GRAIN = [cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 0.7) for _ in range(8)]


def render_video(tmp_video):
    t_end = T_TO if T_TO is not None else DUR
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', f'scale={OUT_W}:{OUT_H}:flags=lanczos,unsharp=5:5:0.35',
                            '-c:v', 'libx264', '-preset', 'ultrafast' if preview else 'slow', '-crf', '18',
                            '-pix_fmt', 'yuv420p', tmp_video], stdin=subprocess.PIPE)
    nframes = int(round(DUR * FPS))
    seg_i, src = -1, None
    dt = 1 / FPS
    for fi in range(nframes):
        t = fi / FPS
        if t > t_end:
            break
        while seg_i + 1 < len(SEGS) and t >= SEGS[seg_i + 1]['start']:
            seg_i += 1
            src = None
        # partículas são simuladas desde o começo (mesmo antes de --from) para o estado ficar igual
        for kt in KILLS:
            if t - dt < kt <= t:
                big = kt == DROP or kt in IMPACTS
                PARTS.burst(CX, CY, 260 if big else 140, 70 if big else 40, SPARK_POST if kt >= DROP else SPARK_PRE,
                            speed=1.35 if big else 1.0)
        PARTS.ambient(t, dt)
        PARTS.step(dt)
        if t < T_FROM:
            for l in LY:
                if l.get('hook') and t >= l['hook_end'] - HOOK_DISSOLVE:
                    l['dissolved'] = True
            continue
        seg = SEGS[seg_i]
        if src is None:
            src = Source(seg)
            print(f'segmento {seg_i + 1}/{len(SEGS)} ({seg["clip"]})', flush=True)
        s_now = src_time(seg, t)
        rate = (src_time(seg, t + 0.5 / FPS) - src_time(seg, t - 0.5 / FPS)) * FPS
        img = grade(src.get(s_now, rate), t)
        z, sh, rgb, fl, rot = impact(t)
        img = camera(img, z, sh, rot)
        for kt in KILLS:
            if 0 <= t - kt < 0.12:
                img = radial_blur(img, 0.12 * (1 - (t - kt) / 0.12))
        img = transition(img, t)
        img = shockwave(img, t)
        img = rgb_split(img, rgb)
        img = bloom_and_streaks(img, t)
        img = letterbox(img, t)
        draw_hook(img, t)
        draw_caption(img, t)
        beat_boost = 0.0
        if t >= DROP:
            for kt in KICKS:
                if 0 <= t - kt < 0.15:
                    beat_boost = 0.6 * (1 - (t - kt) / 0.15)
        img = img + PARTS.render(beat_boost)
        img = speed_lines(img, t)
        img = light_leak(img, t)
        img = impact_frame(img, t)
        if fl > 0:
            img = img + fl * (1 - np.clip(img, 0, 1))
        img = np.clip((img - 0.035) / 0.965, 0, None) * VIG
        img = img / (1 + 0.25 * img)  * 1.25   # ombro suave nas altas
        img = img + GRAIN[fi % len(GRAIN)][..., None] * 0.022
        if t < 0.45:
            img = img * smooth(t / 0.45)
        if t > DUR - 0.35:
            img = img * max(0.0, (DUR - t) / 0.35)
        enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
        if fi % 30 == 0:
            print(f'  {t:5.2f}s', flush=True)
    enc.stdin.close()
    enc.wait()


def render_audio(tmp_audio):
    """música + tiro original de cada jogada + impacto sub-grave nos impact frames."""
    inputs = ['-i', music]
    filt = ['[0:a]aresample=48000,afade=t=out:st=%.2f:d=0.5[m]' % (DUR - 0.5)]
    labels = ['[m]']
    for i, g in enumerate(cfg['game_audio']):
        inputs += ['-ss', f'{max(0, g["src"] - 0.05):.3f}', '-t', '0.7', '-i', clip_path(g['clip'])]
        delay = int(max(0, g['at'] - 0.05) * 1000)
        filt.append(f'[{i + 1}:a]aresample=48000,volume=0.55,afade=t=out:st=0.45:d=0.25,adelay={delay}|{delay}[g{i}]')
        labels.append(f'[g{i}]')
    for j, it in enumerate(IMPACTS):
        d = int(it * 1000)
        filt.append(f'sine=f=48:d=0.6:r=48000,volume=0.9,afade=t=out:st=0.05:d=0.55,aformat=channel_layouts=stereo,'
                    f'adelay={d}|{d}[b{j}]')
        labels.append(f'[b{j}]')
    filt.append(''.join(labels) + f'amix=inputs={len(labels)}:normalize=0,atrim=0:{DUR},alimiter=limit=0.95[a]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(filt), '-map', '[a]',
                    '-c:a', 'aac', '-b:a', '256k', tmp_audio], check=True)


if __name__ == '__main__':
    tv, ta = out_path + '.v.mp4', out_path + '.a.m4a'
    render_audio(ta)
    render_video(tv)
    off = ['-ss', f'{T_FROM:.3f}'] if T_FROM else []
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tv, *off, '-i', ta, '-c', 'copy', '-shortest',
                    '-movflags', '+faststart', out_path], check=True)
    os.remove(tv)
    os.remove(ta)
    print('ok ->', out_path)
