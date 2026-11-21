---
workflow: explainer
aspect: 1920x1080
language: pt-BR
audience: estudante de Compiladores que precisa entender e memorizar Ambientes de Execução para a A2
length: ~11min45s (28 cenas)
voice: Piper pt_BR "dii-high" (local, via sherpa-onnx 1.13.8)
source: slides da A2 (videos/compiladores-analise-semantica/capture/slides-A2.pptx), tópico "Ambientes de execução", slides 130–181
---

## Pedido

Mesmas instruções do primeiro vídeo da conversa (explicar em detalhe, passo a passo, com macetes,
muitas animações e exemplos visuais, voz nova, feito com HyperFrames). Tópico: Ambientes de Execução.

## Conteúdo

Três ambientes · organização da memória (código, global/estática, pilha, heap) · registro de
ativação e registradores (pc, sp, fp, ap) · sequência de ativação/retorno · ambiente estático
(FORTRAN77, sem recursão) · ambiente de pilha (fp, vinculação de controle, gcd(15,10), árvore de
ativação, deslocamentos a partir do fp, f(int x, char c) com a[i] = (−24+2i)(fp), passo a passo da
chamada) · procedimentos locais e vinculação de acesso · ambiente dinâmico (referência pendente,
coleta de lixo), objetos e heap · passagem por valor, referência, valor-resultado e nome · ambiente
do TINY.

## Notas

- Exemplos ilustrativos (não estão nos slides): fat(n) na abertura, a troca(x, y) nas passagens por
  valor e por referência, o quadro comparativo com p(x) somando 1, o programa main/P da cena 9, as
  classes Circulo/Forma, o bloco de 16 bytes do heap e as analogias (pratos, estacionamento,
  mochila, hotel, migalha de pão, fotocópia, chave, empréstimo, receita).
- Regerar: `python3 -I tools/voice.py <modelo-piper>` e `python3 -I tools/assemble.py`.
