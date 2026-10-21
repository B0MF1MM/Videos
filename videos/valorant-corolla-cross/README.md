# Valorant highlight: Dentro do Corolla Cross

Edit de 23,9 s com 4 clipes e a música *Dentro do Corolla Cross*. Os cortes e os tiros caem na batida (130 BPM; o grave entra em 7,94 s).

## Efeitos (v2)
- **Câmera lenta com optical flow** (estilo Twixtor): cria quadros intermediários de verdade, sem tremer, logo depois de cada abate.
- **Motion blur real** (estilo RSMB): o borrão segue o movimento da imagem e fica mais forte quando o vídeo acelera.
- **Partículas:**
  - explosão de faíscas e brasas no ponto da mira em cada abate (maior no drop)
  - poeira azul flutuando antes do drop e brasas rosa subindo depois
  - o texto "COROLLA CROSS" explode em ~1500 partículas no drop, no tiro após a pausa e no fim
- **Texto atrás do cenário:** o modelo de profundidade MiDaS (baixado do GitHub do projeto) estima o que está perto da câmera. O texto grande passa por trás do anel da mira e da arma.
- **Impacto:**
  - onda de choque com distorção
  - zoom radial
  - tremida com rotação
  - aberração cromática radial
  - flash
  - *impact frames* invertidos em preto e branco, com um "boom" grave no áudio
- **Transições:** chicote, zoom radial e glitch digital, alternando. Também light leaks.
- **Subida para o drop e pausa:** linhas de velocidade estilo anime, zoom crescente e faixas pretas de cinema.
- **Acabamento:**
  - color grade frio antes do drop e rosa/roxo depois, com split toning
  - bloom e flares anamórficos nos brilhos
  - granulação de filme e vinheta

## Arquivos
- `edit.json`: toda a montagem
  - cortes e rampas de velocidade (`anchors` = [tempo na música, tempo no clipe])
  - abates
  - letra (`hook_end` define quando o texto grande se desfaz)
  - transições
  - impact frames
  - sons de tiro
- `render.py`: aplica os efeitos.
- `LETRA.md`: letra usada, com as dúvidas marcadas.
- `renders/valorant-corolla-cross.mp4`: resultado (1920x1080, 30 fps).

```
pip install numpy opencv-python-headless pillow onnxruntime
python3 render.py <pasta_dos_clipes> <musica.mp3> renders/valorant-corolla-cross.mp4
# prévia rápida de um trecho:
python3 render.py <pasta_dos_clipes> <musica.mp3> /tmp/teste.mp4 --preview --from 6 --to 9
```

O modelo MiDaS (66 MB) é baixado automaticamente para `assets/models/` na primeira execução.
Os clipes e a música originais não estão no repositório.

## Versão "moonlight" (estilo cinematográfico)
Baseada no vídeo de referência *moonlight - valorant edit*. Usa os mesmos cortes, abates e câmera lenta do `edit.json`; o estilo fica em `moonlight.json`.

- Color grade por cena:
  - roxo monocromático
  - teal noturno (sombras teal, luzes quentes)
  - pastel lavado
  - frio
- Pretos levantados, glow difuso (Pro-Mist), bloom e halation. As altas luzes são comprimidas para não estourar.
- Câmera virtual: push-in lento, ângulo holandês depois dos abates, tremida de mão. O zoom corta parte do HUD.
- Lens blur com bokeh: abertura em rack focus e profundidade de campo nas bordas.
- Transições:
  - mergulho no escuro com raios de luz e volta com flash rosa
  - smear direcional
  - flash superexposto
  - desfoque
- Faixas de cinema 2.35:1 que entram e saem.
- A jogada da pausa da música aparece numa tela 3D flutuante, com reflexo e textura de monitor. No abate, a câmera mergulha na tela. Durante esse trecho a música fica abafada e volta cheia no tiro.
- Sem texto na tela, como na referência.

```
python3 render_moonlight.py <pasta_dos_clipes> <musica.mp3> renders/valorant-corolla-cross-moonlight.mp4
```
