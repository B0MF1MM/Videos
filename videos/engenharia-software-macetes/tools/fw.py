# Frame generator framework: shared chrome, components, and cue-word timing.
import json, os, re, unicodedata

INK = "#1F2BE0"
PAPER = "#F0EBDE"
TOTAL = 20
TAG = "ENG. SOFTWARE · MACETES"


def norm(w):
    return re.sub(r"[^\wÀ-ÿ\-]", "", w.lower()).strip("-")


class Cues:
    def __init__(self, meta_path):
        self.v = {v["frame"]: v for v in json.load(open(meta_path))["voices"]}

    def dur(self, n):
        return self.v[n]["duration_s"]

    def t(self, n, word, occ=1):
        k = 0
        for w in self.v[n]["words"]:
            if norm(w["text"]) == norm(word):
                k += 1
                if k == occ:
                    return w["start"]
        raise KeyError(f"frame {n}: cue '{word}'#{occ} not found")


CUE_RE = re.compile(r"@([A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*)(?:#(\d+))?([+-]\d+(?:\.\d+)?)?")


def resolve(js, cues, n):
    def rep(m):
        t = cues.t(n, m.group(1), int(m.group(2) or 1)) + float(m.group(3) or 0)
        return f"{max(0.0, t):.3f}"
    return CUE_RE.sub(rep, js)


# ---------- HTML components (P = per-frame prefix, e.g. "f07-") ----------

def st(x, y, w=None, h=None, extra=""):
    s = f"left:{x}px;top:{y}px;"
    if w is not None:
        s += f"width:{w}px;"
    if h is not None:
        s += f"height:{h}px;"
    return s + extra


def box(P, id, text, x, y, w, h, fs=30, font="lab", fill=True, inv=False, cls="", sub=None, subfs=26):
    inner = f'<span class="{P}t {P}{font}" style="font-size:{fs}px">{text}</span>'
    if sub:
        inner = f'<div class="{P}stack">{inner}<span class="{P}t {P}mono" style="font-size:{subfs}px">{sub}</span></div>'
    f = f'<div class="{P}fill" id="{P}{id}-f">{inner}</div>' if fill else ""
    return f'<div class="{P}box{" " + P + "inv" if inv else ""} {cls}" id="{P}{id}" style="{st(x, y, w, h)}">{inner}{f}</div>'


def txt(P, id, text, x, y, fs, font="serif", w=None, align="left", cls="", extra=""):
    ws = f"width:{w}px;" if w else ""
    return f'<div class="{P}txt {P}{font} {cls}" id="{P}{id}" style="left:{x}px;top:{y}px;{ws}font-size:{fs}px;text-align:{align};{extra}">{text}</div>'


def arrow(P, id, x, y, w, rot=0, thick=5):
    return (f'<div class="{P}arrow" id="{P}{id}" style="left:{x}px;top:{y}px;width:{w}px;height:{thick}px;'
            f'transform:rotate({rot}deg);"><i class="{P}head"></i></div>') if rot else (
            f'<div class="{P}arrow" id="{P}{id}" style="left:{x}px;top:{y}px;width:{w}px;height:{thick}px;"><i class="{P}head"></i></div>')


def stamp(P, id, text, x, y, fs=52, tag="MACETE"):
    t = f'<span class="{P}stag">{tag}</span>' if tag else ""
    return f'<div class="{P}stamp" id="{P}{id}" style="left:{x}px;top:{y}px;font-size:{fs}px;">{t}{text}</div>'


def question(P, text, tag="PERGUNTA"):
    return (f'<div class="{P}qwrap" id="{P}q"><span class="{P}qtag">{tag}</span>'
            f'<span class="{P}qtext">{text}</span></div>')


def title(P, text, tag=None):
    t = f'<span class="{P}qtag">{tag}</span>' if tag else ""
    return f'<div class="{P}qwrap {P}plain" id="{P}q">{t}<span class="{P}qtext">{text}</span></div>'


