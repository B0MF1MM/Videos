"""Procedural, deterministic textures for the print-on-surface look.
Run: python3 tools/textures.py  (writes into assets/img/)"""
import os
import numpy as np
from PIL import Image, ImageFilter

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)


def fbm(h, w, octaves=6, base=4, persistence=0.55, seed=0):
    r = np.random.default_rng(seed)
    acc = np.zeros((h, w), np.float32)
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        n = base * (2 ** o)
        small = r.random((max(2, h * n // max(h, w)), max(2, n))).astype(np.float32)
        img = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += amp * (np.asarray(img, np.float32) / 255.0)
        tot += amp
        amp *= persistence
    return acc / tot


def norm(a):
    a = a - a.min()
    return a / (a.max() + 1e-6)


def save(arr, name, q=88):
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    im = Image.fromarray(arr)
    p = os.path.join(OUT, name)
    if name.endswith(".jpg"):
        im.convert("RGB").save(p, quality=q)
    else:
        im.save(p, optimize=True)
    print("wrote", name, im.size)


def colorize(t, stops):
    """t in 0..1 -> RGB via gradient stops [(pos,(r,g,b))]."""
    out = np.zeros(t.shape + (3,), np.float32)
    ps = [s[0] for s in stops]
    cs = np.array([s[1] for s in stops], np.float32)
    for c in range(3):
        out[..., c] = np.interp(t, ps, cs[:, c])
    return out


# ---------- wood (warm planks) ----------
def wood():
    H, W = 1600, 2400
    y = np.arange(H)[:, None].astype(np.float32)
    x = np.arange(W)[None, :].astype(np.float32)
    warp = fbm(H, W, 5, 3, seed=11) * 160
    rings = np.sin((y + warp) / 16.0 + x / 900.0 + fbm(H, W, 4, 2, seed=12) * 26) * 0.5 + 0.5
    rings = rings ** 2.2
    streak = Image.fromarray((rng.random((H, 60)) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
    streak = np.asarray(streak, np.float32) / 255
    t = 0.35 * rings + 0.35 * streak + 0.3 * fbm(H, W, 6, 8, seed=13)
    rgb = colorize(norm(t), [(0, (70, 34, 16)), (0.45, (128, 66, 30)), (0.75, (166, 92, 44)), (1, (196, 124, 66))])
    plank = 400
    seams = (np.abs(((y % plank) - 1)) < 2.5).astype(np.float32)
    shade = np.repeat(1 - 0.55 * seams, W, axis=1)
    for i in range(H // plank + 1):  # per-plank tint
        tint = 0.86 + 0.24 * rng.random()
        shade[i * plank:(i + 1) * plank] *= tint
    rgb *= shade[..., None]
    save(rgb, "wood.jpg")


def cork():
    H, W = 1600, 2400
    n1 = rng.random((H, W)).astype(np.float32)
    im = Image.fromarray((n1 * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    n1 = np.asarray(im, np.float32) / 255
    grit = (rng.random((H, W)) > 0.6).astype(np.float32)
    t = 0.45 * norm(n1) + 0.25 * grit + 0.3 * fbm(H, W, 6, 16, seed=21)
    spots = (rng.random((H, W)) > 0.985).astype(np.float32)
    spots = np.asarray(Image.fromarray((spots * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6)), np.float32) / 255
    t = norm(t) - spots * 0.8
    rgb = colorize(np.clip(t, 0, 1), [(0, (92, 56, 28)), (0.4, (160, 108, 62)), (0.7, (196, 146, 92)), (1, (222, 180, 128))])
    save(rgb, "cork.jpg")


def grass():
    H, W = 1600, 2400
    blades = rng.random((H // 6, W)).astype(np.float32)
    b = np.asarray(Image.fromarray((blades * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 255
    fine = rng.random((H, W)).astype(np.float32)
    t = 0.45 * b + 0.25 * fine + 0.3 * fbm(H, W, 5, 4, seed=31)
    rgb = colorize(norm(t), [(0, (16, 40, 14)), (0.4, (42, 86, 30)), (0.7, (74, 122, 46)), (1, (128, 160, 70))])
    save(rgb, "grass.jpg")


def concrete():
    H, W = 1600, 2400
    t = 0.6 * fbm(H, W, 7, 3, seed=41) + 0.4 * rng.random((H, W)).astype(np.float32) * 0.6
    stain = fbm(H, W, 4, 2, seed=42)
    t = norm(t) * 0.75 + 0.25 * norm(stain)
    rgb = colorize(t, [(0, (70, 68, 64)), (0.5, (128, 124, 116)), (1, (176, 172, 162))])
    save(rgb, "concrete.jpg")


def wall():
    H, W = 1200, 2000
    t = 0.7 * fbm(H, W, 6, 3, seed=51) + 0.3 * rng.random((H, W)).astype(np.float32) * 0.4
    rgb = colorize(norm(t), [(0, (196, 190, 180)), (1, (232, 228, 220))])
    save(rgb, "wall.jpg")


def paper():
    # grayscale fiber texture, mid ~ 235, for multiply on prints
    H, W = 1024, 1024
    f = rng.random((H, W)).astype(np.float32)
    fib = np.asarray(Image.fromarray((f * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)), np.float32) / 255
    t = 0.6 * norm(fib) + 0.4 * fbm(H, W, 5, 6, seed=61)
    g = 222 + 33 * norm(t)
    save(np.stack([g, g, g], -1), "paper.jpg", 90)


def crumple():
    # soft creases (gray, mid 128) for soft-light/overlay on posters
    H, W = 1024, 1400
    t = fbm(H, W, 6, 3, seed=71)
    gy, gx = np.gradient(t)
    s = norm(gx * 0.7 + gy * 0.5)
    g = 128 + (s - 0.5) * 120
    save(np.stack([g, g, g], -1), "crumple.jpg", 90)


def grain():
    H = W = 512
    n = rng.normal(0.5, 0.18, (H, W)).astype(np.float32)
    g = np.clip(n, 0, 1) * 255
    a = np.full((H, W), 255, np.float32)
    save(np.stack([g, g, g, a], -1), "grain.png")


def photo(name, stops, beams=(), bokeh=0, seed=0, w=1200, h=1500):
    r = np.random.default_rng(seed)
    y = np.linspace(0, 1, h)[:, None]
    x = np.linspace(0, 1, w)[None, :]
    t = 0.55 * y + 0.25 * x + 0.2 * fbm(h, w, 4, 2, seed=seed)
    rgb = colorize(norm(t), stops)
    light = np.zeros((h, w), np.float32)
    for (cx, cy, rad, k) in beams:
        d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        light += k * np.exp(-(d / rad) ** 2)
    rgb = rgb * (1 + light[..., None] * 1.2) + light[..., None] * 40
    if bokeh:
        layer = np.zeros((h, w, 3), np.float32)
        img = Image.new("RGB", (w, h))
        from PIL import ImageDraw
        dr = ImageDraw.Draw(img)
        for _ in range(bokeh):
            cx, cy = r.random() * w, r.random() * h * 0.8
            rr = 10 + r.random() * 60
            col = tuple(int(c) for c in stops[-1][1])
            dr.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col)
        img = img.filter(ImageFilter.GaussianBlur(14))
        layer = np.asarray(img, np.float32)
        rgb = rgb + layer * 0.45
    g = r.normal(0, 7, (h, w, 1))
    save(rgb + g, name)


def gobo(name, bars, cross):
    """Pre-blurred window-light shadow (RGBA), so no CSS blur is needed."""
    W, H = 1600, 1200
    a = np.zeros((H, W), np.float32)
    # outer wall shadow around the window opening
    a[:] = 1.0
    x0, x1, y0, y1 = int(W * .2), int(W * .8), int(H * .18), int(H * .82)
    a[y0:y1, x0:x1] = 0.0
    period = (x1 - x0) / bars
    for i in range(1, bars):
        cx = int(x0 + i * period)
        a[y0:y1, cx - 14:cx + 14] = 1.0
    if cross:
        cy = (y0 + y1) // 2
        a[cy - 14:cy + 14, x0:x1] = 1.0
    im = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26))
    al = np.asarray(im, np.float32)
    rgba = np.zeros((H, W, 4), np.float32)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = 22, 13, 6
    rgba[..., 3] = al
    save(rgba, name)


if __name__ == "__main__":
    gobo("gobo-a.png", 5, True); gobo("gobo-b.png", 6, False)
    wood(); cork(); grass(); concrete(); wall(); paper(); crumple(); grain()
    photo("ph-teal.jpg", [(0, (6, 18, 20)), (0.5, (16, 52, 56)), (1, (60, 132, 128))], beams=[(0.62, 0.3, 0.28, 0.9)], seed=1)
    photo("ph-pink.jpg", [(0, (120, 20, 52)), (0.6, (196, 62, 102)), (1, (236, 132, 160))], beams=[(0.35, 0.25, 0.4, 0.5)], seed=2)
    photo("ph-garden.jpg", [(0, (6, 14, 8)), (0.6, (18, 42, 22)), (1, (230, 196, 70))], beams=[(0.7, 0.2, 0.25, 0.6)], bokeh=40, seed=3)
    photo("ph-night.jpg", [(0, (8, 6, 14)), (0.7, (30, 18, 40)), (1, (240, 120, 70))], bokeh=60, seed=4)
    photo("ph-yellow.jpg", [(0, (20, 18, 10)), (0.5, (70, 62, 30)), (1, (236, 214, 96))], beams=[(0.5, 0.35, 0.3, 0.8)], seed=5)
    photo("ph-studio.jpg", [(0, (210, 206, 198)), (0.6, (236, 232, 226)), (1, (250, 248, 244))], beams=[(0.5, 0.4, 0.4, 0.2)], seed=6)
