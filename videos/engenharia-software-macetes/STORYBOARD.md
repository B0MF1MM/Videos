---
format: 1920x1080
duration: 300s
message: "Cada pergunta da revisão tem uma resposta-gabarito curta e um macete visual"
arc: how-to — 11 perguntas da revisão, cada uma com resposta do slide + macete, comparação dos modelos, cola final
audience: estudante que faz a prova amanhã de Modelos, Métodos e Técnicas da Engenharia de Software
language: pt-BR
mode: autonomous
music: none
music_brief: trilha de estudo calma reaproveitada (host, assets/music/underscore.mp3)
---

## Video direction

- **chrome:** moldura Cobalt Grid — grade milimetrada, filetes cobalto no topo e na base (y ≤ 896), tag DM Mono "ENG. SOFTWARE · MACETES" no canto superior esquerdo e "NN / 20" no direito.
- **paleta:** só papel creme #F0EBDE e tinta cobalto #1F2BE0 do frame.md. Erro/pegadinha = bloco cobalto invertido ou risco, nunca vermelho.
- **tipo:** Newsreader para títulos e termos; Hanken Grotesk 600 caixa-alta para rótulos; DM Mono para tags. Nada abaixo de ~26 px.
- **forma:** retângulos e linhas retas; setas retas com ponta triangular; ícones desenhados com retângulos/linhas.
- **zona útil:** conteúdo acima de y = 900 (legendas embaixo).
- **movimento:** cada item entra quando a narração o nomeia; macetes entram como carimbo (bloco invertido + overshoot); câmera respira lentamente; parada de leitura só no final.
- **lista negativa:** vermelho/verde, sombras, gradientes, emoji, círculos decorativos, fontes externas.

## Frame 1 — Prova amanhã

- scene: Calendário AMANHÃ; título ENGENHARIA DE SOFTWARE se monta; três cartões PERGUNTA → RESPOSTA → MACETE
- voiceover: "Prova amanhã de Engenharia de Software? Respira. Neste vídeo você vai ver cada pergunta que costuma cair, a resposta que o professor espera, e um macete visual para não esquecer mais."
- duration: 9.931s
- transition_in: cut
- status: animated
- src: compositions/frames/01-prova-amanha.html
- type: hook
- blueprint: kinetic-type-beats (Adapt)
- focal: trilha PERGUNTA → RESPOSTA → MACETE
- roles: trilha PERGUNTA → RESPOSTA → MACETE = herói · rótulos = apoio

narrativeRole: Prova amanhã.
keyMessage: trilha PERGUNTA → RESPOSTA → MACETE.

Scene 1 (0.0–3.3s): calendário com AMANHÃ cai e assenta; título em Newsreader se escreve.
Scene 2 (3.3–6.6s): em 'Respira' a câmera desacelera; rótulo 'RESPIRA' em mono.
Scene 3 (6.6–9.931s): três cartões entram em fila com setas: PERGUNTA, RESPOSTA, MACETE (carimbo cobalto no último).

## Frame 2 — O que é Engenharia de Software

- scene: Engrenagens de produção: ESPECIFICAÇÃO ──► MANUTENÇÃO; balança custo-benefício: + QUALIDADE, − PRAZO, − CUSTO
- voiceover: "Primeira pergunta: o que é Engenharia de Software? É a disciplina que cuida de todos os aspectos da produção de software, desde a especificação até a manutenção. O objetivo é uma boa relação custo-benefício: mais qualidade, com menos prazo e menos custo."
- duration: 14.522s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-o-que-e.html
- type: feature_showcase
- blueprint: compose
- focal: régua do início ao fim e os três sinais + − −
- roles: régua do início ao fim e os três sinais + − − = herói · rótulos = apoio

narrativeRole: O que é Engenharia de Software.
keyMessage: régua do início ao fim e os três sinais + − −.

Scene 1 (0.0–4.8s): pergunta em cartão cobalto 'O QUE É ENGENHARIA DE SOFTWARE?'.
Scene 2 (4.8–9.7s): uma régua se desenha da ESPECIFICAÇÃO à MANUTENÇÃO, engrenagens girando no meio.
Scene 3 (9.7–14.522s): três medidores: QUALIDADE sobe, PRAZO desce, CUSTO desce — macete carimbado.

## Frame 3 — A Crise do Software

