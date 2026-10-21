# Valorant highlight: Dentro do Corolla Cross

Edit de 23,9 s no estilo do highlight de referência ("UNTOUCHABLE"), com 4 clipes e a música *Dentro do Corolla Cross*.
Os cortes e os tiros caem na batida (130 BPM; o grave entra em 7,94 s).

- `edit.json`: toda a montagem
  - cortes e rampas de velocidade (`anchors` = [tempo na música, tempo no clipe])
  - momentos dos abates
  - letra
  - sons de tiro do jogo
- `render.py`: aplica tudo:
  - color grade frio antes do drop e quente/rosa depois
  - zoom, tremida, flash e RGB split nos abates
  - pulso nas batidas
  - transições de chicote nos cortes
  - letra palavra por palavra
  - "COROLLA CROSS" em 3D, como o "UNTOUCHABLE" da referência
  - faixas pretas de cinema na pausa da música
- `LETRA.md`: letra usada, com as dúvidas marcadas.
- `renders/valorant-corolla-cross.mp4`: resultado (1920x1080, 30 fps).

```
pip install numpy opencv-python-headless pillow
python3 render.py <pasta_dos_clipes> <musica.mp3> renders/valorant-corolla-cross.mp4
```

Os clipes e a música originais não estão no repositório.
