---
workflow: explainer
aspect: 1920x1080
language: pt-BR
audience: estudante de Compiladores que precisa entender e memorizar Análise Semântica para a A2
length: ~13min35s (36 cenas)
voice: Piper pt_BR "dii-high" (local, via sherpa-onnx 1.13.8)
source: capture/slides-A2.pptx (tópico "Análise Semântica", slides 2–129)
---

## Pedido

Mesmas instruções do primeiro vídeo da conversa: explicar em detalhe, mostrando como montar a
árvore e aplicar as regras gramaticais/semânticas, com dicas e macetes, muitas animações e exemplos
visuais, a voz nova (menos robótica) e feito com HyperFrames. Tópico: Análise Semântica.

## Conteúdo

Atributos e amarração · gramáticas de atributos (345, (34-3)*42 = 1302, float x,y, 345o = 229 e 189o = erro)
· simplificações · grafo de dependências e ordenação topológica (DAG) · métodos de avaliação ·
sintetizados × herdados (pós/pré-ordem, AvalTipo, uma × duas passadas, 5/2/2.0) · teorema
herdado → sintetizado · tabela de símbolos (operações, hashing, colisões, função de hash) ·
declarações e escopo (aninhamento mais próximo, tabela por escopo) · tipos, construtores
(struct 12 B × union 8 B), typedef e tipos recursivos · verificador de tipos · sobrecarga e coação ·
analisador semântico do TINY.

## Notas

- A abertura usa a ilustração "Planta" do slide 1 do PPTX (assets/img/planta.jpg).
- Exemplos ilustrativos (não estão nos slides): x = "olá" * 3, a tabela de símbolos da cena 24,
  o hash de "ab" (= 64 com TAMANHO 211), o exemplo da lista ligada 7 → 3 → 9 e as analogias
  (etiqueta, fumaça/herança, vestir a roupa, procurar em casa).
- Regerar: `python3 -I tools/voice.py <modelo-piper>` e `python3 -I tools/assemble.py` (ver o
  projeto compiladores-geracao-codigo/BRIEF.md para o modelo de voz).