- scene: Linha do tempo 1960 amador → 1968 OTAN (Alemanha) → CRISE DO SOFTWARE; macete P·R·Q em três blocos
- voiceover: "Por que ela surgiu? Nos anos sessenta, programar era amador e desorganizado. Em mil novecentos e sessenta e oito, uma conferência da OTAN, na Alemanha, deu nome ao problema: a Crise do Software. Macete: P, R, Q. Prazo estourado, requisito ignorado e qualidade baixa."
- duration: 16.643s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-crise.html
- type: feature_showcase
- blueprint: compose
- focal: três blocos P R Q
- roles: três blocos P R Q = herói · rótulos = apoio

narrativeRole: A Crise do Software.
keyMessage: três blocos P R Q.

Scene 1 (0.0–5.5s): linha do tempo: anos 60 com papéis bagunçados que tremem.
Scene 2 (5.5–11.1s): 1968: marcador OTAN · ALEMANHA, carimbo CRISE DO SOFTWARE.
Scene 3 (11.1–16.643s): P, R, Q caem como blocos; sob cada um: PRAZO ESTOURADO, REQUISITO IGNORADO, QUALIDADE BAIXA.

## Frame 4 — Ciclo de vida

- scene: Roda de seis fases do SDLC; cada fase vira um verbo; seta de retorno fecha o ciclo
- voiceover: "O ciclo de vida do software tem seis fases, em roda. Macete: transforme cada fase num verbo. Planeje, analise, desenhe, desenvolva, teste e mantenha. E é um ciclo: a manutenção corrige erros, atualiza o sistema, e tudo recomeça."
- duration: 13.888s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-ciclo-de-vida.html
- type: feature_showcase
- blueprint: compose
- focal: roda das seis fases
- roles: roda das seis fases = herói · rótulos = apoio

narrativeRole: Ciclo de vida.
keyMessage: roda das seis fases.

Scene 1 (0.0–4.6s): seis blocos dispostos em hexágono, numerados.
Scene 2 (4.6–9.3s): cada fase acende e ganha seu verbo: PLANEJE, ANALISE, DESENHE, DESENVOLVA, TESTE, MANTENHA.
Scene 3 (9.3–13.888s): um marcador percorre a roda e volta ao início: RECOMEÇA.

## Frame 5 — O que é requisito

- scene: Dois lados: USUÁRIO PRECISA ↔ SISTEMA PROVÊ, ligados por uma ponte REQUISITO
- voiceover: "O que é requisito? É uma condição ou capacidade que o usuário precisa para resolver um problema ou atingir um objetivo. E é também o que o sistema deve prover para cumprir um contrato, uma norma ou uma especificação. Macete: o usuário precisa, o sistema provê."
- duration: 14.442s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-requisito.html
- type: feature_showcase
- blueprint: comparison-split (Adapt)
- focal: ponte USUÁRIO PRECISA ↔ SISTEMA PROVÊ
- roles: ponte USUÁRIO PRECISA ↔ SISTEMA PROVÊ = herói · rótulos = apoio

narrativeRole: O que é requisito.
keyMessage: ponte USUÁRIO PRECISA ↔ SISTEMA PROVÊ.

Scene 1 (0.0–4.8s): pergunta 'O QUE É REQUISITO?'.
Scene 2 (4.8–9.6s): esquerda: boneco-usuário com balão PROBLEMA / OBJETIVO; direita: caixa SISTEMA com CONTRATO · NORMA · ESPECIFICAÇÃO.
Scene 3 (9.6–14.442s): macete: PRECISA ⇄ PROVÊ em blocos invertidos.

## Frame 6 — Fases de requisitos

- scene: Esteira de quatro estações: ELICITAÇÃO → ANÁLISE E NEGOCIAÇÃO → DEFINIÇÃO E DOCUMENTAÇÃO → VALIDAÇÃO; verbos ESCUTA · ACERTA · ESCREVE · CONFERE
- voiceover: "Os requisitos são trabalhados junto ao cliente, em quatro fases: elicitação, análise e negociação, definição e documentação, e validação. Macete: escuta, acerta, escreve e confere. Alguns slides somam uma quinta, o gerenciamento, que acompanha as mudanças."
- duration: 15.837s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-fases-requisitos.html
- type: feature_showcase
- blueprint: grid-card-assemble (Adapt)
- focal: quatro estações com verbos
- roles: quatro estações com verbos = herói · rótulos = apoio

narrativeRole: Fases de requisitos.
keyMessage: quatro estações com verbos.

