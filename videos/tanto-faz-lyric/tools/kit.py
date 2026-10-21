"""Shared kit for the print-on-surface lyric video.

Every frame is a 3D "set": a textured surface (wood, cork, grass, concrete) with
printed pieces lying on it, seen by a slow camera with tilt-shift depth of
field, window-light shadows, a light leak, vignette and film grain. Lyrics are
typeset INTO the prints and typed on letter by letter as they are sung.
"""
import html
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")


# ----------------------------------------------------------------- lyrics --
def load_lyrics():
    lines = {}
    for raw in open(os.path.join(ROOT, "lyrics.txt"), encoding="utf-8"):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        m = re.match(r"\[([\w-]+)\]\s*(.*)", raw)
        if not m:
            continue
        lid, rest = m.groups()
        words = []
        for tok in rest.split():
            if "@" in tok:
                w, t = tok.rsplit("@", 1)
                words.append([w, float(t)])
            else:
                words.append([tok, None])
        # fill missing times: untimed words are spread between the previous
        # timed word and the next one (e.g. "lá da toca,@14.10")
        timed = [i for i, w in enumerate(words) if w[1] is not None]
        for i, w in enumerate(words):
            if w[1] is not None:
                continue
            prv = max([j for j in timed if j < i], default=None)
            nxt = min([j for j in timed if j > i], default=None)
            if prv is not None and nxt is not None:
                f = (i - prv) / (nxt - prv)
                w[1] = round(words[prv][1] + f * (words[nxt][1] - words[prv][1]), 3)
            elif nxt is not None:
                w[1] = round(words[nxt][1] - 0.15 * (nxt - i), 3)
            elif prv is not None:
                w[1] = round(words[prv][1] + 0.25 * (i - prv), 3)
            else:
                w[1] = 0.0
        lines[lid] = words
    return lines


LYR = load_lyrics()


class Typer:
    """Collects per-character reveal times for one frame."""

    def __init__(self, t0, pfx=""):
        self.t0 = t0
        self.pfx = pfx
        self.tracks = []  # (selector, [times])
        self.n = 0

    def text(self, txt, t, cls="", step=0.05, tag="span", style=""):
        """Free (non-lyric) text typed from track time t."""
        words, tt = [], t
        for w in txt.split(" "):
            words.append([w, tt])
            tt += step * (len(w) + 1)
        return self._emit(words, f"tx{self.n}", cls, False, step, tag, style, 0.0, False)

    def line(self, lid, cls="", upper=False, step_max=0.055, tag="span", style="", shift=0.0, title=False, pre="", post=""):
        """Return HTML for lyric line `lid`; registers char timings.
        pre/post (e.g. quote marks) are typed with the first/last word."""
        words = [list(w) for w in LYR[lid]]
        if pre:
            words[0][0] = pre + words[0][0]
        if post:
            words[-1][0] = words[-1][0] + post
        return self._emit(words, lid, cls, upper, step_max, tag, style, shift, title)

    def lines(self, lids, sep="<br>", **kw):
        return sep.join(self.line(l, **kw) for l in lids)

    def _emit(self, words, lid, cls, upper, step_max, tag, style, shift, title):
        self.n += 1
        el_id = f"{self.pfx}-ly-{lid}-{self.n}"
        out, times = [], []
        em = False
        for i, (w, t) in enumerate(words):
            nxt = words[i + 1][1] if i + 1 < len(words) else t + 0.6
            txt = w
            open_em = txt.startswith("*")
            close_em = txt.endswith("*") or txt.endswith("*.") or txt.endswith("*,")
            txt = txt.replace("*", "")
            if title and txt:
                k = 0
                while k < len(txt) and not txt[k].isalpha():
                    k += 1
                txt = txt[:k] + txt[k:k + 1].upper() + txt[k + 1:]
            if upper:
                txt = txt.upper()
            if open_em:
                em = True
            n = max(1, len(txt))
            step = min(step_max, max(0.012, (nxt - t) * 0.8 / n))
            chars = "".join(f'<span class="ch">{html.escape(c)}</span>' for c in txt)
            word = f'<span class="wd">{chars}</span>'
            if em:
                word = f"<em>{word}</em>"
            out.append(word)
            for k in range(len(txt)):
                times.append(round(t + shift - self.t0 + k * step, 3))
            if close_em:
                em = False
        self.tracks.append((f"#{el_id}", times))
        st = f' style="{style}"' if style else ""
        return f'<{tag} class="ly {cls}" id="{el_id}" data-layout-allow-overlap{st}>{" ".join(out)}</{tag}>'

    def js(self):
        return "const TYPE = " + json.dumps(self.tracks, separators=(",", ":")) + ";"


