"""Scene definitions: one function per frame -> (fid, duration, html)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kit import ROOT, Typer, frame_html, fx_layers, gobo, paper, t_of, LYR  # noqa: E402,F401
import objects as O  # noqa: E402

TITLE = "Tanto Faz"
ARTIST = "Bomfim"
CREDIT = "Bomfim — Tanto Faz (Prod. The Fox)"
YEAR = "2026"
DURATION = 167.68

# Frame cuts (track seconds). Each frame = one printed "set".
CUTS = [
    ("00-mesa", 0.0),
    ("01-cortica", 13.0),
    ("02-tabloide", 27.85),
    ("03-jardim", 45.16),
    ("04-computador", 60.3),
    ("05-jornal", 75.15),
    ("06-muro", 92.0),
    ("07-rosa", 113.7),
    ("08-encarte", 130.0),
    ("09-creditos", 151.7),
]

BODY = ("“Tanto Faz” é uma carta aberta sobre entrega e medo de errar de novo. A faixa "
        "atravessa o refrão como quem repete uma promessa em voz baixa, entre o desejo de ficar "
        "e o receio de se arrepender. Nas estrofes, o amor aparece como resgate: alguém que chega "
        "do nada, tira do sufoco e cura as feridas sem esforço. O que sobra é a vontade de "
        "construir um plano, uma vida inteira, com a pessoa certa ao lado.")
BODY2 = ("Gravada entre madrugadas, a música aposta num grave arrastado e numa voz que conversa "
         "mais do que canta. Cada verso parece escrito no verso de um papel qualquer — um bilhete, "
         "um recado, uma confissão. É sobre escolher e ser escolhido, e sobre pedir, por favor, "
         "que essa escolha não vire arrependimento.")


def span(fid):
    i = [c[0] for c in CUTS].index(fid)
    t0 = CUTS[i][1]
    t1 = CUTS[i + 1][1] if i + 1 < len(CUTS) else DURATION
    return t0, t1


def cam_js(keys):
    import json
    return "shot(" + json.dumps(keys) + ");"


def drift(p, k=1.0):
    d = dict(p)
    d["x"] = p["x"] + 26 * k
    d["y"] = p["y"] + 10 * k
    d["s"] = round(p["s"] * (1 + 0.035 * k), 4)
    d["rz"] = p.get("rz", 0) + 0.5 * k
    return d


def path(t0, t1, start, stops, mv=0.8, ease="power3.inOut"):
    """Camera that holds/drifts on each print and glides to the next one
    so it ARRIVES at each stop's track time."""
    keys = [dict(t=0, **start)]
    cur = start
    for t_abs, pose in stops:
        ta = round(t_abs - t0, 3)
        tm = round(ta - mv, 3)
        if tm > keys[-1]["t"] + 0.2:
            keys.append(dict(t=tm, **drift(cur)))
        keys.append(dict(t=ta, e=ease, **pose))
        cur = pose
    keys.append(dict(t=round(t1 - t0, 3), **drift(cur, 1.4)))
    return cam_js(keys)


def P(x, y, s, rx=10, rz=0):
    return dict(x=x, y=y, s=s, rx=rx, rz=rz)


def surface(img, size="2400px 1600px", extra="", w=9800):
    return (f'<div class="surface" style="left:-2600px;top:-2200px;width:{w}px;height:5200px;'
            f'background-image:url(assets/img/{img});background-size:{size};{extra}"></div>')


def prop(svg, x, y, w, h, rot=0, extra=""):
    return f'<div class="prop" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);{extra}">{svg}</div>'


def ph(img, x, y, w, h, extra="", inner=""):
    return (f'<div class="photo" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background-image:url(assets/img/{img});{extra}">'
            f'{inner}<div class="phfx" style="inset:0"></div></div>')


GRADES = {
    # filter on the photo, then a colour wash to sit it in each scene's palette
    "teal": ("grayscale(.75) contrast(1.15) brightness(.85)", "rgba(40,150,150,.55)", "color"),
    "pink": ("grayscale(.35) contrast(1.08) brightness(.95)", "rgba(232,70,124,.35)", "color"),
    "warm": ("sepia(.25) saturate(.9) contrast(1.06)", "rgba(255,170,90,.18)", "soft-light"),
    "green": ("saturate(.8) contrast(1.08) brightness(.92)", "rgba(80,140,60,.25)", "soft-light"),
    "night": ("saturate(.8) contrast(1.1) brightness(.85)", "rgba(90,40,120,.3)", "soft-light"),
    "mono": ("grayscale(1) brightness(1.2) contrast(1.2)", "rgba(0,0,0,0)", "normal"),
    "teal2": ("grayscale(.5) contrast(1.1) brightness(.8)", "rgba(30,110,120,.45)", "color"),
}


def foto(name, x, y, w, h, grade="warm", pos="50% 30%", extra=""):
    """One of the couple's photos, printed and graded like the rest of the set."""
    flt, wash, blend = GRADES[grade]
    return (f'<div class="photo" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">'
            f'<div style="position:absolute;inset:0;background:url(assets/img/eu/{name}.jpg) {pos}/cover no-repeat;filter:{flt}"></div>'
            f'<div style="position:absolute;inset:0;background:{wash};mix-blend-mode:{blend}"></div>'
            f'<div class="phfx" style="inset:0"></div></div>')


def finish(fid, t0, t1, css, world, fx, T, cam, extra_js=""):
    script = T.js() + "\n        typeOn(TYPE);\n        " + cam + "\n" + extra_js
    return fid, round(t1 - t0, 3), frame_html(fid, t1 - t0, css, world, fx, script)


RAINBOW = ["#f2c230", "#7ec84a", "#3fb5d8", "#8a5fd0", "#e8467c", "#f28a30", "#3fb5d8", "#7ec84a", "#e8467c"]


def rainbow(word, cls=""):
    return "".join(f'<span class="{cls}" style="color:{RAINBOW[i % len(RAINBOW)]}">{c}</span>' for i, c in enumerate(word))


