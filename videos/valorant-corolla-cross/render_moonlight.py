#!/usr/bin/env python3
"""Edit no estilo 'moonlight' (cinematográfico, suave, sonhador) com os mesmos cortes de edit.json.

Uso: python3 render_moonlight.py <pasta_dos_clipes> <musica.mp3> <saida.mp4> [--preview] [--from T --to T]

Efeitos (tirados do vídeo de referência):
  - color grade diferente por cena (roxo monocromático, teal noturno, pastel lavado, frio), pretos levantados
  - glow difuso (Pro-Mist), bloom e halation nas altas luzes, superexposição nos abates
  - câmera virtual: push-in lento, ângulo holandês, tremida de mão; o zoom recorta o HUD
  - lens blur com bokeh (rack focus) e profundidade de campo nas bordas
  - transições: mergulho no escuro com raios de luz, smear direcional, flash superexposto, desfoque
  - faixas de cinema 2.35:1 que entram e saem
  - a jogada da pausa aparece numa tela 3D flutuante e a câmera mergulha nela no abate
  - câmera lenta por optical flow, motion blur, granulação, vinheta, aberração cromática leve
  - som abafado (filtro passa-baixa) durante a tela flutuante, voltando cheio no abate
"""
import json, math, os, subprocess, sys
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1280, 720, 30
OUT_W, OUT_H = 1920, 1080
CX, CY = W / 2, H / 2

cfg = json.load(open(os.path.join(HERE, 'edit.json'), encoding='utf-8'))
sty = json.load(open(os.path.join(HERE, 'moonlight.json'), encoding='utf-8'))
args = sys.argv[1:]
clip_dir, music, out_path = args[0], args[1], args[2]
preview = '--preview' in args
T_FROM = float(args[args.index('--from') + 1]) if '--from' in args else 0.0
T_TO = float(args[args.index('--to') + 1]) if '--to' in args else None
DROP = cfg['drop']
SEGS = cfg['segments']
KILLS = cfg['kills']
DUR = SEGS[-1]['end']
CUTS = [s['start'] for s in SEGS[1:]]
TRANS = sty['transitions']
SCREEN = sty.get('screen')
rng = np.random.default_rng(11)

GX, GY = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
RADN = np.sqrt(((GX - CX) / CX) ** 2 + ((GY - CY) / CY) ** 2)


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


# ================= fonte com optical flow (câmera lenta + motion blur) =================
DIS = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)


