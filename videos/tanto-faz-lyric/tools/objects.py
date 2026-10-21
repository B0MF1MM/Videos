"""Vector "3D" props, shaded with gradients so they read as photographed objects.
Each function returns an inline <svg> sized by its viewBox; place it inside a
positioned container and set width/height there."""

_uid = [0]


def _u(p):
    _uid[0] += 1
    return f"{p}{_uid[0]}"


def pin(color="#d1202f"):
    g = _u("pin")
    return f'''<svg viewBox="0 0 60 60" width="100%" height="100%"><defs>
<radialGradient id="{g}" cx="38%" cy="32%" r="65%"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".18" stop-color="{color}"/><stop offset="1" stop-color="#3a0508"/></radialGradient></defs>
<ellipse cx="34" cy="38" rx="20" ry="9" fill="#000" opacity=".35"/>
<circle cx="28" cy="27" r="17" fill="url(#{g})"/></svg>'''


def phone(color="#e2457f"):
    """Corded telephone handset with coiled cord."""
    g, h = _u("ph"), _u("phh")
    coil = "".join(
        f'<ellipse cx="{150 + i*13}" cy="{300 + i*22}" rx="26" ry="9" fill="none" stroke="#1d1d1d" stroke-width="5" transform="rotate(-35 {150 + i*13} {300 + i*22})"/>'
        for i in range(18))
    return f'''<svg viewBox="0 0 520 720" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd0e2"/><stop offset=".25" stop-color="{color}"/><stop offset=".75" stop-color="#8a1240"/><stop offset="1" stop-color="#3b0418"/></linearGradient>
<radialGradient id="{h}" cx="30%" cy="25%" r="50%"><stop offset="0" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>
{coil}
<path d="M120 40 C60 40 40 90 60 140 L95 210 C110 240 150 235 160 205 L175 160 C182 140 170 120 150 118 L130 116 C120 100 125 80 150 75 L330 60 C360 58 372 78 360 96 L350 112 C338 128 345 150 365 155 L410 168 C440 175 470 150 470 115 C470 60 430 25 360 22 Z" fill="url(#{g})"/>
<path d="M120 40 C60 40 40 90 60 140 L95 210 C110 240 150 235 160 205 L175 160 C182 140 170 120 150 118 L130 116 C120 100 125 80 150 75 L330 60 C360 58 372 78 360 96 L350 112 C338 128 345 150 365 155 L410 168 C440 175 470 150 470 115 C470 60 430 25 360 22 Z" fill="url(#{h})"/>
</svg>'''


