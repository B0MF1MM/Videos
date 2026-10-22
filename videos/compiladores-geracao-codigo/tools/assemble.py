"""Monta o vídeo: tools/src/<cena>.html -> compositions/frames/<cena>.html, index.html e legendas.

As fontes de cena trazem só o miolo (<style>, marcação e o corpo do <script>). Aqui entram o
envelope da composição, a moldura (tag, número, barra de progresso), os tempos da fala (C, D)
e a montagem da raiz com transições, voz, música, efeitos e legendas.
Na marcação, "@x" vira "<id-da-cena>-x".
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = json.load(open(os.path.join(ROOT, "tools", "timing.json"), encoding="utf-8"))
N = len(T)
IDS = [i for i in sorted(T) if os.path.exists(os.path.join(ROOT, "tools", "src", i + ".html"))]
TAIL = 0.35      # respiro depois da última frase
XF = 0.5         # sobreposição da transição

SECTION = {
    "01": "INTRODUÇÃO", "02": "INTRODUÇÃO", "03": "CÓDIGO INTERMEDIÁRIO",
    "04": "TRÊS ENDEREÇOS", "05": "TRÊS ENDEREÇOS", "06": "TRÊS ENDEREÇOS", "07": "TRÊS ENDEREÇOS",
    "08": "TRÊS ENDEREÇOS", "09": "QUÁDRUPLAS",
    "10": "ATRIBUTO SINTETIZADO", "11": "ATRIBUTO SINTETIZADO", "12": "ATRIBUTO SINTETIZADO",
    "13": "ATRIBUTO SINTETIZADO", "14": "ATRIBUTO SINTETIZADO", "15": "ATRIBUTO SINTETIZADO",
    "16": "ATRIBUTO SINTETIZADO", "17": "CÓDIGO ALVO", "18": "ENDEREÇOS", "19": "MATRIZES",
    "20": "MATRIZES", "21": "REGISTROS", "22": "PONTEIROS", "23": "CONTROLE", "24": "CONTROLE",
    "25": "CONTROLE", "26": "EXPRESSÕES LÓGICAS", "27": "FUNÇÕES", "28": "FUNÇÕES",
    "29": "MÁQUINA TM", "30": "MÁQUINA TM", "31": "MÁQUINA TM", "32": "GERADOR TINY",
    "33": "GERADOR TINY", "34": "GERADOR TINY", "35": "REVISÃO",
}

# efeitos sonoros por cena: (cue, arquivo, deslocamento em s, volume)
SFX = {}

FRAME = """<template id="{id}-template">
  <div id="root" data-composition-id="{id}" data-start="0" data-duration="{dur}" data-width="1920" data-height="1080">
    <link rel="stylesheet" href="assets/lib/kit.css" />
{style}
    <div id="s{id}-bg" class="clip k-scene k-bg" data-start="0" data-duration="{dur}" data-track-index="0"></div>
    <div id="s{id}-stage" class="clip k-scene" data-start="0" data-duration="{dur}" data-track-index="1" data-layout-allow-overlap data-layout-allow-overflow>
      <div id="s{id}-cam" class="k-cam">
{markup}
      </div>
    </div>
    <div id="s{id}-chrome" class="clip k-scene" data-start="0" data-duration="{dur}" data-track-index="2">
      <div id="s{id}-tag" class="k-tag">COMPILADORES · <b>{section}</b></div>
      <div id="s{id}-num" class="k-num">{n:02d} / {total:02d}</div>
      <div id="s{id}-progbar" class="k-prog"><i id="s{id}-prog"></i></div>
    </div>
    <script src="assets/vendor/gsap.min.js"></script>
    <script src="assets/lib/kit.js"></script>
    <script>
      (function () {{
        var C = {cues}, D = {dur};
        var S = K.scene("{id}", D, {total}), tl = S.tl, $ = S.$;
{body}
      }})();
    </script>
  </div>