# ======================================================================
# 00 — MESA: overhead desk collage, title appears on a retro computer ad
# ======================================================================
def f00():
    fid = "00-mesa"
    t0, t1 = span(fid)
    T = Typer(t0, "m0")
    crt_screen = (f'<div class="m0-scr">{T.text("> tocando agora", 2.4, "m0-mono", 0.07)}<br>'
                  f'{T.text("tanto_faz.mp3", 3.9, "m0-mono m0-hi", 0.09)}<br>'
                  f'{T.text("▮▮▮▮▮▮▮▯▯▯ 2:47", 5.6, "m0-mono", 0.06)}</div>')
    ad = f'''
      <div class="m0-mast" data-layout-allow-overlap>{rainbow("TANTO FAZ")}</div>
      {prop(O.crt(), 170, 330, 660, 707)}
      {crt_screen}
      <div class="m0-tag">{T.text("Uma música sobre escolher", 7.6, "", 0.05)}<br><em>{T.text("e ser escolhido.", 9.2, "", 0.06)}</em></div>
      <div class="m0-fine">{CREDIT}</div>'''
    tab = f'''<div class="m0-tmast">TANTO FAZ</div>{foto("d07", 0, 170, 760, 860, "pink", "50% 20%")}
      <div class="m0-tq">“SÓ NÃO FAZ EU ME ARREPENDER”</div>
      <div class="obj" style="left:520px;top:860px;width:200px;height:200px">{O.starburst()}</div>'''
    wall = f'''<div class="m0-pw">PACI<br>ENTE</div>{foto("d20", 40, 330, 620, 420, "mono", "50% 25%")}<div style="position:absolute;left:40px;top:330px;width:620px;height:420px;background:#e9d23a;mix-blend-mode:multiply"></div>'''
    news = f'''<div class="m0-nm">O Tanto Faz</div><div class="m0-nl"></div>
      <div class="m0-nh">Você ainda<br>me <i>perdoou</i></div><div class="m0-nb">{BODY}</div>'''
    world = f'''
      {surface("wood.jpg")}
      {paper("m0-news", -1150, -420, 880, 1100, -11, "#ece8df", news)}
      {paper("m0-wall", 1120, -380, 700, 980, 9, "#1a1a16", wall, crease=True)}
      {paper("m0-tab", -1080, 620, 760, 1040, 7, "#111", tab)}
      {prop(O.cassette(), 820, 520, 430, 280, -16)}
      {prop(O.perfume(), 1300, 420, 300, 420, 12)}
      {paper("m0-ad", 0, 0, 1000, 1360, -2.5, "#efece4", ad)}
      {paper("m0-note", 520, -760, 280, 260, 6, "#f3e27a", '<div class="m0-note">faixa nova<br>ouvir alto!</div>')}
      {prop(O.rose(), -420, -900, 240, 380, -60)}
      {gobo(-1600, -1600, 3400, 2600, -24, 0.42, 5)}
    '''
    css = f'''
.m0-mast {{ position:absolute; left:0; right:0; top:60px; text-align:center; font-family:"League Spartan"; font-weight:900; font-size:150px; letter-spacing:-.04em; line-height:1; }}
.m0-scr {{ position:absolute; left:320px; top:410px; width:360px; height:220px; padding:26px 30px; transform:rotate(0deg); }}
.m0-mono {{ font-family:"DM Mono"; font-size:24px; color:#8ff0d8; text-shadow:0 0 8px rgba(120,255,220,.7); }}
.m0-hi {{ color:#ffd7ea; font-size:30px; text-shadow:0 0 10px rgba(255,120,180,.9); }}
.m0-tag {{ position:absolute; left:0; right:0; top:1090px; text-align:center; font-family:"Source Serif"; font-size:52px; line-height:1.05; color:#1d1d1d; }}
.m0-tag em {{ color:#e8467c; }}
.m0-fine {{ position:absolute; left:0; right:0; bottom:40px; text-align:center; font-family:"Source Serif"; font-size:15px; color:#555; }}
.m0-tmast {{ position:absolute; left:20px; top:20px; font-family:"Archivo"; font-weight:900; font-style:italic; font-size:150px; line-height:1; color:#e2243c; -webkit-text-stroke:3px #f4e83a; letter-spacing:-.03em; }}
.m0-tq {{ position:absolute; left:40px; right:200px; top:260px; font-family:"Archivo Black"; font-size:70px; line-height:.95; color:#f4e83a; text-shadow:3px 3px 0 #000; }}
.m0-pw {{ position:absolute; left:30px; top:30px; font-family:Anton; font-size:250px; line-height:.86; color:#f2d43a; }}
.m0-nm {{ position:absolute; left:40px; top:30px; font-family:"Source Serif"; font-weight:600; font-size:96px; color:#111; letter-spacing:-.02em; }}
.m0-nl {{ position:absolute; left:40px; right:40px; top:150px; height:10px; background:#e8467c; }}
.m0-nh {{ position:absolute; left:40px; top:190px; font-family:"Archivo Black"; font-size:96px; line-height:.95; color:#2a2a2a; }}
.m0-nh i {{ color:#e8467c; }}
.m0-nb {{ position:absolute; left:40px; right:40px; top:420px; columns:3; font-family:"Source Serif"; font-size:17px; line-height:1.35; color:#333; text-align:justify; }}
.m0-note {{ position:absolute; inset:30px; font-family:"Source Serif"; font-style:italic; font-size:34px; color:#2a2a2a; }}
'''
    cam = cam_js([
        dict(t=0, x=40, y=-60, s=1.55, rx=4, rz=10),
        dict(t=2.0, x=20, y=-80, s=1.3, rx=5, rz=7, e="sine.inOut"),
        dict(t=6.5, x=0, y=60, s=0.72, rx=8, rz=1, e="power2.inOut"),
        dict(t=10.6, x=-20, y=420, s=0.82, rx=12, rz=-2, e="sine.inOut"),
        dict(t=13.0, x=600, y=300, s=0.62, rx=16, rz=-5, e="power2.in"),
    ])
    fx = fx_layers(grade="rgba(60,50,30,.25)", leak=0.6, dof_t=8, dof_b=6)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 01 — CORTIÇA: dark teal serif posters pinned on a cork board
