---
format: 1920x1080
duration: 180s
message: "A engenharia do futuro acelera o que o curso inteiro ensina: planejar, prevenir, medir e melhorar com dados, agindo antes do problema"
arc: concept-explainer + course recap
audience: estudantes revisando Administração e Integração de Operações e Qualidade (Aulas 9 e 10)
language: pt-BR
mode: autonomous
music: none
music_brief: calm focused minimal study underscore, soft piano and light pulse (host-generated, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** cada quadro leva a moldura Cobalt Grid — grade de papel milimetrado permanente, filetes cobalto no topo e na base (base em y ≤ 896), tag de chrome em DM Mono no canto superior esquerdo "AULAS 9–10 · INOVAÇÃO E REVISÃO" e numeração "NN / 13" no canto superior direito.
- **paleta:** só duas cores do `frame.md` — papel creme e tinta cobalto. "Falha", "perda", "fora de controle" nunca ganham vermelho: usam bloco cobalto invertido (texto creme sobre cobalto) ou um risco cobalto. Nada de gradientes coloridos, sombras ou brilhos.
- **tipo:** Newsreader 400 para títulos, termos e números grandes; Hanken Grotesk 600 caixa-alta espaçada para rótulos; DM Mono para tags, eixos, fórmulas e chrome. Texto que carrega significado nunca abaixo de ~27 px. Todo texto visível em português do Brasil, exatamente como nas linhas Scene.
- **forma:** só retângulos e linhas retas — sem cantos arredondados, sem círculos, sem pílulas; pontos de gráfico são quadrados pequenos. Setas são linhas retas com ponta triangular. Dados viram barras de células da grade quando couber.
- **zona útil:** todo conteúdo acima de y = 900 px (faixa das legendas); herói centrado em y ≈ 454.
- **movimento:** curvas de cauda longa (power3 por padrão; overshoot só onde a cena pede). Anime só transformações e opacidade (x, y, scale, opacity, clip-path, stroke) — nunca left/top/width/height. Cada peça entra quando a narração a nomeia; depois de resolvido, o quadro segura a leitura parado.
- **ritmo:** o quadro 5 (a ponte inovação → curso) e o 12 (o ciclo da operação) são os picos; os quadros 8 e 11 são curtos e diretos; o 13 é o respiro final, quase parado.
- **lista negativa:** vermelho/verde/amarelo, sombras difusas, bokeh, gradiente roxo-azul de "IA", emoji, cantos arredondados, círculos, conteúdo abaixo de y = 900, fontes via @import ou CDN; os dois modos de falha — slide (tudo de uma vez e congela) e protetor de tela (tudo flutuando sem parar).

## Frame 1 — A fábrica que avisa

- scene: Duas frases se constroem: "a máquina avisa antes de falhar" e "o plano se ajusta à demanda"; convergem na expressão FÁBRICA DO FUTURO
- voiceover: "E se a própria máquina avisasse que vai falhar… e o planejamento se ajustasse sozinho à demanda? Essa fábrica já está chegando."
- duration: 7.083s
- transition_in: cut
- status: animated
- src: compositions/frames/01-fabrica-avisa.html
- type: hook
- persuasion: Imagine / scenario
- beat: Curiosity + intrigue
- blueprint: kinetic-type-beats (Adapt)
- focal: a expressão FÁBRICA DO FUTURO em bloco invertido
- roles: FÁBRICA DO FUTURO = herói final · as duas frases = apoio (headline) · grade + filetes = fundo

narrativeRole: Abre a Aula 9 com a promessa da fábrica conectada.
keyMessage: A indústria do futuro antecipa problemas com dados.

Adapt: mantém a frase que se constrói em batidas sobre fundo plano; o payoff vira um bloco-título. Revelação palavra a palavra → dynamic-content-sequencing.
Scene 1 (0.0–2.4s): "a máquina avisa antes de falhar" monta palavra a palavra no terço superior esquerdo (headline), com "avisa" (1.0s) em bloco cobalto invertido e "falhar" em 2.0s.
Scene 2 (2.4–5.4s): "o plano se ajusta à demanda" monta no terço superior direito, com "planejamento" (2.6s) virando "o plano" e "demanda" em 4.6s.
Scene 3 (5.4–7.083s): em "Essa fábrica" (5.7s) as duas frases recuam para ink-soft e sobem; FÁBRICA DO FUTURO entra grande no centro (display-closing) dentro de um bloco cobalto invertido, com linhas retas finas ligando as frases ao bloco; "já está chegando" (6.4s) em mono abaixo do bloco. Segura parado.

## Frame 2 — Quatro revoluções

- scene: Uma linha do tempo com quatro estações: 1ª vapor, 2ª eletricidade e produção em massa, 3ª automação com computadores, 4ª Indústria 4.0 conectada
- voiceover: "Na Aula 9, inovação na indústria. A primeira revolução trouxe o vapor; a segunda, a eletricidade e a produção em massa; a terceira, a automação com computadores. A quarta, a Indústria quatro ponto zero, conecta tudo."
- duration: 12.821s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-revolucoes.html
- type: product_intro
- persuasion: Timeline + escalation
- beat: Orientation + clarity
- blueprint: spatial-pan-stations (Adapt)
- focal: a estação 4.0 no fim da linha do tempo
- roles: linha do tempo horizontal com quatro estações numeradas = herói · rótulos curtos de cada revolução = apoio · estação 4.0 em cobalto invertido = herói final

narrativeRole: Situa a Indústria 4.0 na história das revoluções industriais.
keyMessage: 4.0 = a revolução da conexão.

Adapt: mantém estações pré-posicionadas numa tela larga percorrida por uma câmera virtual, terminando parada na última. Câmera → viewport-change; linha → svg-path-draw.
Scene 1 (0.0–2.3s): rótulo micro-strong "AULA 9" e título display-chapter "Inovação na indústria" (0.9s) centralizados; em 2.0s o título sobe para o topo esquerdo e a linha do tempo começa a se desenhar.
Scene 2 (2.3–9.8s): a câmera faz panorâmica pela linha; cada estação é um bloco retangular de contorno com numeral grande em Newsreader e rótulo em mono: "1ª · VAPOR" (3.9s), "2ª · ELETRICIDADE E PRODUÇÃO EM MASSA" (5.2s), "3ª · AUTOMAÇÃO COM COMPUTADORES" (8.2s).
Scene 3 (9.8–12.821s): em "Indústria 4.0" (10.6s) a quarta estação "4.0" entra em bloco cobalto invertido, maior que as outras; a câmera recua mostrando as quatro; em "conecta tudo" (12.0s) linhas retas finas ligam a estação 4.0 às três anteriores, e o rótulo "CONEXÃO" aparece acima dela. Segura.

## Frame 3 — Pilares da 4.0

- scene: Quatro blocos se encaixam numa grade: SISTEMAS CIBERFÍSICOS, INTERNET DAS COISAS, NUVEM, BIG DATA; linhas de dados ligam máquina, produto e pessoa
- voiceover: "Ela une sistemas ciberfísicos, internet das coisas, computação em nuvem e big data. Máquinas, produtos e pessoas trocam dados em tempo real."
- duration: 8.683s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-pilares.html
- type: feature_showcase
- persuasion: Enumeration + network
- beat: Comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: a grade dos quatro pilares
- roles: quatro blocos em fileira = herói (metade superior) · três nós MÁQUINA / PRODUTO / PESSOA ligados por linhas de dados = herói secundário (metade inferior) · grade = fundo

narrativeRole: Nomeia as bases tecnológicas da Indústria 4.0.
keyMessage: Tudo conectado, trocando dados em tempo real.

Adapt: mantém a montagem escalonada de N blocos, cada um no tempo da fala, e acrescenta uma pequena rede embaixo. Blocos → dynamic-content-sequencing; linhas de dados → svg-path-draw.
Scene 1 (0.0–4.6s): título headline "Pilares da 4.0" no topo esquerdo; quatro blocos de contorno entram na metade superior em fileira, no tempo da fala: "SISTEMAS CIBERFÍSICOS" (0.6s), "INTERNET DAS COISAS" (1.8s), "NUVEM" (3.8s), "BIG DATA" (4.4s), cada um com número mono 01–04.
Scene 2 (4.6–8.683s): na metade inferior, três blocos quadrados pequenos em cobalto invertido entram: "MÁQUINA" (5.4s), "PRODUTO" (6.0s), "PESSOA" (6.6s); em "trocam dados" (7.0s) linhas retas tracejadas se desenham entre eles e até a fileira de pilares; em "tempo real" (8.0s) o rótulo mono "TEMPO REAL" aparece no centro da rede. Segura.

## Frame 4 — Tecnologias na prática

- scene: Grade 2×2: INTELIGÊNCIA ARTIFICIAL, ROBÓTICA COLABORATIVA, MANUFATURA ADITIVA (3D), GÊMEO DIGITAL; o gêmeo digital se destaca com uma fábrica e sua cópia em contorno
- voiceover: "Na prática, aparecem a inteligência artificial, a robótica colaborativa, a manufatura aditiva, ou impressão três D, e o gêmeo digital: uma cópia virtual do processo para testar mudanças antes de mexer na fábrica real."
- duration: 13.333s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-tecnologias.html
- type: feature_showcase
- persuasion: Categorization + concrete definition
- beat: Fascination + comprehension
- blueprint: grid-card-assemble (Adapt)
- focal: o cartão GÊMEO DIGITAL com fábrica e cópia
- roles: quatro cartões em grade 2×2 = herói · cartão GÊMEO DIGITAL (cobalto invertido) com um esquema de fábrica e sua cópia em contorno tracejado = herói final · grade = fundo

narrativeRole: Mostra as tecnologias que a prova costuma citar, com destaque ao gêmeo digital.
keyMessage: IA, cobots, impressão 3D e gêmeo digital.

Adapt: mantém a grade de N cartões, cada um no tempo da sua palavra; o último ganha um mini-diagrama. Cartões → spring-pop-entrance (sem overshoot); esquema → svg-path-draw.
Scene 1 (0.0–1.4s): título headline "Tecnologias" no topo esquerdo; quatro contornos tênues em grade 2×2.
Scene 2 (1.4–7.3s): cartões se preenchem (contorno cobalto, fundo creme): "INTELIGÊNCIA ARTIFICIAL" (1.4s), "ROBÓTICA COLABORATIVA" (3.0s), "MANUFATURA ADITIVA" (4.6s) — com tag mono "IMPRESSÃO 3D" em 6.2s.
Scene 3 (7.3–13.333s): em "gêmeo digital" (7.5s) o quarto cartão vira cobalto invertido: "GÊMEO DIGITAL"; dentro dele, em "cópia virtual" (9.0s) um esquema simples de fábrica (retângulos e telhado em dente de serra, linhas retas creme) e, ao lado, a mesma silhueta em contorno tracejado; em "testar mudanças" (10.6s) uma seta reta vai da cópia para a fábrica com o rótulo "TESTAR ANTES". Segura.

## Frame 5 — Liga com o curso

- scene: À esquerda, SENSORES / MANUTENÇÃO PREDITIVA / IA; à direita, OEE e CEP, FMEA, PREVISÃO DE DEMANDA; linhas retas ligam cada tecnologia ao conteúdo do curso
- voiceover: "E tudo conversa com o que vimos: sensores alimentam o OEE e o CEP em tempo real, a manutenção preditiva antecipa falhas como na FMEA, e a inteligência artificial melhora a previsão de demanda."
- duration: 11.712s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-liga-curso.html
- type: benefit_highlight
- persuasion: Bridge to prior knowledge
- beat: "Aha" + connection
- blueprint: compose
- focal: as quatro linhas que ligam tecnologia a conteúdo do curso
- roles: coluna esquerda TECNOLOGIA (3 blocos) = apoio · coluna direita CURSO (3 blocos em cobalto invertido) = herói · linhas retas entre elas = herói

narrativeRole: Conecta a inovação às ferramentas das aulas anteriores.
keyMessage: A 4.0 turbina OEE, CEP, FMEA e previsão.

Compose: duas colunas e pontes desenhadas no tempo da fala. Linhas → svg-path-draw; entrada dos blocos → dynamic-content-sequencing.
Scene 1 (0.0–2.0s): título headline "Tudo conversa com o curso" no topo; rótulos micro-strong "TECNOLOGIA" sobre a coluna esquerda e "O QUE VIMOS" sobre a direita.
Scene 2 (2.0–5.3s): em "sensores" (2.0s) o bloco esquerdo 1 "SENSORES" entra; em "OEE" (3.3s) e "CEP" (4.0s) o bloco direito 1 "OEE e CEP" (cobalto invertido) entra e uma linha reta liga os dois, com tag mono "TEMPO REAL" sobre a linha (4.6s).
Scene 3 (5.3–8.6s): em "manutenção preditiva" (5.4s) o bloco esquerdo 2; em "FMEA" (7.9s) o bloco direito 2 "FMEA" e a linha reta entre eles, com tag "ANTECIPA FALHAS".
Scene 4 (8.6–11.712s): em "inteligência artificial" (8.9s) o bloco esquerdo 3 "IA"; em "previsão de demanda" (10.7s) o bloco direito 3 "PREVISÃO DE DEMANDA" e a linha, com tag "MELHORA". Segura.

## Frame 6 — Sustentabilidade

- scene: Uma linha reta de produção (extrair → produzir → descartar) se dobra num ciclo quadrado (produzir → usar → recuperar → reaproveitar) — economia circular
- voiceover: "A engenharia do futuro também é sustentável: economia circular, menos desperdício e uso eficiente de energia. É o mesmo espírito da produção enxuta, agora com o planeta na conta."
- duration: 10.923s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-sustentavel.html
- type: feature_showcase
- persuasion: Before/after (linear → circular)
- beat: Recognition
- blueprint: compose
- focal: o ciclo quadrado da economia circular
- roles: linha reta EXTRAIR → PRODUZIR → DESCARTAR = herói inicial · ciclo quadrado de quatro blocos = herói final · três tags de benefício = apoio

narrativeRole: Acrescenta a dimensão ambiental à inovação.
keyMessage: Economia circular = enxuto aplicado ao planeta.

Compose: uma linha que se dobra em ciclo — o antes e depois é o próprio movimento. Setas → svg-path-draw; tags → dynamic-content-sequencing.
Scene 1 (0.0–2.7s): título headline "Engenharia sustentável" no topo esquerdo (1.7s); uma linha reta horizontal com três blocos de contorno: EXTRAIR → PRODUZIR → DESCARTAR, ligados por setas retas.
Scene 2 (2.7–4.0s): em "economia circular" (2.7s) "DESCARTAR" é riscado e a linha se rearranja em quatro blocos formando um quadrado: PRODUZIR → USAR → RECUPERAR → REAPROVEITAR, com setas retas fechando o ciclo; rótulo "ECONOMIA CIRCULAR" em bloco invertido no centro do quadrado.
Scene 3 (4.0–6.9s): à direita, tags empilhadas em mono: "MENOS DESPERDÍCIO" (4.3s), "ENERGIA EFICIENTE" (5.4s).
Scene 4 (6.9–10.923s): em "produção enxuta" (8.1s) uma faixa abaixo: "ENXUTO" (contorno) + "+ PLANETA" (cobalto invertido, em "planeta" 9.9s). Segura.

## Frame 7 — O engenheiro do futuro

- scene: Um perfil com três competências que se acumulam: DADOS, EQUIPE MULTIDISCIPLINAR, APRENDIZADO CONTÍNUO; embaixo, a frase "a tecnologia muda; o método fica"
- voiceover: "E ela pede um novo profissional: alguém que entenda de dados, trabalhe em equipe multidisciplinar e continue aprendendo. A tecnologia muda; o método de pensar fica."
- duration: 10.048s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-engenheiro.html
- type: benefit_highlight
- persuasion: Rule of three + maxim
- beat: Confidence
- blueprint: grid-card-assemble (Adapt)
- focal: o perfil com três competências empilhadas
- roles: ficha de perfil com três linhas de competência (barras de células) = herói · máxima final = apoio (ed-callout)

narrativeRole: Fecha a Aula 9 no perfil profissional e prepara a revisão.
keyMessage: Dados, equipe e aprendizado contínuo.

Adapt: a grade vira uma ficha cujas linhas se acumulam no tempo da fala. Barras → stat-bars-and-fills; entrada das linhas → dynamic-content-sequencing.
Scene 1 (0.0–1.9s): título headline "O engenheiro do futuro" no topo esquerdo (1.1s); ficha retangular de contorno à esquerda (60%) com cabeçalho em faixa invertida "PERFIL".
Scene 2 (1.9–7.0s): linhas da ficha, cada uma com rótulo micro-strong e uma barra de 10 células que enche: "DADOS" (3.1s), "EQUIPE MULTIDISCIPLINAR" (4.2s), "APRENDIZADO CONTÍNUO" (5.7s).
Scene 3 (7.0–10.048s): à direita (40%), a máxima em ed-callout itálico: "A tecnologia muda;" (7.2s) e, em "o método de pensar fica" (8.6s), a segunda linha "o método fica." em bloco cobalto invertido. Segura.

## Frame 8 — A pergunta do curso

- scene: Rótulo AULA 10 · REVISÃO GERAL; uma pergunta se monta em três partes destacadas: produzir CERTO, na HORA CERTA, com QUALIDADE
- voiceover: "Na Aula 10, a revisão geral. A disciplina inteira cabe numa pergunta: como produzir certo, na hora certa e com qualidade?"
- duration: 7.211s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/08-pergunta.html
- type: hook
- persuasion: Distillation into a question
- beat: Focus + orientation
- blueprint: kinetic-type-beats (Adapt)
- focal: a pergunta com os três termos destacados
- roles: pergunta em display = herói · CERTO / HORA CERTA / QUALIDADE em blocos invertidos = herói · rótulo AULA 10 · REVISÃO GERAL = chrome

narrativeRole: Abre a revisão com a pergunta que organiza todo o conteúdo.
keyMessage: Certo, na hora certa, com qualidade.

Adapt: mantém a construção por batidas com termos que acendem no lugar. Entrada palavra a palavra → dynamic-content-sequencing.
Scene 1 (0.0–2.0s): rótulo micro-strong "AULA 10" (0.2s) e título display-chapter "Revisão geral" (1.0s) centralizados no alto.
Scene 2 (2.0–4.3s): o título sobe e reduz; em "numa pergunta" (3.4s) aparece em mono "A DISCIPLINA EM UMA PERGUNTA".
Scene 3 (4.3–7.211s): a pergunta monta em headline grande no centro: "Como produzir" (4.3s) "certo," (5.1s) "na hora certa" (5.6s) "e com qualidade?" (6.3s) — cada termo-chave (certo / hora certa / qualidade) vira bloco cobalto invertido ao ser dito. Segura.

## Frame 9 — Na hora certa

- scene: Três estações em sequência: PPCP (planejar, programar, controlar) → JIT + KANBAN (puxar pela demanda) → PREVISÃO (quanto vão pedir + erro)
- voiceover: "Para produzir na hora certa: o PPCP planeja, programa e controla; o just in time e o kanban puxam a produção pela demanda; e a previsão estima quanto o cliente vai pedir, sempre com o seu erro."
- duration: 11.285s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-hora-certa.html
- type: feature_showcase
- persuasion: Recap enumeration
- beat: Mastery
- blueprint: spatial-pan-stations (Adapt)
- focal: as três estações do planejamento
- roles: três estações em sequência ligadas por setas = herói · rótulo de seção NA HORA CERTA = apoio · tags com o vídeo de origem = apoio

narrativeRole: Revisa as ferramentas de planejamento (vídeos 1 e 2).
keyMessage: PPCP, JIT/kanban e previsão garantem o tempo certo.

Adapt: mantém estações numa faixa larga, percorrida por uma câmera virtual leve, terminando com as três à vista. Câmera → viewport-change; setas → svg-path-draw.
Scene 1 (0.0–1.4s): faixa de seção em cobalto invertido no topo: "NA HORA CERTA" (1.0s).
Scene 2 (1.4–4.0s): estação 1, bloco de contorno: "PPCP" (1.5s, display-chapter) com três verbos em mono empilhados: "PLANEJA" (2.2s), "PROGRAMA" (2.8s), "CONTROLA" (3.4s).
Scene 3 (4.0–7.3s): a câmera desliza para a estação 2 e uma seta reta liga as duas: "JIT + KANBAN" (4.2s, kanban em 5.4s) com tag mono "PUXA PELA DEMANDA" (5.8s).
Scene 4 (7.3–11.285s): estação 3: "PREVISÃO" (7.6s) com tag "QUANTO VÃO PEDIR" (8.6s) e, em "erro" (10.9s), uma segunda tag em bloco invertido "+ ERRO"; a câmera recua e mostra as três estações. Segura.

## Frame 10 — Certo da primeira vez

- scene: Dois cartões lado a lado: FMEA (NPR = S × O × D) e GQT + CUSTOS (prevenir < corrigir)
- voiceover: "Para produzir certo: a FMEA prioriza riscos com severidade, ocorrência e detecção, e a GQT envolve todos na qualidade, porque prevenir sai mais barato que corrigir."
- duration: 9.984s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/10-certo.html
- type: feature_showcase
- persuasion: Recap comparison
- beat: Mastery
- blueprint: comparison-split (Adapt)
- focal: os dois cartões FMEA e GQT
- roles: cartão FMEA = herói esquerdo (contorno) · cartão GQT (cobalto invertido) = herói direito · faixa PREVENIR < CORRIGIR = apoio final

narrativeRole: Revisa as ferramentas de prevenção (vídeos 2 e 3).
keyMessage: FMEA e GQT: prevenir antes de corrigir.

Adapt: mantém a entrada dividida com inclinações espelhadas; selos e faixa são retângulos. Cartões → split-tilt-cards; faixa final → spring-pop-entrance (sem overshoot).
Scene 1 (0.0–1.3s): faixa de seção em cobalto invertido no topo: "CERTO DA PRIMEIRA VEZ" (0.7s).
Scene 2 (1.3–5.0s): em "FMEA" (1.3s) o cartão esquerdo entra da esquerda: "FMEA" (display-chapter) + fórmula mono "NPR = S × O × D" que monta termo a termo em "severidade" (2.8s), "ocorrência" (3.5s), "detecção" (4.3s).
Scene 3 (5.0–7.5s): em "GQT" (5.3s) o cartão direito entra da direita, fundo cobalto invertido: "GQT" + "todos na qualidade" (6.4s).
Scene 4 (7.5–9.984s): em "prevenir" (7.8s) uma faixa sob os cartões: "PREVENIR" (bloco invertido) "<" "CORRIGIR" (contorno), com "<" em display grande. Segura.

## Frame 11 — Com qualidade medida

- scene: À esquerda, a barra do OEE (D × P × Q); à direita, um mini gráfico de controle com LSC, LM e LIC e um ponto fora
- voiceover: "E para garantir a qualidade: o OEE mede as perdas do equipamento, e o CEP separa a variação normal das causas especiais."
- duration: 7.36s
- transition_in: crossfade
- status: animated
- src: compositions/frames/11-medir.html
- type: feature_showcase
- persuasion: Recap demonstration
- beat: Mastery
- blueprint: dataviz-countup (Adapt)
- focal: o mini gráfico de controle com o ponto fora
- roles: barra OEE (D × P × Q) = herói esquerdo · mini gráfico de controle = herói direito · faixa de seção = apoio

narrativeRole: Revisa as ferramentas de medição (vídeo 3).
keyMessage: OEE mede perdas; CEP detecta causas especiais.

Adapt: dois instrumentos de dado lado a lado, sem contagem numérica (nenhum valor novo). Barra → stat-bars-and-fills; gráfico → svg-path-draw.
Scene 1 (0.0–1.6s): faixa de seção em cobalto invertido no topo: "COM QUALIDADE MEDIDA" (0.9s).
Scene 2 (1.6–3.9s): à esquerda, em "OEE" (1.8s), o rótulo "OEE" (display-chapter) e uma barra de 20 células que enche só em parte; em "perdas" (2.9s) a parte vazia ganha hachura e o rótulo "PERDAS"; legenda mono "D × P × Q".
Scene 3 (3.9–7.36s): à direita, em "CEP" (4.2s), um mini gráfico: LM, LSC e LIC se desenham com rótulos mono; em "variação normal" (5.2s) pontos quadrados oscilam dentro dos limites; em "causas especiais" (6.2s) um ponto sai acima do LSC e ganha moldura e o rótulo invertido "CAUSA ESPECIAL". Segura.

## Frame 12 — O padrão

- scene: Quatro blocos quadrados formam um ciclo: PLANEJAR → PREVENIR → MEDIR → MELHORAR; um rótulo "PDCA DA OPERAÇÃO" no centro e, ao redor, "INDÚSTRIA 4.0 = DADOS MAIS RÁPIDOS"
- voiceover: "Repare no padrão: planejar, prevenir, medir e melhorar. É o PDCA aplicado à operação inteira, e a Indústria quatro ponto zero só acelera esse ciclo com dados."
- duration: 9.429s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/12-padrao.html
- type: benefit_highlight
- persuasion: Pattern reveal + callback (PDCA)
- beat: "Aha" + satisfaction
- blueprint: compose
- focal: o ciclo quadrado PLANEJAR → PREVENIR → MEDIR → MELHORAR
- roles: quatro blocos quadrados em ciclo 2×2 = herói (centro, ~50% da largura) · rótulo central PDCA DA OPERAÇÃO = herói · faixa INDÚSTRIA 4.0 = apoio

narrativeRole: Une as dez aulas num único ciclo e liga a inovação à revisão.
keyMessage: Planejar, prevenir, medir, melhorar — o PDCA da operação.

Compose: o ciclo quadrado do vídeo 3 (PDCA) retorna, agora com os verbos do curso. Setas → svg-path-draw; blocos → dynamic-content-sequencing.
Scene 1 (0.0–3.5s): título headline "O padrão" no topo esquerdo (0.6s); quatro blocos quadrados em 2×2 acendem (cobalto invertido) no tempo da fala, com a seta reta do anterior se desenhando: "PLANEJAR" (1.1s), "PREVENIR" (1.7s), "MEDIR" (2.2s), "MELHORAR" (2.9s); a seta de MELHORAR volta a PLANEJAR fechando o ciclo.
Scene 2 (3.5–5.9s): em "PDCA" (3.8s) um rótulo quadrado no centro do ciclo: "PDCA" (display-chapter) com "DA OPERAÇÃO" em mono abaixo (4.9s).
Scene 3 (5.9–9.429s): em "Indústria 4.0" (6.2s) uma faixa à direita do ciclo: "INDÚSTRIA 4.0"; em "acelera" (7.7s) as setas do ciclo engrossam uma a uma em sequência, como um pulso que roda o ciclo uma vez; em "dados" (8.9s) a faixa ganha a tag invertida "= DADOS MAIS RÁPIDOS". Segura.

## Frame 13 — Encerramento

- scene: As palavras-chave do curso se acumulam em linhas finas e convergem em ANTES + DADOS; por fim, "Boa prova!"
- voiceover: "Resumindo o curso: operações bem geridas agem antes do problema e decidem com dados. Bons estudos, e boa prova!"
- duration: 7.019s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/13-encerramento.html
- type: branding
- persuasion: Distillation + callback to both earlier videos
- beat: Satisfaction + send-off
- blueprint: titlecard-reveal (Adapt)
- focal: ANTES + DADOS e a despedida
- roles: linhas finas com palavras-chave do curso = apoio de fundo · blocos ANTES e DADOS = herói · 'Boa prova!' = payoff

narrativeRole: Fecha a série com as duas ideias-mãe (antes, dados) e uma despedida.
keyMessage: Agir antes do problema e decidir com dados.

Adapt: mantém o cartão-título calmo com um único movimento contido e a parada final; une os ganchos dos vídeos anteriores (ANTES, DADOS). Entrada → dynamic-content-sequencing.
Scene 1 (0.0–2.8s): em linhas finas tênues (ink-faint, mono), as palavras-chave do curso aparecem rápidas em cascata no alto: PPCP · JIT · KANBAN · FMEA · PREVISÃO · GQT · CUSTOS · OEE · CEP · 4.0.
Scene 2 (2.8–4.6s): em "antes do problema" (2.8s) o bloco cobalto invertido "ANTES" entra no centro esquerdo (display-closing); em "dados" (4.6s) o bloco "DADOS" entra ao lado, com "+" entre eles.
Scene 3 (4.6–7.019s): em "Bons estudos" (5.3s) as palavras-chave somem; abaixo dos blocos, "Bons estudos," em ed-callout e, em "boa prova" (6.2s), "Boa prova!" em headline. Um único movimento de subida; parada total até o fim.
