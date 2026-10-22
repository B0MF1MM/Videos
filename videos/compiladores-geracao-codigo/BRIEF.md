---
workflow: explainer
aspect: 1920x1080
language: pt-BR
audience: estudante de Compiladores que precisa entender e memorizar Geração de Código para a prova
length: ~11min30s (35 cenas)
voice: Piper pt_BR "dii-high" (local, via sherpa-onnx)
source: capture/compiladores-06-geracao-de-codigo.pdf (Compiladores 06 – Geração de Código, 91 slides)
---

## Pedido

Vídeo bem explicativo da aula 06 (Geração de Código), ensinando passo a passo como montar a
árvore, aplicar as regras gramaticais/semânticas (atributo sintetizado) etc., com dicas e macetes,
muitas animações e exemplos visuais. Trocar o locutor anterior (Kokoro `pf_dora`, robótico).

## Voz

Sem credenciais de HeyGen/ElevenLabs/Google nesta sessão e com a rede restrita (Hugging Face e
Microsoft Edge TTS bloqueados), a voz mais natural disponível foi a **Piper pt_BR `dii-high`**
(modelo "high", voz feminina diferente da anterior), baixada dos releases do sherpa-onnx no GitHub.
Alternativa testada: `faber-medium` (masculina). Para trocar, basta regerar a narração com outro
modelo (veja abaixo) e remontar.

## Como regerar

```bash
pip install sherpa-onnx soundfile
# modelo: https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-pt_BR-dii-high.tar.bz2
python3 -I tools/voice.py <pasta-do-modelo>   # SCRIPT.txt -> assets/voice/*.wav + tools/timing.json
python3 -I tools/assemble.py                  # tools/src/*.html -> compositions/frames, index.html, legendas
npm run check && npm run render
```

- `SCRIPT.txt`: roteiro por cena; cada frase é um "cue" de tempo; `||` separa legenda de pronúncia.
- `tools/src/<cena>.html`: miolo de cada cena (marcação + animação); `@x` vira id da cena.
- `assets/lib/kit.css` / `kit.js`: tema visual e funções de animação compartilhadas.

## Notas de conteúdo

- Tudo segue o PDF. Exemplos ilustrativos (não estão no material): a analogia do tradutor, o
  convite com a data em branco (backpatching), os valores `reg[1] = 80` / `dMem[80] = 42` do
  `LD 7,0(1)`, o programa TM curto da cena 29, o `1023` como "maior endereço válido" e as
  instruções TM da cena 03.
- Macetes: "folha é nome, nó interior é temporário", "bola de neve = sintetizado", "B·I·T",
  "falso pula / while é um if que volta", "abre, entrega, chama", "RO três registradores, RM
  parênteses", "JEQ 0,4(7) pula 5".
