---
format: 1920x1080
duration: 210s
message: "FMEA é descobrir o que pode falhar antes de falhar: causa → modo → efeito, notar severidade, ocorrência e detecção, multiplicar no NPR, agir e reavaliar"
arc: concept-explainer with mnemonics + worked example + exam answer
audience: estudante que precisa entender e memorizar FMEA para a prova (Administração e Integração de Operações e Qualidade, Aula 4)
language: pt-BR
mode: autonomous
music: none
music_brief: calm focused minimal study underscore, soft piano and light pulse (host-generated, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** cada quadro leva a moldura Cobalt Grid — grade de papel milimetrado permanente, filetes cobalto no topo e na base (base em y ≤ 896), tag de chrome em DM Mono no canto superior esquerdo "FMEA · MACETES" e numeração "NN / 16" no canto superior direito.
- **paleta:** só duas cores do `frame.md` — papel creme e tinta cobalto. "Falha", "perda", "fora de controle" nunca ganham vermelho: usam bloco cobalto invertido (texto creme sobre cobalto) ou um risco cobalto. Nada de gradientes coloridos, sombras ou brilhos.
- **tipo:** Newsreader 400 para títulos, termos e números grandes; Hanken Grotesk 600 caixa-alta espaçada para rótulos; DM Mono para tags, eixos, fórmulas e chrome. Texto que carrega significado nunca abaixo de ~27 px. Todo texto visível em português do Brasil, exatamente como nas linhas Scene.
- **forma:** só retângulos e linhas retas — sem cantos arredondados, sem círculos, sem pílulas; pontos de gráfico são quadrados pequenos. Setas são linhas retas com ponta triangular. Dados viram barras de células da grade quando couber.
- **zona útil:** todo conteúdo acima de y = 900 px (faixa das legendas); herói centrado em y ≈ 454.
- **movimento:** curvas de cauda longa (power3 por padrão; overshoot só onde a cena pede). Anime só transformações e opacidade (x, y, scale, opacity, clip-path, stroke) — nunca left/top/width/height. Cada peça entra quando a narração a nomeia; depois de resolvido, o quadro segura a leitura parado.
- **ritmo e riqueza de animação:** este vídeo é para memorizar — "use e abuse de animações e exemplos". Cada item falado ganha sua PRÓPRIA entrada animada (pop, desenho de linha, contagem, deslize, carimbo), e cada exemplo vira uma mini-cena desenhada com retângulos e linhas (caixas, esteira, gangorra, medidores, máquina). Movimento contínuo e com propósito: objetos do exemplo se mexem (esteira corre, peças caem, ponteiros giram, barras sobem) enquanto a narração fala deles; a parada de leitura só acontece nos últimos ~0,8 s. Macetes (palavras-gancho) entram com destaque forte: bloco cobalto invertido + leve overshoot ou carimbo. Os quadros 10 (336) e 13 (336 → 48) são os clímax numéricos; o 15 (resposta de prova) e o 16 (cola) consolidam.
- **lista negativa:** vermelho/verde/amarelo, sombras difusas, bokeh, gradiente roxo-azul de "IA", emoji, cantos arredondados, círculos, conteúdo abaixo de y = 900, fontes via @import ou CDN; os dois modos de falha — slide (tudo de uma vez e congela) e protetor de tela (tudo flutuando sem parar).

## Frame 1 — Antes de falhar

- scene: Uma engrenagem quadrada gira; uma rachadura começa a se desenhar nela e o tempo congela; a palavra ANTES surge; a sigla FMEA cai no centro
- voiceover: "E se você pudesse descobrir onde o seu processo vai falhar, antes de ele falhar? É exatamente isso que a FMEA faz."
- duration: 6.891s
- transition_in: cut
- status: animated
- src: compositions/frames/01-antes.html
- type: hook
- persuasion: Imagine / scenario
- beat: Curiosity
- blueprint: kinetic-type-beats (Adapt)
- focal: a sigla FMEA que cai sobre a engrenagem congelada
- roles: engrenagem quadrada girando com rachadura = herói inicial · palavra ANTES = apoio · sigla FMEA = herói final

narrativeRole: Abre com a promessa central da ferramenta.
keyMessage: FMEA = descobrir falhas antes que aconteçam.

Adapt: abertura em batidas com um objeto vivo; o payoff é a sigla. Rachadura → svg-path-draw; sigla → kinetic-beat-slam.
Scene 1 (0.0–2.6s): uma engrenagem feita de quadrados (dentes retangulares) gira no centro; em "processo" (2.0s) uma esteira com caixas passa por baixo.
Scene 2 (2.6–4.4s): em "falhar" (2.6s) uma rachadura em zigue-zague começa a se desenhar na engrenagem; em "antes de ele falhar" (3.1s) TUDO congela (a engrenagem para, a rachadura para pela metade) e um bloco invertido ANTES aparece com um relógio quadrado pausado.
Scene 3 (4.4–6.891s): em "exatamente isso" (4.6s) a rachadura se apaga para trás (desfeita); em "FMEA" (5.6s) a sigla FMEA cai do alto em display-hero e bate no centro (leve tremor), com rótulo mono "ANÁLISE PREVENTIVA" embaixo. Segura.

## Frame 2 — O nome

- scene: As letras F · M · E · A caem; cada uma desdobra sua palavra em inglês e em português: Failure = Falha, Mode = Modo, Effects = Efeitos, Analysis = Análise; a frase completa se monta: Análise dos Modos de Falha e seus Efeitos
- voiceover: "FMEA vem do inglês e significa Análise dos Modos de Falha e seus Efeitos. Macete: as quatro letras já contam a história: falha, modo, efeito, análise."
- duration: 9.536s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-nome.html
- type: product_intro
- persuasion: Acronym decoding
- beat: Clarity
- blueprint: kinetic-type-beats (Adapt)
- focal: as quatro letras F · M · E · A desdobrando suas palavras
- roles: quatro blocos-letra = herói · palavras em inglês (riscadas leves) e português = apoio · nome completo = herói final

narrativeRole: Decodifica a sigla para nunca mais esquecer.
keyMessage: Análise dos Modos de Falha e seus Efeitos.

Adapt: acrônimo decodificado letra a letra, com troca no lugar inglês → português. Troca → discrete-text-sequence; entradas → spring-pop-entrance.
Scene 1 (0.0–2.2s): quatro quadrados com F, M, E, A caem em fileira (0.0s–0.4s); sob cada letra, em mono pequeno, a palavra em inglês aparece: FAILURE, MODE, EFFECTS, ANALYSIS (1.2s), com rótulo "DO INGLÊS" (1.2s).
Scene 2 (2.2–4.6s): em "Análise dos Modos de Falha e seus Efeitos" (2.2s) a frase completa monta-se em headline abaixo, palavra a palavra no tempo da fala (Análise 2.2s, Modos 2.7s, Falha 3.2s, Efeitos 3.9s); linhas retas finas ligam cada letra à sua palavra na frase.
Scene 3 (4.6–9.536s): em "Macete" (4.6s) faixa invertida "AS LETRAS CONTAM A HISTÓRIA"; as palavras em inglês trocam no lugar para o português no tempo da fala: FALHA (7.6s), MODO (8.2s), EFEITO (8.6s), ANÁLISE (9.0s), cada bloco acendendo em cobalto invertido. Segura.

## Frame 3 — O que ela evita

- scene: Três cenas de problema surgem e são riscadas por um traço cobalto: um cliente insatisfeito, uma linha de produção parada, uma peça voltando para o retrabalho
- voiceover: "Para que serve? Para identificar problemas potenciais antes que causem três estragos: dano ao cliente, parada de produção ou retrabalho."
- duration: 8.171s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-evita.html
- type: benefit_highlight
- persuasion: Rule of three (losses avoided)
- beat: Stakes
- blueprint: grid-card-assemble (Adapt)
- focal: três mini-cenas de estrago sendo riscadas
- roles: três painéis com mini-cenas (cliente bravo, linha parada, peça voltando) = herói · traço que risca = herói · título = apoio

narrativeRole: Dá a finalidade com as palavras do material.
keyMessage: Evita dano ao cliente, parada de produção e retrabalho.

Adapt: três cartões que entram e são riscados no tempo da fala. Cenas → spring-pop-entrance; riscos → svg-path-draw.
Scene 1 (0.0–4.3s): título headline "Para que serve?" (0.0s); em "identificar problemas potenciais" (1.2s) uma lupa QUADRADA varre a tela da esquerda para a direita; rótulo "3 ESTRAGOS EVITADOS" aparece em 4.0s.
Scene 2 (4.3–6.2s): em "dano ao cliente" (5.2s) painel 1: um rosto feito de quadrados com boca para baixo e um produto quebrado (duas metades separadas); um X cobalto grande risca o painel em 5.7s e o rosto vira sorriso reto.
Scene 3 (6.2–8.171s): em "parada de produção" (6.2s) painel 2: uma esteira que para com um sinal de pausa (dois retângulos) — risco em 6.7s e a esteira volta a andar; em "retrabalho" (7.4s) painel 3: uma peça fazendo uma seta de volta (U reto) — risco em 7.8s. Segura.

## Frame 4 — A analogia da viagem

- scene: Um carro (blocos retos) antes da viagem; uma prancheta de checagem: pneu, freio, óleo; cada item é verificado; "isso é FMEA: pensar no que pode falhar antes de sair"
- voiceover: "Pense numa viagem de carro. Antes de sair, você confere o pneu, o freio e o óleo, porque sabe o que pode dar errado na estrada. A FMEA faz isso com um processo: pensa nas falhas antes de elas acontecerem."
- duration: 12.352s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-viagem.html
- type: feature_showcase
- persuasion: Everyday analogy
- beat: "Aha"
- blueprint: compose
- focal: o carro e a prancheta de checagem
- roles: carro de blocos retos sobre a estrada = herói · prancheta com três itens = herói · ponte 'isso é FMEA' = payoff

narrativeRole: Ancora o conceito numa cena do dia a dia.
keyMessage: FMEA = checklist do que pode falhar, antes de acontecer.

Compose: analogia animada, cada item checado no tempo da fala. Checks → spring-pop-entrance; estrada → svg-path-draw.
Scene 1 (0.0–2.9s): uma estrada (duas linhas retas em perspectiva simples) se desenha; um carro feito de retângulos (rodas quadradas pretas) entra e para numa marca "LARGADA"; rótulo mono "ANTES DE SAIR".
Scene 2 (2.9–5.0s): uma prancheta desliza à direita; itens marcados no tempo: PNEU (3.4s, o pneu do carro pisca e uma lupa quadrada vai até ele), FREIO (3.8s), ÓLEO (4.4s, uma gota quadrada sobe numa vareta) — cada item ganha ✓.
Scene 3 (5.0–7.4s): em "o que pode dar errado na estrada" (5.5s) à frente na estrada aparecem placas de aviso quadradas: "BURACO", "CHUVA"; o carro não sai ainda.
Scene 4 (7.4–12.352s): em "A FMEA faz isso com um processo" (7.6s) o carro se transforma (troca de cena por escala) numa linha de produção de blocos e a prancheta vira uma tabela "FALHAS POSSÍVEIS"; em "antes de elas acontecerem" (10.9s) faixa invertida: "PENSAR NAS FALHAS ANTES". Segura.

## Frame 5 — Causa, modo, efeito

- scene: Uma corrente de três elos quadrados se monta: CAUSA → MODO DE FALHA → EFEITO; sobre cada elo, a pergunta-macete: "POR QUÊ?" · "O QUÊ?" · "E DAÍ?"
- voiceover: "O coração da FMEA são três elementos em corrente. A causa responde por quê. O modo de falha responde o quê pode dar errado. E o efeito responde: e daí, qual a consequência?"
- duration: 10.56s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-corrente.html
- type: feature_showcase
- persuasion: Causal chain + question mnemonic
- beat: Comprehension
- blueprint: compose
- focal: a corrente de três elos com as perguntas POR QUÊ? · O QUÊ? · E DAÍ?
- roles: três elos quadrados encadeados = herói · perguntas-macete em blocos invertidos = herói · título = apoio

narrativeRole: Ensina os três elementos com perguntas fáceis.
keyMessage: Causa = por quê; modo = o quê; efeito = e daí.

Compose: corrente que se monta elo a elo no tempo da fala. Elos → spring-pop-entrance; ligações → svg-path-draw.
Scene 1 (0.0–3.4s): título headline "O coração da FMEA" (0.0s); em "três elementos em corrente" (2.0s) três elos quadrados vazios surgem em fileira, ligados por traços que se desenham, e a corrente dá um leve puxão (os elos se aproximam).
Scene 2 (3.4–5.0s): em "causa" (3.5s) o elo 1 se preenche: "CAUSA"; acima, a pergunta "POR QUÊ?" em bloco invertido salta (4.5s).
Scene 3 (5.0–7.6s): em "modo de falha" (5.1s) o elo 2: "MODO DE FALHA"; pergunta "O QUÊ?" (6.4s).
Scene 4 (7.6–10.56s): em "efeito" (7.8s) o elo 3: "EFEITO"; pergunta "E DAÍ?" (8.9s); setas retas mostram a direção CAUSA → MODO → EFEITO, e um pulso percorre a corrente da esquerda para a direita. Segura.

## Frame 6 — O exemplo da bomba

- scene: Uma bomba centrífuga (formas retas) monta-se; a corrente aplicada: TREINAMENTO INSUFICIENTE → VEDAÇÃO MAL MONTADA → VAZAMENTO; gotas quadradas pingam da bomba
- voiceover: "Veja na bomba centrífuga. Causa: treinamento insuficiente. Modo de falha: a vedação foi mal montada. Efeito: vazamento. Dica de prova: a causa vem antes, o efeito vem depois, e o modo de falha fica no meio."
- duration: 12.48s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-bomba.html
- type: feature_showcase
- persuasion: Worked example + exam tip
- beat: "Aha"
- blueprint: compose
- focal: a bomba centrífuga pingando e a corrente aplicada
- roles: bomba centrífuga de formas retas = herói · corrente com os três exemplos = herói · dica de posição = apoio

narrativeRole: Aplica a corrente ao exemplo do material e dá a regra de posição.
keyMessage: Treinamento insuficiente → vedação mal montada → vazamento.

Compose: o diagrama da corrente vira um caso real animado. Gotas → spring-pop-entrance; setas → svg-path-draw.
Scene 1 (0.0–1.8s): uma bomba centrífuga monta-se à esquerda (corpo retangular, rotor quadrado girando, cano de entrada e saída), com rótulo mono "BOMBA CENTRÍFUGA" (0.8s).
Scene 2 (1.8–6.2s): à direita, a corrente de três elos do quadro anterior volta; em "treinamento insuficiente" (2.2s) o elo CAUSA recebe "TREINAMENTO INSUFICIENTE" e um bonequinho quadrado com um manual fechado; em "vedação foi mal montada" (4.6s) o elo MODO recebe "VEDAÇÃO MAL MONTADA" e na bomba a vedação (um retângulo fino) fica torta.
Scene 3 (6.2–7.6s): em "vazamento" (6.7s) o elo EFEITO recebe "VAZAMENTO" e gotas quadradas começam a pingar da bomba numa poça retangular que cresce.
Scene 4 (7.6–12.48s): em "Dica de prova" (7.6s) faixa invertida "DICA DE PROVA"; uma linha do tempo sob a corrente: "ANTES" sob CAUSA (9.3s), "DEPOIS" sob EFEITO (10.4s), "NO MEIO" sob MODO (12.0s) — o elo do meio pulsa. As gotas continuam pingando devagar.

## Frame 7 — As três notas

- scene: Três réguas de 1 a 10 entram lado a lado: SEVERIDADE, OCORRÊNCIA, DETECÇÃO; acima de cada uma, o macete: "É SÉRIO?" · "OCORRE MUITO?" · "DÁ PRA PERCEBER?"
- voiceover: "Depois, cada falha ganha três notas, de um a dez. Severidade: o efeito é sério? Ocorrência: a causa ocorre muito? Detecção: dá para perceber a falha antes que ela chegue ao cliente?"
- duration: 10.432s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-notas.html
- type: feature_showcase
- persuasion: Rule of three + question mnemonic
- beat: Comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: as três réguas de 1 a 10 com perguntas-gancho
- roles: três réguas verticais de 10 células = herói · nomes S/O/D = herói · perguntas-macete = herói

narrativeRole: Apresenta as três notas com perguntas-gancho.
keyMessage: Severidade = gravidade; ocorrência = frequência; detecção = percepção.

Adapt: três colunas que se montam no tempo da fala; cada régua enche como termômetro. Réguas → stat-bars-and-fills; perguntas → spring-pop-entrance.
Scene 1 (0.0–3.0s): título headline "Três notas" (0.0s); em "de 1 a 10" (2.0s) três réguas verticais vazias de 10 células entram, com marcas mono "1" embaixo e "10" em cima.
Scene 2 (3.0–4.9s): em "Severidade" (3.0s) a coluna 1 ganha a letra S (display) e "SEVERIDADE"; a pergunta "É SÉRIO?" salta em bloco invertido (4.4s); a régua enche de baixo para cima e volta.
Scene 3 (4.9–6.9s): em "Ocorrência" (4.9s) coluna 2: O, "OCORRÊNCIA", "OCORRE MUITO?" (6.2s); régua enche e volta.
Scene 4 (6.9–10.432s): em "Detecção" (6.9s) coluna 3: D, "DETECÇÃO", "DÁ PRA PERCEBER?" (8.1s); régua enche e volta. As três perguntas ficam visíveis lado a lado. Segura.

## Frame 8 — A pegadinha da detecção

- scene: A régua da detecção vira um jogo de esconde-esconde: nota 1 = uma falha com um alarme tocando (fácil de pegar); nota 10 = a falha escondida atrás de um muro (ninguém vê até o cliente); "D ALTO = PIOR"
- voiceover: "Agora a pegadinha mais cobrada. Na detecção, nota alta é ruim. Nota um: a falha é pega na hora. Nota dez: a falha se esconde e só o cliente descobre. Macete: detecção alta, falha escondida."
- duration: 11.349s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/08-pegadinha.html
- type: pain_point
- persuasion: Counterintuitive warning + game metaphor
- beat: Tension → "aha"
- blueprint: compose
- focal: o esconde-esconde: falha com alarme × falha atrás do muro
- roles: régua da detecção horizontal = herói · mini-cena nota 1 (alarme) e nota 10 (muro) = herói · selo D ALTO = PIOR = payoff

narrativeRole: Neutraliza o erro mais comum de prova.
keyMessage: D alto = difícil de detectar = pior.

Compose: jogo de esconde-esconde que explica a escala invertida. Alarme e muro → spring-pop-entrance; selo → kinetic-beat-slam.
Scene 1 (0.0–3.9s): faixa invertida "PEGADINHA" (0.4s) com um sinal de atenção quadrado; em "nota alta é ruim" (2.6s) uma régua horizontal de 1 a 10 se desenha no meio, com o 10 em bloco invertido.
Scene 2 (3.9–5.8s): em "Nota 1" (3.9s) à esquerda, acima do 1: uma falha (quadrado com X) ao lado de um alarme (retângulo com ondas em linhas retas) que pisca; rótulo "PEGA NA HORA".
Scene 3 (5.8–8.7s): em "Nota 10" (5.8s) à direita, acima do 10: um muro de tijolos (retângulos) sobe e a falha se esconde atrás dele (só a ponta aparece); uma seta leva até um bonequinho quadrado CLIENTE que levanta um "!"; rótulo "SÓ O CLIENTE DESCOBRE" (7.7s).
Scene 4 (8.7–11.349s): em "detecção alta, falha escondida" (9.5s) um carimbo grande "D ALTO = FALHA ESCONDIDA = PIOR" bate no centro com tremor. Segura.

## Frame 9 — O NPR

- scene: A fórmula NPR = S × O × D monta-se peça por peça; abaixo, o nome por extenso; uma faixa: "MULTIPLICA, NÃO SOMA" e a escala de 1 a 1000
- voiceover: "As três notas se multiplicam no NPR, o Número de Prioridade de Risco. Macete: multiplica, não soma. Por isso o NPR vai de um a mil."
- duration: 8.427s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-npr.html
- type: product_intro
- persuasion: Formula + range
- beat: Clarity
- blueprint: kinetic-type-beats (Adapt)
- focal: a fórmula NPR = S × O × D e a escala 1 → 1.000
- roles: fórmula montada peça por peça = herói · nome por extenso = apoio · faixa MULTIPLICA, NÃO SOMA = herói · escala 1–1000 = apoio

narrativeRole: Ensina a fórmula e evita o erro de somar.
keyMessage: NPR = S × O × D (1 a 1000).

Adapt: fórmula construída em batidas com um token trocado (+ → ×). Troca → discrete-text-sequence; entradas → spring-pop-entrance.
Scene 1 (0.0–2.3s): S, O e D (display-chapter) entram vindo das réguas do quadro anterior (deslizam de baixo); em "NPR" (1.7s) "NPR =" encaixa à esquerda.
Scene 2 (2.3–4.4s): em "Número de Prioridade de Risco" (2.5s) o nome por extenso escreve-se em micro-strong sob NPR.
Scene 3 (4.4–6.6s): em "Macete" (4.4s) entre as letras aparecem sinais "+", que são riscados e TROCADOS por "×" no tempo de "multiplica, não soma" (5.1s–5.9s); faixa invertida "MULTIPLICA, NÃO SOMA".
Scene 4 (6.6–8.427s): em "vai de 1 a 1.000" (7.5s) uma escala horizontal se desenha sob a fórmula com "1" à esquerda e "1.000" à direita (= 10 × 10 × 10 em mono pequeno). Segura.

## Frame 10 — 336

- scene: As letras viram números um a um: S = 8, O = 7, D = 6; a multiplicação acontece em duas etapas (8 × 7 = 56; 56 × 6 = 336) e o 336 conta até o fim num bloco cobalto
- voiceover: "No exemplo da bomba: severidade oito, ocorrência sete e detecção seis. Oito vezes sete, cinquenta e seis. Vezes seis: o NPR é trezentos e trinta e seis."
- duration: 9.6s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/10-336.html
- type: social_proof
- persuasion: Worked numeric example
- beat: Mastery
- blueprint: dataviz-countup (Adapt)
- focal: o número 336
- roles: fórmula com letras virando números = herói · conta em duas etapas = apoio · 336 em bloco invertido = herói final

narrativeRole: Calcula o NPR do exemplo do material passo a passo.
keyMessage: 8 × 7 × 6 = 336.

Adapt: contagem até um número herói com a conta feita em etapas visíveis. Contagem → counting-dynamic-scale; troca → scale-swap-transition.
Scene 1 (0.0–4.4s): a fórmula "NPR = S × O × D" no centro superior; uma miniatura da bomba pingando no canto (callback); as letras viram números no tempo da fala: S→8 (1.9s), O→7 (3.0s), D→6 (3.9s), cada troca com um flip.
Scene 2 (4.4–6.5s): em "8 × 7" (4.4s) os dois primeiros números se juntam numa caixa mono "8 × 7 = 56" e o 56 conta (5.4s).
Scene 3 (6.5–9.6s): em "× 6" (6.5s) o 56 e o 6 se juntam; em "336" (8.2s) o resultado conta até 336 em vbig-numeral dentro de um bloco cobalto invertido, com um leve empurrão de câmera até ele. Segura.

## Frame 11 — Ranking de riscos

- scene: Uma tabela com três falhas e seus NPRs se reordena sozinha do maior para o menor (pódio): VAZAMENTO 336 no topo; selo "ATACAR PRIMEIRO"
- voiceover: "Para que serve o número? Para priorizar. A equipe calcula o NPR de cada falha, coloca em ordem, e ataca primeiro as que têm o NPR mais alto."
- duration: 8.448s
- transition_in: crossfade
- status: animated
- src: compositions/frames/11-ranking.html
- type: feature_showcase
- persuasion: Sorting animation
- beat: Clarity
- blueprint: grid-card-assemble (Adapt)
- focal: a tabela que se reordena com VAZAMENTO 336 no topo
- roles: tabela de três linhas (falha + NPR) = herói · reordenação animada = herói · selo ATACAR PRIMEIRO = payoff

narrativeRole: Mostra que o NPR é uma ferramenta de prioridade.
keyMessage: Maior NPR = atacar primeiro.

Adapt: linhas que entram e depois trocam de posição como um ranking. Linhas → dynamic-content-sequencing; selo → spring-pop-entrance.
Scene 1 (0.0–2.2s): título headline "Para priorizar" (1.4s); cabeçalho de tabela "FALHA · NPR" com rótulo mono "EXEMPLO".
Scene 2 (2.2–5.2s): em "calcula o NPR de cada falha" (2.7s) três linhas entram fora de ordem: "RUÍDO NA BOMBA · 120" (2.9s), "VAZAMENTO · 336" (3.4s), "RISCO NA PINTURA · 45" (3.9s); cada NPR conta rapidamente; barras horizontais proporcionais crescem ao lado.
Scene 3 (5.2–8.448s): em "coloca em ordem" (5.2s) as linhas deslizam e trocam de posição até ficarem 336 → 120 → 45 (pódio 1º, 2º, 3º); em "ataca primeiro" (5.8s) a linha VAZAMENTO vira bloco invertido e um selo "ATACAR PRIMEIRO" salta ao lado. Segura.

## Frame 12 — Agir

- scene: As barras S = 8, O = 7, D = 6; duas ações entram como ferramentas: INSTRUÇÃO VISUAL (derruba a barra O) e VERIFICAÇÃO ESPECÍFICA (derruba a barra D); a barra S fica parada com um cadeado quadrado: "S É TEIMOSO"
- voiceover: "Com a prioridade definida, vêm as ações. Uma instrução visual reduz a ocorrência. Uma verificação específica melhora a detecção. E a severidade? É teimosa: só muda se a consequência mudar."
- duration: 11.328s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/12-agir.html
- type: benefit_highlight
- persuasion: Before/after + personification
- beat: "Aha"
- blueprint: dataviz-countup (Adapt)
- focal: as barras O e D derrubadas e a barra S com cadeado
- roles: três barras horizontais S=8, O=7, D=6 = herói · duas ferramentas-ação = herói · cadeado S É TEIMOSO = payoff

narrativeRole: Ensina qual nota cada ação muda.
keyMessage: Ações derrubam O e D; S só muda se a consequência mudar.

Adapt: barras que se movem quando as ações as atingem. Barras → stat-bars-and-fills; ferramentas → spring-pop-entrance.
Scene 1 (0.0–2.6s): três barras horizontais de 10 células com rótulos S, O, D e valores 8, 7, 6; título headline "Agir" (1.4s).
Scene 2 (2.6–5.0s): em "instrução visual" (2.9s) um cartaz retangular com um desenho de passo a passo (1-2-3) desce sobre a barra O como um martelo; a barra O cai para 3 células e o número conta 7 → 3 (4.2s); rótulo "REDUZ A OCORRÊNCIA".
Scene 3 (5.0–7.5s): em "verificação específica" (5.2s) uma lupa quadrada com um ✓ passa sobre a barra D; a barra D cai para 2 e conta 6 → 2 (6.9s); rótulo "MELHORA A DETECÇÃO".
Scene 4 (7.5–11.328s): em "severidade" (7.8s) um martelo tenta bater na barra S e quica sem efeito; em "teimosa" (8.8s) um cadeado quadrado fecha na barra S e o carimbo "S É TEIMOSO" bate; em "só muda se a consequência mudar" (9.5s) legenda mono "SÓ MUDA SE A CONSEQUÊNCIA MUDAR". Segura.

## Frame 13 — Reavaliar em equipe

- scene: O NPR é recalculado: exemplo 8 × 3 × 2 = 48 (rótulo EXEMPLO); 336 → 48 em contagem regressiva; quatro crachás quadrados da equipe ao redor: PROJETO, PRODUÇÃO, QUALIDADE, MANUTENÇÃO
- voiceover: "Depois, a equipe recalcula o NPR. Se a ocorrência caiu para três e a detecção para dois, o risco despenca de trezentos e trinta e seis para quarenta e oito. E essa análise é feita em equipe: projeto, produção, qualidade e manutenção."
- duration: 13.547s
- transition_in: crossfade
- status: animated
- src: compositions/frames/13-reavaliar.html
- type: benefit_highlight
- persuasion: Before/after count-down + team
- beat: Resolve
- blueprint: dataviz-countup (Adapt)
- focal: a contagem regressiva 336 → 48 e a equipe
- roles: NPR antigo e novo = herói · conta 8 × 3 × 2 = apoio · quatro crachás da equipe = herói final

narrativeRole: Fecha o ciclo com reavaliação e equipe multidisciplinar.
keyMessage: Recalcular o NPR; equipe multidisciplinar.

Adapt: contagem regressiva como payoff do antes/depois, seguida da equipe que se reúne. Contagem → counting-dynamic-scale; crachás → spring-pop-entrance.
Scene 1 (0.0–2.3s): título headline "Reavaliar" (0.8s); à esquerda o "NPR ANTES: 336" (riscado só depois); rótulo mono "EXEMPLO".
Scene 2 (2.3–5.2s): no tempo da fala a nova conta monta-se: "8 ×" (2.3s), "3" (3.7s), "× 2" (4.8s).
Scene 3 (5.2–8.8s): em "despenca" (5.5s) um número grande conta para baixo de 336 até 48 (7.8s) com uma seta ↓ grande descendo junto; o 336 é riscado; o 48 fica em bloco invertido.
Scene 4 (8.8–13.547s): em "em equipe" (10.4s) quatro crachás quadrados com ícones simples entram em volta da mesa (um retângulo central "ANÁLISE FMEA"): PROJETO (11.0s), PRODUÇÃO (11.6s), QUALIDADE (12.2s), MANUTENÇÃO (12.8s); linhas retas ligam cada crachá à mesa. Segura.

## Frame 14 — O ciclo em cinco passos

- scene: Cinco blocos em ciclo quadrado acendem: LISTAR → AVALIAR → PRIORIZAR → AGIR → REAVALIAR; as iniciais formam uma trilha
- voiceover: "Resumindo o método em cinco verbos: listar as falhas, avaliar com as três notas, priorizar pelo NPR, agir e reavaliar. E o ciclo recomeça."
- duration: 8.555s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/14-ciclo.html
- type: feature_showcase
- persuasion: Process cycle
- beat: Mastery
- blueprint: compose
- focal: o ciclo de cinco blocos LISTAR → AVALIAR → PRIORIZAR → AGIR → REAVALIAR
- roles: cinco blocos em ciclo (pentágono de quadrados) = herói · setas retas = apoio · pulso que percorre o ciclo = apoio

narrativeRole: Condensa o método inteiro em um ciclo.
keyMessage: Listar, avaliar, priorizar, agir, reavaliar.

Compose: ciclo que acende bloco a bloco e depois gira. Setas → svg-path-draw; blocos → spring-pop-entrance.
Scene 1 (0.0–1.9s): título headline "O método em 5 verbos" (0.6s); cinco quadrados em contorno dispostos em anel.
Scene 2 (1.9–6.2s): no tempo da fala cada bloco acende (cobalto invertido) com seu verbo e um mini-ícone, e a seta do anterior se desenha: LISTAR (1.9s, lista de linhas), AVALIAR (3.0s, três mini-réguas), PRIORIZAR (4.3s, pódio de blocos), AGIR (5.8s, ferramenta), REAVALIAR (6.2s, seta circular quadrada).
Scene 3 (6.2–8.555s): em "o ciclo recomeça" (7.2s) a seta de REAVALIAR volta a LISTAR e um pulso percorre o anel inteiro uma vez. Segura.

## Frame 15 — Resposta de prova

- scene: Uma folha de prova se preenche em quatro faixas I · D · E · F com a resposta modelo sobre FMEA
- voiceover: "Na prova, use a fórmula. Importância: identifica falhas antes que causem dano ao cliente, parada ou retrabalho. Definição: modo, efeito e causa, com severidade, ocorrência e detecção. Efeito: o NPR mostra o que atacar primeiro. Fecho: a empresa previne problemas, reduz custos e melhora a qualidade."
- duration: 17.877s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/15-resposta.html
- type: benefit_highlight
- persuasion: Worked exam answer
- beat: Mastery
- blueprint: grid-card-assemble (Adapt)
- focal: a folha de prova preenchida I · D · E · F
- roles: folha de prova com quatro faixas = herói · marcadores I D E F = herói · palavras-chave sublinhadas = apoio

narrativeRole: Entrega uma resposta pronta na estrutura I-D-E-F.
keyMessage: Resposta modelo de FMEA.

Adapt: a folha se preenche faixa por faixa como se alguém escrevesse. Linhas → dynamic-content-sequencing; sublinhados → css-marker-patterns.
Scene 1 (0.0–1.6s): uma folha de prova (retângulo com pautas) desliza ao centro com cabeçalho "RESPOSTA · FMEA"; marcadores quadrados I, D, E, F à esquerda.
Scene 2 (1.6–6.5s): em "Importância" (1.6s) I acende e a faixa escreve-se: "Identifica falhas potenciais antes que causem dano ao cliente, parada de produção ou retrabalho."
Scene 3 (6.5–10.8s): em "Definição" (6.5s) D acende: "Analisa modo de falha (o quê), efeito (consequência) e causa (origem), com notas de severidade, ocorrência e detecção."
Scene 4 (10.8–13.7s): em "Efeito" (10.8s) E acende: "NPR = S × O × D mostra o que atacar primeiro; após as ações, recalcula-se o NPR."
Scene 5 (13.7–17.877s): em "Fecho" (13.7s) F acende: "A empresa previne problemas, reduz custos e melhora a qualidade e a satisfação do cliente." — "previne", "reduz custos" e "qualidade" ganham sublinhado no tempo da fala (14.9s, 15.8s, 17.3s); selo "✓" carimba o canto. Segura.

## Frame 16 — Cola da FMEA

- scene: Uma cola em grade: SIGLA · CORRENTE (por quê → o quê → e daí) · NOTAS (sério? ocorre? percebe?) · PEGADINHA (D alto = pior) · NPR = S × O × D (8 × 7 × 6 = 336) · CICLO; no fim, "Boa prova!"
- voiceover: "Sua cola: corrente causa, modo, efeito; três notas, com detecção alta sendo pior; NPR multiplica, oito vezes sete vezes seis dá trezentos e trinta e seis; e o ciclo: listar, avaliar, priorizar, agir e reavaliar. Boa prova!"
- duration: 14.812s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/16-cola.html
- type: branding
- persuasion: Recap grid + send-off
- beat: Calm confidence
- blueprint: grid-card-assemble (Adapt)
- focal: a cola da FMEA em grade
- roles: folha COLA com seis células = herói · macetes em blocos invertidos = herói · 'Boa prova!' = payoff

narrativeRole: Consolida todos os macetes numa tela de revisão.
keyMessage: Tudo da FMEA numa cola.

Adapt: grade que se preenche no tempo da fala, terminando na despedida. Entradas → dynamic-content-sequencing; destaques → spring-pop-entrance.
Scene 1 (0.0–2.2s): folha "COLA · FMEA" desliza ao centro com seis células; em "corrente" (0.6s) célula 1: três elos mini "CAUSA → MODO → EFEITO" com "POR QUÊ? · O QUÊ? · E DAÍ?" (1.0s–1.8s).
Scene 2 (2.2–4.4s): célula 2 (2.2s): "S · O · D" com "SÉRIO? · OCORRE? · PERCEBE?"; célula 3 (3.0s): mini-régua com "D ALTO = PIOR" em bloco invertido (3.4s).
Scene 3 (4.4–8.6s): célula 4 (4.4s): "NPR = S × O × D" e "MULTIPLICA" (5.0s); célula 5 (5.6s): "8 × 7 × 6 = 336" escrevendo-se no tempo da fala, com 336 invertido em 7.2s.
Scene 4 (8.6–12.5s): célula 6 (8.9s): mini-ciclo "LISTAR → AVALIAR → PRIORIZAR → AGIR → REAVALIAR", cada verbo acendendo no tempo (9.4s, 9.9s, 10.6s, 11.1s, 11.5s).
Scene 5 (12.5–14.812s): em "Boa prova" (12.5s) a folha encolhe levemente e "Boa prova!" sobe em display-closing abaixo dela; parada total até o fim.