# ======================================================================
def f01():
    fid = "01-cortica"
    t0, t1 = span(fid)
    T = Typer(t0, "c1")
    W, H = 900, 1270

    def poster(pid, x, y, rot, lid, photo, pos, grade, layout="top"):
        inner = f'''
        {foto(photo, 0, 0, W, 860, grade, pos)}
        <div class="c1-grad"></div>
        <div class="c1-head c1-{layout}">{T.line(lid, "c1-big", title=True)}</div>
        <div class="c1-cols"><p>{BODY}</p><p>{BODY2}</p></div>
        <div class="c1-sig">{ARTIST.upper()} — {TITLE.upper()}</div>
        <div class="c1-fine">Prod. The Fox · Lado A, faixa 1 · {YEAR}</div>
        <div class="obj" style="left:{W/2-22}px;top:14px;width:44px;height:44px">{O.pin()}</div>'''
        return paper(pid, x, y, W, H, rot, "#0f1718", inner)

    cal = ('<div class="c1-cal">' + "".join(
        f'<div class="m"><b>{m}</b>' + "".join("<i></i>" for _ in range(30)) + "</div>"
        for m in ["Março", "Abril", "Julho", "Agosto", "Novembro", "Dezembro"]) +
        f'</div><div class="obj" style="left:190px;top:8px;width:40px;height:40px">{O.pin("#e8b04a")}</div>')
    world = f'''
      {surface("cork.jpg")}
      {paper("c1-cal", -820, -80, 420, 600, 4, "#e9e6df", cal)}
      {poster("c1-p1", 0, 0, -2.2, "c1", "d21", "50% 20%", "teal")}
      {poster("c1-p2", 1120, 90, 2.6, "c2", "d34", "50% 40%", "teal2", "mid")}
      {paper("c1-note", 640, -720, 260, 240, -6, "#f3e27a", '<div class="c1-note">não esquecer:<br>ligar pra ela</div>')}
      {paper("c1-note2", 1680, 860, 230, 210, 8, "#f7b3c7", '<div class="c1-note">sábado<br>22h</div>')}
      {poster("c1-p3", 2230, -40, -1.4, "c3", "d18", "50% 40%", "teal")}
      {poster("c1-p4", 3330, 60, 1.8, "c4", "d06", "50% 30%", "teal2", "mid")}
      {paper("c1-flyer", 2800, -900, 520, 360, -3, "#111", '<div class="c1-fly">TANTO<br>FAZ</div>')}
      {paper("c1-flyer2", 4200, -700, 400, 560, 5, "#e9e6df", '<div class="c1-fly" style="color:#e2243c">SÁB<br>22H</div>')}
      {gobo(-900, -1400, 2600, 2000, -22, 0.5, 5)}
      {gobo(2100, -1300, 2600, 2000, -22, 0.45, 5)}
    '''
    css = '''
.c1-grad { position:absolute; inset:0; background:linear-gradient(to bottom, rgba(15,23,24,0) 32%, rgba(15,23,24,.92) 58%, #0f1718 70%); }
.c1-head { position:absolute; left:60px; right:60px; text-align:center; color:#eef3ef; font-family:"Source Serif"; font-weight:400; }
.c1-top { top:690px; } .c1-mid { top:650px; }
.c1-big { display:block; font-size:82px; line-height:1.02; letter-spacing:-.01em; }
.c1-big em { font-weight:600; }
.c1-cols { position:absolute; left:70px; right:70px; top:965px; columns:2; column-gap:40px; color:#c9d4d0; font-family:"Source Serif"; font-size:15.5px; line-height:1.35; text-align:justify; }
.c1-cols p { margin:0 0 8px; text-indent:1.2em; }
.c1-sig { position:absolute; left:0; right:0; bottom:58px; text-align:center; color:#eef3ef; font-family:"Source Serif"; font-weight:600; letter-spacing:.06em; font-size:20px; }
.c1-fine { position:absolute; left:0; right:0; bottom:34px; text-align:center; color:#8ea09b; font-family:"Source Serif"; font-size:11px; }
.c1-cal { position:absolute; inset:30px; display:grid; grid-template-columns:1fr 1fr; gap:20px 26px; font-family:"Source Serif"; color:#333; }
.c1-cal .m { display:flex; flex-wrap:wrap; gap:4px; align-content:flex-start; }
.c1-cal .m b { display:block; width:100%; font-size:22px; font-weight:600; margin-bottom:6px; }
.c1-cal .m i { width:16px; height:12px; background:#8a8a8a; opacity:.5; }
.c1-note { position:absolute; inset:28px; font-family:"Source Serif"; font-style:italic; font-size:30px; line-height:1.2; color:#2a2a2a; transform:rotate(-2deg); }
.c1-fly { position:absolute; inset:30px; font-family:Anton; font-size:120px; line-height:.92; color:#f4e83a; }
'''
    cam = path(t0, t1, P(-260, -40, 0.5, 18, -6), [
        (t_of("c1"), P(0, 60, 0.7, 11, -2)),
        (t_of("c2"), P(1110, 100, 0.72, 10, 1.5)),
        (t_of("c3"), P(2220, 40, 0.72, 11, -1.2)),
        (t_of("c4"), P(3320, 80, 0.72, 11, 1.5)),
    ], mv=0.7)
    fx = fx_layers(grade="rgba(30,80,80,.28)", leak=0.55, dof_t=9, dof_b=6)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 02 — TABLOIDE: gossip magazine on a wooden table, yellow/red quotes
# ======================================================================
def f02():
    fid = "02-tabloide"
    t0, t1 = span(fid)
    T = Typer(t0, "t2")
    W, H = 980, 1300
    cover = f'''
      {foto("d07", 0, 0, W, H, "pink", "60% 25%")}
      <div class="t2-mast">TANTO FAZ</div>
      <div class="t2-strap">EXCLUSIVO · A FAIXA QUE TODO MUNDO ESTÁ CANTANDO · Nº 01</div>
      <div class="t2-q t2-q1">{T.line("c5", "", upper=True, pre="“", post="”")}</div>
      <div class="t2-q t2-q2">{T.line("c6", "", upper=True)}</div>
      <div class="obj" style="left:720px;top:1060px;width:220px;height:220px">{O.starburst()}</div>
      <div class="t2-burst" style="left:720px;top:1135px">SÓ<br>AQUI!</div>
      <div class="t2-bar"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>'''
    left = f'''
      {foto("d11", 0, 0, W, H, "night", "50% 30%")}
      <div style="position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0) 45%)"></div>
      <div class="t2-q t2-q3">{T.line("c7", "", upper=True, pre="“", post="”")}</div>
      <div class="obj" style="left:80px;top:900px;width:300px;height:300px">{O.starburst("#e2243c")}</div>
      <div class="t2-burst2" style="left:80px;top:1000px">{T.line("c8", "", upper=True)}</div>
      <div class="t2-cap">Foto: arquivo · Página 4</div>'''
    right = f'''
      <div class="t2-q t2-q4">{T.line("c9", "", upper=True, pre="“…", post="”")}</div>
      <div class="t2-body">{BODY} {BODY2}</div>
      {foto("d12", 90, 700, 400, 460, "warm", "50% 40%", "border:8px solid #e2243c")}
      <div class="t2-q t2-q5">{T.line("c10", "", upper=True, pre="“", post="”")}</div>
      <div class="obj" style="left:640px;top:1020px;width:240px;height:240px">{O.starburst()}</div>
      <div class="t2-burst" style="left:640px;top:1100px;font-size:40px">{T.line("c11", "", upper=True)}</div>'''
    back = f'''
      {foto("d16", 0, 0, W, H, "warm", "50% 30%")}
      <div style="position:absolute;left:0;right:0;top:500px;height:420px;background:rgba(244,232,58,.82)"></div>
      <div class="t2-q t2-q6">{T.line("c12", "", upper=True, pre="“", post="”")}</div>
      <div class="t2-strap" style="top:auto;bottom:40px;background:#111;color:#f4e83a">TANTO FAZ · {YEAR} · PÁGINA 6</div>'''
    world = f'''
      {surface("wood.jpg")}
      {paper("t2-cover", 0, 0, W, H, -3, "#111", cover)}
      {paper("t2-l", 1600, 140, W, H, 2, "#111", left)}
      {paper("t2-r", 2585, 165, W, H, 2, "#f1ede4", right)}
      {paper("t2-back", 3900, 40, W, H, -2.5, "#111", back)}
      {prop(O.perfume(), -760, 380, 300, 420, -12)}
      {prop(O.cassette(), 3150, -880, 420, 270, 18)}
      <div class="obj" style="left:1200px;top:-800px;width:520px;height:22px;transform:rotate(24deg);background:linear-gradient(#3a5fd8,#1c2f80);border-radius:12px;box-shadow:0 18px 18px rgba(0,0,0,.4)"></div>
      {gobo(-1200, -1500, 3200, 2400, -20, 0.5, 4)}
      {gobo(2200, -1500, 3200, 2400, -20, 0.45, 4)}
    '''
    css = '''
.t2-mast { position:absolute; left:24px; top:18px; font-family:"Archivo"; font-weight:900; font-style:italic; font-size:150px; line-height:1; color:#e2243c; -webkit-text-stroke:4px #f4e83a; letter-spacing:-.035em; }
.t2-strap { position:absolute; left:0; right:0; top:206px; padding:8px 24px; font-family:"Archivo"; font-weight:800; font-size:22px; background:#f4e83a; color:#111; letter-spacing:.04em; }
.t2-q { position:absolute; font-family:"Archivo Black"; color:#f4e83a; line-height:.96; text-shadow:4px 4px 0 #000; letter-spacing:-.01em; }
.t2-q1 { left:50px; right:330px; top:300px; font-size:86px; }
.t2-q2 { left:50px; top:640px; font-size:120px; color:#fff; }
.t2-q3 { left:60px; right:60px; top:80px; font-size:96px; }
.t2-q4 { left:60px; right:60px; top:70px; font-size:84px; color:#111; text-shadow:none; }
.t2-q4 .ly .ch:nth-child(n) { }
.t2-q5 { left:520px; right:50px; top:640px; font-size:52px; color:#e2243c; text-shadow:none; }
.t2-q6 { left:60px; right:60px; top:560px; font-size:118px; color:#111; text-shadow:4px 4px 0 #fff; }
.t2-burst, .t2-burst2 { position:absolute; width:240px; text-align:center; font-family:"Archivo Black"; font-size:44px; line-height:.9; color:#111; transform:rotate(-10deg); }
.t2-burst2 { width:300px; color:#fff; font-size:46px; }
.t2-bar { position:absolute; left:40px; bottom:40px; display:flex; gap:3px; }
.t2-bar i { display:block; width:6px; height:70px; background:#fff; }
.t2-bar i:nth-child(2n) { width:3px; }
.t2-cap { position:absolute; left:60px; bottom:30px; font-family:"Archivo"; font-size:16px; color:#ddd; }
.t2-body { position:absolute; left:60px; right:60px; top:420px; columns:2; column-gap:36px; font-family:"Archivo"; font-size:19px; line-height:1.35; color:#222; text-align:justify; }
'''
    cam = path(t0, t1, P(-200, -300, 0.62, 18, -8), [
        (t_of("c5"), P(-40, 100, 0.76, 12, -3)),
        (t_of("c7"), P(1600, 80, 0.78, 12, 2)),
        (t_of("c9"), P(2560, 30, 0.82, 12, 2)),
        (t_of("c10"), P(2600, 600, 0.9, 13, 1)),
        (t_of("c12") - 0.2, P(3880, 160, 0.78, 12, -2)),
    ], mv=0.75)
    fx = fx_layers(grade="rgba(90,50,20,.22)", leak=0.65, dof_t=10, dof_b=7)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 03 — JARDIM: fashion-editorial pages lying on grass with dry leaves
