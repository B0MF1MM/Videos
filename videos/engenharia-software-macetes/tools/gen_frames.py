import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fw import Cues, build
import frames_a, frames_b
proj = sys.argv[1]
cues = Cues(os.path.join(proj, "audio_meta.json"))
FR = {**frames_a.FR, **frames_b.FR}
os.makedirs(os.path.join(proj, "compositions/frames"), exist_ok=True)
sb = open(os.path.join(proj, "STORYBOARD.md")).read()
for n in sorted(FR):
    slug, css, html, js = FR[n]
    out = build(n, slug, cues, css, html, js)
    open(os.path.join(proj, f"compositions/frames/{n:02d}-{slug}.html"), "w").write(out)
    sb = re.sub(rf"(## Frame {n} —[^\n]*\n(?:.*\n)*?- status: )\w+", r"\1animated", sb, count=1)
open(os.path.join(proj, "STORYBOARD.md"), "w").write(sb)
print("frames:", len(FR))
