---
format: 1920x1080
duration: 180s
message: "Prevenir falhas antes que aconteçam e prever a demanda com seu erro: duas formas de agir antes do problema"
arc: concept-explainer with process
audience: estudantes revisando Administração e Integração de Operações e Qualidade (Aulas 4 e 5)
language: pt-BR
mode: autonomous
music: none
music_brief: calm focused minimal study underscore, soft piano and light pulse (host-generated, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** cada quadro leva a moldura Cobalt Grid — grade de papel milimetrado permanente, filetes cobalto no topo e na base, tag de chrome em DM Mono no canto superior esquerdo "AULAS 4–5 · OPERAÇÕES" e numeração "NN / 13" no canto superior direito (a base fica livre para as legendas).
- **paleta:** só duas cores do `frame.md` — papel creme (fundo, superfícies) e tinta cobalto (texto, linhas, barras, blocos). "Problema", "risco" ou "erro" nunca ganham vermelho: usam bloco cobalto invertido (texto creme sobre cobalto) ou um risco cobalto. Nada de gradientes coloridos.
- **tipo:** Newsreader 400 para títulos, termos e números grandes (hierarquia por tamanho, não por peso); Hanken Grotesk 600 caixa-alta espaçada para rótulos; DM Mono para tags, eixos, fórmulas pequenas e chrome. Todo texto visível em português do Brasil, exatamente como nas linhas Scene.
- **forma:** só retângulos e linhas retas — sem cantos arredondados, sem círculos, sem pílulas. Setas são linhas retas com ponta triangular. Dados viram barras de células da grade (pixel-stack) quando couber.
- **zona útil:** todo conteúdo acima de y = 900 px (faixa das legendas embaixo); herói centrado em y ≈ 454.
- **movimento:** curvas de cauda longa (power3 por padrão; overshoot só onde a cena pede). Cada peça entra quando a narração a nomeia — nunca despejar tudo no início. Depois de resolvido, o quadro segura a leitura parado (no máximo um tremor sutil).
- **ritmo:** quadros 5 (336) e 11 (1.000) são os clímax numéricos; o quadro 10 é curto e leve; o quadro 13 é o respiro final, quase parado. Os quadros 8 e 13 seguram a leitura no último terço.
- **lista negativa:** vermelho/verde/amarelo, sombras difusas, bokeh, gradiente roxo-azul de "IA", ícones de emoji, cantos arredondados, círculos, conteúdo abaixo de y = 900, fontes do Google via @import; os dois modos de falha — slide (tudo de uma vez e congela) e protetor de tela (tudo flutuando sem parar).

## Frame 1 — Agir antes

- scene: Duas perguntas se constroem na tela: "e se falhar?" e "quanto vão pedir?", que convergem na palavra ANTES
- voiceover: "E se desse para descobrir uma falha antes de ela acontecer… e saber quanto o cliente vai pedir antes de ele pedir?"
- duration: 6.421s
- transition_in: cut
- status: outline
- src: compositions/frames/01-agir-antes.html
- type: hook
- persuasion: Rhetorical question + imagine / scenario
- beat: Curiosity + intrigue
- blueprint: kinetic-type-beats (Adapt)
- focal: a palavra ANTES em display-hero
- roles: ANTES = herói em primeiro plano · as duas perguntas = apoio (headline) · grade + filetes = fundo

narrativeRole: Abre a lacuna que une as duas aulas — antecipar em vez de reagir.
keyMessage: FMEA e previsão de demanda são ferramentas para agir antes do problema.

Adapt: mantém a assinatura de frase que se constrói em batidas sobre fundo plano; troca o payoff de marca por duas perguntas que convergem numa palavra. Revelação palavra a palavra → dynamic-content-sequencing.
Scene 1 (0.0–1.8s): grade e chrome já presentes; a pergunta "e se falhar?" monta palavra a palavra no terço superior esquerdo (headline, cobalto), cravando "falhar?" em "falha" (1.4s).
Scene 2 (1.8–3.3s): em "antes" (1.8s) um pequeno rótulo mono "ANTES DE ACONTECER" aparece sob a primeira pergunta; ela se acomoda.
Scene 3 (3.3–5.2s): a segunda pergunta "quanto vão pedir?" monta palavra a palavra no terço superior direito, terminando em "pedir" (4.9s) — layout espelhado 50/50.
Scene 4 (5.2–6.42s): em "antes de ele pedir?" (5.3s) as duas perguntas deslizam para o centro e encolhem para cima, e ANTES entra grande no centro (display-hero, ~55% da largura) dentro de um bloco cobalto invertido (texto creme); duas linhas retas finas ligam cada pergunta ao bloco. Segura parado até o fim.

## Frame 2 — O que é FMEA

- scene: A sigla FMEA se expande em "Análise dos Modos de Falha e seus Efeitos"; abaixo, três consequências evitadas são riscadas: dano ao cliente, parada de produção, retrabalho
- voiceover: "Na Aula 4, a FMEA: Análise dos Modos de Falha e seus Efeitos. Ela identifica problemas potenciais antes que causem dano ao cliente, parada de produção ou retrabalho."
- duration: 10.368s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-fmea.html
- type: product_intro
- persuasion: Concept announcement + progressive disclosure
- beat: Clarity + orientation
- blueprint: kinetic-type-beats (Adapt)
- focal: a sigla FMEA que se expande no nome completo
- roles: FMEA / nome por extenso = herói · lista das três consequências = apoio · rótulo AULA 4 = chrome

narrativeRole: Nomeia a ferramenta da Aula 4 e o que ela evita.
keyMessage: FMEA = identificar falhas potenciais antes de causarem prejuízo.

Adapt: mantém a troca de tokens no lugar (a sigla vira o nome) e a construção por batidas; o payoff vira uma lista riscada. Troca no lugar → discrete-text-sequence; riscos → css-marker-patterns.
Scene 1 (0.0–0.8s): rótulo micro-strong "AULA 4" entra no topo à esquerda.
Scene 2 (0.8–1.6s): em "FMEA" (0.8s) a sigla FMEA entra enorme (vbig-numeral) centrada na metade superior.
Scene 3 (1.6–4.2s): em "Análise" (1.6s) cada letra da sigla ganha embaixo sua palavra: F→Falha, M→Modos, E→Efeitos, A→Análise — a linha "Análise dos Modos de Falha e seus Efeitos" se escreve em headline sob a sigla, que sobe e reduz para display-chapter (troca no lugar, cortes secos por palavra no tempo da fala: Modos 2.2s, Falha 2.7s, Efeitos 3.4s).
Scene 4 (4.2–7.4s): "identifica problemas potenciais ANTES" (4.6s–6.5s) aparece em body-lede abaixo, com ANTES em bloco cobalto invertido no 6.5s.
Scene 5 (7.4–10.37s): três linhas em lista na metade inferior útil (acima de y=900), rótulos micro-strong: "DANO AO CLIENTE" (7.4s), "PARADA DE PRODUÇÃO" (8.5s), "RETRABALHO" (9.7s) — cada uma entra e é riscada por uma linha cobalto reta logo em seguida (evitados). Segura.

## Frame 3 — Causa, modo, efeito

- scene: Uma cadeia de três blocos ligados por setas: CAUSA → MODO DE FALHA → EFEITO, cada um com um exemplo curto
- voiceover: "Separe três coisas. O modo de falha é o que pode dar errado numa etapa. O efeito é a consequência para o produto, o usuário ou a segurança. E a causa é o mecanismo que origina a falha, como treinamento insuficiente ou montagem incorreta."
- duration: 13.696s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/03-modo-efeito-causa.html
- type: feature_showcase
- persuasion: Causal chain + rule of three
- beat: Comprehension + focus
- blueprint: compose
- focal: a cadeia de três blocos CAUSA → MODO DE FALHA → EFEITO
- roles: os três blocos = herói (tríptico horizontal, ~80% da largura) · setas retas = apoio · exemplos em mono = apoio · grade = fundo

narrativeRole: Distingue os três elementos que a prova costuma cobrar e evita soluções superficiais.
keyMessage: Modo = o que falha; efeito = consequência; causa = origem.

Compose: diagrama de processo que se monta na ordem em que a narração nomeia — modo, efeito, causa. Setas que se desenham → svg-path-draw; blocos entram com spring-pop-entrance suave (sem overshoot).
Scene 1 (0.0–1.4s): título headline "Separe três coisas" no topo esquerdo; três contornos vazios de retângulos aparecem tênues (ink-faint) em tríptico no centro, já posicionados.
Scene 2 (1.4–4.4s): em "modo de falha" (1.6s) o bloco do MEIO se preenche em cobalto invertido: "MODO DE FALHA" (table-name, creme) + descrição "o que pode dar errado numa etapa" (body); exemplo em mono abaixo: "vedação mal montada".
Scene 3 (4.4–8.1s): em "efeito" (4.6s) a seta reta do meio para a direita se desenha e o bloco DIREITO acende (contorno cobalto, fundo creme): "EFEITO" + "consequência para o produto, o usuário ou a segurança"; exemplo mono: "vazamento".
Scene 4 (8.1–10.7s): em "causa" (8.4s) a seta da esquerda para o meio se desenha e o bloco ESQUERDO acende: "CAUSA" + "mecanismo que origina a falha".
Scene 5 (10.7–13.7s): em "treinamento insuficiente" (11.0s) e "montagem incorreta" (12.6s) duas tags mono empilham sob o bloco CAUSA. A cadeia inteira lê CAUSA → MODO DE FALHA → EFEITO; segura parada.

## Frame 4 — Severidade, ocorrência, detecção

- scene: Três escalas de 1 a 10 lado a lado, rotuladas S, O e D, cada uma com sua pergunta
- voiceover: "Depois, três notas. Severidade: quão grave é o efeito. Ocorrência: com que frequência a causa acontece. Detecção: quão difícil é perceber a falha antes de ela chegar ao cliente. Atenção: quanto maior o D, pior a detecção."
- duration: 12.821s
- transition_in: crossfade
- status: outline
- src: compositions/frames/04-sod.html
- type: feature_showcase
- persuasion: Rule of three + counterexample (D maior = pior)
- beat: Comprehension + "aha"
- blueprint: grid-card-assemble (Adapt)
- focal: as três escalas verticais S, O, D de 1 a 10
- roles: três colunas de escala (pixel-stack, 10 células) = herói · letras S/O/D em vbig-numeral = herói · perguntas em body = apoio · alerta 'D maior = pior' em bloco invertido = apoio

narrativeRole: Apresenta as três notas e destaca a pegadinha da detecção.
keyMessage: S = gravidade, O = frequência, D = dificuldade de detectar.

Adapt: mantém a montagem escalonada de N cartões numa grade, mas cada cartão entra no tempo da sua palavra (não em cascata única). Escalas que enchem → stat-bars-and-fills; destaque final → css-marker-patterns.
Scene 1 (0.0–1.4s): título headline "Três notas" no topo esquerdo; rótulo mono "ESCALA 1–10".
Scene 2 (1.4–3.4s): em "Severidade" (1.4s) a coluna 1 monta: letra S grande, rótulo "SEVERIDADE", pergunta "Quão grave é o efeito?"; a escala de 10 células enche de baixo para cima até o topo e volta a ficar só contornada (demonstra 1→10).
Scene 3 (3.4–6.2s): em "Ocorrência" (3.4s) a coluna 2 monta: O, "OCORRÊNCIA", "Com que frequência a causa acontece?", mesma escala.
Scene 4 (6.2–10.3s): em "Detecção" (6.2s) a coluna 3 monta: D, "DETECÇÃO", "Quão difícil é perceber a falha antes do cliente?". Triptych, as três colunas ocupam ~75% da largura.
Scene 5 (10.3–12.82s): em "Atenção" (10.3s) a coluna D destaca: sua escala enche até 10 e um bloco cobalto invertido aparece sob ela: "D ALTO = DETECÇÃO PIOR" (micro-strong, creme), com um sublinhado traçado em "pior" (11.9s). S e O baixam para ink-soft. Segura.

## Frame 5 — NPR na prática

- scene: A fórmula NPR = S × O × D se monta e vira o exemplo da vedação de bomba: 8 × 7 × 6 = 336
- voiceover: "As três se multiplicam no NPR, o Número de Prioridade de Risco. Exemplo: uma vedação mal montada numa bomba centrífuga causa vazamento. Severidade oito, ocorrência sete, detecção seis: NPR igual a trezentos e trinta e seis."
- duration: 14.272s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/05-npr.html
- type: social_proof
- persuasion: Worked example with real numbers
- beat: "Aha" + mastery
- blueprint: dataviz-countup (Adapt)
- focal: o número 336
- roles: fórmula NPR = S × O × D = herói inicial · 8 × 7 × 6 e o 336 = herói final · card do exemplo (bomba centrífuga) = apoio · grade = fundo

narrativeRole: Mostra o cálculo do NPR com o exemplo exato do material.
keyMessage: NPR = S × O × D; 8 × 7 × 6 = 336.

Adapt: mantém a contagem até um número herói com empurrão de câmera que aterrissa nele; sem gráfico de tendência — a fórmula vira a conta. Contagem → counting-dynamic-scale; troca das letras pelos números no lugar → scale-swap-transition.
Scene 1 (0.0–2.0s): em "NPR" (1.3s) a fórmula "NPR = S × O × D" monta termo a termo no centro superior (display-chapter, cobalto).
Scene 2 (2.0–4.1s): em "Número de Prioridade de Risco" (2.2s) a legenda por extenso aparece em micro-strong sob "NPR".
Scene 3 (4.1–8.5s): em "Exemplo" (4.1s) um card retangular de contorno cobalto entra à esquerda (asymmetric 40/60): rótulo mono "EXEMPLO" e o texto "Vedação mal montada numa bomba centrífuga → vazamento" (vazamento entra em 7.6s); a fórmula desliza para a direita.
Scene 4 (8.5–11.8s): as letras viram números no lugar, cada uma no tempo da fala: S→8 (9.3s), O→7 (10.4s), D→6 (11.3s); cada número com rótulo pequeno embaixo.
Scene 5 (11.8–14.27s): em "igual a" (12.4s) a câmera empurra levemente para a direita da fórmula e "336" conta de 0 até 336 em vbig-numeral dentro de um bloco cobalto invertido, aterrissando em 12.9s; segura parado.

## Frame 6 — Agir e reavaliar

- scene: Ações preventivas (instrução visual, verificação específica) baixam as barras de O e D, enquanto S permanece igual; o NPR é recalculado; ícones da equipe (projeto, produção, qualidade, manutenção) em volta
- voiceover: "Com o risco priorizado, vêm as ações: instrução visual e uma verificação específica reduzem a ocorrência e melhoram a detecção. A severidade continua igual, se a consequência ainda for grave. Então a equipe recalcula o NPR."
- duration: 13.589s
- transition_in: crossfade
- status: outline
- src: compositions/frames/06-reavaliar.html
- type: benefit_highlight
- persuasion: Before/after + demonstration
- beat: Resolve + confidence
- blueprint: dataviz-countup (Adapt)
- focal: as barras S, O, D e o NPR recalculado
- roles: três barras horizontais S/O/D (pixel-stack) = herói · tags das ações = apoio · NPR antes/depois = apoio · rótulos da equipe em mono = apoio de borda

narrativeRole: Fecha a FMEA como ciclo: priorizar, agir, reavaliar.
keyMessage: Ações reduzem O e D; S só muda se a consequência mudar; o NPR é recalculado.

Adapt: mantém número e barras como herói, com a recontagem como payoff; sem câmera atravessando — as barras se movem. Barras que baixam → stat-bars-and-fills; recontagem → counting-dynamic-scale.
Scene 1 (0.0–2.4s): três barras horizontais de 10 células no centro esquerdo (60/40): S = 8, O = 7, D = 6, rótulos à esquerda; à direita "NPR 336" em headline.
Scene 2 (2.4–5.0s): em "instrução visual" (2.4s) e "verificação específica" (3.8s) duas tags retangulares de contorno entram acima das barras: "AÇÃO: INSTRUÇÃO VISUAL", "AÇÃO: VERIFICAÇÃO ESPECÍFICA".
Scene 3 (5.0–7.6s): em "reduzem a ocorrência" (5.6s) a barra O recua de 7 para 3 células; em "melhoram a detecção" (6.8s) a barra D recua de 6 para 2 — o número ao lado de cada barra conta para baixo junto.
Scene 4 (7.6–11.4s): em "severidade continua igual" (7.8s) a barra S fica parada e ganha uma marca mono "= 8 (CONSEQUÊNCIA AINDA GRAVE)".
Scene 5 (11.4–13.59s): em "equipe" (11.9s) quatro rótulos mono aparecem nas bordas superior e inferior úteis: PROJETO · PRODUÇÃO · QUALIDADE · MANUTENÇÃO; em "recalcula o NPR" (12.2s) o "336" à direita é riscado e abaixo dele aparece, em bloco cobalto invertido, "NOVO NPR = 8 × O↓ × D↓" (mono), com uma seta reta para baixo. Segura.

## Frame 7 — Por que prever

- scene: Uma linha do tempo com três decisões que levam tempo (comprar materiais, contratar pessoas, expandir instalações) e uma seta voltando no tempo: "inércia decisória"
- voiceover: "Agora, a Aula 5: previsão de demanda. Comprar materiais, contratar pessoas, expandir a fábrica: nada disso acontece na hora. Essa demora se chama inércia decisória — e é por isso que precisamos prever."
- duration: 11.883s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/07-por-que-prever.html
- type: pain_point
- persuasion: Causal chain + stakes
- beat: Tension → clarity
- blueprint: spatial-pan-stations (Adapt)
- focal: a linha do tempo com as três decisões e a seta de volta 'inércia decisória'
- roles: linha do tempo horizontal com três estações = herói · rótulos de prazo em mono = apoio · seta de volta + termo 'inércia decisória' = herói final · grade = fundo

narrativeRole: Justifica a previsão pela antecedência que as decisões exigem.
keyMessage: Decisões operacionais demoram; a previsão orienta estoque, capacidade e programação.

Adapt: mantém estações pré-posicionadas numa tela larga percorrida por uma câmera virtual, terminando parada na última; adiciona uma seta voltando no tempo. Câmera → viewport-change; seta → svg-path-draw.
Scene 1 (0.0–2.6s): rótulo micro-strong "AULA 5" e título display-chapter "Previsão de demanda" centralizados; em 1.9s o título sobe para o topo esquerdo e uma linha do tempo horizontal começa a se desenhar da esquerda.
Scene 2 (2.6–5.8s): a câmera faz panorâmica pela linha: estação 1 "COMPRAR MATERIAIS" (3.0s, tag "semanas"), estação 2 "CONTRATAR PESSOAS" (4.2s, tag "meses"), estação 3 "EXPANDIR A FÁBRICA" (5.3s, tag "anos") — cada estação é um bloco retangular de contorno sobre a linha.
Scene 3 (5.8–7.7s): em "nada disso acontece na hora" a câmera recua e mostra as três estações juntas; um marcador "HOJE" no início da linha.
Scene 4 (7.7–11.88s): em "inércia decisória" (8.8s) uma seta reta se desenha da estação 3 de volta ao marcador HOJE, e o termo "inércia decisória" entra em ed-callout itálico acima dela; em "prever" (11.3s) um bloco cobalto invertido "POR ISSO, PREVER" aparece sobre o marcador HOJE. Segura.

## Frame 8 — Meta não é previsão

- scene: Dois cartões opostos: META ("o que queremos vender") × PREVISÃO ("o que esperamos que aconteça, com base em evidências")
- voiceover: "Cuidado: meta não é previsão. Meta é o resultado que a empresa deseja. Previsão é o que se espera que aconteça, com base em evidências. Confundir as duas leva a decisões otimistas demais."
- duration: 10.923s
- transition_in: crossfade
- status: outline
- src: compositions/frames/08-meta-previsao.html
- type: feature_showcase
- persuasion: Common-belief vs reality + comparison of two options
- beat: Recognition + "aha"
- blueprint: comparison-split (Adapt)
- focal: os dois cartões META × PREVISÃO
- roles: cartão META = herói esquerdo · cartão PREVISÃO = herói direito (invertido em cobalto) · selo '≠' entre eles = apoio · aviso final = apoio

narrativeRole: Desfaz a confusão clássica entre meta e previsão.
keyMessage: Meta = desejo; previsão = estimativa fundamentada.

Adapt: mantém a entrada dividida com inclinações espelhadas e os selos nas bordas internas; selos são retângulos (sem pílula) e os cartões entram cada um no tempo da sua palavra. Cartões → split-tilt-cards; selos → spring-pop-entrance.
Scene 1 (0.0–1.8s): em "Cuidado" um rótulo micro-strong "CUIDADO" no topo; título headline "Meta não é previsão" centralizado no alto, com "≠" em destaque.
Scene 2 (1.8–4.2s): em "Meta" (1.8s) o cartão esquerdo entra da esquerda com inclinação espelhada: "META" (display-chapter) + "o que a empresa deseja" (body-lede); contorno cobalto, fundo creme.
Scene 3 (4.2–7.8s): em "Previsão" (4.2s) o cartão direito entra da direita: "PREVISÃO" + "o que se espera que aconteça, com base em evidências", fundo cobalto invertido; um selo quadrado "≠" salta na borda interna entre os dois.
Scene 4 (7.8–10.92s): em "Confundir" (7.8s) um bloco faixa abaixo dos cartões (acima de y=900): "CONFUNDIR AS DUAS → DECISÕES OTIMISTAS DEMAIS" em micro-strong. Segura parado.

## Frame 9 — Horizontes e métodos qualitativos

- scene: Três faixas de horizonte (curto, médio, longo) ligadas a decisões operacionais, táticas e estratégicas; depois três fontes qualitativas: Delphi, pesquisa de mercado, força de vendas
- voiceover: "A previsão pode ser de curto, médio ou longo prazo, conforme a decisão: operacional, tática ou estratégica. Sem dados suficientes, usam-se métodos qualitativos: o método Delphi com especialistas, a pesquisa de mercado e a força de vendas."
- duration: 14.699s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/09-horizontes.html
- type: feature_showcase
- persuasion: Frame-then-fill + numbered enumeration
- beat: Focus + comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: as três faixas de horizonte e, depois, os três métodos qualitativos
- roles: três faixas de horizonte (largura crescente) = herói da primeira metade · três cartões de método = herói da segunda metade · conectores = apoio

narrativeRole: Organiza horizontes e fontes qualitativas da previsão.
keyMessage: Horizonte segue o tipo de decisão; sem dados, opiniões estruturadas complementam.

Adapt: mantém a montagem escalonada em grade, em duas fileiras disparadas pela fala (horizontes, depois métodos). Entrada palavra a palavra → dynamic-content-sequencing; conectores → svg-path-draw.
Scene 1 (0.0–3.0s): três faixas horizontais empilhadas na metade superior, com larguras crescentes como uma régua de tempo: "CURTO" (1.2s), "MÉDIO" (1.7s), "LONGO PRAZO" (2.2s).
Scene 2 (3.0–6.8s): em "operacional" (4.3s), "tática" (5.1s), "estratégica" (5.8s) cada faixa ganha à direita, ligada por um traço reto, o tipo de decisão em table-name.
Scene 3 (6.8–10.2s): em "Sem dados suficientes" (6.8s) as faixas sobem e encolhem para o topo; rótulo micro-strong "SEM DADOS SUFICIENTES → MÉTODOS QUALITATIVOS" aparece (9.2s).
Scene 4 (10.2–14.7s): três cartões retangulares em tríptico na metade inferior útil: "MÉTODO DELPHI · especialistas" (10.6s), "PESQUISA DE MERCADO" (12.5s), "FORÇA DE VENDAS" (13.7s), cada um com número mono 01/02/03. Segura.

## Frame 10 — Séries temporais

- scene: Um gráfico de linha que se decompõe em quatro camadas: nível, tendência, sazonalidade e variação aleatória
- voiceover: "Com dados, entram as séries temporais. Uma série pode ter nível, tendência, sazonalidade e variações aleatórias."
- duration: 7.061s
- transition_in: crossfade
- status: outline
- src: compositions/frames/10-series.html
- type: feature_showcase
- persuasion: Progressive disclosure + demonstration
- beat: Fascination + comprehension
- blueprint: dataviz-countup (Adapt)
- focal: o gráfico de linha decomposto em quatro camadas
- roles: gráfico de linha principal = herói · quatro mini-faixas (nível, tendência, sazonalidade, aleatória) = herói secundário · eixos mono = apoio

narrativeRole: Mostra os padrões que um método de previsão precisa considerar.
keyMessage: Nível, tendência, sazonalidade e aleatoriedade.

Adapt: mantém o gráfico como herói; troca a contagem por uma decomposição em camadas — sem empurrão de câmera (quadro curto e leve). Linhas que se desenham → svg-path-draw.
Scene 1 (0.0–2.4s): em "séries temporais" (1.2s) uma linha de série se desenha da esquerda para a direita na metade superior (60% da largura), com eixos finos e rótulo mono "DEMANDA × TEMPO".
Scene 2 (2.4–5.6s): a série se separa em camadas empilhadas abaixo, cada uma com rótulo micro-strong à esquerda, no tempo da fala: "NÍVEL" linha reta (3.4s), "TENDÊNCIA" linha inclinada (4.0s), "SAZONALIDADE" ondas em degraus retos (4.7s).
Scene 3 (5.6–7.06s): "VARIAÇÃO ALEATÓRIA" ruído em degraus (6.2s). As quatro camadas e a série seguram juntas.

## Frame 11 — Média móvel

- scene: Três barras de vendas (900, 1.000, 1.100) se somam e se dividem por três, gerando a barra prevista de 1.000; ao lado, a versão ponderada com pesos maiores para os meses recentes
- voiceover: "A média móvel simples tira a média dos períodos recentes. Vendas de novecentos, mil e mil e cem: somando e dividindo por três, a previsão do próximo mês é mil unidades. Na média ponderada, os meses mais recentes ganham peso maior."
- duration: 13.76s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/11-media-movel.html
- type: social_proof
- persuasion: Worked example with real numbers + build-up
- beat: "Aha" + mastery
- blueprint: dataviz-countup (Adapt)
- focal: a barra prevista de 1.000
- roles: três barras de vendas (900, 1.000, 1.100) = herói · barra prevista 1.000 = herói final (cobalto invertido) · conta (900 + 1.000 + 1.100) ÷ 3 em mono = apoio · painel da ponderada = apoio

narrativeRole: Calcula a média móvel com o exemplo exato do material.
keyMessage: (900 + 1.000 + 1.100) ÷ 3 = 1.000.

Adapt: mantém barras + contagem aterrissando em um número herói; o empurrão vira o colapso das três barras na prevista. Barras → stat-bars-and-fills; contagem → counting-dynamic-scale.
Scene 1 (0.0–3.4s): título headline "Média móvel simples" no topo esquerdo; eixo de base com rótulos mono M1, M2, M3, M4 (previsto).
Scene 2 (3.4–5.9s): barras de células crescem no tempo de cada valor: M1 = 900 (4.1s), M2 = 1.000 (4.7s), M3 = 1.100 (5.1s), com o número no topo de cada barra.
Scene 3 (5.9–8.8s): em "somando" (5.9s) a conta "(900 + 1.000 + 1.100) ÷ 3" se escreve em mono acima das barras, termo a termo; em "por três" (7.0s) o "÷ 3" destaca.
Scene 4 (8.8–10.0s): em "1.000 unidades" (8.8s) a barra M4 cresce em cobalto sólido e o número conta até 1.000 em headline sobre ela.
Scene 5 (10.0–13.76s): em "média ponderada" (10.6s) um painel menor à direita (70/30): "PONDERADA" com pesos mono 0,2 · 0,3 · 0,5 sob M1, M2, M3 — em "mais recentes ganham peso maior" (12.1s) o peso 0,5 fica em bloco invertido. Segura.

## Frame 12 — O erro também importa

- scene: A barra real de 1.080 aparece ao lado da prevista de 1.000; a diferença +80 se destaca; depois três indicadores de erro: erro médio absoluto, erro quadrático médio, sinal de rastreamento
- voiceover: "Mas a demanda real foi de mil e oitenta. Erro: real menos previsto, mais oitenta. O erro médio absoluto mostra o tamanho dos desvios, o erro quadrático pesa mais os grandes, e o sinal de rastreamento revela viés. Uma boa previsão vem sempre com seu erro esperado."
- duration: 15.509s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/12-erro.html
- type: benefit_highlight
- persuasion: Worked example + enumeration
- beat: Unease → conviction
- blueprint: dataviz-countup (Adapt)
- focal: o erro +80
- roles: barra real 1.080 ao lado da prevista 1.000 = herói · faixa da diferença +80 = herói · três indicadores de erro = apoio · frase final = apoio

narrativeRole: Fecha a previsão mostrando que medir o erro é parte do método.
keyMessage: Erro = real − previsto = +80; previsão completa inclui o erro esperado.

Adapt: mantém número herói + barras; o destaque cai no vão entre previsto e real. Barras → stat-bars-and-fills; destaque → css-marker-patterns.
Scene 1 (0.0–2.3s): barra PREVISTO 1.000 (contorno) já à esquerda; em "1.080" (1.1s) a barra REAL cresce ao lado em cobalto sólido até 1.080, um pouco mais alta.
Scene 2 (2.3–5.0s): em "Erro" (2.3s) a fórmula mono "ERRO = REAL − PREVISTO" aparece à direita; em "+80" (4.3s) o vão entre o topo das duas barras é marcado por um retângulo invertido com "+80" em display-chapter.
Scene 3 (5.0–12.7s): as barras recuam para a esquerda (40/60) e três linhas de indicador entram à direita no tempo da fala, cada uma com número mono 01/02/03 e descrição curta: "ERRO MÉDIO ABSOLUTO — tamanho dos desvios" (5.2s), "ERRO QUADRÁTICO MÉDIO — pesa mais os grandes" (8.0s), "SINAL DE RASTREAMENTO — revela viés" (10.4s).
Scene 4 (12.7–15.51s): em "Uma boa previsão" (12.7s) uma faixa no topo: "PREVISÃO BOA = VALOR + ERRO ESPERADO", com "ERRO ESPERADO" sublinhado em 14.6s. Segura.

## Frame 13 — Síntese

- scene: Duas colunas convergem: FMEA (priorizar riscos com S × O × D) e PREVISÃO (estimar a demanda e o erro); embaixo, a palavra ANTES volta
- voiceover: "Resumindo: a FMEA prioriza riscos com severidade, ocorrência e detecção. A previsão estima a demanda e o seu erro. As duas fazem a mesma coisa: agir antes do problema."
- duration: 9.984s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/13-sintese.html
- type: branding
- persuasion: Distillation + callback
- beat: Satisfaction + "now I get it"
- blueprint: titlecard-reveal (Adapt)
- focal: a palavra ANTES (retorno do gancho)
- roles: duas colunas FMEA e PREVISÃO = apoio que converge · ANTES em bloco cobalto invertido = herói final · grade = fundo

narrativeRole: Responde ao gancho e une as duas aulas numa ideia.
keyMessage: Prevenir e prever: agir antes do problema.

Adapt: mantém o cartão-título calmo com um único movimento contido e a parada final; precedido pela convergência das duas colunas. Entrada das linhas → dynamic-content-sequencing.
Scene 1 (0.0–4.2s): split 50/50 com filete vertical no meio; em "FMEA" (0.6s) a coluna esquerda: "FMEA" (display-chapter) + "prioriza riscos" + mono "S × O × D" (2.0s–3.4s).
Scene 2 (4.2–6.7s): em "previsão" (4.3s) a coluna direita: "PREVISÃO" + "estima a demanda" + mono "e o seu erro" (6.2s).
Scene 3 (6.7–8.6s): em "As duas" (6.7s) as colunas deslizam uma em direção à outra e o filete central some.
Scene 4 (8.6–9.98s): em "agir antes" (8.6s) a palavra ANTES volta em display-hero dentro de um bloco cobalto invertido no centro (eco do quadro 1), com "do problema" em ed-callout abaixo — um único movimento de subida com fade; parada total até o fim.