# ======================================================================
def f03():
    fid = "03-jardim"
    t0, t1 = span(fid)
    T = Typer(t0, "g3")
    W, H = 960, 1260
    pA = f'''
      <div class="g3-ttl" style="top:50px">{T.line("v1", "", title=True)}<br>{T.line("v2", "", title=True)}</div>
      {foto("d30", 60, 330, 840, 560, "green", "50% 30%")}
      <div class="g3-body" style="top:930px">{BODY}</div>
      <div class="g3-fol">BOMFIM — TANTO FAZ<span>12</span></div>'''
    pB = f'''
      {foto("d31", 60, 60, 840, 500, "green", "50% 25%")}
      {prop(O.perfume("#7fd8da"), 90, 600, 300, 420, 4)}
      <div class="g3-ttl g3-r" style="top:600px">{T.line("v3", "", title=True)}<br>{T.line("v4", "", title=True)}</div>
      <div class="g3-body" style="left:470px;top:860px;columns:1">{BODY2}</div>
      <div class="g3-fol">BOMFIM — TANTO FAZ<span>13</span></div>'''
    pC = f'''
      {foto("d20", 0, 0, W, 900, "green", "60% 30%")}
      <div style="position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0))"></div>
      <div class="g3-ttl g3-big" style="top:60px;left:56px;color:#f5f0e6">{T.line("v5", "", title=True)}</div>
      <div class="g3-sub" style="top:960px">{T.line("v6", "")}</div>
      <div class="g3-body" style="top:1060px">{BODY}</div>'''
    pD = f'''
      {foto("d13", 50, 50, 420, 620, "green", "50% 30%")}
      {foto("d34", 490, 50, 420, 620, "green", "50% 50%")}
      <div class="g3-sub" style="top:730px;left:60px;right:60px;font-size:64px">{T.line("v7", "")}<br>{T.line("v8", "")}</div>
      <div class="g3-body" style="top:1000px">{BODY2}</div>
      <div class="g3-fol">{CREDIT}<span>14</span></div>'''
    leaves = "".join(
        f'<div class="obj g3-leaf" style="left:{x}px;top:{y}px;width:150px;height:88px;transform:rotate({r}deg)">{O.leaf(c)}</div>'
        for x, y, r, c in [(-700, -500, 20, "#8a4b1c"), (-560, 560, -40, "#a4651e"), (420, -760, 80, "#6b3a14"),
                           (980, 700, 10, "#b98a2a"), (1500, -700, -30, "#8a4b1c"), (2050, 760, 60, "#6b3a14"),
                           (2640, -780, 15, "#a4651e"), (3100, 700, -70, "#8a4b1c"), (3700, -760, 35, "#b98a2a"),
                           (4100, 640, 5, "#6b3a14"), (-300, 820, 50, "#b98a2a"), (580, 760, -10, "#a4651e")])
    torn = "clip-path:polygon(0 0,100% 0,100% 97%,96% 99%,91% 97.5%,86% 99.5%,80% 98%,74% 99.4%,68% 97.6%,61% 99.2%,55% 98%,48% 99.6%,41% 97.8%,35% 99.3%,28% 98%,21% 99.5%,14% 97.7%,8% 99.2%,3% 98%,0 99%)"
    world = f'''
      {surface("grass.jpg", "1800px 1200px")}
      {paper("g3-a", 0, 0, W, H, -3, "#f1ede4", pA, extra_style=torn)}
      {paper("g3-b", 1120, 70, W, H, 2.5, "#f1ede4", pB, extra_style=torn)}
      {paper("g3-c", 2260, -20, W, H, -1.5, "#f1ede4", pC, extra_style=torn)}
      {paper("g3-d", 3420, 60, W, H, 2, "#f1ede4", pD, extra_style=torn)}
      {leaves}
      {gobo(-1400, -1500, 3200, 2400, -30, 0.5, 6, False)}
      {gobo(2000, -1500, 3200, 2400, -30, 0.5, 6, False)}
    '''
    css = '''
.g3-ttl { position:absolute; left:60px; right:60px; font-family:"Source Serif"; font-weight:400; font-size:66px; line-height:1.02; color:#1c1c1a; letter-spacing:-.01em; }
.g3-r { left:450px; right:50px; font-size:58px; }
.g3-big { font-size:96px; line-height:.95; right:420px; }
.g3-sub { position:absolute; left:60px; right:60px; font-family:"Source Serif"; font-size:56px; line-height:1.05; color:#1c1c1a; }
.g3-sub em, .g3-ttl em { font-style:italic; color:#2e6b3a; }
.g3-body { position:absolute; left:60px; right:60px; columns:2; column-gap:34px; font-family:"Source Serif"; font-size:16px; line-height:1.38; color:#3a3a36; text-align:justify; }
.g3-fol { position:absolute; left:60px; right:60px; bottom:40px; font-family:"Source Serif"; font-size:14px; letter-spacing:.08em; color:#555; }
.g3-fol span { float:right; }
.g3-leaf { opacity:.95; }
'''
    cam = path(t0, t1, P(-140, 80, 0.66, 16, -4), [
        (t_of("v1") + 0.3, P(0, 40, 0.74, 12, -2)),
        (t_of("v3"), P(1120, 80, 0.74, 12, 2)),
        (t_of("v5"), P(2240, 0, 0.74, 12, -1)),
        (t_of("v6"), P(2260, 300, 0.82, 12, -1)),
        (t_of("v7"), P(3420, 160, 0.76, 12, 2)),
    ], mv=0.7)
    fx = fx_layers(grade="rgba(70,100,40,.25)", leak=0.5, dof_t=10, dof_b=7)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 04 — COMPUTADOR: retro-computer ads taped on a pale wall
