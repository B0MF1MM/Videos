---
format: 1920x1080
fps: 24
duration: 167.68s
music: assets/bgm.mp3 (áudio do WhatsApp enviado, 2:47)
reference: "TIXA – PRESSA" (lyric video editorial 3D)
language: pt-BR
---

# Tanto Faz — lyric video no estilo "PRESSA"

## O que a referência faz (análise)

**Conceito.** Não é tipografia "solta" na tela: cada trecho da letra é diagramado *dentro de um
impresso* (cartaz, revista de fofoca, jornal, encarte, anúncio, lambe-lambe) e esse impresso é um
objeto físico fotografado numa cena 3D. A câmera passeia de impresso em impresso; a letra vai sendo
"digitada" letra a letra no papel no momento exato em que é cantada.

**Câmera.** Um único plano contínuo por cenário, sem cortes secos dentro dele. Lente longa,
inclinada sobre a superfície (8–18° de *tilt*), leve rotação no eixo Z, *dolly* lento e
deslizes suaves (ease in/out) de um papel para o próximo, chegando ao papel junto com a frase.
Entre cenários há um movimento rápido com desfoque (*whip*/blur) para a superfície seguinte.

**Profundidade de campo.** Foco raso tipo *tilt-shift*: faixa central nítida, topo e base do quadro
desfocados (o topo mais, por estar mais longe). Vende a escala de maquete/objeto real.

**Superfícies e texturas.** Mesa coberta de impressos, quadro de cortiça com tachinhas e calendário,
mesa de madeira, grama com folhas secas, muro de concreto com cartazes colados e rasgados, parede
clara com fita adesiva. Papel com fibra, vincos, borda rasgada, sombra de contato e sombra longa.

**Luz.** Luz de janela entrando de lado: sombras de caixilho (barras) projetadas sobre os papéis,
manchas quentes de *light leak*, vinheta forte, grão de filme, *grade* por cenário (teal e escuro na
cortiça, quente na madeira, verde no jardim, rosa no anúncio).

**Modelos 3D / objetos.** Computador retrô bege (Apple II), telefone com fio, perfume, carro
vermelho, batom, além das fotos da artista impressas nos layouts.

**Tipografia (um sistema por impresso).**
- Cartaz serifado escuro: serifa editorial em *Title Case*, centralizada, com uma palavra em itálico
  ou negrito, dois blocos de texto corrido justificado e assinatura "ARTISTA — MÚSICA ANO".
- Revista de fofoca: *masthead* itálico pesado vermelho com contorno amarelo, citações em caixa
  alta grotesca pesada amarela/vermelha entre aspas, estrelas de "EXCLUSIVO".
- Editorial de moda no jardim: serifa leve, alinhada à esquerda, página com borda rasgada.
- Anúncio de computador: logotipo arco-íris geométrico pesado + serifa com palavra colorida.
- Pôster preto: grotesca pesada caixa-alta branca empilhada.
- Jornal: título serifado, fios rosa, manchetes grotescas e caixa rosa invertida.
- Lambe-lambe: condensada gigante (Anton) + tarjas com a linha completa, cartazes repetidos em
  amarelo/cinza/preto.
- Encarte: caixa-alta técnica/larga (Michroma) com as letras voando e se montando.

## Como foi recriado aqui

HyperFrames (HTML + GSAP, renderizado em Chrome headless). Cada cenário é uma composição com:
`stage` (perspectiva fixa = lente) → `world` (preserve-3d, a câmera é a pose dele) → superfície
texturizada + papéis + objetos; por cima, camadas de *tilt-shift* (backdrop blur com máscara),
*grade*, *light leak*, vinheta e grão animado em passos (determinístico).

- Texturas procedurais: `tools/textures.py` (madeira, cortiça, grama, concreto, parede, papel,
  vinco, grão, fundos "fotográficos").
- Objetos vetoriais sombreados: `tools/objects.py` (computador, telefone, perfume, anel, rosa,
  carro, batom, sacola, fita cassete, coração, folha, tachinha).
- Cenários: `tools/scenes.py`. Kit compartilhado (câmera, digitação, efeitos): `tools/kit.py`.
- **Letra e tempos: `lyrics.txt`** → depois de corrigir, rode `python3 tools/build.py`.

> Não há fotos da artista: os espaços de foto usam fundos fotográficos gerados + objetos.
> Para usar fotos reais, coloque os arquivos em `assets/img/` e troque os nomes `ph-*.jpg`
> nas cenas.

## Cenários

| # | Arquivo | Trecho | Superfície / impresso | Linhas |
|---|---|---|---|---|
| 0 | `00-mesa` | 0:00–0:13 | Mesa de madeira coberta de impressos; anúncio do computador "TANTO FAZ" | (intro) título digitado na tela |
| 1 | `01-cortica` | 0:13–0:27.9 | Cortiça; 4 cartazes serifados teal | c1–c4 |
| 2 | `02-tabloide` | 0:27.9–0:45.2 | Madeira; revista de fofoca (capa, miolo, contracapa) | c5–c12 |
| 3 | `03-jardim` | 0:45.2–1:00.3 | Grama com folhas; páginas de editorial de moda | v1–v8 |
| 4 | `04-computador` | 1:00.3–1:15.2 | Parede clara; anúncios do computador retrô | p1–p5 |
| 5 | `05-jornal` | 1:15.2–1:32 | Madeira escura; jornal com destaques rosa | n1–n9 |
| 6 | `06-muro` | 1:32–1:53.7 | Concreto; lambe-lambes repetidos | m1–m6 |
| 7 | `07-rosa` | 1:53.7–2:10 | Madeira; páginas rosa + anúncio do carro | r1–r5 |
| 8 | `08-encarte` | 2:10–2:31.7 | Parede; encarte/zine, letras se montando | f1–f7 |
| 9 | `09-creditos` | 2:31.7–2:47.7 | Madeira; último cartaz, créditos, fade para preto | — |