Scene 1 (0.0–5.3s): quatro estações entram em sequência com seta correndo.
Scene 2 (5.3–10.6s): cada estação ganha seu verbo-macete com ícone (orelha, aperto, folha, check).
Scene 3 (10.6–15.837s): quinta estação tracejada: GERENCIAMENTO (mudanças).

## Frame 7 — Funcional × não funcional

- scene: Divisão O QUE × COMO; tela de cadastro à esquerda, medidores de velocidade/documento/facilidade à direita
- voiceover: "A pergunta mais clássica: funcional ou não funcional? Funcional é o que o sistema faz: o cliente faz o próprio cadastro. Não funcional é como o sistema funciona: rápido, documentado, fácil de usar. Macete: funcional é funcionalidade, não funcional é qualidade."
- duration: 16.04s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-funcional.html
- type: feature_showcase
- blueprint: comparison-split (Adapt)
- focal: O QUE × COMO
- roles: O QUE × COMO = herói · rótulos = apoio

narrativeRole: Funcional × não funcional.
keyMessage: O QUE × COMO.

Scene 1 (0.0–5.3s): pergunta 'FUNCIONAL OU NÃO FUNCIONAL?'.
Scene 2 (5.3–10.7s): esquerda O QUE: formulário de cadastro se preenche; direita COMO: velocímetro, documento, interface.
Scene 3 (10.7–16.04s): macete: FUNCIONALIDADE × QUALIDADE.

## Frame 8 — Pegadinha da biblioteca

- scene: Quiz: cartões da biblioteca caem em duas caixas FUNCIONAL / NÃO FUNCIONAL; o cartão SEGURANÇA DOS DADOS tenta a caixa errada e é desviado
- voiceover: "Teste com a biblioteca online. Pesquisar, reservar e renovar livros: funcional. Interface intuitiva, vários idiomas, aguentar muitos usuários e ficar no ar o tempo todo: não funcional. E a pegadinha: garantir a segurança dos dados parece função, mas é qualidade. É não funcional."
- duration: 16.641s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-biblioteca.html
- type: feature_showcase
- blueprint: compose
- focal: cartão SEGURANÇA DOS DADOS → NÃO FUNCIONAL
- roles: cartão SEGURANÇA DOS DADOS → NÃO FUNCIONAL = herói · rótulos = apoio

narrativeRole: Pegadinha da biblioteca.
keyMessage: cartão SEGURANÇA DOS DADOS → NÃO FUNCIONAL.

Scene 1 (0.0–5.5s): duas caixas abertas; cartões PESQUISAR, RESERVAR, RENOVAR caem em FUNCIONAL.
Scene 2 (5.5–11.1s): INTERFACE, IDIOMAS, MUITOS USUÁRIOS, 24/7 caem em NÃO FUNCIONAL.
Scene 3 (11.1–16.641s): SEGURANÇA DOS DADOS vai para FUNCIONAL, carimbo PEGADINHA!, e desliza para NÃO FUNCIONAL.

## Frame 9 — Processo de software

- scene: Definição de processo e quatro pilares com perguntas: O QUE? · COMO? · ESTÁ CORRETO? · ADAPTAR
- voiceover: "O que é processo de software? É um conjunto estruturado de atividades, métodos e práticas que as pessoas usam para desenvolver e manter o software. Quatro pilares: especificação, o que fazer. Design e implementação, como fazer. Validação, está correto? E evolução, adaptar com o tempo."
- duration: 17.355s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-processo.html
- type: feature_showcase
- blueprint: grid-card-assemble (Adapt)
- focal: quatro pilares
- roles: quatro pilares = herói · rótulos = apoio

narrativeRole: Processo de software.
keyMessage: quatro pilares.

Scene 1 (0.0–5.8s): frase-definição com destaque CONJUNTO ESTRUTURADO.
Scene 2 (5.8–11.6s): quatro colunas sobem como pilares: ESPECIFICAÇÃO, DESIGN E IMPLEMENTAÇÃO, VALIDAÇÃO, EVOLUÇÃO.
Scene 3 (11.6–17.355s): sob cada pilar a sua pergunta-macete.

## Frame 10 — Modelo × processo