# ======================================================================
def f04():
    fid = "04-computador"
    t0, t1 = span(fid)
    T = Typer(t0, "k4")
    W, H = 960, 1320
    scr = lambda img: ph(img, 0, 0, 300, 222, "border-radius:30px")
    pA = f'''
      <div class="k4-mast" data-layout-allow-overlap>{rainbow("AMOR")}</div>
      {prop(O.crt(), 150, 300, 660, 707, 0, "filter:drop-shadow(0 30px 30px rgba(0,0,0,.35))")}
      <div class="obj" style="left:268px;top:354px;width:390px;height:262px;border-radius:34px;overflow:hidden">{foto("d28", 0, 0, 390, 262, "pink", "50% 40%")}</div>
      <div class="k4-ser" style="top:1010px">{T.line("p1", "", title=True)}<div class="k4-s2">{T.line("p5", "", title=True)}</div></div>
      <div class="k4-fine">{CREDIT}</div>'''
    pB = f'''
      <div class="k4-blk">{T.line("p2", "", upper=True)}</div>
      {prop(O.crt("#203a52"), 150, 640, 660, 707)}
      <div class="obj" style="left:268px;top:694px;width:390px;height:262px;border-radius:34px;overflow:hidden">{foto("d05", 0, 0, 390, 262, "teal2", "50% 45%")}</div>
      <div class="k4-foot">TANTO FAZ | {YEAR}</div>'''
    pC = f'''
      <div class="k4-blk k4-blk2">{T.line("p3", "", upper=True)}<br>{T.line("p4", "", upper=True)}</div>
      {prop(O.phone("#3fb5d8"), 470, 760, 420, 540, 18)}
      <div class="k4-foot" style="background:#e8467c">TANTO FAZ | {YEAR}</div>'''
    tape = lambda x, y, r: f'<div class="k4-tape" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"></div>'
    world = f'''
      {surface("wall.jpg", "2000px 1200px")}
      {paper("k4-a", 0, 0, W, H, -1.2, "#f4f2ec", pA)}
      {paper("k4-b", 1080, 30, W, H, 1.4, "#0d0f14", pB, extra_style="background:linear-gradient(#0d0f14 55%, #2b9fb0)")}
      {paper("k4-c", 2160, -10, W, H, -1.0, "#111", pC, extra_style="background:linear-gradient(#141018 50%, #e8467c)")}
      {tape(-120, -690, -6)}{tape(960, -660, 5)}{tape(2040, -700, -4)}
      {gobo(-1200, -1400, 3600, 2600, -14, 0.38, 5)}
    '''
    css = '''
.k4-mast { position:absolute; left:0; right:0; top:40px; text-align:center; font-family:"League Spartan"; font-weight:900; font-size:250px; line-height:1; letter-spacing:-.05em; }
.k4-ser { position:absolute; left:40px; right:40px; text-align:center; font-family:"Source Serif"; font-size:60px; line-height:1.05; color:#1d1d1d; }
.k4-s2 { font-size:44px; color:#555; margin-top:10px; }
.k4-fine { position:absolute; left:0; right:0; bottom:36px; text-align:center; font-family:"Source Serif"; font-size:15px; color:#666; }
.k4-blk { position:absolute; left:50px; right:50px; top:50px; text-align:center; font-family:"Archivo Black"; font-size:104px; line-height:.92; color:#fff; letter-spacing:-.01em; }
.k4-blk2 { font-size:96px; }
.k4-foot { position:absolute; left:0; right:0; bottom:0; padding:22px; text-align:center; font-family:"Archivo"; font-weight:800; font-size:26px; letter-spacing:.1em; color:#111; background:#3fb5d8; }
.k4-tape { position:absolute; width:240px; height:64px; background:rgba(235,230,210,.7); box-shadow:0 2px 3px rgba(0,0,0,.15); }
'''
    cam = path(t0, t1, P(0, -520, 0.62, 6, -3), [
        (t_of("p1"), P(0, 320, 0.8, 8, -1)),
        (t_of("p2"), P(1080, -120, 0.74, 8, 1.5)),
        (t_of("p3"), P(2160, -160, 0.74, 8, -1)),
        (t_of("p5"), P(0, 380, 0.82, 8, -1)),
    ], mv=0.75)
    keys_extra = ""
    fx = fx_layers(grade="rgba(40,70,90,.18)", leak=0.45, dof_t=7, dof_b=6)
    return finish(fid, t0, t1, css, world, fx, T, cam, keys_extra)


