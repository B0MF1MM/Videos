---
format: 1920x1080
duration: 180s
message: "Qualidade se gerencia com dados: envolver todos, prevenir custos, medir o OEE e controlar o processo"
arc: concept-explainer with process
audience: estudantes revisando Administração e Integração de Operações e Qualidade (Aulas 6 a 8)
language: pt-BR
mode: autonomous
music: none
music_brief: calm focused minimal study underscore, soft piano and light pulse (host-generated, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** cada quadro leva a moldura Cobalt Grid — grade de papel milimetrado permanente, filetes cobalto no topo e na base (base em y ≤ 896), tag de chrome em DM Mono no canto superior esquerdo "AULAS 6–8 · QUALIDADE" e numeração "NN / 13" no canto superior direito.
- **paleta:** só duas cores do `frame.md` — papel creme e tinta cobalto. "Falha", "perda", "fora de controle" nunca ganham vermelho: usam bloco cobalto invertido (texto creme sobre cobalto) ou um risco cobalto. Nada de gradientes coloridos, sombras ou brilhos.
- **tipo:** Newsreader 400 para títulos, termos e números grandes; Hanken Grotesk 600 caixa-alta espaçada para rótulos; DM Mono para tags, eixos, fórmulas e chrome. Texto que carrega significado nunca abaixo de ~27 px. Todo texto visível em português do Brasil, exatamente como nas linhas Scene.
- **forma:** só retângulos e linhas retas — sem cantos arredondados, sem círculos, sem pílulas; pontos de gráfico são quadrados pequenos. Setas são linhas retas com ponta triangular. Dados viram barras de células da grade quando couber.
- **zona útil:** todo conteúdo acima de y = 900 px (faixa das legendas); herói centrado em y ≈ 454.
- **movimento:** curvas de cauda longa (power3 por padrão; overshoot só onde a cena pede). Anime só transformações e opacidade (x, y, scale, opacity, clip-path, stroke) — nunca left/top/width/height. Cada peça entra quando a narração a nomeia; depois de resolvido, o quadro segura a leitura parado.
- **ritmo:** o quadro 9 (68,4%) é o clímax numérico; o 12 (ponto fora do limite) é o segundo pico; os quadros 7 e 10 são curtos e diretos; o 13 é o respiro final, quase parado.
- **lista negativa:** vermelho/verde/amarelo, sombras difusas, bokeh, gradiente roxo-azul de "IA", emoji, cantos arredondados, círculos, conteúdo abaixo de y = 900, fontes via @import ou CDN; os dois modos de falha — slide (tudo de uma vez e congela) e protetor de tela (tudo flutuando sem parar).

## Frame 1 — Quanto custa a qualidade

- scene: Duas perguntas se constroem: "qualidade custa caro?" e "ou a falta dela?"; depois surgem "a máquina rende?" e "o processo saiu do controle?", que convergem na palavra DADOS
- voiceover: "Qualidade custa caro… ou é a falta dela que sai mais cara? E como saber se uma máquina rende de verdade, ou se um processo saiu do controle?"
- duration: 8.213s
- transition_in: cut
- status: animated
- src: compositions/frames/01-custa-caro.html
- type: hook
- persuasion: Rhetorical question + reversal
- beat: Curiosity + intrigue
- blueprint: kinetic-type-beats (Adapt)
- focal: a palavra DADOS em display-hero
- roles: DADOS = herói final · as quatro perguntas = apoio (headline) · grade + filetes = fundo

narrativeRole: Abre as três aulas com perguntas que só os dados respondem.
keyMessage: Qualidade se gerencia com dados, não com impressão.

Adapt: mantém a assinatura de frase que se constrói em batidas sobre fundo plano; o payoff vira a palavra DADOS. Revelação palavra a palavra → dynamic-content-sequencing.
Scene 1 (0.0–1.3s): "qualidade custa caro?" monta palavra a palavra no terço superior esquerdo (headline), cravando "caro?" em 1.0s.
Scene 2 (1.3–3.6s): em "falta dela" (1.8s) a resposta "ou a falta dela?" monta no terço superior direito, com "falta" em bloco cobalto invertido (3.0s).
Scene 3 (3.6–7.7s): as duas perguntas sobem e encolhem; abaixo, em duas linhas centrais menores, "a máquina rende?" (4.7s) e "o processo saiu do controle?" (6.8s).
Scene 4 (7.7–8.21s): em "controle?" (7.7s) as quatro perguntas recuam para ink-soft e DADOS entra grande no centro em bloco cobalto invertido (texto creme), com linhas retas finas ligando as perguntas ao bloco. Segura parado.

## Frame 2 — O que é GQT

- scene: A sigla GQT se expande em "Gestão da Qualidade Total"; um bloco "INSPEÇÃO" isolado se dissolve numa fileira de setores: projeto, compras, produção, atendimento
- voiceover: "Na Aula 6, a Gestão da Qualidade Total, a GQT. A qualidade deixa de ser tarefa de um setor de inspeção e passa a ser responsabilidade de todos, do projeto ao atendimento, sempre com foco no cliente."
- duration: 12.309s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-gqt.html
- type: product_intro
- persuasion: Concept announcement + before/after
- beat: Clarity + orientation
- blueprint: kinetic-type-beats (Adapt)
- focal: a sigla GQT que se expande no nome completo
- roles: GQT / nome por extenso = herói · bloco INSPEÇÃO → fileira de setores = apoio · rótulo AULA 6 = chrome

narrativeRole: Nomeia a abordagem da Aula 6 e a mudança que ela traz.
keyMessage: GQT = qualidade é responsabilidade de todos, com foco no cliente.

Adapt: mantém a troca de tokens no lugar (a sigla vira o nome) e a construção por batidas; o payoff vira um bloco que se abre em setores. Troca no lugar → discrete-text-sequence; abertura em leque → center-outward-expansion.
Scene 1 (0.0–1.0s): rótulo micro-strong "AULA 6" no topo esquerdo.
Scene 2 (1.0–3.4s): "Gestão da Qualidade Total" escreve-se em headline no alto, palavra a palavra (Gestão 1.0s, Qualidade 1.4s, Total 1.9s); em "GQT" (2.6s) a sigla GQT (display-chapter) entra acima, cada letra ligada à sua palavra por um traço curto.
Scene 3 (3.4–6.9s): no centro, um único bloco retangular "INSPEÇÃO" (contorno cobalto) entra em "setor de inspeção" (5.7s); em "passa" (6.9s) ele é riscado.
Scene 4 (6.9–9.8s): em "responsabilidade de todos" (7.5s) o bloco se abre do centro para fora numa fileira de quatro blocos iguais: PROJETO · COMPRAS · PRODUÇÃO · ATENDIMENTO (os extremos acendem em "projeto" 9.1s e "atendimento" 9.8s).
Scene 5 (9.8–12.31s): em "foco no cliente" (11.2s) uma faixa cobalto invertida "FOCO NO CLIENTE" aparece sob a fileira, ligada a ela por traços retos verticais. Segura.

## Frame 3 — Princípios e PDCA

- scene: Três princípios entram (foco no cliente, envolvimento de todos, melhoria contínua); o terceiro abre um ciclo quadrado de quatro blocos P → D → C → A
- voiceover: "Ela se apoia em três ideias: foco no cliente, envolvimento de todas as pessoas e melhoria contínua, que gira o ciclo PDCA: planejar, executar, verificar e agir."
- duration: 9.493s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-pdca.html
- type: feature_showcase
- persuasion: Rule of three + cycle diagram
- beat: Comprehension + focus
- blueprint: compose
- focal: o ciclo quadrado PDCA
- roles: três princípios numerados = apoio (coluna esquerda) · ciclo PDCA em quatro blocos quadrados = herói (direita, ~50% da largura) · setas retas entre blocos = apoio

narrativeRole: Organiza os princípios e mostra o PDCA como motor da melhoria.
keyMessage: Cliente, pessoas, melhoria contínua — PDCA: planejar, executar, verificar, agir.

Compose: lista de três que desemboca num diagrama de ciclo montado na ordem da fala. Revelação de itens → dynamic-content-sequencing; setas do ciclo → svg-path-draw.
Scene 1 (0.0–1.8s): título headline "Três ideias" no topo esquerdo (0.9s).
Scene 2 (1.8–5.5s): coluna esquerda (40%), linhas numeradas em mono 01/02/03: "Foco no cliente" (1.8s), "Envolvimento de todos" (2.9s), "Melhoria contínua" (4.6s) — esta fica em bloco cobalto invertido.
Scene 3 (5.5–7.1s): em "ciclo PDCA" (6.2s) uma linha reta liga "Melhoria contínua" à direita (60%), onde quatro blocos quadrados em contorno formam um quadrado 2×2, rotulados P, D, C, A em display-chapter.
Scene 4 (7.1–9.49s): cada bloco acende (cobalto invertido) e ganha o verbo embaixo no tempo da fala: P "PLANEJAR" (7.1s), D "EXECUTAR" (7.8s), C "VERIFICAR" (8.4s), A "AGIR" (9.0s); a seta reta do bloco anterior ao atual se desenha a cada passo, e a última volta de A para P fecha o ciclo. Segura.

## Frame 4 — Os quatro custos

- scene: Uma grade 2×2: PREVENÇÃO e AVALIAÇÃO em cima (custos de controle), FALHAS INTERNAS e FALHAS EXTERNAS embaixo (custos das falhas), cada uma com exemplos
- voiceover: "Na Aula 6 também vêm os custos da qualidade, em quatro grupos. Prevenção: treinamento e planejamento para evitar defeitos. Avaliação: inspeções e testes. Falhas internas: refugo e retrabalho antes da entrega. E falhas externas: garantia, devoluções e reclamações depois da entrega."
- duration: 17.067s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-quatro-custos.html
- type: feature_showcase
- persuasion: Categorization + concrete examples
- beat: Comprehension + "aha"
- blueprint: grid-card-assemble (Adapt)
- focal: a grade 2×2 dos quatro custos
- roles: quatro cartões em grade 2×2 = herói (~80% da área útil) · rótulos de grupo CUSTOS DE CONTROLE / CUSTOS DAS FALHAS = apoio · exemplos em body = apoio

narrativeRole: Apresenta as quatro categorias que a prova costuma cobrar.
keyMessage: Prevenção, avaliação, falhas internas, falhas externas.

Adapt: mantém a montagem de N cartões numa grade, mas cada cartão entra no tempo da sua palavra. Entrada dos cartões → spring-pop-entrance (sem overshoot); exemplos sublinhados → css-marker-patterns.
Scene 1 (0.0–3.8s): título headline "Custos da qualidade" no topo esquerdo (1.4s) e, em "quatro grupos" (2.6s), quatro contornos vazios aparecem tênues (ink-faint) em grade 2×2.
Scene 2 (3.8–7.1s): em "Prevenção" (3.8s) o cartão superior esquerdo se preenche: "PREVENÇÃO" (table-name) + "treinamento · planejamento" (body).
Scene 3 (7.1–9.2s): em "Avaliação" (7.1s) o cartão superior direito: "AVALIAÇÃO" + "inspeções · testes"; um rótulo micro-strong "CUSTOS DE CONTROLE" aparece acima da fileira de cima (8.5s).
Scene 4 (9.2–12.6s): em "Falhas internas" (9.2s) o cartão inferior esquerdo em cobalto invertido: "FALHAS INTERNAS" + "refugo · retrabalho — antes da entrega".
Scene 5 (12.6–17.07s): em "falhas externas" (12.7s) o cartão inferior direito em cobalto invertido: "FALHAS EXTERNAS" + "garantia · devoluções · reclamações — depois da entrega"; rótulo "CUSTOS DAS FALHAS" acima da fileira de baixo (14.6s); "depois da entrega" ganha sublinhado em 16.1s. Segura.

## Frame 5 — Prevenir sai mais barato

- scene: Uma linha do tempo projeto → produção → cliente com o custo de corrigir um defeito crescendo a cada etapa; depois duas barras empilhadas: antes (muita falha) e depois (mais prevenção, total menor)
- voiceover: "Quanto mais tarde o defeito é descoberto, mais caro ele fica. Por isso, investir em prevenção e avaliação reduz as falhas, e o custo total da qualidade cai."
- duration: 9.109s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-prevenir.html
- type: benefit_highlight
- persuasion: Escalation + before/after
- beat: "Aha" + conviction
- blueprint: dataviz-countup (Adapt)
- focal: as duas barras empilhadas ANTES × DEPOIS
- roles: linha do tempo com três etapas e degraus crescentes = herói da primeira metade · duas barras empilhadas (pixel-stack) = herói da segunda metade · legenda das camadas = apoio

narrativeRole: Responde ao gancho: a falta de qualidade é o que sai caro.
keyMessage: Prevenir custa menos que corrigir; o custo total cai.

Adapt: mantém as barras como herói e a escalada como argumento; sem contagem numérica (nenhum valor inventado). Barras → stat-bars-and-fills; linha do tempo → svg-path-draw.
Scene 1 (0.0–3.5s): uma linha do tempo horizontal se desenha na metade superior com três marcos: PROJETO · PRODUÇÃO · CLIENTE; em "mais tarde" (0.6s) acima de cada marco cresce uma coluna de células — 1, depois 3, depois 8 células — e em "mais caro" (2.4s) um rótulo "CUSTO DE CORRIGIR" sobe junto com a escada.
Scene 2 (3.5–7.1s): a linha do tempo sobe e encolhe; na metade inferior surgem duas barras empilhadas lado a lado. ANTES (3.8s): camadas finas de prevenção e avaliação embaixo e uma camada grossa de falhas em cima. Em "prevenção e avaliação" (4.8s) a barra DEPOIS monta com camadas de prevenção e avaliação mais grossas; em "reduz as falhas" (6.0s) sua camada de falhas entra bem mais fina.
Scene 3 (7.1–9.11s): em "custo total" (7.4s) uma linha reta horizontal marca o topo de cada barra, e um bloco cobalto invertido "CUSTO TOTAL ↓" aparece sobre a barra DEPOIS em "cai" (8.6s). Legenda à direita: PREVENÇÃO · AVALIAÇÃO · FALHAS (células com densidades diferentes do mesmo cobalto). Segura.

## Frame 6 — Indicadores

- scene: Um cartão de indicador se monta campo a campo: nome, fórmula, meta, frequência, responsável
- voiceover: "Na Aula 7, os indicadores de desempenho. O que não se mede não se gerencia. Um bom indicador tem fórmula clara, meta, frequência de medição e um responsável."
- duration: 9.835s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/06-indicadores.html
- type: feature_showcase
- persuasion: Maxim + checklist
- beat: Focus + orientation
- blueprint: grid-card-assemble (Adapt)
- focal: o cartão de indicador com seus cinco campos
- roles: cartão de indicador (ficha retangular, ~55% da largura) = herói · máxima 'O que não se mede não se gerencia' = apoio (ed-callout) · rótulo AULA 7 = chrome

narrativeRole: Abre a Aula 7 com o que torna um indicador útil.
keyMessage: Indicador = fórmula, meta, frequência e responsável.

Adapt: a grade vira uma ficha cujas linhas se montam em cascata no tempo da fala. Entrada das linhas → dynamic-content-sequencing.
Scene 1 (0.0–2.6s): rótulo micro-strong "AULA 7" e título headline "Indicadores de desempenho" (1.1s) no topo esquerdo.
Scene 2 (2.6–4.9s): a máxima "O que não se mede não se gerencia." entra em ed-callout itálico à esquerda (40%), com "não se gerencia" em bloco cobalto invertido em 3.7s.
Scene 3 (4.9–6.1s): em "Um bom indicador" (5.0s) a ficha retangular de contorno cobalto entra à direita (60%), com cabeçalho "INDICADOR" em faixa cobalto invertida.
Scene 4 (6.1–9.84s): as linhas da ficha (ledger-row: rótulo micro-strong à esquerda, valor em mono à direita) entram no tempo da fala: "FÓRMULA" (6.1s), "META" (7.0s), "FREQUÊNCIA" (7.5s), "RESPONSÁVEL" (8.9s); cada linha ganha um pequeno quadrado preenchido à esquerda como check. Segura.

## Frame 7 — O que é OEE

- scene: A sigla OEE se expande em "Eficiência Global do Equipamento"; abaixo, a fórmula OEE = D × P × Q se monta
- voiceover: "O indicador mais cobrado é o OEE, a Eficiência Global do Equipamento. Ele multiplica três fatores: disponibilidade, desempenho e qualidade."
- duration: 8.661s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-oee.html
- type: product_intro
- persuasion: Concept announcement + formula
- beat: Clarity + focus
- blueprint: kinetic-type-beats (Adapt)
- focal: a fórmula OEE = DISPONIBILIDADE × DESEMPENHO × QUALIDADE
- roles: sigla OEE = herói inicial · nome por extenso = apoio · fórmula = herói final

narrativeRole: Nomeia o OEE e sua estrutura multiplicativa.
keyMessage: OEE = disponibilidade × desempenho × qualidade.

Adapt: mantém a troca no lugar da sigla pelo nome e a construção por batidas; o payoff vira a fórmula. Troca no lugar → discrete-text-sequence.
Scene 1 (0.0–2.2s): em "OEE" (1.6s) a sigla OEE entra enorme (vbig-numeral) no centro superior; rótulo mono "O INDICADOR MAIS COBRADO" acima dela (0.6s).
Scene 2 (2.2–4.2s): "Eficiência Global do Equipamento" escreve-se em headline sob a sigla, palavra a palavra (2.3s, 2.8s, 3.4s); a sigla sobe e reduz.
Scene 3 (4.2–8.66s): em "multiplica" (4.6s) aparece "OEE =" à esquerda da fórmula na metade inferior útil; os três termos entram em blocos retangulares de contorno, separados por "×": "DISPONIBILIDADE" (6.2s), "DESEMPENHO" (7.3s), "QUALIDADE" (8.0s). Segura.

## Frame 8 — Os três fatores

- scene: Três colunas, cada uma com sua razão em forma de fração: tempo operando ÷ tempo planejado; produção real ÷ produção na velocidade ideal; peças boas ÷ total produzido
- voiceover: "Disponibilidade: o tempo que a máquina realmente operou sobre o tempo planejado. Desempenho: o que ela produziu sobre o que poderia produzir na velocidade ideal. Qualidade: as peças boas sobre o total produzido."
- duration: 12.437s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/08-fatores.html
- type: feature_showcase
- persuasion: Rule of three + definitions as fractions
- beat: Comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: as três frações (real ÷ ideal)
- roles: três colunas de fração (numerador / traço / denominador) = herói em tríptico · títulos dos fatores = apoio · grade = fundo

narrativeRole: Define cada fator como uma razão, que é como a prova pede.
keyMessage: Cada fator é uma fração entre o real e o ideal.

Adapt: a grade vira um tríptico de frações; cada coluna entra no tempo do seu fator e a fração se monta de cima para baixo. Montagem → dynamic-content-sequencing; traço de fração que se desenha → svg-path-draw.
Scene 1 (0.0–4.9s): coluna 1 — "DISPONIBILIDADE" (table-name) em 0.0s; numerador "tempo operando" (1.3s), o traço de fração se desenha em "sobre" (3.3s) e o denominador "tempo planejado" entra (3.6s).
Scene 2 (4.9–9.4s): coluna 2 — "DESEMPENHO" (4.9s); numerador "produção real" (6.2s), traço em "sobre" (6.6s), denominador "produção na velocidade ideal" (7.5s).
Scene 3 (9.4–12.44s): coluna 3 — "QUALIDADE" (9.4s); numerador "peças boas" (10.3s), traço em "sobre" (11.1s), denominador "total produzido" (11.4s). Uma faixa mono abaixo do tríptico: "REAL ÷ IDEAL" (11.8s). Segura.

## Frame 9 — OEE na prática

- scene: Três barras 90%, 80% e 95% se multiplicam e encolhem até 68,4%
- voiceover: "Exemplo: disponibilidade de noventa por cento, desempenho de oitenta e qualidade de noventa e cinco. Multiplicando, o OEE é de sessenta e oito vírgula quatro por cento. Cada fator parecia bom, mas juntos revelam as perdas."
- duration: 13.269s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/09-oee-exemplo.html
- type: social_proof
- persuasion: Worked example with real numbers + surprise
- beat: "Aha" + mastery
- blueprint: dataviz-countup (Adapt)
- focal: o número 68,4%
- roles: três barras horizontais 90% / 80% / 95% = herói inicial · barra resultante e o número 68,4% = herói final · conta em mono = apoio

narrativeRole: Calcula o OEE e mostra o efeito multiplicativo das perdas.
keyMessage: 0,90 × 0,80 × 0,95 = 68,4%.

Adapt: mantém a contagem até um número herói; as barras multiplicadas encolhem até o resultado. Barras → stat-bars-and-fills; contagem → counting-dynamic-scale.
Scene 1 (0.0–5.8s): rótulo mono "EXEMPLO" no topo; três barras horizontais de 20 células (cada célula = 5%) entram no tempo da fala com rótulo à esquerda e valor à direita: DISPONIBILIDADE 90% (1.7s), DESEMPENHO 80% (3.4s), QUALIDADE 95% (4.6s).
Scene 2 (5.8–8.5s): em "Multiplicando" (5.8s) a conta "0,90 × 0,80 × 0,95" escreve-se em mono acima de uma quarta barra vazia; o intermediário "= 0,72" pisca brevemente em 6.6s.
Scene 3 (8.5–9.9s): em "68,4%" (8.5s) a quarta barra "OEE" se preenche em cobalto até ~68% e o número conta de 0 até 68,4% em vbig-numeral dentro de um bloco cobalto invertido à direita.
Scene 4 (9.9–13.27s): em "juntos revelam as perdas" (11.8s) a parte vazia da barra OEE (os ~32% restantes) ganha hachura e o rótulo "PERDAS" acima dela. Segura parado.

## Frame 10 — Todo processo varia

- scene: A sigla CEP se expande em "Controle Estatístico de Processo"; uma fileira de medições oscila em torno de uma linha média; surge a pergunta "normal ou problema?"
- voiceover: "Na Aula 8, o Controle Estatístico de Processo, o CEP. Todo processo varia. A pergunta é: essa variação é normal, ou tem algo errado?"
- duration: 7.915s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/10-cep.html
- type: pain_point
- persuasion: Concept announcement + question
- beat: Tension → curiosity
- blueprint: compose
- focal: a fileira de medições oscilando em torno da linha média
- roles: sigla CEP / nome = apoio no topo · série de pontos quadrados em torno de uma linha média = herói (faixa larga central) · pergunta final = apoio

narrativeRole: Abre a Aula 8 com a pergunta central do CEP.
keyMessage: Variação sempre existe; o CEP separa a normal da anormal.

Compose: troca de sigla por nome seguida de uma série que se desenha ponto a ponto. Troca no lugar → discrete-text-sequence; linha da série → svg-path-draw.
Scene 1 (0.0–3.4s): rótulo micro-strong "AULA 8" (0.2s); "Controle Estatístico de Processo" em headline palavra a palavra (1.0s–2.2s); em "CEP" (2.8s) a sigla em display-chapter à esquerda do nome.
Scene 2 (3.4–4.7s): em "Todo processo varia" (3.4s) uma linha média horizontal fina se desenha numa faixa larga (80% da largura) no centro, e pontos quadrados pequenos entram da esquerda para a direita, subindo e descendo em torno dela, ligados por uma linha fina; rótulo mono "MEDIÇÕES" à esquerda.
Scene 3 (4.7–7.915s): em "essa variação é normal" (5.5s) um rótulo "NORMAL?" em contorno aparece acima da série; em "algo errado?" (7.2s) um segundo rótulo "PROBLEMA?" em bloco cobalto invertido aparece ao lado, com "ou" entre eles em ed-callout. Segura.

## Frame 11 — Causas comuns × especiais

- scene: Dois cartões opostos: CAUSAS COMUNS ("variação natural, sempre presente") × CAUSAS ESPECIAIS ("eventos pontuais: ferramenta gasta, lote ruim — investigar e eliminar")
- voiceover: "Causas comuns são pequenas variações naturais, sempre presentes. Causas especiais são eventos pontuais, como uma ferramenta gasta ou um lote ruim de matéria-prima. Essas precisam ser investigadas e eliminadas."
- duration: 12.459s
- transition_in: crossfade
- status: animated
- src: compositions/frames/11-causas.html
- type: feature_showcase
- persuasion: Comparison of two options
- beat: Recognition + "aha"
- blueprint: comparison-split (Adapt)
- focal: os dois cartões CAUSAS COMUNS × CAUSAS ESPECIAIS
- roles: cartão CAUSAS COMUNS = herói esquerdo (contorno) · cartão CAUSAS ESPECIAIS = herói direito (cobalto invertido) · selo 'INVESTIGAR' = apoio

narrativeRole: Distingue os dois tipos de causa, base do gráfico de controle.
keyMessage: Comum = natural; especial = evento a investigar.

Adapt: mantém a entrada dividida com inclinações espelhadas e os selos nas bordas internas; selos são retângulos (sem pílula) e cada cartão entra no tempo da sua palavra. Cartões → split-tilt-cards; selo → spring-pop-entrance.
Scene 1 (0.0–3.8s): em "Causas comuns" (0.0s) o cartão esquerdo entra da esquerda com inclinação espelhada: "CAUSAS COMUNS" (display-chapter) + "variação natural, sempre presente" (body-lede, 1.4s); dentro do cartão, uma mini-série de pontos quadrados oscilando dentro de uma faixa estreita.
Scene 2 (3.8–9.8s): em "Causas especiais" (3.8s) o cartão direito entra da direita, fundo cobalto invertido: "CAUSAS ESPECIAIS" + "eventos pontuais" (5.1s); exemplos em mono entram um a um: "ferramenta gasta" (6.6s), "lote ruim de matéria-prima" (7.8s); dentro do cartão, uma mini-série com um ponto que salta para fora da faixa.
Scene 3 (9.8–12.46s): em "investigadas" (10.9s) um selo retangular "INVESTIGAR E ELIMINAR" salta na borda interna do cartão direito (a única entrada com leve overshoot). Segura parado.

## Frame 12 — Gráfico de controle

- scene: Um gráfico de controle se monta: linha média, LSC e LIC; os pontos entram um a um e um ponto sai acima do LSC e é destacado
- voiceover: "O gráfico de controle mostra isso: uma linha média e os limites superior e inferior de controle, em geral a três desvios-padrão da média. Um ponto fora dos limites, ou uma sequência estranha de pontos, sinaliza causa especial."
- duration: 13.312s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/12-grafico-controle.html
- type: benefit_highlight
- persuasion: Demonstration + signal detection
- beat: Unease → conviction
- blueprint: dataviz-countup (Adapt)
- focal: o ponto fora do LSC
- roles: gráfico de controle (eixos, LM, LSC, LIC, série de pontos quadrados) = herói (~75% da largura) · rótulos das linhas em mono = apoio · destaques = apoio

narrativeRole: Mostra a ferramenta do CEP e como ler um sinal.
keyMessage: LM, LSC e LIC (±3σ); ponto fora = causa especial.

Adapt: mantém o gráfico como herói, com o destaque final aterrissando no sinal; sem contagem. Linhas e série → svg-path-draw; destaque do ponto → css-marker-patterns.
Scene 1 (0.0–2.2s): título headline "Gráfico de controle" no topo esquerdo (0.2s); eixos finos do gráfico se desenham na área central.
Scene 2 (2.2–5.7s): em "linha média" (2.4s) a LM se desenha (linha cheia) com rótulo mono "LM" à direita; em "superior" (3.8s) a LSC (linha tracejada) acima, rótulo "LSC"; em "inferior" (4.5s) a LIC abaixo, rótulo "LIC".
Scene 3 (5.7–8.4s): em "três desvios-padrão" (6.3s) duas chaves retas marcam a distância LM→LSC e LM→LIC com "+3σ" e "−3σ" em mono; ao mesmo tempo a série de pontos quadrados começa a entrar da esquerda, oscilando dentro dos limites.
Scene 4 (8.4–10.3s): em "Um ponto fora" (8.6s) um ponto sai acima da LSC; ele vira um quadrado cobalto maior emoldurado por um retângulo, com o rótulo "FORA DO LIMITE" em bloco invertido.
Scene 5 (10.3–13.31s): em "sequência estranha" (10.3s) os pontos seguintes formam uma sequência de 7 pontos todos acima da LM, destacada por um retângulo de contorno tracejado com rótulo "SEQUÊNCIA"; em "causa especial" (12.4s) uma faixa cobalto invertida "SINAL DE CAUSA ESPECIAL" aparece no topo do gráfico. Segura.

## Frame 13 — Síntese

- scene: Quatro colunas convergem: GQT (todos), CUSTOS (prevenir), OEE (medir perdas), CEP (controlar); embaixo, a palavra DADOS volta
- voiceover: "Resumindo: a GQT envolve todos na qualidade, os custos mostram que prevenir sai mais barato, o OEE mede as perdas da máquina, e o CEP separa a variação normal do problema. Qualidade se gerencia com dados."
- duration: 12.757s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/13-sintese.html
- type: branding
- persuasion: Distillation + callback
- beat: Satisfaction + "now I get it"
- blueprint: titlecard-reveal (Adapt)
- focal: a palavra DADOS (retorno do gancho)
- roles: quatro colunas GQT / CUSTOS / OEE / CEP = apoio que converge · DADOS em bloco cobalto invertido = herói final · grade = fundo

narrativeRole: Responde ao gancho e une as três aulas numa ideia.
keyMessage: Qualidade se gerencia com dados.

Adapt: mantém o cartão-título calmo com um único movimento contido e a parada final, precedido pela montagem de quatro colunas. Entrada das colunas → dynamic-content-sequencing.
Scene 1 (0.0–2.8s): quatro colunas separadas por filetes verticais na metade superior; em "GQT" (0.6s) a primeira: "GQT" (display-chapter) + "envolve todos".
Scene 2 (2.8–5.4s): em "custos" (3.0s) a segunda: "CUSTOS" + "prevenir sai mais barato".
Scene 3 (5.4–7.7s): em "OEE" (5.6s) a terceira: "OEE" + "mede as perdas".
Scene 4 (7.7–10.6s): em "CEP" (7.9s) a quarta: "CEP" + "separa o normal do problema".
Scene 5 (10.6–12.757s): em "Qualidade se gerencia" (10.6s) os filetes somem, as colunas encolhem levemente para cima, e "com dados" — a palavra DADOS — sobe em display-hero dentro de um bloco cobalto invertido no centro inferior útil (eco do quadro 1), com "qualidade se gerencia com" em ed-callout acima dela. Um único movimento; parada total até o fim.