- scene: Receita de bolo (MODELO) + relógio/cozinheiro/quantidade (PLANEJAMENTO) = PROCESSO
- voiceover: "E modelo? Modelo é uma representação simplificada da realidade: algo teórico, um conjunto de possíveis ações. Processo é prático, com prazos e métricas. Pense num bolo: a receita é o modelo. Com horário, cozinheiro e quantidade, vira processo. Modelo mais planejamento é igual a processo."
- duration: 17.975s
- transition_in: crossfade
- status: animated
- src: compositions/frames/10-modelo-processo.html
- type: feature_showcase
- blueprint: compose
- focal: equação MODELO + PLANEJAMENTO = PROCESSO
- roles: equação MODELO + PLANEJAMENTO = PROCESSO = herói · rótulos = apoio

narrativeRole: Modelo × processo.
keyMessage: equação MODELO + PLANEJAMENTO = PROCESSO.

Scene 1 (0.0–6.0s): cartão MODELO: TEÓRICO, POSSÍVEIS AÇÕES.
Scene 2 (6.0–12.0s): receita de bolo vira modelo; relógio, chapéu de cozinheiro e balança entram como PLANEJAMENTO.
Scene 3 (12.0–17.975s): equação final em blocos com '=' piscando.

## Frame 11 — Modelo cascata

- scene: Quatro modelos em fila; a cascata vira escada de seis degraus; bolinha desce degrau a degrau; seta de voltar riscada
- voiceover: "Agora os quatro modelos tradicionais. O primeiro é a cascata, o primeiro modelo publicado: uma sequência de passos em ordem. Requisitos, projeto, implementação, teste, implantação e manutenção. Macete: é uma escada que só desce. Terminou o degrau, não volta."
- duration: 15.717s
- transition_in: crossfade
- status: animated
- src: compositions/frames/11-cascata.html
- type: feature_showcase
- blueprint: compose
- focal: escada que só desce
- roles: escada que só desce = herói · rótulos = apoio

narrativeRole: Modelo cascata.
keyMessage: escada que só desce.

Scene 1 (0.0–5.2s): quatro rótulos: CASCATA, PROTOTIPAÇÃO, INCREMENTAL, ESPIRAL; foco na CASCATA.
Scene 2 (5.2–10.5s): seis degraus se montam: REQUISITOS → MANUTENÇÃO.
Scene 3 (10.5–15.717s): bolinha desce; seta de subir é riscada: NÃO VOLTA.

## Frame 12 — Cascata: prós e contras

- scene: Tabela PRÓS × CONTRAS da cascata; ícones: folha a cada degrau, organograma; contras: curva fora da escada, cliente com '?', cadeado
- voiceover: "Vantagens da cascata: documentação produzida em cada fase, e um fluxo muito organizado, fácil de gerenciar. Desvantagens: projetos reais raramente são sequenciais, o cliente tem dificuldade de dizer todos os requisitos no início, e há pouca flexibilidade para mudanças."
- duration: 15.627s
- transition_in: crossfade
- status: animated
- src: compositions/frames/12-cascata-vd.html
- type: benefit_highlight
- blueprint: comparison-split (Adapt)
- focal: tabela prós × contras
- roles: tabela prós × contras = herói · rótulos = apoio

narrativeRole: Cascata: prós e contras.
keyMessage: tabela prós × contras.

Scene 1 (0.0–5.2s): coluna VANTAGENS: DOCUMENTAÇÃO EM CADA FASE, ORGANIZADO E FÁCIL DE GERENCIAR.
Scene 2 (5.2–10.4s): coluna DESVANTAGENS: RARAMENTE SEQUENCIAL, CLIENTE NÃO SABE TUDO NO INÍCIO, POUCA FLEXIBILIDADE.
Scene 3 (10.4–15.627s): palavra-gancho: RÍGIDA.

## Frame 13 — Prototipação

- scene: Roda de cinco passos da prototipação; um rascunho de tela fica mais completo a cada volta
- voiceover: "A prototipação é um modelo evolucionário e iterativo: a cada volta, o software fica mais completo. São cinco passos em roda: comunicação, planejamento rápido, modelagem rápida, construção do protótipo, e entrega com feedback, que refina os requisitos. Macete: é o rascunho que o cliente testa."
- duration: 17.057s
- transition_in: crossfade
- status: animated
- src: compositions/frames/13-prototipacao.html
- type: feature_showcase
- blueprint: compose
- focal: rascunho que evolui a cada volta
- roles: rascunho que evolui a cada volta = herói · rótulos = apoio

narrativeRole: Prototipação.
keyMessage: rascunho que evolui a cada volta.

