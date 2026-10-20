---
format: 1920x1080
duration: 240s
message: "Uma fórmula (I, D, E, F) e um macete visual por questão para responder as 4 perguntas da Revisão B como o gabarito espera"
arc: how-to (formula) + 4 worked answers + recap
audience: estudante que faz a prova amanhã e precisa memorizar as respostas das Questões de Revisão B (Administração e Integração de Operações e Qualidade)
language: pt-BR
mode: autonomous
music: none
music_brief: calm focused minimal study underscore, soft piano and light pulse (host-generated, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** cada quadro leva a moldura Cobalt Grid — grade de papel milimetrado permanente, filetes cobalto no topo e na base (base em y ≤ 896), tag de chrome em DM Mono no canto superior esquerdo "REVISÃO B · MACETES" e numeração "NN / 18" no canto superior direito.
- **paleta:** só duas cores do `frame.md` — papel creme e tinta cobalto. "Falha", "perda", "fora de controle" nunca ganham vermelho: usam bloco cobalto invertido (texto creme sobre cobalto) ou um risco cobalto. Nada de gradientes coloridos, sombras ou brilhos.
- **tipo:** Newsreader 400 para títulos, termos e números grandes; Hanken Grotesk 600 caixa-alta espaçada para rótulos; DM Mono para tags, eixos, fórmulas e chrome. Texto que carrega significado nunca abaixo de ~27 px. Todo texto visível em português do Brasil, exatamente como nas linhas Scene.
- **forma:** só retângulos e linhas retas — sem cantos arredondados, sem círculos, sem pílulas; pontos de gráfico são quadrados pequenos. Setas são linhas retas com ponta triangular. Dados viram barras de células da grade quando couber.
- **zona útil:** todo conteúdo acima de y = 900 px (faixa das legendas); herói centrado em y ≈ 454.
- **movimento:** curvas de cauda longa (power3 por padrão; overshoot só onde a cena pede). Anime só transformações e opacidade (x, y, scale, opacity, clip-path, stroke) — nunca left/top/width/height. Cada peça entra quando a narração a nomeia; depois de resolvido, o quadro segura a leitura parado.
- **ritmo e riqueza de animação:** este vídeo é para memorizar — "use e abuse de animações e exemplos". Cada item falado ganha sua PRÓPRIA entrada animada (pop, desenho de linha, contagem, deslize, carimbo), e cada exemplo vira uma mini-cena desenhada com retângulos e linhas (caixas, esteira, gangorra, medidores, máquina). Movimento contínuo e com propósito: objetos do exemplo se mexem (esteira corre, peças caem, ponteiros giram, barras sobem) enquanto a narração fala deles; a parada de leitura só acontece nos últimos ~0,8 s. Macetes (palavras-gancho) entram com destaque forte: bloco cobalto invertido + leve overshoot ou carimbo. Os quadros 6 (resposta Q1 montada) e 17 (cola) são os de consolidação; o 18 é o respiro final.
- **lista negativa:** vermelho/verde/amarelo, sombras difusas, bokeh, gradiente roxo-azul de "IA", emoji, cantos arredondados, círculos, conteúdo abaixo de y = 900, fontes via @import ou CDN; os dois modos de falha — slide (tudo de uma vez e congela) e protetor de tela (tudo flutuando sem parar).

## Frame 1 — A prova é amanhã

- scene: Um calendário com AMANHÃ em destaque; quatro cartões de questão caem empilhados (Q1–Q4); todos ganham o mesmo carimbo "EXPLIQUE COM SUAS PALAVRAS"; surge uma chave: FÓRMULA
- voiceover: "A prova é amanhã. São quatro perguntas, e todas pedem a mesma coisa: explicar com suas palavras. Com uma fórmula de quatro passos, você responde qualquer uma delas."
- duration: 9.472s
- transition_in: cut
- status: outline
- src: compositions/frames/01-amanha.html
- type: hook
- persuasion: Stakes + promise
- beat: Urgency → relief
- blueprint: kinetic-type-beats (Adapt)
- focal: o carimbo EXPLIQUE COM SUAS PALAVRAS sobre os quatro cartões
- roles: calendário AMANHÃ = apoio inicial · quatro cartões Q1–Q4 = herói · carimbo = herói · chave FÓRMULA = payoff

narrativeRole: Acalma e promete um método único.
keyMessage: As quatro questões têm a mesma estrutura; uma fórmula resolve todas.

Adapt: frase em batidas vira uma mini-cena com objetos que caem e são carimbados. Entradas → spring-pop-entrance; carimbo → kinetic-beat-slam.
Scene 1 (0.0–1.3s): uma folha de calendário retangular cai de cima e assenta à esquerda; a palavra AMANHÃ é destacada em bloco cobalto invertido (0.6s), com rótulo mono "PROVA".
Scene 2 (1.3–3.3s): em "quatro perguntas" (1.5s) quatro cartões retangulares Q1, Q2, Q3, Q4 caem um a um em leque à direita (overshoot leve), cada um com um título curto em mono: "4 V'S", "PPCP", "PREVISÃO", "INDICADORES".
Scene 3 (3.3–5.9s): em "explicar com suas palavras" (4.1s) um carimbo retangular "EXPLIQUE COM SUAS PALAVRAS" bate em cada cartão em sequência rápida (4.1s, 4.4s, 4.7s, 5.0s), com leve tremor do cartão a cada batida.
Scene 4 (5.9–9.472s): em "fórmula de quatro passos" (6.3s) os cartões se alinham numa fileira e, acima deles, uma faixa invertida "1 FÓRMULA → 4 RESPOSTAS" desce; em "qualquer uma" (8.5s) linhas retas finas ligam a faixa a cada cartão. Segura.

## Frame 2 — Fórmula: I e D

- scene: Quatro blocos-letra I · D · E · F alinhados; I acende com "IMPORTÂNCIA — por que o tema importa"; D acende com "DEFINIÇÃO — cada elemento em 1 frase"
- voiceover: "Grave a fórmula das quatro iniciais: importância, definição, efeito e fecho. Importância: comece dizendo por que o tema é importante. Definição: explique cada elemento em uma frase curta."
- duration: 10.688s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-formula-id.html
- type: feature_showcase
- persuasion: Acronym mnemonic
- beat: Clarity
- blueprint: kinetic-type-beats (Adapt)
- focal: os blocos-letra I · D · E · F
- roles: quatro blocos-letra grandes I D E F = herói · descrições sob I e D = apoio · E e F ainda em contorno = apoio

narrativeRole: Ensina a primeira metade da fórmula.
keyMessage: I = importância; D = definição.

Adapt: acrônimo que se constrói em batidas; cada letra acende e desdobra sua palavra. Entradas → spring-pop-entrance; palavras → dynamic-content-sequencing.
Scene 1 (0.0–2.0s): título headline "A fórmula" no topo esquerdo; quatro quadrados vazios em contorno entram em fileira no centro superior com pop escalonado.
Scene 2 (2.0–4.5s): as letras I, D, E, F aparecem nos quadrados (display-hero) no tempo das palavras: I (2.0s), D (2.6s), E (3.2s), F (3.8s); cada letra estica para revelar sua palavra embaixo em micro-strong: IMPORTÂNCIA, DEFINIÇÃO, EFEITO, FECHO.
Scene 3 (4.5–7.6s): em "Importância" (4.5s) o bloco I vira cobalto invertido e cresce; abaixo dele um cartão desce: "Por que o tema é importante?" + exemplo mono "“…é importante porque…”" (6.1s).
Scene 4 (7.6–10.688s): em "Definição" (7.6s) o bloco D acende; seu cartão mostra "Cada elemento em 1 frase" e três linhas curtas que se desenham uma a uma como frases (8.9s, 9.3s, 9.7s). E e F seguem em contorno, piscando de leve para criar expectativa. Segura.

## Frame 3 — Fórmula: E e F

- scene: E acende com "EFEITO — o que muda na empresa + exemplo"; F acende com "FECHO" e as quatro palavras mágicas caem numa caixa: PRODUTIVIDADE · QUALIDADE · EFICIÊNCIA · SATISFAÇÃO DO CLIENTE
- voiceover: "Efeito: mostre o que muda na empresa, com um exemplo. Fecho: termine com as palavras que aparecem em todo gabarito: produtividade, qualidade, eficiência e satisfação do cliente."
- duration: 10.517s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/03-formula-ef.html
- type: feature_showcase
- persuasion: Acronym mnemonic + magic words
- beat: "Aha"
- blueprint: kinetic-type-beats (Adapt)
- focal: a caixa das quatro palavras mágicas
- roles: blocos E e F acesos = herói · cartão do efeito com mini-exemplo = apoio · caixa FECHO recebendo quatro palavras = herói final

narrativeRole: Completa a fórmula e entrega as palavras de fecho.
keyMessage: E = efeito com exemplo; F = fecho com as 4 palavras.

Adapt: continuação do acrônimo; o payoff são palavras que caem numa caixa. Palavras caindo → spring-pop-entrance; destaque → css-marker-patterns.
Scene 1 (0.0–3.0s): a fileira I D E F volta no topo (I e D acesos, menores); em "Efeito" (0.2s) o bloco E acende; seu cartão: "O que muda na empresa" + em "exemplo" (2.2s) um mini-ícone de fábrica (retângulos + telhado em dente de serra) com uma seta reta de ANTES → DEPOIS.
Scene 2 (3.0–6.7s): em "Fecho" (3.0s) o bloco F acende; abaixo, uma caixa retangular aberta (contorno) com o rótulo "PALAVRAS QUE O PROFESSOR ESPERA" (5.0s).
Scene 3 (6.7–10.517s): quatro palavras caem uma a uma dentro da caixa com overshoot, empilhando: PRODUTIVIDADE (6.7s), QUALIDADE (7.7s), EFICIÊNCIA (8.4s), SATISFAÇÃO DO CLIENTE (9.2s) — esta em bloco invertido; a caixa ganha um sublinhado cobalto traçado. Segura.

## Frame 4 — Q1: quatro V, quatro perguntas

- scene: Quatro blocos V empilham; cada um vira uma pergunta com ícone geométrico: VOLUME "quanto?" (pilha de caixas), VARIEDADE "quantos tipos?" (formas diferentes), VARIAÇÃO "a demanda muda?" (linha em degraus), VISIBILIDADE "o cliente vê?" (janela)
- voiceover: "Primeira questão: os quatro vês. Macete: transforme cada um em uma pergunta. Volume: quanto produz? Variedade: quantos tipos diferentes? Variação: a demanda muda ao longo do tempo? Visibilidade: quanto o cliente vê da operação?"
- duration: 12.928s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/04-quatro-v.html
- type: feature_showcase
- persuasion: Mnemonic: turn terms into questions
- beat: Comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: as quatro colunas V → pergunta
- roles: quatro colunas: bloco V + nome + pergunta + mini-ícone animado = herói · título = apoio

narrativeRole: Define os 4 V's de forma memorizável.
keyMessage: Volume, variedade, variação, visibilidade = quanto, quais, muda, vê.

Adapt: quatro cartões que se montam no tempo da fala; cada um vira uma pergunta com ícone vivo. Entradas → spring-pop-entrance; ícones → svg-path-draw.
Scene 1 (0.0–2.4s): faixa de seção invertida "QUESTÃO 1 · OS 4 V'S" no topo (0.5s); quatro blocos "V" grandes caem em fileira (1.0s–1.4s).
Scene 2 (2.4–4.3s): em "transforme cada um em uma pergunta" (2.4s) cada V gira em 3D (rotationY) e vira um ponto de interrogação, voltando a V em 3.6s — o gesto do macete.
Scene 3 (4.3–10.4s): as colunas se completam no tempo da fala: VOLUME (4.3s) "quanto?" com caixas que se empilham; VARIEDADE (5.7s) "quantos tipos?" com quadrado, triângulo e retângulo diferentes; VARIAÇÃO (7.8s) "a demanda muda?" com uma linha em degraus que sobe e desce sendo desenhada.
Scene 4 (10.4–12.928s): VISIBILIDADE (10.4s) "o cliente vê?" com uma janela retangular cujas persianas (linhas) se abrem revelando a operação; as quatro perguntas ficam em bloco invertido. Segura.

## Frame 5 — Q1: parafuso × alfaiate

- scene: Split: à esquerda uma esteira cheia de parafusos idênticos (VOLUME ALTO · VARIEDADE BAIXA → PADRONIZADA); à direita um alfaiate com peças únicas (POUCO · PERSONALIZADO → FLEXÍVEL)
- voiceover: "Agora o exemplo que o gabarito quer: uma fábrica de parafusos tem volume alto e variedade baixa, então trabalha padronizada. Um alfaiate faz peças personalizadas, em pouca quantidade, então precisa de flexibilidade."
- duration: 13.397s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/05-parafuso-alfaiate.html
- type: feature_showcase
- persuasion: Concrete contrast example
- beat: "Aha"
- blueprint: comparison-split (Adapt)
- focal: a esteira de parafusos × a mesa do alfaiate
- roles: metade esquerda: esteira com parafusos idênticos correndo = herói · metade direita: alfaiate com peças únicas = herói · etiquetas das conclusões = apoio

narrativeRole: Dá o exemplo que vira o "E" da resposta.
keyMessage: Alto volume + baixa variedade = padronização; personalizado = flexibilidade.

Adapt: duas mini-cenas lado a lado entrando de alas opostas, cada uma animada enquanto é narrada. Cartões → split-tilt-cards; objetos → spring-pop-entrance.
Scene 1 (0.0–2.1s): título headline "O exemplo do gabarito" no topo; divisória vertical se desenha no meio.
Scene 2 (2.1–7.5s): à esquerda, em "fábrica de parafusos" (2.3s), uma esteira horizontal (retângulo com roletes em linhas) entra e começa a correr; parafusos idênticos (retângulos estreitos com cabeça quadrada) passam em fila contínua; contador mono sobe rápido. Etiquetas entram no tempo: "VOLUME ALTO" (3.8s), "VARIEDADE BAIXA" (4.6s); em "padronizada" (6.6s) carimbo invertido "PADRONIZADA".
Scene 3 (7.5–13.397s): à direita, em "alfaiate" (7.8s), uma mesa com uma fita métrica (régua de células) e três peças de roupa diferentes (silhuetas retangulares: camisa, calça, colete) que aparecem uma a uma, cada uma com etiqueta "SOB MEDIDA"; etiquetas "POUCA QUANTIDADE" (10.2s), "PERSONALIZADO" (9.1s); em "flexibilidade" (12.4s) carimbo invertido "FLEXÍVEL". A esteira à esquerda segue correndo devagar. Segura no fim.

## Frame 6 — Q1: resposta montada

- scene: Uma folha de resposta se preenche em quatro faixas marcadas I · D · E · F, cada uma com a frase-chave da Q1
- voiceover: "Montando a resposta: os quatro vês ajudam a entender as diferenças entre as operações. Defina os quatro, use o contraste entre padronização e flexibilidade, e feche: estratégias adequadas trazem produtividade, qualidade, eficiência e satisfação."
- duration: 15.168s
- transition_in: crossfade
- status: outline
- src: compositions/frames/06-q1-resposta.html
- type: benefit_highlight
- persuasion: Worked answer
- beat: Mastery
- blueprint: grid-card-assemble (Adapt)
- focal: a folha de resposta preenchida I · D · E · F
- roles: folha de prova retangular com quatro faixas marcadas I/D/E/F = herói · frases-chave escritas linha a linha = herói · palavras do fecho destacadas = apoio

narrativeRole: Mostra a resposta da Q1 completa na fórmula.
keyMessage: Q1 pronta: I-D-E-F aplicada.

Adapt: a grade vira uma folha de prova que se preenche faixa por faixa, como se alguém escrevesse. Linhas → dynamic-content-sequencing; destaque → css-marker-patterns.
Scene 1 (0.0–1.2s): uma folha de prova (retângulo creme com contorno e pautas finas) desliza para o centro com o cabeçalho "Q1 · RESPOSTA"; à esquerda da folha, quatro marcadores quadrados I, D, E, F empilhados.
Scene 2 (1.2–5.1s): em "os 4 V's ajudam a entender" (1.4s) o marcador I acende e a faixa I se escreve (revelação da esquerda para a direita, como caneta): "Os 4 V's ajudam a entender as diferenças entre as operações."
Scene 3 (5.1–9.1s): em "Defina os quatro" (5.1s) o marcador D acende: "Volume = quantidade · Variedade = diversidade · Variação = mudanças na demanda · Visibilidade = contato com o cliente." Em "contraste" (6.7s) o marcador E acende: "Alto volume + baixa variedade → padronizada; personalizado → flexível."
Scene 4 (9.1–15.168s): em "feche" (9.4s) o marcador F acende: "Estratégias adequadas → produtividade, qualidade, eficiência e satisfação dos clientes." — cada uma das quatro palavras ganha um sublinhado cobalto traçado no tempo da fala (12.0s, 12.9s, 13.6s, 14.4s); um selo quadrado "✓ Q1" carimba o canto da folha. Segura.

## Frame 7 — Q2: PPCP em três perguntas

- scene: As letras P · P · C caem; cada uma vira uma pergunta: PLANEJAMENTO "o quê? com quais recursos?", PROGRAMAÇÃO "quando? em que ordem?" (relógio quadrado + sequência 1-2-3), CONTROLE "bateu com o plano?" (duas colunas plano × real com check)
- voiceover: "Questão dois: PPCP. Separe as letras em três perguntas. Planejamento: o que produzir e com quais recursos. Programação: quando e em que sequência. Controle: o que foi feito bate com o que foi planejado?"
- duration: 11.648s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/07-ppcp.html
- type: feature_showcase
- persuasion: Mnemonic: letters → questions
- beat: Comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: as três colunas P · P · C com suas perguntas e mini-cenas
- roles: letras P P C gigantes = herói inicial · três colunas com pergunta + mini-cena animada = herói · título = apoio

narrativeRole: Define as três funções do PPCP.
keyMessage: Planejar = o quê; programar = quando; controlar = conferiu?

Adapt: três cartões que se montam no tempo da fala; cada um ganha uma mini-cena. Entradas → spring-pop-entrance; desenhos → svg-path-draw.
Scene 1 (0.0–3.6s): faixa invertida "QUESTÃO 2 · PPCP" (0.4s); as letras P, P, C caem grandes em fileira (0.7s); em "três perguntas" (2.6s) cada letra encolhe para o topo de sua coluna.
Scene 2 (3.6–6.5s): coluna 1 PLANEJAMENTO (3.6s): pergunta "O QUÊ? COM QUAIS RECURSOS?"; mini-cena: uma prancheta com três itens de lista (caixas que ganham check) e ícones de recursos (engrenagem feita de quadrados, pessoa em blocos, caixa de material) que entram em 5.4s.
Scene 3 (6.5–8.6s): coluna 2 PROGRAMAÇÃO (6.5s): "QUANDO? EM QUE ORDEM?"; mini-cena: um relógio QUADRADO cujo ponteiro (linha) gira e três blocos numerados 1 → 2 → 3 que se encaixam em sequência numa linha do tempo (7.9s).
Scene 4 (8.6–11.648s): coluna 3 CONTROLE (8.6s): "BATEU COM O PLANO?"; mini-cena: duas barras lado a lado PLANEJADO × REALIZADO que crescem até a mesma altura e um selo quadrado ✓ salta entre elas em "planejado" (11.0s). Segura.

## Frame 8 — Q2: Kanban, JIT, Enxuta

- scene: Três mini-cenas: um cartão Kanban levantado como placa ("SINALIZA"), uma peça chegando exatamente quando o relógio bate ("NA HORA"), uma pilha de desperdícios encolhendo ("ENXUGA")
- voiceover: "Agora o trio, com um verbo para cada um. O Kanban sinaliza, como um cartão que avisa o que repor. O Just in Time entrega na quantidade e no momento certos. E a Produção Enxuta enxuga: corta desperdícios e melhora continuamente."
- duration: 13.12s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/08-trio.html
- type: feature_showcase
- persuasion: One verb per tool
- beat: "Aha"
- blueprint: grid-card-assemble (Adapt)
- focal: três mini-cenas com os verbos SINALIZA · NA HORA · ENXUGA
- roles: três painéis com mini-cenas animadas = herói · verbos-gancho em blocos invertidos = herói · descrições = apoio

narrativeRole: Dá um verbo-gancho a cada ferramenta.
keyMessage: Kanban sinaliza; JIT na hora; Enxuta enxuga.

Adapt: três painéis, um por ferramenta, cada um com uma ação animada que ilustra o verbo. Entradas → spring-pop-entrance; barras → stat-bars-and-fills.
Scene 1 (0.0–2.2s): título headline "Um verbo para cada um" (0.4s); três painéis em contorno entram em fileira.
Scene 2 (2.2–5.3s): painel 1 KANBAN (2.2s): uma prateleira com caixas; quando a última caixa sai, um cartão retangular levanta como placa (2.7s) e o verbo "SINALIZA" carimba em bloco invertido; legenda "cartão que avisa o que repor" (3.6s); uma caixa nova entra deslizando para repor.
Scene 3 (5.3–8.6s): painel 2 JUST IN TIME (5.4s): um relógio quadrado com ponteiro girando e uma peça que desliza por uma linha e chega EXATAMENTE quando o ponteiro bate no topo (7.7s); verbo "NA HORA" carimba; legenda "quantidade e momento certos".
Scene 4 (8.6–13.12s): painel 3 PRODUÇÃO ENXUTA (8.9s): uma pilha de blocos rotulados "DESPERDÍCIO" que encolhe em degraus (10.5s) enquanto uma seta em ciclo quadrado gira ao lado (melhoria contínua, 11.8s); verbo "ENXUGA" carimba (9.8s). Segura.

## Frame 9 — Q2: os quatro ganhos

- scene: Quatro medidores se movem: ESTOQUE ↓, ATRASOS ↓, USO DOS RECURSOS ↑, EFICIÊNCIA ↑; depois a faixa de fecho
- voiceover: "No efeito, cite quatro ganhos: menos estoque desnecessário, menos atrasos, melhor uso dos recursos e mais eficiência. E feche: a empresa produz de forma coordenada e atende melhor o cliente."
- duration: 11.456s
- transition_in: crossfade
- status: outline
- src: compositions/frames/09-ganhos.html
- type: benefit_highlight
- persuasion: Before/after gauges
- beat: Confidence
- blueprint: dataviz-countup (Adapt)
- focal: os quatro medidores com setas ↓ ↓ ↑ ↑
- roles: quatro medidores (barras verticais de células) = herói · setas de direção = herói · faixa de fecho = apoio

narrativeRole: Fecha a Q2 com os resultados do gabarito.
keyMessage: Menos estoque e atraso; mais uso de recursos e eficiência.

Adapt: quatro instrumentos que se movem no tempo da fala, sem números. Barras → stat-bars-and-fills; setas → spring-pop-entrance.
Scene 1 (0.0–1.9s): título headline "Os 4 ganhos" (0.6s); quatro medidores verticais de 10 células em fileira, todos começando em meia altura, com rótulos embaixo.
Scene 2 (1.9–6.9s): no tempo da fala, cada medidor se move com uma seta grande ao lado: ESTOQUE DESNECESSÁRIO desce para 2 células com seta ↓ (1.9s); ATRASOS desce com ↓ (3.5s); USO DOS RECURSOS sobe para 9 células com ↑ (4.5s); EFICIÊNCIA sobe com ↑ (5.8s) — as setas de subida em bloco invertido.
Scene 3 (6.9–11.456s): em "feche" (7.1s) uma faixa invertida desliza sob os medidores: "PRODUÇÃO COORDENADA → CLIENTE MAIS BEM ATENDIDO", com "COORDENADA" em 9.2s e "CLIENTE" em 10.9s. Segura.

## Frame 10 — Q3: antecipar

- scene: Uma luneta (formas retas) aponta para o futuro; dela saem cinco setas para ESTOQUES, PRODUÇÃO, COMPRAS, RECURSOS, CAPACIDADE
- voiceover: "Questão três: previsão de demanda. A palavra da importância é antecipar. Com a previsão, a empresa planeja estoques, produção, compras, recursos e capacidade."
- duration: 9.429s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/10-antecipar.html
- type: feature_showcase
- persuasion: Keyword + fan-out
- beat: Clarity
- blueprint: compose
- focal: a luneta e as cinco setas para o planejamento
- roles: luneta (tubo de retângulos) apontando para a direita = herói inicial · palavra ANTECIPAR = herói · cinco destinos em leque = herói final

narrativeRole: Dá a importância e o que a previsão permite planejar.
keyMessage: Previsão = antecipar para planejar estoque, produção, compras, recursos, capacidade.

Compose: um objeto-metáfora que se monta e dispara setas em leque no tempo da fala. Setas → svg-path-draw; destinos → spring-pop-entrance.
Scene 1 (0.0–2.1s): faixa invertida "QUESTÃO 3 · PREVISÃO DE DEMANDA" (0.8s); à esquerda, uma luneta feita de três retângulos encaixados se estica (telescópio abrindo).
Scene 2 (2.1–4.3s): em "antecipar" (3.5s) a palavra ANTECIPAR sai da ponta da luneta e para no meio em display-chapter dentro de bloco invertido; ao fundo, uma linha do tempo HOJE → FUTURO se desenha.
Scene 3 (4.3–9.429s): da palavra ANTECIPAR saem cinco setas retas em leque para a direita, cada uma terminando num bloco no tempo da fala: ESTOQUES (6.2s, ícone de caixas), PRODUÇÃO (6.8s, engrenagem quadrada), COMPRAS (7.4s, carrinho em linhas), RECURSOS (7.9s, pessoa em blocos), CAPACIDADE (8.6s, barra de células). Segura.

## Frame 11 — Q3: não é garantia

- scene: Um carimbo "ESTIMATIVA" se sobrepõe a "GARANTIA" riscado; ao lado, META (o que a empresa quer) × PREVISÃO (o que deve acontecer)
- voiceover: "Mas cuidado: previsão não é garantia, nem é meta. Meta é o que a empresa quer alcançar; previsão é só uma estimativa, e pode errar."
- duration: 7.573s
- transition_in: crossfade
- status: outline
- src: compositions/frames/11-nao-garantia.html
- type: pain_point
- persuasion: Common-mistake warning
- beat: Recognition
- blueprint: comparison-split (Adapt)
- focal: o carimbo ESTIMATIVA sobre GARANTIA riscada
- roles: palavra GARANTIA riscada + carimbo ESTIMATIVA = herói · cartões META × PREVISÃO = herói secundário

narrativeRole: Introduz a incerteza e diferencia meta × previsão.
keyMessage: Previsão = estimativa, pode errar; meta = desejo.

Adapt: mantém dois cartões opostos, precedidos por um carimbo de correção. Carimbo → kinetic-beat-slam; cartões → split-tilt-cards.
Scene 1 (0.0–2.4s): "Cuidado" (0.2s) entra como faixa invertida; a palavra GARANTIA aparece grande no centro (1.4s) e é riscada por um traço cobalto; um carimbo retangular ESTIMATIVA bate por cima (1.7s) com tremor.
Scene 2 (2.4–5.0s): a palavra encolhe para o topo; em "Meta" (3.0s) o cartão esquerdo entra com inclinação: "META" + "o que a empresa QUER alcançar", com um alvo quadrado (quadrados concêntricos) ao lado.
Scene 3 (5.0–7.573s): em "previsão" (5.0s) o cartão direito entra (cobalto invertido): "PREVISÃO" + "estimativa — pode errar"; em "errar" (7.1s) um pequeno "±" pisca ao lado. Segura.

## Frame 12 — Q3: a gangorra

- scene: Uma gangorra (prancha reta sobre triângulo): lado PREVIU DEMAIS desce com caixas empilhadas (SOBRA: estoque, desperdício, custo); depois inclina para PREVIU DE MENOS (FALTA: falta de produto, atraso, cliente insatisfeito)
- voiceover: "O macete da gangorra. Previu demais? Sobra: excesso de estoque, desperdício e custo alto. Previu de menos? Falta: produto em falta, atraso e cliente insatisfeito."
- duration: 9.579s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/12-gangorra.html
- type: feature_showcase
- persuasion: Physical metaphor + symmetric contrast
- beat: "Aha"
- blueprint: compose
- focal: a gangorra que inclina para SOBRA e depois para FALTA
- roles: gangorra (prancha reta sobre triângulo) = herói · caixas que se empilham/somem = herói · rótulos das consequências = apoio

narrativeRole: Torna memorável o efeito do erro para cima e para baixo.
keyMessage: Acima = sobra e custo; abaixo = falta e atraso.

Compose: metáfora física animada — o peso muda e a gangorra inclina. Inclinação e caixas → spring-pop-entrance; consequências → dynamic-content-sequencing.
Scene 1 (0.0–1.3s): título headline "O macete da gangorra" (0.1s); uma gangorra (prancha retangular sobre um triângulo) equilibrada no centro, com rótulos nas pontas: PREVIU DEMAIS (esquerda) e PREVIU DE MENOS (direita).
Scene 2 (1.3–5.2s): em "Previu demais" (1.3s) caixas caem uma a uma e empilham na ponta esquerda, que DESCE (rotação da prancha); em "Sobra" (2.2s) carimbo invertido "SOBRA"; abaixo, consequências entram no tempo: "EXCESSO DE ESTOQUE" (2.7s), "DESPERDÍCIO" (3.6s), "CUSTO ALTO" (4.4s, com um cifrão em blocos que cresce).
Scene 3 (5.2–9.579s): em "Previu de menos" (5.2s) as caixas somem, a gangorra inclina para o outro lado, a ponta direita fica com uma prateleira VAZIA; carimbo "FALTA" (6.3s); consequências: "PRODUTO EM FALTA" (6.8s), "ATRASO" (7.8s, relógio quadrado), "CLIENTE INSATISFEITO" (8.4s, rosto feito de quadrados com boca reta para baixo). As consequências de SOBRA permanecem esmaecidas à esquerda para comparação. Segura.

## Frame 13 — Q3: três As

- scene: Três blocos A em sequência com ícones: ACOMPANHAR (gráfico real × previsto), ANALISAR (lupa quadrada sobre o erro), ATUALIZAR (seta de ciclo); fecho em faixa
- voiceover: "E qual é a solução? Três As: acompanhar os resultados, analisar os erros e atualizar as estimativas. Assim, a previsão reduz incertezas e apoia decisões melhores."
- duration: 10.048s
- transition_in: crossfade
- status: outline
- src: compositions/frames/13-tres-as.html
- type: benefit_highlight
- persuasion: Alliteration mnemonic
- beat: Confidence
- blueprint: grid-card-assemble (Adapt)
- focal: os três blocos A · A · A em sequência
- roles: três blocos A com ícones animados = herói · setas entre eles = apoio · faixa de fecho = apoio

narrativeRole: Fecha a Q3 com a ação que o gabarito pede.
keyMessage: Acompanhar, analisar, atualizar.

Adapt: três cartões em sequência com setas, cada um com uma ação animada. Entradas → spring-pop-entrance; gráfico e setas → svg-path-draw.
Scene 1 (0.0–2.2s): título headline "A solução" (0.6s); em "Três As" (1.3s) três blocos "A" grandes caem em fileira com overshoot.
Scene 2 (2.2–3.5s): bloco 1 ACOMPANHAR (2.2s): um mini gráfico com duas linhas — REAL e PREVISTO — se desenhando lado a lado.
Scene 3 (3.5–4.6s): bloco 2 ANALISAR (3.5s): uma lupa QUADRADA (quadrado + cabo reto) desliza até o vão entre as linhas e destaca "ERRO".
Scene 4 (4.6–10.048s): bloco 3 ATUALIZAR (4.6s): uma seta em ciclo quadrado gira e a linha PREVISTO se ajusta, aproximando-se da REAL. Em "reduz incertezas" (7.4s) uma faixa invertida desliza embaixo: "MENOS INCERTEZA → DECISÕES MELHORES" ("DECISÕES" em 9.0s). Segura.

## Frame 14 — Q4: para que medir

- scene: Um painel de indicadores acende três funções: ACOMPANHAR RESULTADOS, AVALIAR PROCESSOS, ACHAR MELHORIAS
- voiceover: "Questão quatro: indicadores de desempenho. Eles são importantes porque permitem acompanhar resultados, avaliar os processos e encontrar oportunidades de melhoria."
- duration: 9.792s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/14-medir.html
- type: feature_showcase
- persuasion: Rule of three
- beat: Orientation
- blueprint: grid-card-assemble (Adapt)
- focal: o painel de indicadores com três funções
- roles: painel retangular com três mostradores = herói · três verbos ACOMPANHAR · AVALIAR · ENCONTRAR = herói · título = apoio

narrativeRole: Dá a importância da Q4.
keyMessage: Indicadores acompanham, avaliam e mostram melhorias.

Adapt: um painel de controle cujos mostradores ligam no tempo da fala. Mostradores → stat-bars-and-fills; rótulos → dynamic-content-sequencing.
Scene 1 (0.0–2.8s): faixa invertida "QUESTÃO 4 · INDICADORES" (0.5s); um painel retangular grande desliza para o centro com três mostradores apagados (retângulos com barras de células e um ponteiro reto).
Scene 2 (2.8–4.9s): em "importantes porque" (3.4s) o painel liga: as bordas acendem e um rótulo mono "POR QUE MEDIR?" aparece no topo.
Scene 3 (4.9–9.792s): cada mostrador liga no tempo da fala e ganha seu verbo em bloco invertido: ACOMPANHAR RESULTADOS (4.9s, barras sobem), AVALIAR PROCESSOS (6.3s, ponteiro gira até o meio), ENCONTRAR MELHORIAS (7.8s, uma seta ↑ pisca e um quadrado ✓ surge). Segura.

## Frame 15 — Q4: P, E, Q na máquina

- scene: Uma máquina (blocos retos) cospe peças; contadores: 200 peças em 8 h → 25 por hora (PRODUTIVIDADE = resultado ÷ recursos); régua com o padrão 30 (EFICIÊNCIA = real × padrão); 190 boas de 200 (QUALIDADE = cumpre requisitos)
- voiceover: "Decore o trio produtividade, eficiência e qualidade com um exemplo. Uma máquina faz duzentas peças em oito horas: produtividade de vinte e cinco por hora, resultado sobre recursos. O padrão era trinta: eficiência é comparar com o esperado. Cento e noventa saíram boas: qualidade é cumprir os requisitos."
- duration: 17.579s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/15-peq.html
- type: social_proof
- persuasion: Worked numeric example
- beat: "Aha" + mastery
- blueprint: dataviz-countup (Adapt)
- focal: a máquina e os três contadores P · E · Q
- roles: máquina (blocos retos) soltando peças numa esteira = herói · três contadores com fórmulas = herói · letras P E Q = apoio

narrativeRole: Define produtividade, eficiência e qualidade com números fáceis.
keyMessage: P = resultado ÷ recursos; E = real × padrão; Q = conformidade.

Adapt: contagem até números-herói, alimentada por uma mini-cena de fábrica. Contagens → counting-dynamic-scale; barras/régua → stat-bars-and-fills.
Scene 1 (0.0–4.0s): título headline "P · E · Q" com as palavras PRODUTIVIDADE (0.9s), EFICIÊNCIA (1.7s), QUALIDADE (2.5s) se desdobrando de cada letra; à esquerda, uma máquina (retângulos, uma chaminé, um botão quadrado) entra.
Scene 2 (4.0–10.4s): em "máquina faz" (4.2s) a máquina liga e solta peças quadradas numa esteira que corre; um contador "PEÇAS" sobe até 200 (5.0s→5.6s) e um relógio quadrado marca "8 h" (5.9s). Em "produtividade" (6.7s) o contador P mostra "200 ÷ 8 =" e conta até "25 /h" (7.7s); fórmula mono "RESULTADO ÷ RECURSOS" (8.8s).
Scene 3 (10.4–13.9s): em "padrão era 30" (10.6s) uma régua horizontal com marca "PADRÃO 30" aparece; a barra "REAL 25" para antes dela; contador E: "25 vs 30" (11.7s) e rótulo "COMPARA COM O ESPERADO" (12.4s).
Scene 4 (13.9–17.579s): em "190" (13.9s) as peças na esteira se separam: 190 seguem (contador conta até 190) e 10 caem num cesto "REFUGO"; contador Q: "190 de 200 boas" e rótulo "CUMPRE OS REQUISITOS" (16.4s). Segura.

## Frame 16 — Q4: medir para decidir

- scene: Um ciclo de quatro passos acende (IDENTIFICAR PROBLEMAS → COMPARAR COM METAS → RECONHECER DESPERDÍCIOS → AGIR); no centro, a frase de ouro "não só medir: orientar decisões"
- voiceover: "Com os números, o gestor identifica problemas, compara com as metas, reconhece desperdícios e age. A frase de ouro: indicadores não servem só para medir; servem para orientar decisões e gerar melhoria contínua."
- duration: 12.779s
- transition_in: crossfade
- status: outline
- src: compositions/frames/16-decidir.html
- type: benefit_highlight
- persuasion: Cycle + golden sentence
- beat: Conviction
- blueprint: compose
- focal: o ciclo de quatro passos com a frase de ouro no centro
- roles: ciclo quadrado de quatro blocos = herói · frase de ouro = herói central · números do exemplo anterior pequenos = apoio

narrativeRole: Fecha a Q4 com uso dos indicadores e a frase do gabarito.
keyMessage: Indicadores orientam decisões e melhoria contínua.

Compose: um ciclo que se percorre no tempo da fala e revela a frase de ouro no centro. Setas → svg-path-draw; blocos → spring-pop-entrance.
Scene 1 (0.0–1.4s): os três contadores do quadro anterior aparecem pequenos no canto superior esquerdo ("25/h · 25 vs 30 · 190/200") com rótulo mono "COM OS NÚMEROS…".
Scene 2 (1.4–5.8s): quatro blocos em quadrado acendem em sequência com a seta reta do anterior se desenhando: IDENTIFICAR PROBLEMAS (1.4s), COMPARAR COM METAS (2.6s), RECONHECER DESPERDÍCIOS (3.8s), AGIR (5.1s, bloco invertido com leve overshoot); a seta de AGIR volta a IDENTIFICAR.
Scene 3 (5.8–12.779s): em "A frase de ouro" (5.9s) um selo "FRASE DE OURO" no centro do ciclo; a frase escreve-se em duas linhas: "Indicadores não servem só para medir;" (7.1s) e "servem para orientar decisões" (9.5s) em bloco invertido; em "melhoria contínua" (11.7s) as quatro setas do ciclo engrossam em sequência, como um pulso que roda o ciclo. Segura.

## Frame 17 — Cola visual

- scene: Uma "cola" em grade 2×2, um quadrante por questão, cada um com seu macete: Q1 "QUANTO · QUAIS · MUDA · VÊ"; Q2 "O QUÊ · QUANDO · CONFERIU / SINALIZA · NA HORA · ENXUGA"; Q3 "SOBRA CUSTA · FALTA ATRASA / 3 As"; Q4 "P · E · Q"
- voiceover: "Revise a cola. Volume, variedade, variação e visibilidade viram perguntas. PPCP: o quê, quando e conferiu. Kanban sinaliza, Just in Time na hora, Enxuta enxuga. Previsão: sobra custa, falta atrasa, e os três As. Indicadores: produtividade, eficiência e qualidade."
- duration: 16.256s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/17-cola.html
- type: branding
- persuasion: Recap grid
- beat: Mastery
- blueprint: grid-card-assemble (Adapt)
- focal: a cola 2×2 com os macetes das quatro questões
- roles: quatro quadrantes Q1–Q4 com macetes = herói · palavras-gancho em blocos invertidos = herói · título COLA = apoio

narrativeRole: Consolida todos os macetes numa tela para revisar.
keyMessage: Os quatro macetes numa tela.

Adapt: grade 2×2 que se preenche no tempo da fala, como uma cola sendo escrita. Entradas → dynamic-content-sequencing; destaques → spring-pop-entrance.
Scene 1 (0.0–1.0s): uma folha "COLA" (retângulo com pautas) desliza para o centro dividida em quatro quadrantes com cabeçalhos Q1, Q2, Q3, Q4.
Scene 2 (1.0–4.6s): Q1 (1.0s): "VOLUME · VARIEDADE · VARIAÇÃO · VISIBILIDADE" e, abaixo, as perguntas "QUANTO? QUAIS? MUDA? VÊ?" (3.5s) em blocos invertidos pequenos.
Scene 3 (4.6–9.9s): Q2 (4.6s): "PPCP = O QUÊ · QUANDO · CONFERIU" e, em 6.5s, "KANBAN SINALIZA · JIT NA HORA · ENXUTA ENXUGA" (cada verbo invertido ao ser dito: 7.0s, 8.4s, 9.2s).
Scene 4 (9.9–13.1s): Q3 (9.9s): uma mini-gangorra com "SOBRA CUSTA" (10.4s) e "FALTA ATRASA" (11.2s) nas pontas + "3 As" (12.2s).
Scene 5 (13.1–16.256s): Q4 (13.1s): "P · E · Q" em display com as palavras embaixo (13.9s, 14.8s, 15.6s). A folha inteira ganha um leve zoom final. Segura.

## Frame 18 — Boa prova

- scene: As letras I · D · E · F voltam grandes e se alinham; embaixo, "Boa prova!"
- voiceover: "E em toda resposta: importância, definição, efeito e fecho. Respire, siga a fórmula, e boa prova!"
- duration: 7.409s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/18-boa-prova.html
- type: branding
- persuasion: Callback
- beat: Calm confidence
- blueprint: titlecard-reveal (Adapt)
- focal: I · D · E · F grandes e 'Boa prova!'
- roles: quatro blocos-letra I D E F = herói · palavras sob cada letra = apoio · 'Boa prova!' = payoff

narrativeRole: Encerra com a fórmula e uma despedida tranquilizadora.
keyMessage: I-D-E-F em toda resposta.

Adapt: cartão-título calmo com um movimento contido e parada final. Entradas → dynamic-content-sequencing.
Scene 1 (0.0–3.6s): os quatro blocos I, D, E, F voltam grandes (cobalto invertido) em fileira no centro; cada um acende no tempo da sua palavra, com a palavra embaixo em micro-strong: IMPORTÂNCIA (1.2s), DEFINIÇÃO (1.9s), EFEITO (2.4s), FECHO (3.0s).
Scene 2 (3.6–5.2s): em "Respire" (3.6s) o movimento desacelera; um rótulo mono "EM TODA RESPOSTA" aparece acima da fileira.
Scene 3 (5.2–7.409s): em "boa prova" (5.2s) "Boa prova!" sobe em display-closing abaixo da fileira, num único movimento; parada total até o fim.
