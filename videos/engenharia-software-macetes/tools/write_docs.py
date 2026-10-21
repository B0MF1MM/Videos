import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from lines import LINES
from plan import PLAN
proj = sys.argv[1]
meta = {v["frame"]: v for v in json.load(open(os.path.join(proj, "audio_meta.json")))["voices"]}
s = ["# SCRIPT — engenharia-software-macetes", "", "**Voice:** Piper pt_BR faber-medium (local, sherpa-onnx), provisória até Gemini TTS",
     "**Voice settings:** speed 1.07", "**Voice direction:** Clara, didática e encorajadora, como um colega ajudando a decorar na véspera da prova.", "", "---", ""]
b = ["---", "format: 1920x1080", "duration: 300s",
     'message: "Cada pergunta da revisão tem uma resposta-gabarito curta e um macete visual"',
     "arc: how-to — 11 perguntas da revisão, cada uma com resposta do slide + macete, comparação dos modelos, cola final",
     "audience: estudante que faz a prova amanhã de Modelos, Métodos e Técnicas da Engenharia de Software",
     "language: pt-BR", "mode: autonomous", "music: none",
     "music_brief: trilha de estudo calma reaproveitada (host, assets/music/underscore.mp3)", "---", "",
     "## Video direction", "",
     "- **chrome:** moldura Cobalt Grid — grade milimetrada, filetes cobalto no topo e na base (y ≤ 896), tag DM Mono \"ENG. SOFTWARE · MACETES\" no canto superior esquerdo e \"NN / 20\" no direito.",
     "- **paleta:** só papel creme #F0EBDE e tinta cobalto #1F2BE0 do frame.md. Erro/pegadinha = bloco cobalto invertido ou risco, nunca vermelho.",
     "- **tipo:** Newsreader para títulos e termos; Hanken Grotesk 600 caixa-alta para rótulos; DM Mono para tags. Nada abaixo de ~26 px.",
     "- **forma:** retângulos e linhas retas; setas retas com ponta triangular; ícones desenhados com retângulos/linhas.",
     "- **zona útil:** conteúdo acima de y = 900 (legendas embaixo).",
     "- **movimento:** cada item entra quando a narração o nomeia; macetes entram como carimbo (bloco invertido + overshoot); câmera respira lentamente; parada de leitura só no final.",
     "- **lista negativa:** vermelho/verde, sombras, gradientes, emoji, círculos decorativos, fontes externas.", ""]
for i, (lid, slug, title, text) in enumerate(LINES):
    n = int(lid); d = meta[n]["duration_s"]
    s += [f"## Line {n} — {title} (Frame {n})", "", "**Delivery:** ritmo de estudo, pausas leves nas listas.", "", "    " + text, ""]
    scene, typ, bp, focal, scenes = PLAN[lid]
    tr = "cut" if n == 1 else ("blur-crossfade" if n == 20 else "crossfade")
    b += [f"## Frame {n} — {title}", "", f"- scene: {scene}", f"- voiceover: \"{text}\"", f"- duration: {d}s", f"- transition_in: {tr}",
          "- status: outline", f"- src: compositions/frames/{lid}-{slug}.html", f"- type: {typ}", f"- blueprint: {bp}", f"- focal: {focal}",
          f"- roles: {focal} = herói · rótulos = apoio", "", f"narrativeRole: {title}.", f"keyMessage: {focal}.", ""]
    k = len(scenes)
    for j, sc in enumerate(scenes):
        a = round(d * j / k, 1); z = round(d * (j + 1) / k, 1) if j < k - 1 else d
        b.append(f"Scene {j+1} ({a}–{z}s): {sc}.")
    b.append("")
open(os.path.join(proj, "SCRIPT.md"), "w").write("\n".join(s))
open(os.path.join(proj, "STORYBOARD.md"), "w").write("\n".join(b))
print("ok")
