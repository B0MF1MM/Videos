---
workflow: explainer
aspect: 1920x1080
language: pt-BR
audience: estudante de Compiladores revisando a teoria da A2
length: ~17min50s (37 cenas)
voice: Piper pt_BR "dii-high" (local, via sherpa-onnx 1.13.8)
source: slides da A2 (videos/compiladores-analise-semantica/capture/slides-A2.pptx), slides 1–243
---

## Pedido

Um vídeo único com os três temas, **focado em teoria**: só a explicação do conteúdo, sem prática,
sem código, sem exercícios resolvidos e sem cartões de macete. Mesmo pipeline (HyperFrames, voz nova).

## Estrutura

- Visão geral (onde cada tema entra no compilador).
- Parte 1 · Análise semântica: atributos e amarração, gramáticas de atributos, grafo de dependências,
  ordem de avaliação, sintetizados e herdados, passadas e o teorema, tabela de símbolos e hashing,
  declarações e escopo, tipos e verificação de tipos.
- Parte 2 · Ambientes de execução: organização da memória, registro de ativação e registradores,
  sequências de ativação/retorno, ambientes estático, de pilha e dinâmico, deslocamentos, vinculação de
  acesso, objetos e heap, passagem de parâmetros.
- Parte 3 · Geração de código: código intermediário, três endereços, quádruplas, geração como atributo
  sintetizado, código alvo (macros × simulação estática), cálculo de endereços, controle e
  backpatching, expressões lógicas, procedimentos, máquina TM e gerador TINY.
- Encerramento: significado → memória → código.

## Notas

- Os diagramas são conceituais (esquemas de memória, fluxos, árvores genéricas); não há trechos de
  código nem exemplos numéricos resolvidos.
- Regerar: `python3 -I tools/voice.py <modelo-piper>` e `python3 -I tools/assemble.py`.