Scene 1 (0.0–5.7s): roda com COMUNICAÇÃO, PLANEJAMENTO RÁPIDO, MODELAGEM RÁPIDA, CONSTRUÇÃO, ENTREGA E FEEDBACK.
Scene 2 (5.7–11.4s): no centro, um wireframe ganha detalhes a cada volta (v1, v2, v3).
Scene 3 (11.4–17.057s): macete: RASCUNHO QUE O CLIENTE TESTA.

## Frame 14 — Prototipação: prós e contras

- scene: Prós × contras da prototipação com ícones: cifrão, documento rasgado, cliente apressado, contador ∞ de voltas
- voiceover: "Vantagens: é flexível, fica fácil detectar erros e funções que faltam, o usuário participa e o cliente fica mais satisfeito. Desvantagens: é caro, a documentação fica deficiente, o cliente pode exigir o produto logo depois de ver o protótipo, e ninguém sabe quantas voltas serão necessárias."
- duration: 17.353s
- transition_in: crossfade
- status: animated
- src: compositions/frames/14-prototipacao-vd.html
- type: benefit_highlight
- blueprint: comparison-split (Adapt)
- focal: prós × contras
- roles: prós × contras = herói · rótulos = apoio

narrativeRole: Prototipação: prós e contras.
keyMessage: prós × contras.

Scene 1 (0.0–5.8s): VANTAGENS: FLEXÍVEL, DETECTA ERROS, USUÁRIO PARTICIPA, CLIENTE SATISFEITO.
Scene 2 (5.8–11.6s): DESVANTAGENS: CARO, DOCUMENTAÇÃO DEFICIENTE, CLIENTE QUER O PRODUTO JÁ, Nº DE VOLTAS INCERTO.
Scene 3 (11.6–17.353s): palavra-gancho: FEEDBACK.

## Frame 15 — Modelo incremental

- scene: Pizza quadrada em fatias entregues uma a uma num gráfico tempo × funcionalidades; fatia 1 = NÚCLEO
- voiceover: "O incremental combina a cascata com a prototipação. Em vez de entregar tudo de uma vez, entrega pequenos pedaços. A primeira entrega é o núcleo do produto, e cada parte pronta se soma às outras. Macete: é pizza entregue fatia por fatia."
- duration: 13.791s
- transition_in: crossfade
- status: animated
- src: compositions/frames/15-incremental.html
- type: feature_showcase
- blueprint: compose
- focal: pizza fatia por fatia
- roles: pizza fatia por fatia = herói · rótulos = apoio

narrativeRole: Modelo incremental.
keyMessage: pizza fatia por fatia.

Scene 1 (0.0–4.6s): CASCATA + PROTOTIPAÇÃO = INCREMENTAL.
Scene 2 (4.6–9.2s): eixo tempo × funcionalidades: entregas 1, 2, 3 sobem em degraus; entrega 1 = NÚCLEO.
Scene 3 (9.2–13.791s): pizza (quadrada, estilo grade) recebe fatias uma a uma: FATIA POR FATIA.

## Frame 16 — Incremental: prós e contras

- scene: Prós × contras do incremental com módulos que se encaixam (e um que não encaixa)
- voiceover: "Vantagens: entrega rápida de funcionalidades, redução de riscos, flexibilidade, gerenciamento eficiente e controle de qualidade em cada módulo. Desvantagens: integrar os módulos é complexo e custa caro, é difícil estimar o tempo total, o cliente perde a visão geral, e mudanças geram retrabalho."
- duration: 17.274s
- transition_in: crossfade
- status: animated
- src: compositions/frames/16-incremental-vd.html
- type: benefit_highlight
- blueprint: comparison-split (Adapt)
- focal: prós × contras
- roles: prós × contras = herói · rótulos = apoio

narrativeRole: Incremental: prós e contras.
keyMessage: prós × contras.

Scene 1 (0.0–5.8s): VANTAGENS: ENTREGA RÁPIDA, MENOS RISCO, FLEXÍVEL, GERENCIAMENTO, QUALIDADE POR MÓDULO.
Scene 2 (5.8–11.5s): DESVANTAGENS: INTEGRAÇÃO COMPLEXA E CARA, TEMPO TOTAL DIFÍCIL, SEM VISÃO GERAL, RETRABALHO.
Scene 3 (11.5–17.274s): palavra-gancho: PARTES.

## Frame 17 — Modelo espiral

