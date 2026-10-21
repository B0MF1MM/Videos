"""Build every frame composition + index.html from lyrics.txt.
Run from the project dir:  python3 tools/build.py [frame-id ...]"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kit import ROOT  # noqa: E402
from scenes import CUTS, FRAMES  # noqa: E402


def write_index(built):
    parts = []
    first = min(dict(CUTS)[f] for f, _ in built)
    for i, (fid, dur) in enumerate(built):
        t0 = dict(CUTS)[fid] - first
        parts.append(f'''      <div id="el-{fid}" class="scene clip" data-composition-id="{fid}" data-composition-src="compositions/frames/{fid}.html"
        data-start="{t0:.3f}" data-duration="{dur + (0.5 if i < len(built) - 1 else 0):.3f}" data-track-index="{i % 2}"></div>''')
    total = max(dict(CUTS)[f] + d for f, d in built)
    trans = []
    for (a, _), (b, _) in zip(built, built[1:]):
        t = dict(CUTS)[b] - first
        trans.append(f'tl.fromTo("#el-{b}", {{ opacity: 0, filter: "blur(14px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.45, ease: "power2.out" }}, {t:.3f});')
    html = f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #000; }}
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total - first:.3f}" data-width="1920" data-height="1080">
{chr(10).join(parts)}
      <audio id="bgm" src="assets/bgm.mp3" data-start="0" data-media-start="{first:.3f}" data-duration="{total - first:.3f}" data-track-index="11" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join("      " + x for x in trans)}
      tl.to({{}}, {{ duration: {total - first:.3f} }}, 0);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(ROOT, "index.html"), "w").write(html)


if __name__ == "__main__":
    only = sys.argv[1:]
    built = []
    os.makedirs(os.path.join(ROOT, "compositions", "frames"), exist_ok=True)
    for f in FRAMES:
        fid, dur, html = f()
        if only and fid not in only:
            continue
        open(os.path.join(ROOT, "compositions", "frames", fid + ".html"), "w").write(html)
        built.append((fid, dur))
        print(f"built {fid}  {dur:.2f}s")
    write_index(built)
    print("index.html written")