def t_of(lid, word_index=0):
    return LYR[lid][word_index][1]


def t_end(lid):
    return LYR[lid][-1][1] + 0.5


# ------------------------------------------------------------------- fonts --
FONTS = [
    ("Source Serif", "source-serif-4-300-normal", 300, "normal"),
    ("Source Serif", "source-serif-4-400-normal", 400, "normal"),
    ("Source Serif", "source-serif-4-400-italic", 400, "italic"),
    ("Source Serif", "source-serif-4-600-normal", 600, "normal"),
    ("Source Serif", "source-serif-4-600-italic", 600, "italic"),
    ("Anton", "anton-400-normal", 400, "normal"),
    ("Archivo Black", "archivo-black-400-normal", 400, "normal"),
    ("Archivo", "archivo-400-normal", 400, "normal"),
    ("Archivo", "archivo-500-normal", 500, "normal"),
    ("Archivo", "archivo-800-normal", 800, "normal"),
    ("Archivo", "archivo-900-italic", 900, "italic"),
    ("League Spartan", "league-spartan-700-normal", 700, "normal"),
    ("League Spartan", "league-spartan-900-normal", 900, "normal"),
    ("Bebas Neue", "bebas-neue-400-normal", 400, "normal"),
    ("DM Mono", "dm-mono-400-normal", 400, "normal"),
    ("Michroma", "michroma-400-normal", 400, "normal"),
    ("Oswald", "oswald-700-normal", 700, "normal"),
]


def font_css():
    return "\n".join(
        f'@font-face{{font-family:"{f}";src:url("assets/fonts/{n}.woff2") format("woff2");font-weight:{w};font-style:{s};font-display:block}}'
        for f, n, w, s in FONTS
    )