- scene: Espiral desenhada em quatro quadrantes O · R · D · P; selo BOEHM 1988; palavra RISCO no centro
- voiceover: "O espiral foi criado por Barry Boehm, em mil novecentos e oitenta e oito. A palavra-chave é risco: ele junta a iteração da prototipagem com o controle da cascata. Cada volta passa por quatro quadrantes. Macete: O, R, D, P. Objetivos, riscos, desenvolver e planejar a próxima fase."
- duration: 17.566s
- transition_in: crossfade
- status: animated
- src: compositions/frames/17-espiral.html
- type: feature_showcase
- blueprint: compose
- focal: espiral com quadrantes O R D P
- roles: espiral com quadrantes O R D P = herói · rótulos = apoio

narrativeRole: Modelo espiral.
keyMessage: espiral com quadrantes O R D P.

Scene 1 (0.0–5.9s): selo BARRY BOEHM · 1988; palavra-chave RISCO.
Scene 2 (5.9–11.7s): PROTOTIPAGEM (iteração) + CASCATA (controle) se fundem.
Scene 3 (11.7–17.566s): espiral se desenha passando por OBJETIVOS, RISCOS, DESENVOLVER, PLANEJAR.

## Frame 18 — Espiral: prós e contras

- scene: Prós × contras do espiral; contraste GRANDE PORTE × pequeno porte
- voiceover: "Vantagens: abordagem realista, reduz os riscos antes que virem problema, estimativas mais realistas, e não separa desenvolvimento de manutenção. Desvantagens: exige um analista experiente em riscos, é difícil convencer o cliente, e não serve para sistemas pequenos: é para grande porte."
- duration: 15.927s
- transition_in: crossfade
- status: animated
- src: compositions/frames/18-espiral-vd.html
- type: benefit_highlight
- blueprint: comparison-split (Adapt)
- focal: prós × contras
- roles: prós × contras = herói · rótulos = apoio

narrativeRole: Espiral: prós e contras.
keyMessage: prós × contras.

Scene 1 (0.0–5.3s): VANTAGENS: REALISTA, REDUZ RISCOS CEDO, ESTIMATIVAS REALISTAS, DESENVOLVIMENTO = MANUTENÇÃO.
Scene 2 (5.3–10.6s): DESVANTAGENS: ANALISTA EXPERIENTE, DIFÍCIL CONVENCER O CLIENTE, NÃO PARA SISTEMAS PEQUENOS.
Scene 3 (10.6–15.927s): prédio grande ✓ × casinha ✗: GRANDE PORTE.

## Frame 19 — Qual modelo escolher

- scene: Quatro situações → quatro modelos, como um quiz com setas
- voiceover: "E se a prova pedir para escolher o modelo? Requisitos claros e estáveis: cascata. Cliente não sabe direito o que quer: prototipação. Precisa entregar rápido, em partes: incremental. Sistema grande e cheio de risco: espiral."
- duration: 13.192s
- transition_in: crossfade
- status: animated
- src: compositions/frames/19-qual-modelo.html
- type: feature_showcase
- blueprint: grid-card-assemble (Adapt)
- focal: situação → modelo
- roles: situação → modelo = herói · rótulos = apoio

narrativeRole: Qual modelo escolher.
keyMessage: situação → modelo.

Scene 1 (0.0–4.4s): REQUISITOS CLAROS → CASCATA.
Scene 2 (4.4–8.8s): CLIENTE NÃO SABE → PROTOTIPAÇÃO; ENTREGAR RÁPIDO EM PARTES → INCREMENTAL.
Scene 3 (8.8–13.192s): GRANDE E ARRISCADO → ESPIRAL.

## Frame 20 — Cola final

- scene: Cola final em grade com ícones: PRQ, O QUE × COMO, MODELO + PLANEJAMENTO = PROCESSO, escada · rascunho · pizza · risco; BOA PROVA!
- voiceover: "Sua cola final. Crise de sessenta e oito: prazo, requisito e qualidade. Funcional é o quê, não funcional é como. Modelo mais planejamento é processo. E os modelos: cascata é escada, prototipação é rascunho, incremental é pizza, e espiral é risco. Boa prova!"
- duration: 16.829s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/20-cola.html
- type: branding
- blueprint: titlecard-reveal (Adapt)
- focal: cola em grade
- roles: cola em grade = herói · rótulos = apoio

narrativeRole: Cola final.
keyMessage: cola em grade.

Scene 1 (0.0–5.6s): título SUA COLA.
Scene 2 (5.6–11.2s): linhas da cola entram uma a uma com seus ícones.
Scene 3 (11.2–16.829s): BOA PROVA! sobe; parada final.