BASE_CSS = """
#root { position:absolute; inset:0; width:1920px; height:1080px; overflow:hidden; color:INK; font-family:"Hanken Grotesk", sans-serif; }
.Pground { position:absolute; inset:0; background-color:PAPER;
  background-image: linear-gradient(rgba(31,43,224,0.10) 1px, transparent 1px), linear-gradient(90deg, rgba(31,43,224,0.10) 1px, transparent 1px);
  background-size:38.4px 38.4px; background-position:-1px -1px; }
.Pstage { position:absolute; inset:0; }
.Phair { position:absolute; left:77px; right:77px; height:2px; background:INK; }
.Phair-top { top:70px; } .Phair-bot { top:892px; }
.Pchrome { position:absolute; top:30px; font-family:"DM Mono", monospace; font-size:26px; letter-spacing:0.06em; line-height:1; white-space:nowrap; }
.Pchrome-tag { left:77px; } .Pchrome-num { right:77px; }
.Pcam { position:absolute; inset:0; transform-origin:50% 48%; }
.Pqwrap { position:absolute; left:0; right:0; top:96px; display:flex; flex-direction:column; align-items:center; gap:4px; }
.Pqtag { font-family:"DM Mono", monospace; font-size:26px; letter-spacing:0.14em; background:INK; color:PAPER; padding:4px 14px 2px; }
.Pqtext { font-family:"Newsreader", serif; font-size:66px; line-height:1.08; letter-spacing:-0.01em; white-space:nowrap; }
.Pplain .Pqtag { background:transparent; color:INK; border:2px solid INK; }
.Pbox { position:absolute; border:4px solid INK; background:PAPER; box-sizing:border-box; display:flex; align-items:center; justify-content:center; text-align:center; overflow:hidden; }
.Pinv { background:INK; color:PAPER; }
.Pfill { position:absolute; inset:-1px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; text-align:center; clip-path:inset(0 100% 0 0); }
.Pstack { display:flex; flex-direction:column; align-items:center; gap:6px; }
.Pt { display:block; line-height:1.12; padding:0 12px; }
.Plab { font-family:"Hanken Grotesk", sans-serif; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; }
.Pserif { font-family:"Newsreader", serif; font-weight:400; letter-spacing:-0.01em; }
.Pmono { font-family:"DM Mono", monospace; letter-spacing:0.06em; }
.Pbody { font-family:"Hanken Grotesk", sans-serif; font-weight:400; }
.Ptxt { position:absolute; line-height:1.12; white-space:nowrap; }
.Parrow { position:absolute; background:INK; transform-origin:0% 50%; }
.Phead { position:absolute; right:-4px; top:50%; margin-top:-13px; width:0; height:0; border-left:24px solid INK; border-top:13px solid transparent; border-bottom:13px solid transparent; }
.Pstamp { position:absolute; background:INK; color:PAPER; font-family:"Newsreader", serif; padding:10px 30px 12px; white-space:nowrap; line-height:1.1; }
.Pstag { position:absolute; left:-4px; top:-40px; font-family:"DM Mono", monospace; font-size:26px; letter-spacing:0.14em; color:INK; background:PAPER; border:2px solid INK; padding:2px 10px 0; line-height:1.2; }
.Prow { position:absolute; height:92px; display:flex; align-items:center; gap:22px; border-bottom:3px solid rgba(31,43,224,0.35); box-sizing:border-box; }
.Pico { flex:0 0 64px; height:64px; border:4px solid INK; box-sizing:border-box; display:flex; align-items:center; justify-content:center; font-family:"Newsreader", serif; font-size:46px; line-height:1; }
.Pico.Pinv { background:INK; color:PAPER; }
.Prow-t { font-family:"Hanken Grotesk", sans-serif; font-weight:400; font-size:36px; white-space:nowrap; }
.Pcolhead { position:absolute; height:76px; display:flex; align-items:center; gap:18px; padding:0 22px; box-sizing:border-box; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:32px; letter-spacing:0.12em; }
.Pcolhead b { font-family:"Newsreader", serif; font-weight:400; font-size:58px; line-height:1; letter-spacing:0; }
"""

FONTS = """
    @font-face { font-family: "Newsreader"; src: url("assets/fonts/Newsreader-400.woff2") format("woff2"); font-weight: 400; font-style: normal; }
    @font-face { font-family: "Newsreader"; src: url("assets/fonts/Newsreader-400-italic.woff2") format("woff2"); font-weight: 400; font-style: italic; }
    @font-face { font-family: "Hanken Grotesk"; src: url("assets/fonts/Hanken_Grotesk-400.woff2") format("woff2"); font-weight: 400; }
    @font-face { font-family: "Hanken Grotesk"; src: url("assets/fonts/Hanken_Grotesk-600.woff2") format("woff2"); font-weight: 600; }
    @font-face { font-family: "DM Mono"; src: url("assets/fonts/DM_Mono-400.woff2") format("woff2"); font-weight: 400; }
"""