class Source:
    def __init__(self, seg):
        path = clip_path(seg['clip'])
        pad = 0.6   # margem para as transições que usam o segmento antes/depois do corte
        ts = [src_time(seg, seg['start'] - pad + i / FPS) for i in range(int((seg['end'] - seg['start'] + 2 * pad) * FPS) + 2)]
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
        if (i, j) not in self.flows:
            a = cv2.cvtColor(cv2.resize(self.frames[i], (W // 2, H // 2)), cv2.COLOR_RGB2GRAY)
            b = cv2.cvtColor(cv2.resize(self.frames[j], (W // 2, H // 2)), cv2.COLOR_RGB2GRAY)
            self.flows[(i, j)] = cv2.resize(DIS.calc(a, b, None), (W, H)) * 2
        return self.flows[(i, j)]

    def get(self, s, rate):
        x = (s - self.t0) * self.fps
        i = int(np.clip(math.floor(x), 0, len(self.frames) - 2))
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
        shutter = 0.5 * rate
        if np.abs(fab).mean() * shutter > 1.2:
            n = int(min(10, 3 + np.abs(fab).mean() * shutter / 3))
            acc = np.zeros_like(img)
            for k in range(n):
                o = (k / (n - 1) - 0.5) * shutter
                acc += cv2.remap(img, GX - o * fab[..., 0], GY - o * fab[..., 1], cv2.INTER_LINEAR,
                                 borderMode=cv2.BORDER_REFLECT)
            img = acc / n
        return img


_sources = {}


def source(i):
    if i not in _sources:
        for k in [k for k in _sources if abs(k - i) > 1]:
            del _sources[k]
        _sources[i] = Source(SEGS[i])
        print(f'segmento {i + 1}/{len(SEGS)} ({SEGS[i]["clip"]})', flush=True)
    return _sources[i]


# ================= lente =================
_disks = {}


def disk(r):
    if r not in _disks:
        k = np.zeros((2 * r + 1, 2 * r + 1), np.float32)
        cv2.circle(k, (r, r), r, 1.0, -1, cv2.LINE_AA)
        _disks[r] = k / k.sum()
    return _disks[r]


def lens_blur(img, r):
    """desfoque de lente com bokeh: feito em luz linear para os brilhos virarem discos."""
    if r < 0.8:
        return img
    s = 2 if r > 3 else 1
    small = cv2.resize(np.clip(img, 0, 1.5), (W // s, H // s), interpolation=cv2.INTER_AREA)
    lin = small ** 2.2
    b = cv2.filter2D(lin, -1, disk(max(1, int(round(r / s)))), borderType=cv2.BORDER_REFLECT)
    out = np.power(np.maximum(b, 0), 1 / 2.2)
    return cv2.resize(out, (W, H), interpolation=cv2.INTER_LINEAR) if s > 1 else out


DOF_MASK = np.clip((RADN - 0.55) / 0.5, 0, 1)[..., None] ** 1.3


def depth_of_field(img, amount=1.0):
    return img * (1 - DOF_MASK * amount) + lens_blur(img, 5) * DOF_MASK * amount


# ================= cor =================
LOOKS = {
    # sat, contraste, gamma, lift rgb, gain rgb, tint rgb, mistura do tint
    'purple':     dict(sat=0.55, con=1.08, gam=1.15, lift=(0.07, 0.01, 0.12), gain=(0.98, 0.72, 1.05), tint=(0.9, 0.35, 1.0), mix=0.45),
    'teal_night': dict(sat=0.95, con=1.02, gam=1.12, lift=(0.0, 0.06, 0.09), gain=(1.02, 0.98, 1.0), tint=(0.3, 0.9, 1.0), mix=0.12),
    'pastel':     dict(sat=0.9, con=0.98, gam=0.95, lift=(0.10, 0.07, 0.10), gain=(1.08, 1.0, 1.04), tint=(1.0, 0.8, 0.9), mix=0.1),
    'cold':       dict(sat=0.7, con=1.06, gam=1.0, lift=(0.05, 0.08, 0.1), gain=(0.95, 1.0, 1.04), tint=(0.5, 0.85, 1.0), mix=0.15),
}


def look(img, name):
    L = LOOKS[name]
    x = (img - 0.5) * L['con'] + 0.5
    lum = x.mean(2, keepdims=True)
    x = lum + (x - lum) * L['sat']
    x = x * (1 - L['mix']) + lum * np.array(L['tint'], np.float32) * L['mix'] * 1.15
    lift, gain = np.array(L['lift'], np.float32), np.array(L['gain'], np.float32)
    x = lift + (gain - lift) * np.clip(x, 0, 1)
    if name == 'teal_night':   # sombras teal, luzes quentes
        lum = x.mean(2, keepdims=True)
        x = x + (1 - lum) * np.array([-0.02, 0.02, 0.03], np.float32) + lum * np.array([0.04, 0.01, -0.03], np.float32)
    return np.power(np.clip(x, 0, 1), L['gam'])


def glow_stack(img, extra=0.0):
    """Pro-Mist + bloom + halation."""
    small = cv2.resize(np.clip(img, 0, 2), (W // 4, H // 4), interpolation=cv2.INTER_AREA)
    mist = cv2.GaussianBlur(small, (0, 0), 10)
    lum = small.max(2, keepdims=True)
    hl = np.clip((lum - 0.72) * 3, 0, 1) * small
    bloom = cv2.GaussianBlur(hl, (0, 0), 5) * 0.35 + cv2.GaussianBlur(hl, (0, 0), 18) * 0.4
    hal = cv2.GaussianBlur(np.clip((lum - 0.75) * 4, 0, 1), (0, 0), 3)[..., None] * np.array([1.0, 0.35, 0.15], np.float32) * 0.35
    add = cv2.resize(bloom * (1 + 1.2 * extra) + hal, (W, H))
    mist = cv2.resize(mist, (W, H))
    out = img * 0.88 + np.maximum(img, mist) * 0.12    # difusão suave
    return out + add


def god_rays(img, amt, origin=(CX, CY * 0.75)):
    if amt < 0.02:
        return img
    q = 4
    small = cv2.resize(np.clip(img, 0, 1.5), (W // q, H // q), interpolation=cv2.INTER_AREA)
    lum = small.max(2, keepdims=True)
    src = np.clip((lum - 0.55) * 2.5, 0, 1) * small
    ox, oy = origin[0] / q, origin[1] / q
    acc = np.zeros_like(src)
    n = 18
    for k in range(n):
        s = 1 + 0.6 * k / n
        M = np.float32([[1 / s, 0, ox * (1 - 1 / s)], [0, 1 / s, oy * (1 - 1 / s)]])
        acc += cv2.warpAffine(src, M, (W // q, H // q), borderMode=cv2.BORDER_CONSTANT) * (1 - k / n)
    rays = cv2.resize(cv2.GaussianBlur(acc / n * 3.0, (0, 0), 1.5), (W, H))
    return img + rays * amt


def chroma(img, s=0.0025):
    out = img.copy()
    out[..., 0] = cv2.remap(img[..., 0], CX + (GX - CX) * (1 - s), CY + (GY - CY) * (1 - s), cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_REFLECT)
    out[..., 2] = cv2.remap(img[..., 2], CX + (GX - CX) * (1 + s), CY + (GY - CY) * (1 + s), cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_REFLECT)
    return out


# ================= câmera =================
def cam_params(i, t):
    keys = sty['camera'][i]
    if t <= keys[0][0]:
        k = keys[0][1:]
    elif t >= keys[-1][0]:
        k = keys[-1][1:]
    else:
        for a, b in zip(keys, keys[1:]):
            if a[0] <= t <= b[0]:
                u = smooth((t - a[0]) / (b[0] - a[0]))
                k = [a[n] + (b[n] - a[n]) * u for n in range(1, 5)]
                break
    z, x, y, r = k
    # câmera na mão
    x += 5 * math.sin(t * 1.3) + 2.5 * math.sin(t * 3.1)
    y += 4 * math.sin(t * 1.7 + 1) + 2 * math.sin(t * 2.6)
    r += 0.35 * math.sin(t * 0.9)
    for kt in KILLS:
        d = t - kt
        if 0 <= d < 0.6:
            z += (0.06 if kt == DROP else 0.035) * math.exp(-d / 0.12)
    return z, x, y, r


def camera(img, i, t):
    z, x, y, r = cam_params(i, t)
    M = cv2.getRotationMatrix2D((CX, CY), r, z)
    M[0, 2] += x
    M[1, 2] += y
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


# ================= tela 3D flutuante =================
def screen_card(img, t):
    a, b = SCREEN['start'], SCREEN['end']
    p = smooth((t - a) / (b - a))
    q = smooth((t - (b - 0.32)) / 0.32)          # mergulho final na tela
    s = 0.56 + 0.1 * p
    s = s + (1.0 - s) * q
    ang = math.radians(-22 * (1 - 0.45 * p) * (1 - q))
    roll = math.radians(2.5 * (1 - q))
    off_x = -40 * (1 - q)
    f = 1500.0
    pts = []
    for x, y in ((-W / 2, -H / 2), (W / 2, -H / 2), (W / 2, H / 2), (-W / 2, H / 2)):
        x, y = x * s, y * s
        x, y = x * math.cos(roll) - y * math.sin(roll), x * math.sin(roll) + y * math.cos(roll)
        X, Z = x * math.cos(ang), x * math.sin(ang)
        pts.append((CX + off_x + X * f / (f + Z), CY + y * f / (f + Z)))
    Hm = cv2.getPerspectiveTransform(np.float32([[0, 0], [W, 0], [W, H], [0, H]]), np.float32(pts))
    card = cv2.warpPerspective(img, Hm, (W, H), flags=cv2.INTER_LINEAR)
    mask = cv2.warpPerspective(np.ones((H, W), np.float32), Hm, (W, H))
    mask = cv2.GaussianBlur(mask, (0, 0), 0.8)[..., None]
    # quarto escuro iluminado pela tela
    bg = lens_blur(img, 26) * np.array([0.32, 0.26, 0.42], np.float32) * (0.6 + 0.4 * (1 - q))
    glow = cv2.GaussianBlur(mask[..., 0], (0, 0), 40)[..., None] * img.mean((0, 1)) * 0.9
    # reflexo no "chão"
    refl = cv2.warpPerspective(img[::-1], Hm, (W, H))
    shift = int((pts[3][1] - pts[0][1]) + 6)
    refl = np.roll(refl, shift, axis=0)
    rmask = np.roll(mask, shift, axis=0) * np.clip(1 - (GY[..., None] - pts[3][1]) / 140, 0, 1) * 0.18 * (1 - q)
    refl = lens_blur(refl, 4)
    scan = 1 - 0.05 * (1 - q) * (np.sin(GY * 1.6) > 0.6)[..., None]   # textura de monitor
    out = bg + glow * (1 - q)
    out = out * (1 - rmask) + refl * rmask
    out = out * (1 - mask) + card * scan * mask
    return out


# ================= cena e transições =================
def shot(i, t):
    seg = SEGS[i]
    rate = (src_time(seg, t + 0.5 / FPS) - src_time(seg, t - 0.5 / FPS)) * FPS
    img = look(source(i).get(src_time(seg, t), rate), sty['looks'][i])
    if SCREEN and i == SCREEN['segment'] and t < SCREEN['end']:
        return screen_card(img, t)
    img = camera(img, i, t)
    return depth_of_field(img, 0.6)


def seg_at(t):
    i = 0
    while i + 1 < len(SEGS) and t >= SEGS[i + 1]['start']:
        i += 1
    return i


def frame(t):
    i = seg_at(t)
    for k, c in enumerate(CUTS):
        tr = TRANS[k]
        d = tr['dur']
        if not (c - d <= t < c + d):
            continue
        u = (t - c) / d                         # -1..1
        A = shot(k, t) if t < c or tr['type'] != 'dip' else None
        B = shot(k + 1, t) if t >= c or tr['type'] != 'dip' else None
        if tr['type'] == 'dip':
            if t < c:   # escurece com raios de luz e desfoque
                p = smooth(u + 1)
                img = god_rays(lens_blur(A, 14 * p), 1.4 * p) * (1 - 0.92 * p)
            else:       # volta com flash colorido
                p = 1 - smooth(u)
                tint = np.array([0.95, 0.45, 0.85], np.float32)
                img = B * (1 - 0.85 * p) + tint * 0.75 * p
                img = lens_blur(img, 10 * p)
            return img
        m = smooth((u + 1) / 2)
        peak = 1 - abs(u)
        if tr['type'] == 'smear':
            L = int(6 + 120 * peak)
            kx = np.zeros((1, L), np.float32)
            kx[0] = 1 / L
            dx = (-1 if k % 2 else 1) * 160 * peak * (1 if t < c else -1)
            Ma = np.float32([[1, 0, dx], [0, 1, 0]])
            A = cv2.filter2D(cv2.warpAffine(A, Ma, (W, H), borderMode=cv2.BORDER_REFLECT), -1, kx)
            B = cv2.filter2D(cv2.warpAffine(B, Ma, (W, H), borderMode=cv2.BORDER_REFLECT), -1, kx)
            return A * (1 - m) + B * m
        if tr['type'] == 'flash':
            img = A * (1 - m) + B * m
            img = lens_blur(img, 9 * peak)
            return img * (1 + 1.1 * peak ** 1.5) + 0.18 * peak ** 2
        if tr['type'] == 'defocus':
            img = lens_blur(A, 22 * peak) * (1 - m) + lens_blur(B, 22 * peak) * m
            return img * (1 - 0.25 * peak)
    return shot(i, t)


def letterbox(img, t):
    bar_full = int((H - W / 2.35) / 2)
    for a, b in sty['letterbox']:
        if a - 0.25 <= t < b + 0.25:
            p = smooth((t - (a - 0.25)) / 0.3) * (1 - smooth((t - b) / 0.25))
            bar = int(bar_full * p)
            if bar:
                img[:bar] = img[:bar] * 0.0 + np.array([0.01, 0.01, 0.02], np.float32)
                img[H - bar:] = np.array([0.01, 0.01, 0.02], np.float32)
    return img


VIG = np.clip(1 - 0.5 * np.clip(RADN - 0.45, 0, 1) ** 1.3, 0, 1)[..., None].astype(np.float32)
GRAIN = [cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 0.8) for _ in range(10)]


def render_video(tmp_video):
    t_end = T_TO if T_TO is not None else DUR
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', f'scale={OUT_W}:{OUT_H}:flags=lanczos',
                            '-c:v', 'libx264', '-preset', 'ultrafast' if preview else 'slow', '-crf', '18',
                            '-tune', 'grain', '-pix_fmt', 'yuv420p', tmp_video], stdin=subprocess.PIPE)
    for fi in range(int(round(DUR * FPS))):
        t = fi / FPS
        if t > t_end:
            break
        if t < T_FROM:
            continue
        img = frame(t)
        # abate: superexposição curta
        ex = 0.0
        for kt in KILLS:
            d = t - kt
            if 0 <= d < 0.35:
                ex += (1.0 if kt == DROP else 0.55) * math.exp(-d / 0.07)
        ex = min(ex, 1.0)
        img = img * (1 + 0.5 * ex) + 0.04 * ex
        img = glow_stack(img, ex)
        # ombro suave: as altas luzes comprimem em vez de estourar
        img = np.where(img > 0.75, 0.75 + 0.25 * np.tanh((img - 0.75) / 0.25), img)
        for gt in sty.get('god_rays', []):
            if 0 <= t - gt < 0.9:
                img = god_rays(img, 1.1 * math.exp(-(t - gt) / 0.3))
        img = chroma(img)
        # abertura (rack focus) e final
        if t < 1.1:
            img = lens_blur(img, 16 * (1 - smooth(t / 1.1))) * smooth(t / 0.9)
        if t > DUR - 1.0:
            p = smooth((t - (DUR - 1.0)) / 1.0)
            img = lens_blur(img, 12 * p) * (1 - p)
        img = img * VIG
        img = letterbox(img, t)
        img = img + GRAIN[fi % len(GRAIN)][..., None] * 0.028
        enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
        if fi % 30 == 0:
            print(f'  {t:5.2f}s', flush=True)
    enc.stdin.close()
    enc.wait()


def render_audio(tmp_audio):
    """música (abafada durante a tela flutuante) + tiros do jogo mais baixos."""
    a, b = sty.get('muffle', [0, 0])
    inputs = ['-i', music]
    filt = ['[0:a]aresample=48000,asplit=2[m0][m1]',
            f"[m0]volume='if(between(t,{a},{b}),0,1)':eval=frame[dry]",
            f"[m1]lowpass=f=500,lowpass=f=500,volume='if(between(t,{a},{b}),1.25,0)':eval=frame[wet]",
            f'[dry][wet]amix=inputs=2:normalize=0,afade=t=out:st={DUR - 1.0:.2f}:d=1.0[m]']
    labels = ['[m]']
    for i, g in enumerate(cfg['game_audio']):
        inputs += ['-ss', f'{max(0, g["src"] - 0.05):.3f}', '-t', '0.7', '-i', clip_path(g['clip'])]
        delay = int(max(0, g['at'] - 0.05) * 1000)
        filt.append(f'[{i + 1}:a]aresample=48000,volume=0.35,afade=t=out:st=0.4:d=0.3,adelay={delay}|{delay}[g{i}]')
        labels.append(f'[g{i}]')
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