def rose(color="#c8163c", leaf="#2e5a22", stem=True):
    g = _u("ro")
    petals = []
    import math
    for ring, (n, r, rr) in enumerate([(7, 70, 52), (6, 48, 40), (5, 28, 30), (4, 12, 20)]):
        for i in range(n):
            a = i / n * math.tau + ring * 0.5
            cx, cy = 150 + math.cos(a) * r * 0.9, 140 + math.sin(a) * r * 0.7
            petals.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rr}" ry="{rr*0.8:.1f}" transform="rotate({math.degrees(a):.0f} {cx:.1f} {cy:.1f})" fill="url(#{g})" stroke="#5c0518" stroke-width="2" opacity=".96"/>')
    st = (f'<path d="M150 200 C150 300 140 380 150 470" stroke="{leaf}" stroke-width="9" fill="none"/>'
          f'<path d="M150 320 C100 300 70 310 50 340 C90 350 120 345 150 320Z" fill="{leaf}"/>'
          f'<path d="M152 380 C200 360 230 370 250 395 C210 405 180 400 152 380Z" fill="{leaf}"/>') if stem else ""
    return f'''<svg viewBox="0 0 300 480" width="100%" height="100%"><defs>
<radialGradient id="{g}" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#ff7a92"/><stop offset=".45" stop-color="{color}"/><stop offset="1" stop-color="#4a0010"/></radialGradient></defs>
{st}{"".join(petals)}</svg>'''


def perfume(glass="#6fd3d6", label="TANTO FAZ"):
    g, h, c = _u("pf"), _u("pfh"), _u("pfc")
    return f'''<svg viewBox="0 0 300 420" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1f6f74"/><stop offset=".2" stop-color="{glass}"/><stop offset=".55" stop-color="#c8f4f2"/><stop offset=".8" stop-color="{glass}"/><stop offset="1" stop-color="#1a5a5e"/></linearGradient>
<linearGradient id="{c}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3b3b44"/><stop offset=".4" stop-color="#e9e9f0"/><stop offset=".6" stop-color="#9a9aa8"/><stop offset="1" stop-color="#2a2a30"/></linearGradient>
<linearGradient id="{h}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<ellipse cx="150" cy="405" rx="120" ry="12" fill="#000" opacity=".35"/>
<rect x="118" y="20" width="64" height="80" rx="6" fill="url(#{c})"/>
<rect x="130" y="96" width="40" height="30" fill="#bfc9cc"/>
<path d="M40 150 Q40 120 80 120 L220 120 Q260 120 260 150 L265 370 Q265 400 230 400 L70 400 Q35 400 35 370 Z" fill="url(#{g})"/>
<path d="M60 140 L90 140 L80 380 L58 380 Z" fill="url(#{h})"/>
<rect x="85" y="230" width="130" height="70" fill="#f6efe6"/>
<rect x="85" y="230" width="130" height="70" fill="none" stroke="#c23" stroke-width="2"/>
<text x="150" y="262" text-anchor="middle" font-family="Source Serif" font-size="20" font-style="italic" fill="#c23">{label}</text>
<text x="150" y="285" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#333">EAU DE PARFUM</text>
</svg>'''


def ring():
    g, d = _u("rg"), _u("rgd")
    return f'''<svg viewBox="0 0 300 300" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3c4"/><stop offset=".3" stop-color="#d7a73c"/><stop offset=".6" stop-color="#7a5310"/><stop offset="1" stop-color="#f3d27a"/></linearGradient>
<linearGradient id="{d}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".4" stop-color="#bfe8ff"/><stop offset=".7" stop-color="#6aa0c8"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>
<ellipse cx="150" cy="270" rx="100" ry="14" fill="#000" opacity=".35"/>
<ellipse cx="150" cy="190" rx="95" ry="72" fill="none" stroke="url(#{g})" stroke-width="18"/>
<path d="M115 118 L150 70 L185 118 L150 150 Z" fill="url(#{d})" stroke="#e8f6ff" stroke-width="2"/>
<path d="M115 118 L185 118 M150 70 L150 150 M132 95 L168 95" stroke="#fff" stroke-width="1.5" opacity=".8"/>
</svg>'''


def crt(screen_html_bg="#0d2b2e"):
    """Beige retro computer (Apple II-ish) with a screen area id'd for overlays."""
    g, s, k = _u("cr"), _u("crs"), _u("crk")
    keys = "".join(
        f'<rect x="{70 + c*29 + r*8}" y="{455 + r*24}" width="24" height="18" rx="3" fill="#e6dfcd" stroke="#a89f88"/>'
        for r in range(4) for c in range(13))
    return f'''<svg viewBox="0 0 560 600" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7f2e4"/><stop offset=".6" stop-color="#ddd4bd"/><stop offset="1" stop-color="#a99f86"/></linearGradient>
<radialGradient id="{s}" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#3fa7a0"/><stop offset=".6" stop-color="{screen_html_bg}"/><stop offset="1" stop-color="#020807"/></radialGradient>
<linearGradient id="{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9e2cf"/><stop offset="1" stop-color="#b9b098"/></linearGradient></defs>
<ellipse cx="290" cy="585" rx="260" ry="16" fill="#000" opacity=".35"/>
<rect x="80" y="20" width="400" height="330" rx="22" fill="url(#{g})"/>
<rect x="115" y="50" width="330" height="250" rx="26" fill="#2b2a26"/>
<rect x="130" y="64" width="300" height="222" rx="30" fill="url(#{s})"/>
<rect x="150" y="80" width="120" height="40" rx="20" fill="#fff" opacity=".12"/>
<rect x="120" y="350" width="320" height="40" fill="#cfc6ad"/>
<path d="M30 420 L530 420 L555 560 L5 560 Z" fill="url(#{k})"/>
<path d="M30 420 L530 420 L536 440 L24 440 Z" fill="#f4efe2"/>
{keys}
<rect x="430" y="370" width="18" height="10" fill="#d23"/>
</svg>'''


def car(color="#d0121e"):
    g, w, gl = _u("ca"), _u("caw"), _u("cag")
    wheel = lambda cx: (f'<circle cx="{cx}" cy="300" r="62" fill="#111"/><circle cx="{cx}" cy="300" r="40" fill="url(#{w})"/>'
                        f'<circle cx="{cx}" cy="300" r="10" fill="#333"/>')
    return f'''<svg viewBox="0 0 900 380" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff9a9a"/><stop offset=".18" stop-color="{color}"/><stop offset=".6" stop-color="#7a0008"/><stop offset="1" stop-color="#2a0003"/></linearGradient>
<radialGradient id="{w}" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#f4f4f4"/><stop offset=".6" stop-color="#8b8b8b"/><stop offset="1" stop-color="#3a3a3a"/></radialGradient>
<linearGradient id="{gl}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#cfe6f0"/><stop offset=".5" stop-color="#2d3a44"/><stop offset="1" stop-color="#9fb8c6"/></linearGradient></defs>
<ellipse cx="450" cy="355" rx="420" ry="22" fill="#000" opacity=".45"/>
<path d="M40 250 L60 200 Q90 180 200 170 L300 110 Q330 92 380 90 L560 90 Q600 92 630 115 L710 170 Q820 178 855 205 L870 255 Q872 285 850 290 L60 290 Q35 285 40 250 Z" fill="url(#{g})"/>
<path d="M320 118 Q340 104 380 104 L455 104 L455 170 L250 170 Z" fill="url(#{gl})"/>
<path d="M475 104 L555 104 Q590 106 615 125 L680 170 L475 170 Z" fill="url(#{gl})"/>
<path d="M60 205 Q300 190 860 215" stroke="#fff" stroke-opacity=".45" stroke-width="5" fill="none"/>
<rect x="830" y="215" width="34" height="18" rx="4" fill="#ffe9a8"/>
<rect x="40" y="220" width="26" height="16" rx="4" fill="#ff3b3b"/>
{wheel(200)}{wheel(700)}
</svg>'''


def lipstick(color="#c4102c"):
    g, b = _u("lp"), _u("lpb")
    return f'''<svg viewBox="0 0 140 420" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5a0010"/><stop offset=".35" stop-color="{color}"/><stop offset=".55" stop-color="#ff8c9c"/><stop offset="1" stop-color="#4a000c"/></linearGradient>
<linearGradient id="{b}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a2a08"/><stop offset=".4" stop-color="#f1d27a"/><stop offset=".6" stop-color="#a77d22"/><stop offset="1" stop-color="#2a1d04"/></linearGradient></defs>
<path d="M40 40 L100 10 L100 150 L40 150 Z" fill="url(#{g})"/>
<rect x="32" y="150" width="76" height="70" fill="url(#{b})"/>
<rect x="26" y="220" width="88" height="190" rx="6" fill="#141414"/>
<rect x="34" y="226" width="14" height="176" fill="#fff" opacity=".12"/>
</svg>'''


def bag(color="#f2c6d4", text="TANTO FAZ"):
    g = _u("bg")
    return f'''<svg viewBox="0 0 320 420" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b88a98"/><stop offset=".45" stop-color="{color}"/><stop offset="1" stop-color="#9c6b7a"/></linearGradient></defs>
<ellipse cx="160" cy="408" rx="150" ry="10" fill="#000" opacity=".35"/>
<path d="M110 120 C110 40 210 40 210 120" stroke="#2a1a1f" stroke-width="10" fill="none"/>
<path d="M30 110 L290 110 L310 400 L10 400 Z" fill="url(#{g})"/>
<text x="160" y="260" text-anchor="middle" font-family="Source Serif" font-size="34" font-style="italic" fill="#2a1a1f">{text}</text>
</svg>'''


def starburst(color="#f4e83a", n=14, inner=0.62):
    import math
    pts = []
    for i in range(n * 2):
        r = 100 if i % 2 == 0 else 100 * inner
        a = i / (n * 2) * math.tau - math.pi / 2
        pts.append(f"{100 + math.cos(a)*r:.1f},{100 + math.sin(a)*r:.1f}")
    return f'<svg viewBox="0 0 200 200" width="100%" height="100%"><polygon points="{" ".join(pts)}" fill="{color}"/></svg>'


def heart(color="#e0244c"):
    g = _u("ht")
    return f'''<svg viewBox="0 0 200 180" width="100%" height="100%"><defs>
<radialGradient id="{g}" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#ff9fb4"/><stop offset=".4" stop-color="{color}"/><stop offset="1" stop-color="#5a0014"/></radialGradient></defs>
<path d="M100 170 C40 120 0 90 0 50 C0 20 25 0 52 0 C75 0 92 14 100 32 C108 14 125 0 148 0 C175 0 200 20 200 50 C200 90 160 120 100 170Z" fill="url(#{g})"/></svg>'''


def leaf(color="#8a4b1c"):
    return f'''<svg viewBox="0 0 120 70" width="100%" height="100%"><path d="M5 35 C30 0 90 0 115 35 C90 70 30 70 5 35Z" fill="{color}"/><path d="M5 35 L115 35" stroke="#3a1c08" stroke-width="2" opacity=".6"/></svg>'''


def cassette():
    g = _u("cs")
    return f'''<svg viewBox="0 0 400 260" width="100%" height="100%"><defs>
<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#333"/><stop offset="1" stop-color="#0c0c0c"/></linearGradient></defs>
<rect x="0" y="0" width="400" height="260" rx="16" fill="url(#{g})"/>
<rect x="30" y="26" width="340" height="130" rx="6" fill="#f2e9d8"/>
<rect x="30" y="26" width="340" height="30" fill="#e2245c"/>
<text x="200" y="110" text-anchor="middle" font-family="Archivo Black" font-size="34" fill="#111">TANTO FAZ</text>
<circle cx="120" cy="190" r="26" fill="#ddd"/><circle cx="280" cy="190" r="26" fill="#ddd"/>
<rect x="150" y="176" width="100" height="28" fill="#222"/></svg>'''