# --------------------------------------------------------------- base css --
def base_css(fid):
    return f"""
{font_css()}
[data-composition-id="{fid}"] {{ position:absolute; inset:0; width:1920px; height:1080px; overflow:hidden; background:#0b0a09; }}
[data-composition-id="{fid}"] * {{ box-sizing:border-box; }}
.stage {{ position:absolute; inset:0; perspective:2400px; perspective-origin:50% 45%; overflow:hidden; }}
.world {{ position:absolute; left:0; top:0; width:0; height:0; transform-style:preserve-3d; transform-origin:0 0; will-change:transform; }}
.surface {{ position:absolute; background-size:cover; }}
.obj {{ position:absolute; transform-origin:50% 50%; }}
.paper {{ position:absolute; overflow:hidden; transform-origin:50% 50%;
  box-shadow: 0 2px 3px rgba(0,0,0,.35), 0 28px 50px -10px rgba(0,0,0,.55), 0 60px 120px -30px rgba(0,0,0,.45); }}
.paper > .tex {{ position:absolute; inset:0; pointer-events:none; background:url("assets/img/paper.jpg") center/700px; mix-blend-mode:multiply; opacity:.55; z-index:50; }}
.paper > .curl {{ position:absolute; inset:0; pointer-events:none; z-index:51;
  background: linear-gradient(115deg, rgba(255,255,255,.10) 0%, rgba(255,255,255,0) 30%, rgba(0,0,0,0) 62%, rgba(0,0,0,.16) 100%); }}
.paper > .crease {{ position:absolute; inset:0; pointer-events:none; z-index:52; background:url("assets/img/crumple.jpg") center/cover; mix-blend-mode:soft-light; opacity:.55; }}
.photo {{ position:absolute; overflow:hidden; background-size:cover; background-position:center; }}
.prop {{ position:absolute; transform-origin:50% 50%; filter: drop-shadow(0 26px 24px rgba(0,0,0,.55)) saturate(.82) contrast(1.06); }}
.phfx {{ position:absolute; pointer-events:none; box-shadow: inset 0 0 140px rgba(0,0,0,.5);
   background: linear-gradient(160deg, rgba(255,255,255,.10), rgba(255,255,255,0) 45%); }}
.phfx::after {{ content:""; position:absolute; inset:0; background:url("assets/img/grain.png") 0 0/256px; mix-blend-mode:overlay; opacity:.35; }}
.ly .ch {{ opacity:0; }}
.ly .wd {{ white-space:nowrap; }}
.ly em {{ font-style:italic; }}
.fx {{ position:absolute; inset:0; pointer-events:none; }}
.fx-dof-t {{ bottom:auto; height:44%; backdrop-filter: blur(var(--dt, 7px)); -webkit-backdrop-filter: blur(var(--dt, 7px));
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, rgba(0,0,0,.6) 41%, transparent 91%);
          mask-image: linear-gradient(to bottom, #000 0%, rgba(0,0,0,.6) 41%, transparent 91%); }}
.fx-dof-b {{ top:auto; height:36%; backdrop-filter: blur(var(--db, 5px)); -webkit-backdrop-filter: blur(var(--db, 5px));
  -webkit-mask-image: linear-gradient(to top, #000 0%, rgba(0,0,0,.55) 39%, transparent 94%);
          mask-image: linear-gradient(to top, #000 0%, rgba(0,0,0,.55) 39%, transparent 94%); }}
.fx-leak {{ left:-30%; top:-30%; width:160%; height:160%; inset:auto; mix-blend-mode:screen; opacity:.5;
  background: radial-gradient(40% 35% at 12% 18%, rgba(255,170,90,.55), rgba(255,120,60,0) 70%),
              radial-gradient(30% 40% at 92% 90%, rgba(255,210,150,.25), rgba(255,200,150,0) 70%); }}
.fx-vig {{ background: radial-gradient(120% 95% at 50% 48%, rgba(0,0,0,0) 45%, rgba(0,0,0,.42) 78%, rgba(0,0,0,.78) 100%); }}
.fx-grade {{ mix-blend-mode:soft-light; }}
.fx-grain {{ background:url("assets/img/grain.png"); background-size:512px 512px; mix-blend-mode:overlay; opacity:.22; }}
.gobo {{ position:absolute; pointer-events:none; mix-blend-mode:multiply; }}
"""


def fx_layers(grade="rgba(40,90,90,.35)", leak=0.5, dof_t=7, dof_b=5, extra="", top=""):
    return f"""
    <div class="fx fx-dof-t" style="--dt:{dof_t}px"></div>
    <div class="fx fx-dof-b" style="--db:{dof_b}px"></div>
    {extra}
    <div class="fx fx-grade" style="background:{grade}"></div>
    <div class="fx fx-leak" style="opacity:{leak}"></div>
    <div class="fx fx-vig"></div>
    <div class="fx fx-grain"></div>
    {top}
"""


def gobo(x, y, w, h, rot=-18, strength=0.55, bars=4, cross=True):
    """Window-light shadow lying on the surface (in world space); pre-blurred PNG."""
    img = "gobo-a.png" if cross else "gobo-b.png"
    return (f'<div class="gobo" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'transform:rotate({rot}deg);opacity:{min(1, strength * 1.25):.2f};'
            f'background:url(assets/img/{img}) center/100% 100% no-repeat;"></div>')


