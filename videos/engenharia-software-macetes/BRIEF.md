---
workflow: faceless-explainer
flow: automation
storyboard: no
message: "Cada pergunta da revisão de Engenharia de Software tem uma resposta-gabarito curta e um macete visual: crise PRQ, seis verbos do ciclo, o QUE × COMO, Modelo + Planejamento = Processo, e escada · rascunho · pizza · risco"
destination: youtube
aspect: 1920x1080
language: pt-BR
audience: estudante que faz a prova amanhã e precisa memorizar as respostas da revisão de Modelos, Métodos e Técnicas da Engenharia de Software
length: 300s
angle: how-to
voice: piper-pt_BR-faber-medium
style_preset: cobalt-grid
---

## Intent

Vídeo de memorização para a prova de amanhã, baseado no PDF de revisão "Modelos, métodos e técnicas da
engenharia de software" (25 slides). Ensina como responder cada pergunta provável de forma correta e fácil de
lembrar, com dicas, macetes, exemplos e muitas animações ("use e abuse de animações e exemplos").
Pedido explícito: trocar o locutor, porque o anterior (Kokoro pf_dora) soava robótico.

## Assets

- capture/revisao-engenharia-software.pdf — PDF original (fonte da verdade).
- capture/extracted/visible-text.txt — texto extraído do PDF.
- assets/music/underscore.mp3 — trilha de estudo reaproveitada dos vídeos anteriores (host).

## Customizations

- Locutor: Piper pt_BR "faber" (local, via sherpa-onnx). Provisório até o usuário configurar GEMINI_API_KEY;
  então a narração será regenerada com Gemini TTS e o vídeo renderizado de novo.
- Uma pergunta por quadro (ou par de quadros): pergunta → resposta do slide → macete em destaque.
- Mesmo tema Cobalt Grid dos vídeos anteriores; tag "ENG. SOFTWARE · MACETES".

## Notes

- O PDF não traz perguntas escritas: as perguntas são as que cada slide responde; a resposta é o texto do slide.
- Pegadinha do slide 10: "garantir segurança e proteção dos dados" aparece em vermelho na lista de funcionais —
  é requisito NÃO funcional (qualidade).
- Analogias ilustrativas (não estão nos slides): escada (cascata), rascunho (prototipação), pizza em fatias
  (incremental), receita de bolo (modelo × processo), e os macetes PRQ, seis verbos, E-A-D-V, O-R-D-P.
- Mais longo que o normal da rota (~5 min) porque o material tem 11 tópicos; usuário pediu completo.