HELPERS = """
          const q = (s) => R.querySelector(s);
          const qa = (s) => Array.from(R.querySelectorAll(s));
          const pop = (s, t, o = {}) => tl.fromTo(q(s), { opacity: 0, scale: o.s ?? 0.6, y: o.y ?? 24 }, { opacity: 1, scale: 1, y: 0, duration: o.d ?? 0.5, ease: "back.out(1.7)" }, t);
          const rise = (s, t, o = {}) => tl.fromTo(q(s), { opacity: 0, y: o.y ?? 36 }, { opacity: 1, y: 0, duration: o.d ?? 0.6, ease: "power3.out" }, t);
          const slide = (s, t, dx, o = {}) => tl.fromTo(q(s), { opacity: 0, x: dx }, { opacity: 1, x: 0, duration: o.d ?? 0.6, ease: "power3.out" }, t);
          const fade = (s, t, d = 0.5) => tl.fromTo(q(s), { opacity: 0 }, { opacity: 1, duration: d, ease: "power2.out" }, t);
          const wipe = (s, t, d = 0.6) => tl.fromTo(q(s), { clipPath: "inset(-30% 100% -30% -4%)" }, { clipPath: "inset(-30% -4% -30% -4%)", duration: d, ease: "power2.inOut" }, t);
          const lit = (id, t, d = 0.35) => tl.fromTo(q(id + "-f"), { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: d, ease: "power2.inOut" }, t);
          const drawX = (s, t, d = 0.7) => tl.fromTo(q(s), { scaleX: 0 }, { scaleX: 1, duration: d, ease: "power3.inOut" }, t);
          const drawY = (s, t, d = 0.7) => tl.fromTo(q(s), { scaleY: 0 }, { scaleY: 1, duration: d, ease: "power3.inOut" }, t);
          const shake = (t) => { tl.to(q("#Pshk"), { x: 7, duration: 0.04, ease: "none" }, t); tl.to(q("#Pshk"), { x: -6, duration: 0.05, ease: "none" }, t + 0.04); tl.to(q("#Pshk"), { x: 3, duration: 0.05, ease: "none" }, t + 0.09); tl.to(q("#Pshk"), { x: 0, duration: 0.08, ease: "power2.out" }, t + 0.14); };
          const stampIn = (s, t, r = -2) => { tl.fromTo(q(s), { opacity: 0, scale: 1.9, rotation: r * 4 }, { opacity: 1, scale: 1, rotation: r, duration: 0.4, ease: "power4.in" }, t); shake(t + 0.4); };
          const bump = (s, t, k = 1.08) => { tl.to(q(s), { scale: k, duration: 0.14, ease: "power2.out" }, t); tl.to(q(s), { scale: 1, duration: 0.3, ease: "power2.out" }, t + 0.14); };
          const rows = (ids, times, dx) => ids.forEach((s, i) => slide(s, times[i], dx));
"""


def build(n, slug, cues, css, html, js, P=None):
    P = P or f"f{n:02d}-"
    cid = f"{n:02d}-{slug}"
    D = cues.dur(n)
    base = BASE_CSS.replace("INK", INK).replace("PAPER", PAPER).replace(".P", "." + P)
    css = css.replace(".P", "." + P).replace("#P", "#" + P)
    html = html.replace("#P", "#" + P)
    js = resolve(js, cues, n).replace("#P", "#" + P).replace("$D", f"{D}")
    helpers = HELPERS.replace("#P", "#" + P)
    return f"""<template>
  <script src="assets/vendor/gsap.min.js"></script>
  <style>{FONTS}{base}{css}
  </style>

  <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{D}">
    <div id="{P}ground" class="{P}ground clip" data-start="0" data-duration="{D}" data-track-index="0"></div>

    <div id="{P}stage" class="{P}stage clip" data-start="0" data-duration="{D}" data-track-index="1">
      <div class="{P}hair {P}hair-top"></div>
      <div class="{P}hair {P}hair-bot"></div>
      <div class="{P}chrome {P}chrome-tag">{TAG}</div>
      <div class="{P}chrome {P}chrome-num">{n:02d} / {TOTAL}</div>
      <div class="{P}cam" id="{P}cam"><div class="{P}cam" id="{P}shk">
{html}
      </div></div>
    </div>

    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        const D = {D};
        const R = document.querySelector('[data-composition-id="{cid}"]');
{helpers}
        tl.fromTo(q("#{P}cam"), {{ scale: 1 }}, {{ scale: 1.03, duration: D, ease: "none" }}, 0);
{js}
        tl.to({{}}, {{ duration: 0.001 }}, D - 0.001);
        window.__timelines = window.__timelines || {{}};
        window.__timelines["{cid}"] = tl;
      }})();
    </script>
  </div>
</template>
"""


def procon(P, left, right, y0=330, gap=104, lx=150, rx=1000, w=770):
    """left/right: lists of (id, glyph, text). Returns html with column heads + rows."""
    h = [f'<div class="{P}colhead {P}inv" id="{P}hl" style="left:{lx}px;top:{y0 - 106}px;width:{w}px;"><b>+</b>VANTAGENS</div>',
         f'<div class="{P}colhead" id="{P}hr" style="left:{rx}px;top:{y0 - 106}px;width:{w}px;border:4px solid {INK};"><b>–</b>DESVANTAGENS</div>']
    for col, x, inv in ((left, lx, True), (right, rx, False)):
        for i, (id, g, t) in enumerate(col):
            h.append(f'<div class="{P}row" id="{P}{id}" style="left:{x}px;top:{y0 + i * gap}px;width:{w}px;">'
                     f'<div class="{P}ico{" " + P + "inv" if inv else ""}">{g}</div><div class="{P}row-t">{t}</div></div>')
    return "\n".join(h)