# ======================================================================
# 05 — JORNAL: a pink-accented newspaper on a desk
# ======================================================================
def f05():
    fid = "05-jornal"
    t0, t1 = span(fid)
    T = Typer(t0, "n5")
    W, H = 1000, 1340
    front = f'''
      <div class="n5-mast">O TANTO FAZ</div>
      <div class="n5-date">EDIÇÃO DE DOMINGO · {YEAR} · ANO I · Nº 1</div>
      {foto("d25", 50, 210, 520, 600, "mono", "50% 40%")}
      <div class="n5-hd">{T.line("n1", "")}</div>
      <div class="n5-hd2">{T.line("n2", "")}</div>
      <div class="n5-body" style="top:1010px">{BODY} {BODY2}</div>'''
    inner = f'''
      <div class="n5-k">{T.line("n3", "")}</div>
      <div class="n5-rule"></div>
      <div class="n5-huge">{T.line("n4", "", title=True)}</div>
      {foto("d27", 560, 520, 380, 470, "pink", "50% 30%")}
      <div class="n5-pink"><b>{T.line("n5", "")}</b><br>{T.line("n6", "")}</div>
      <div class="n5-body" style="top:1040px">{BODY2}</div>'''
    quote = f'''
      {foto("d35", 0, 0, W, 660, "warm", "50% 45%")}
      <div class="n5-q">{T.line("n7", "", pre="“")}<br>{T.line("n8", "")}<br>{T.line("n9", "", post="”")}</div>
      <div class="n5-sig">— {CREDIT.upper()}</div>'''
    world = f'''
      {surface("wood.jpg", "2400px 1600px", "filter:brightness(.85)")}
      {paper("n5-f", 0, 0, W, H, -2, "#ebe7dc", front)}
      {paper("n5-i", 1180, 80, W, H, 1.6, "#ebe7dc", inner)}
      {paper("n5-q", 2380, -20, W, H, -1.4, "#ebe7dc", quote)}
      {prop(O.cassette(), -900, -500, 420, 270, 24)}
      <div class="obj" style="left:-860px;top:500px;width:520px;height:18px;transform:rotate(-30deg);background:linear-gradient(#222,#000);border-radius:10px;box-shadow:0 16px 16px rgba(0,0,0,.45)"></div>
      <div class="obj" style="left:1750px;top:-860px;width:110px;height:34px;transform:rotate(14deg);background:#d8d2c2;box-shadow:0 10px 10px rgba(0,0,0,.4)"></div>
      {gobo(-1300, -1500, 3600, 2600, -26, 0.5, 5)}
    '''
    css = '''
.n5-mast { position:absolute; left:40px; right:40px; top:24px; text-align:center; font-family:"Source Serif"; font-weight:600; font-size:120px; letter-spacing:-.03em; color:#111; border-bottom:6px solid #111; line-height:1.05; }
.n5-date { position:absolute; left:40px; right:40px; top:168px; text-align:center; font-family:"Archivo"; font-weight:800; font-size:18px; letter-spacing:.12em; color:#e8467c; }
.n5-hd { position:absolute; left:600px; right:40px; top:220px; font-family:"Archivo Black"; font-size:58px; line-height:.98; color:#1a1a1a; }
.n5-hd2 { position:absolute; left:50px; right:40px; top:840px; font-family:"Archivo"; font-weight:900; font-style:italic; font-size:92px; line-height:1; color:#e8467c; }
.n5-hd2 em { color:#111; }
.n5-body { position:absolute; left:50px; right:50px; columns:3; column-gap:30px; font-family:"Source Serif"; font-size:16px; line-height:1.36; color:#2a2a2a; text-align:justify; }
.n5-k { position:absolute; left:50px; top:50px; font-family:"Archivo"; font-weight:900; font-style:italic; font-size:64px; color:#555; }
.n5-rule { position:absolute; left:50px; right:50px; top:140px; height:10px; background:#e8467c; }
.n5-huge { position:absolute; left:50px; right:50px; top:170px; font-family:"Archivo Black"; font-size:118px; line-height:.92; color:#2a2a2a; letter-spacing:-.02em; }
.n5-pink { position:absolute; left:50px; top:540px; width:470px; padding:34px; background:#e8467c; color:#fff; font-family:"Archivo"; font-weight:800; font-size:50px; line-height:1.02; }
.n5-pink b { font-weight:900; font-style:italic; }
.n5-pink em { color:#111; }
.n5-q { position:absolute; left:60px; right:60px; top:700px; font-family:"Source Serif"; font-size:60px; line-height:1.05; color:#1a1a1a; }
.n5-q em { color:#e8467c; font-weight:600; }
.n5-sig { position:absolute; left:60px; bottom:50px; font-family:"Archivo"; font-weight:800; letter-spacing:.1em; color:#e8467c; font-size:22px; }
'''
    cam = path(t0, t1, P(-300, -360, 0.6, 18, -7), [
        (t_of("n1"), P(80, -60, 0.78, 12, -2)),
        (t_of("n2"), P(0, 420, 0.8, 12, -2)),
        (t_of("n3"), P(1180, -160, 0.8, 12, 1.5)),
        (t_of("n5"), P(1060, 320, 0.86, 12, 1.5)),
        (t_of("n7"), P(2380, 220, 0.8, 12, -1.4)),
    ], mv=0.75)
    fx = fx_layers(grade="rgba(90,40,60,.18)", leak=0.55, dof_t=10, dof_b=7)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 06 — MURO: repeated wheat-paste posters on a concrete wall
# ======================================================================
def f06():
    fid = "06-muro"
    t0, t1 = span(fid)
    T = Typer(t0, "w6")
    W, H = 640, 920
    rows = [("m1", "PACIENTE", "d38"), ("m2", "FRENTE", "d16"), ("m3", "GENTE", "d23"),
            ("m4", "ENTENDE", "d28"), ("m5", "REPENTE", "d09"), ("m6", "QUENTE", "d37")]

    def poster(lid, word, obj, live, tone):
        words = LYR[lid]
        if live:
            strip = T.line(lid, "", upper=True)
            big = T.text(word, words[-1][1] - 0.05, "", 0.06)
        else:
            strip = " ".join(w.replace("*", "").upper() for w, _ in words)
            big = word
        bg = {"y": "#e9d23a", "g": "#cfcac0", "k": "#1b1a17"}[tone]
        fg = "#151411" if tone != "k" else "#e9d23a"
        size = min(210, int(1150 / max(5, len(word))))
        return (bg, f'''
          <div class="w6-big" style="color:{fg};font-size:{size}px">{big}</div>
          <div class="w6-ph" style="background:{fg}">{foto(obj, 0, 0, 560, 380, "mono", "50% 30%")}
            <div style="position:absolute;inset:0;background:{bg};mix-blend-mode:multiply;opacity:{.85 if tone == 'y' else .35}"></div></div>
          <div class="w6-strip" style="{'background:#151411;color:#e9d23a' if tone != 'k' else 'background:#e9d23a;color:#151411'}">{strip}</div>
          <div class="w6-sm" style="color:{fg}">TANTO FAZ</div><div class="w6-sm w6-yr" style="color:{fg}">{YEAR}</div>''')

    papers = []
    x = 0
    stops = []
    for i, (lid, word, obj) in enumerate(rows):
        for k, tone in enumerate(["g", "y", "k"] if i % 2 == 0 else ["k", "y", "g"]):
            live = tone == "y"
            bg, inner = poster(lid, word, obj, live, tone)
            rot = [-1.2, 0.6, 1.4][k] * (1 if i % 2 else -1)
            papers.append(paper(f"w6-{i}-{k}", x, (k - 1) * 14, W, H, rot, bg, inner, crease=True))
            if live:
                stops.append((t_of(lid), P(x, 120, 0.86, 7, -1.5 if i % 2 else 1.5)))
            x += W + 16
    rips = "".join(f'<div class="w6-rip" style="left:{80 + i*537}px;top:{(-505 + (i*7) % 30) if i % 2 else (432 + (i*11) % 24)}px;transform:rotate({(i*37)%40-20}deg)"></div>' for i in range(16))
    world = f'''
      {surface("concrete.jpg", "2400px 1600px", w=15400)}
      {"".join(papers)}
      {rips}
      {gobo(-1500, -1600, 4800, 2800, -16, 0.55, 6)}
      {gobo(3300, -1600, 4800, 2800, -16, 0.55, 6)}
      {gobo(8100, -1600, 4800, 2800, -16, 0.55, 6)}
    '''
    css = '''
.w6-big { position:absolute; left:20px; right:20px; top:24px; text-align:center; font-family:Anton; line-height:.9; letter-spacing:-.01em; white-space:nowrap; }
.w6-ph { position:absolute; left:40px; top:300px; width:560px; height:380px; overflow:hidden; }
.w6-strip { position:absolute; left:26px; right:26px; top:705px; padding:10px 14px; font-family:"Bebas Neue"; font-size:50px; line-height:.98; transform:rotate(-2deg); }
.w6-sm { position:absolute; left:40px; bottom:40px; font-family:"Bebas Neue"; font-size:30px; letter-spacing:.1em; }
.w6-yr { left:auto; right:40px; }
.w6-rip { position:absolute; width:150px; height:46px; background:#e9e4d6; opacity:.8; }
'''
    cam = path(t0, t1, P(-400, -200, 0.62, 10, 6), stops, mv=0.85)
    fx = fx_layers(grade="rgba(80,70,30,.22)", leak=0.55, dof_t=10, dof_b=7)
    return finish(fid, t0, t1, css, world, fx, T, cam)


