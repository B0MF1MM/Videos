# tools — gerar voz e quadros deste vídeo

Os 20 quadros (`compositions/frames/*.html`) são gerados por `gen_frames.py` a partir de `fw.py`
(moldura e componentes) e de `frames_a.py` / `frames_b.py` (um bloco por quadro). Cada animação usa
marcas como `@palavra`, `@palavra#2` ou `@palavra+0.3`. Elas viram o instante em que a narração diz
aquela palavra (lido de `audio_meta.json`). Trocar a voz e rodar o gerador de novo re-sincroniza tudo.

## Trocar a narração pela voz do Gemini

Requer `GEMINI_API_KEY` no ambiente (configurações do ambiente → variável de ambiente; vale numa sessão nova).

```bash
cd videos/engenharia-software-macetes
pip install numpy soundfile
python3 -I tools/make_voice.py . gemini Charon            # ou Kore, Puck, Aoede...
S=../../.claude/skills/faceless-explainer/scripts
node $S/audio.mjs sync-durations --audio-meta ./audio_meta.json --storyboard ./STORYBOARD.md
python3 -I tools/gen_frames.py .
node $S/captions.mjs build --storyboard ./STORYBOARD.md --audio-meta ./audio_meta.json --hyperframes . --out ./caption_groups.json
node $S/assemble-index.mjs --storyboard ./STORYBOARD.md --hyperframes .
node $S/transitions.mjs inject --storyboard ./STORYBOARD.md --hyperframes .
# assemble/captions reescrevem o GSAP para a CDN (bloqueada aqui): voltar para o arquivo local
sed -i 's#https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js#assets/vendor/gsap.min.js#' index.html compositions/captions.html
# marcar o trilho de legendas
python3 -c "p='index.html';s=open(p).read();s=s.replace('id=\"el-captions\"','id=\"el-captions\"\n        data-track-kind=\"captions\"',1) if 'data-track-kind=\"captions\"' not in s else s;open(p,'w').write(s)"
npx --yes hyperframes@0.8.181 check
npx --yes hyperframes@0.8.181 render --skill=faceless-explainer --quality high --output renders/video.mp4
```

O texto falado está em `lines.py` (`SPOKEN` corrige a pronúncia de siglas e de "Boehm").
A voz provisória atual é Piper pt_BR faber-medium (`make_voice.py . piper <dir> 1.07`).