</template>
"""


def build_scene(sid, dur):
    src = open(os.path.join(ROOT, "tools", "src", sid + ".html"), encoding="utf-8").read()
    style = ""
    m = re.search(r"<!--sfx:(.*?)-->", src)
    if m:
        for it in m.group(1).split(","):
            cue, _, rest = it.strip().partition(":")
            rest, _, vol = rest.partition("*")
            f, _, off = rest.partition("@")
            SFX.setdefault(sid, []).append((cue, f, float(off or 0), float(vol or 0.35)))
        src = src.replace(m.group(0), "")
    m = re.search(r"<style>.*?</style>", src, re.S)
    if m:
        style = "    " + m.group(0)
        src = src.replace(m.group(0), "")
    i = src.rfind("<script>")
    markup, body = src[:i], src[i + len("<script>"):]
    body = body[: body.rfind("</script>")]
    fix = lambda s: re.sub(r'(["\'#])@([\w-]+)', lambda mm: mm.group(1) + "s" + sid + "-" + mm.group(2), s)
    markup = fix(markup).strip("\n")  # sem reindentar: há texto em white-space: pre
    body = "\n".join("        " + l if l.strip() else "" for l in body.strip("\n").split("\n"))
    out = FRAME.format(id=sid, dur=dur, style=fix(style), markup=markup, body=body,
                       cues=json.dumps(T[sid]["cues"]), n=int(sid[:2]), total=N,
                       section=SECTION.get(sid[:2], ""))
    open(os.path.join(ROOT, "compositions", "frames", sid + ".html"), "w", encoding="utf-8").write(out)


TRANS = ["fade", "push", "fade", "zoom"]


def media_len(path):
    import subprocess
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          os.path.join(ROOT, path)], capture_output=True, text=True).stdout
    return round(float(out.strip()) - 0.01, 2)


def main():
    t = 0.0
    hosts, audio, trans, groups = [], [], [], []
    starts = {}
    for k, sid in enumerate(IDS):
        v = T[sid]["duration"]
        dur = round(v + TAIL + (XF if k < len(IDS) - 1 else 1.8), 3)
        starts[sid] = round(t, 3)
        build_scene(sid, dur)
        hosts.append(f'      <div id="el-{sid}" class="scene clip" data-composition-id="{sid}" data-composition-src="compositions/frames/{sid}.html" data-start="{round(t,3)}" data-duration="{dur}" data-track-index="{k % 2}" data-track-kind="graphics"></div>')
        audio.append(f'      <audio id="el-{sid}-voice" src="{T[sid]["voice"]}" data-start="{round(t,3)}" data-duration="{v}" data-track-index="10" data-volume="1"></audio>')
        for (cue, f, off, vol) in SFX.get(sid, []):
            at = round(t + T[sid]["cues"][cue] + off, 3)
            audio.append(f'      <audio id="el-{sid}-sfx-{cue}-{f}" src="assets/sfx/{f}.mp3" data-start="{at}" data-duration="{media_len('assets/sfx/' + f + '.mp3')}" data-track-index="12" data-volume="{vol}"></audio>')
        # legendas: grupos de até 7 palavras, quebrando em pontuação
        ws = T[sid]["words"]
        cur = []
        for j, w in enumerate(ws):
            cur.append(w)
            nxt = ws[j + 1] if j + 1 < len(ws) else None
            brk = (len(cur) >= 9 or len(" ".join(x["text"] for x in cur)) > 46 or nxt is None or nxt["cue"] != w["cue"]
                   or (re.search(r"[.,:;?!]$", w["text"]) and len(cur) >= 4))
            if brk:
                groups.append({"start": round(t + cur[0]["start"], 3), "end": round(t + cur[-1]["end"], 3),
                               "text": " ".join(x["text"] for x in cur)})
                cur = []
        nt = round(t + v + TAIL + (0 if k < len(IDS) - 1 else 1.8), 3)
        if k < len(IDS) - 1:
            nxt_id = IDS[k + 1]
            kind = TRANS[k % len(TRANS)]
            a, b = f"#el-{sid}", f"#el-{nxt_id}"
            if kind == "fade":
                trans.append(f'        tl.to("{a}", {{ opacity: 0, duration: 0.5, ease: "power2.inOut" }}, {nt});')
                trans.append(f'        tl.fromTo("{b}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: "power2.inOut" }}, {nt});')
            elif kind == "push":
                trans.append(f'        tl.to("{a}", {{ x: -1920, duration: 0.5, ease: "power3.inOut" }}, {nt});')
                trans.append(f'        tl.fromTo("{b}", {{ x: 1920 }}, {{ x: 0, duration: 0.5, ease: "power3.inOut" }}, {nt});')
            else:
                trans.append(f'        tl.to("{a}", {{ scale: 1.6, opacity: 0, duration: 0.45, ease: "power3.in" }}, {nt});')
                trans.append(f'        tl.fromTo("{b}", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "power3.out" }}, {nt});')
            audio.append(f'      <audio id="el-{sid}-whoosh" src="assets/sfx/whoosh-short.mp3" data-start="{max(0, round(nt - 0.1, 3))}" data-duration="{media_len('assets/sfx/whoosh-short.mp3')}" data-track-index="13" data-volume="0.18"></audio>')
        t = nt
    total = round(t, 3)
    # música: a trilha tem ~235 s; repete com fades para cobrir o vídeo
    MUS = 235.0
    k, mt = 0, 0.0
    while mt < total:
        d = round(min(MUS, total - mt), 3)
        audio.append(f'      <audio id="el-bgm-{k}" src="assets/music/underscore.mp3" data-start="{round(mt,3)}" data-duration="{d}" data-track-index="{11 if k % 2 == 0 else 14}" data-volume="0.09"></audio>')
        mt += MUS - 0.5
        k += 1

    html = open(os.path.join(ROOT, "tools", "index.tpl.html"), encoding="utf-8").read()
    html = (html.replace("__TOTAL__", str(total)).replace("__HOSTS__", "\n".join(hosts))
            .replace("__AUDIO__", "\n".join(audio)).replace("__TRANS__", "\n".join(trans)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)

    cap = open(os.path.join(ROOT, "tools", "captions.tpl.html"), encoding="utf-8").read()
    cap = cap.replace("__GROUPS__", json.dumps(groups, ensure_ascii=False)).replace("__TOTAL__", str(total))
    open(os.path.join(ROOT, "compositions", "captions.html"), "w", encoding="utf-8").write(cap)
    json.dump({"total": total, "starts": starts}, open(os.path.join(ROOT, "tools", "starts.json"), "w"), indent=1)
    print("total", total, "scenes", N, "caption groups", len(groups))


if __name__ == "__main__":
    main()