# ======================================================================
# 07 — ROSA: pink fashion pages + a red-car magazine ad
# ======================================================================
def f07():
    fid = "07-rosa"
    t0, t1 = span(fid)
    T = Typer(t0, "r7")
    W, H = 980, 1300
    pA = f'''
      {foto("d26", 0, 0, W, H, "pink", "40% 50%")}
      <div style="position:absolute;left:0;right:0;top:0;height:400px;background:linear-gradient(rgba(60,0,20,.6),rgba(60,0,20,0))"></div>
      <div class="r7-s" style="top:80px;left:60px;right:60px;color:#fff">{T.line("r1", "")}</div>
      <div class="r7-fine" style="color:#fbe3ea">BOMFIM — TANTO FAZ · Pág. 22</div>'''
    pB = f'''
      {foto("d12", 0, 0, W, 520, "pink", "50% 35%")}
      <div class="r7-s" style="top:580px;left:60px;right:60px;color:#1d1d1d;font-size:66px">{T.line("r2", "", pre="…")}</div>
      <div class="r7-body" style="top:860px;right:380px">{BODY}</div>
      {prop(O.lipstick(), 700, 820, 140, 420, 8)}
      <div class="r7-logo">TANTO FAZ</div>'''
    pC = f'''
      <div class="r7-ad">{T.line("r3", "", upper=True)}</div>
      <div class="r7-body r7-dark" style="top:470px;left:520px">{BODY2}</div>
      <div class="r7-body r7-dark" style="top:470px;right:500px">{BODY}</div>
      {prop(O.car(), 60, 860, 860, 362, 0, "filter:drop-shadow(0 30px 30px rgba(0,0,0,.8)) saturate(1.1)")}
      <div class="r7-tag">{CREDIT.upper()}</div>'''
    pD = f'''
      {foto("d07", 0, 0, W, H, "night", "55% 30%")}
      <div style="position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(rgba(20,0,10,.75),rgba(20,0,10,0))"></div>
      <div class="r7-s" style="top:90px;left:60px;right:60px;color:#fff;font-size:82px">{T.line("r4", "")}</div>
      <div class="r7-s" style="top:480px;left:60px;color:#f2a6bd;font-size:66px"><em>{T.line("r5", "")}</em></div>'''
    world = f'''
      {surface("wood.jpg", "2400px 1600px", "filter:hue-rotate(-12deg) brightness(.8)")}
      {paper("r7-a", 0, 0, W, H, -2, "#e8467c", pA)}
      {paper("r7-b", 1140, 60, W, H, 2, "#f1ede4", pB)}
      {paper("r7-c", 2300, -10, W, H, -1.5, "#0c0c0c", pC)}
      {paper("r7-d", 3460, 50, W, H, 2.2, "#200a14", pD)}
      {prop(O.perfume("#f2a6bd"), -820, 300, 300, 420, -18)}
      {prop(O.ring(), 1700, -860, 240, 240, 10)}
      {gobo(-1300, -1500, 3600, 2600, -24, 0.5, 5)}
      {gobo(2300, -1500, 3600, 2600, -24, 0.5, 5)}
    '''
    css = '''
.r7-s { position:absolute; font-family:"Source Serif"; font-weight:400; font-size:76px; line-height:1.03; letter-spacing:-.01em; }
.r7-s em { font-style:italic; }
.r7-fine { position:absolute; left:60px; bottom:40px; font-family:"Source Serif"; font-size:16px; }
.r7-body { position:absolute; left:60px; font-family:"Source Serif"; font-size:17px; line-height:1.4; color:#333; text-align:justify; }
.r7-dark { color:#ddd; width:400px; font-family:"Archivo"; font-size:16px; }
.r7-logo { position:absolute; left:60px; bottom:50px; font-family:"Source Serif"; font-size:60px; color:#e8467c; letter-spacing:.02em; }
.r7-ad { position:absolute; left:50px; right:50px; top:60px; text-align:center; font-family:"Archivo Black"; font-size:92px; line-height:.94; color:#fff; letter-spacing:-.01em; }
.r7-tag { position:absolute; left:0; right:0; bottom:40px; text-align:center; font-family:"Archivo Black"; font-size:28px; color:#fff; }
'''
    cam = path(t0, t1, P(-200, 300, 0.6, 16, -6), [
        (t_of("r1"), P(0, -40, 0.76, 12, -2)),
        (t_of("r2"), P(1140, 200, 0.78, 12, 2)),
        (t_of("r3"), P(2300, -60, 0.78, 12, -1.5)),
        (t_of("r4"), P(3460, -40, 0.78, 12, 2)),
    ], mv=0.75)
    fx = fx_layers(grade="rgba(120,30,60,.22)", leak=0.6, dof_t=10, dof_b=7)
    return finish(fid, t0, t1, css, world, fx, T, cam)


SCATTER_JS = """
        // letters fly in from scattered positions (deterministic offsets)
        TYPE.forEach(([sel, times]) => {
          const el = q(sel);
          if (!el || !el.classList.contains("scat")) return;
          qa(sel + " .ch").forEach((c, i) => {
            const t = times[Math.min(i, times.length - 1)];
            const dx = (((i * 73) % 29) - 14) * 18, dy = (((i * 47) % 23) - 11) * 22, r = ((i * 31) % 50) - 25;
            tl.fromTo(c, { x: dx, y: dy, rotation: r }, { x: 0, y: 0, rotation: 0, duration: 0.55, ease: "power3.out", immediateRender: true }, Math.max(0, t - 0.05));
          });
        });
"""