def paper(id_, x, y, w, h, rot=0, bg="#f1ede4", inner="", cls="", crease=False, z=0, extra_style=""):
    zt = f" translateZ({z}px)" if z else ""
    return (f'<div class="paper {cls}" id="{id_}" style="left:{x - w/2}px;top:{y - h/2}px;width:{w}px;height:{h}px;'
            f'background:{bg};transform:rotate({rot}deg){zt};{extra_style}">{inner}'
            f'<div class="tex"></div>{"<div class=crease></div>" if crease else ""}<div class="curl"></div></div>')


# ------------------------------------------------------------------- frame --
def frame_html(fid, dur, css, world, fx, script, bg="#0b0a09"):
    return f"""<template id="{fid}-template">
  <script src="assets/vendor/gsap.min.js"></script>
  <style>
{base_css(fid)}
{css}
  </style>
  <div id="root" data-composition-id="{fid}" data-width="1920" data-height="1080" data-duration="{dur:.3f}" style="background:{bg}">
    <div class="stage" data-layout-allow-overflow>
      <div class="world" data-layout-allow-overflow>
{world}
      </div>
    </div>
{fx}
    <script>
      (function () {{
        const R = document.querySelector('[data-composition-id="{fid}"]');
        const q = (s) => R.querySelector(s);
        const qa = (s) => Array.from(R.querySelectorAll(s));
        const tl = gsap.timeline({{ paused: true }});
        const D = {dur:.3f};

        // ---- camera: one state object, one writer ----
        const world = q(".world");
        const cam = {{ x: 0, y: 0, z: 0, rx: 0, rz: 0, s: 1 }};
        function applyCamera() {{
          world.style.transform = `translate3d(960px, 540px, ${{cam.z}}px) rotateX(${{cam.rx}}deg) rotateZ(${{cam.rz}}deg) scale(${{cam.s}}) translate(${{-cam.x}}px, ${{-cam.y}}px)`;
        }}
        function shot(keys) {{
          Object.assign(cam, keys[0]);
          delete cam.t; delete cam.e;
          applyCamera();
          tl.set(cam, Object.assign({{}}, strip(keys[0]), {{ onUpdate: applyCamera }}), 0);
          for (let i = 1; i < keys.length; i++) {{
            const a = keys[i - 1], b = keys[i];
            tl.to(cam, Object.assign(strip(b), {{ duration: b.t - a.t, ease: b.e || "sine.inOut", onUpdate: applyCamera }}), a.t);
          }}
        }}
        function strip(k) {{ const o = Object.assign({{}}, k); delete o.t; delete o.e; return o; }}

        // ---- typing ----
        function typeOn(TYPE) {{
          TYPE.forEach(([sel, times]) => {{
            const chars = qa(sel + " .ch");
            chars.forEach((c, i) => {{
              const t = times[Math.min(i, times.length - 1)];
              tl.fromTo(c, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.05, ease: "none", immediateRender: false }}, Math.max(0, t));
            }});
          }});
        }}

        // ---- film grain: stepped jitter (seek-safe) ----
        const g = q(".fx-grain");
        const steps = Math.round(D * 12);
        tl.fromTo(g, {{ backgroundPosition: "0px 0px" }}, {{ backgroundPosition: `${{steps * 173}}px ${{steps * 251}}px`, duration: D, ease: `steps(${{steps}})` }}, 0);
        tl.fromTo(q(".fx-leak"), {{ x: 0, y: 0 }}, {{ x: 120, y: 60, duration: D, ease: "sine.inOut" }}, 0);

{script}

        tl.to({{}}, {{ duration: 0.001 }}, D - 0.001);
        window.__timelines = window.__timelines || {{}};
        window.__timelines["{fid}"] = tl;
      }})();
    </script>
  </div>
</template>
"""