# ======================================================================
# 08 — ENCARTE: CD-booklet / zine pages, techno caps assembling
# ======================================================================
def f08():
    fid = "08-encarte"
    t0, t1 = span(fid)
    T = Typer(t0, "e8")
    W, H = 1000, 1300
    pA = f'''
      {foto("d05", 50, 60, 300, 380, "pink", "50% 40%")}
      {foto("d35", 50, 460, 300, 300, "teal2", "50% 50%")}
      <div class="e8-t" style="left:390px;top:70px">{T.line("f1", "scat", upper=True)}</div>
      <div class="e8-t" style="left:390px;top:610px;font-size:38px;color:#e8467c">{T.line("f2", "scat", upper=True)}</div>
      <div class="e8-b" style="left:390px;top:860px">{BODY}</div>'''
    pB = f'''
      {foto("d06", 0, 0, W, H, "teal2", "50% 30%")}
      <div style="position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))"></div>
      <div class="e8-t" style="left:60px;right:60px;top:80px;color:#fff;font-size:68px">{T.line("f3", "scat", upper=True)}</div>
      <div class="e8-b" style="left:60px;top:1020px;width:440px;color:#ccc">{BODY2}</div>'''
    pC = f'''
      {prop(O.bag("#e8467c"), 520, 520, 380, 500, 6)}
      {prop(O.bag("#3fb5d8", "AMOR"), 300, 640, 300, 400, -10)}
      <div class="e8-t" style="left:60px;right:60px;top:70px">{T.line("f4", "scat", upper=True)}</div>
      <div class="e8-t" style="left:60px;right:420px;top:420px;font-size:40px;color:#3fb5d8">{T.line("f5", "scat", upper=True)}</div>
      <div class="e8-b" style="left:60px;top:1060px;width:420px">{BODY2}</div>'''
    pD = f'''
      {foto("d33", 0, 0, W, 760, "teal", "50% 20%")}
      <div class="c1-grad" style="position:absolute;inset:0;background:linear-gradient(to bottom, rgba(15,23,24,0) 30%, #0f1718 60%)"></div>
      <div class="e8-s" style="top:600px">{T.line("f6", "", title=True)}<div style="font-style:italic;margin-top:14px">{T.line("f7", "", title=True)}</div></div>
      <div class="e8-b" style="left:70px;right:70px;top:930px;columns:2;column-gap:40px;color:#c9d4d0">{BODY} {BODY2}</div>'''
    world = f'''
      {surface("wall.jpg", "2000px 1200px", "filter:brightness(.92)")}
      {paper("e8-a", 0, 0, W, H, -1.5, "#f6f4ef", pA)}
      {paper("e8-b", 1150, 50, W, H, 1.8, "#0c0c0c", pB)}
      {paper("e8-c", 2300, -20, W, H, -1.2, "#f6f4ef", pC)}
      {paper("e8-d", 3450, 40, W, H, 1.2, "#0f1718", pD)}
      {prop(O.perfume(), -800, -400, 280, 400, 14)}
      {prop(O.rose(), 2850, -900, 260, 420, -70)}
      {gobo(-1300, -1500, 3600, 2600, -18, 0.42, 5)}
      {gobo(2400, -1500, 3600, 2600, -18, 0.42, 5)}
    '''
    css = '''
.e8-t { position:absolute; right:60px; font-family:Michroma; font-size:46px; line-height:1.12; color:#111; letter-spacing:.02em; }
.scat .ch { display:inline-block; }
.e8-b { position:absolute; right:60px; font-family:"Archivo"; font-size:16px; line-height:1.42; color:#444; text-align:justify; }
.e8-s { position:absolute; left:60px; right:60px; text-align:center; font-family:"Source Serif"; font-size:84px; line-height:1.02; color:#eef3ef; }
'''
    cam = path(t0, t1, P(-260, -300, 0.62, 14, -6), [
        (t_of("f1"), P(120, -80, 0.8, 9, -1)),
        (t_of("f3"), P(1150, -80, 0.78, 9, 1.5)),
        (t_of("f4"), P(2300, -140, 0.8, 9, -1)),
        (t_of("f6"), P(3450, 160, 0.82, 10, 1)),
    ], mv=0.75)
    fx = fx_layers(grade="rgba(40,60,80,.2)", leak=0.5, dof_t=9, dof_b=6)
    return finish(fid, t0, t1, css, world, fx, T, cam, SCATTER_JS)


# ======================================================================
# 09 — CRÉDITOS: the last poster, credits typed, fade to black
# ======================================================================
def f09():
    fid = "09-creditos"
    t0, t1 = span(fid)
    T = Typer(t0, "z9")
    W, H = 1000, 1300
    pD = f'''
      {foto("d30", 0, 0, W, 760, "teal", "50% 30%")}
      <div style="position:absolute;inset:0;background:linear-gradient(to bottom, rgba(15,23,24,0) 30%, #0f1718 60%)"></div>
      <div class="z9-s" style="top:560px">Uma Vida É Com Você.</div>
      <div class="z9-cr">{T.text(CREDIT, 153.6, "", 0.07)}</div>'''
    world = f'''
      {surface("wood.jpg", "2400px 1600px", "filter:brightness(.55)")}
      {paper("z9-d", 0, 0, W, H, 1.2, "#0f1718", pD)}
      {paper("z9-x", -1150, 120, W, H, -3, "#f6f4ef", '<div class="z9-ghost">TANTO<br>FAZ</div>')}
      {gobo(-1300, -1500, 3600, 2600, -18, 0.5, 5)}
    '''
    css = '''
.z9-s { position:absolute; left:60px; right:60px; text-align:center; font-family:"Source Serif"; font-size:88px; line-height:1.02; color:#eef3ef; }
.z9-cr { position:absolute; left:60px; right:60px; top:820px; text-align:center; font-family:"Source Serif"; font-size:40px; letter-spacing:.02em; color:#c9d4d0; }
.z9-c { position:absolute; left:90px; right:90px; top:760px; columns:2; column-gap:44px; font-family:"Source Serif"; font-size:22px; line-height:1.4; color:#c9d4d0; text-align:justify; }
.z9-c p { margin:0 0 12px; text-indent:1.2em; }
.z9-u { text-decoration:underline; }
.z9-sig { position:absolute; left:0; right:0; bottom:60px; text-align:center; font-family:"Source Serif"; font-weight:600; letter-spacing:.08em; font-size:26px; color:#eef3ef; }
.z9-ghost { position:absolute; inset:60px; font-family:"League Spartan"; font-weight:900; font-size:250px; line-height:.9; color:#e8467c; }
.z9-black { background:#000; opacity:0; }
'''
    cam = cam_js([
        dict(t=0, x=60, y=-120, s=0.82, rx=10, rz=1.5),
        dict(t=3.0, x=40, y=160, s=0.95, rx=12, rz=0.5, e="sine.inOut"),
        dict(t=9.5, x=0, y=190, s=1.0, rx=14, rz=-0.5, e="sine.inOut"),
        dict(t=round(t1 - t0, 3), x=-200, y=0, s=0.55, rx=20, rz=-4, e="sine.inOut"),
    ])
    fade = f'tl.fromTo(q(".z9-black"), {{ opacity: 0 }}, {{ opacity: 1, duration: 2.6, ease: "power1.in" }}, {round(t1 - t0 - 2.8, 3)});'
    fx = fx_layers(grade="rgba(30,80,80,.28)", leak=0.45, dof_t=9, dof_b=6, top='<div class="fx z9-black"></div>')
    return finish(fid, t0, t1, css, world, fx, T, cam, fade)


FRAMES = [f00, f01, f02, f03, f04, f05, f06, f07, f08, f09]
