import math
from fw import box, txt, arrow, stamp, question, title, procon, INK

FR = {}
C = lambda s: s.replace("INK", INK).replace("PAPER", "#F0EBDE")

PROCON_JS = """
          pop("#Pq", 0.05, { s: 0.9 });
          slide("#Phl", @vantagens-0.1, -60); slide("#Phr", @desvantagens-0.1, 60);
"""

# ---------------------------------------------------------------- 11
P = "f11-"
steps = ["REQUISITOS", "PROJETO", "IMPLEMENTAÇÃO", "TESTE", "IMPLANTAÇÃO", "MANUTENÇÃO"]
sh = ""
for i, s in enumerate(steps):
    x, y = 170 + i * 250, 320 + i * 86
    sh += box(P, f"s{i}", s, x, y, 240, 72, fs=26)
    if i < 5:
        sh += f'<div class="{P}elb" id="{P}e{i}" style="left:{x + 240}px;top:{y + 34}px"></div>'
tabs = ""
for i, t in enumerate(["CASCATA", "PROTOTIPAÇÃO", "INCREMENTAL", "ESPIRAL"]):
    tabs += box(P, f"t{i}", t, 260 + i * 360, 200, 340, 64, fs=28)
FR[11] = ("cascata", C("""
.Pelb { position:absolute; width:22px; height:52px; border-top:5px solid INK; border-right:5px solid INK; box-sizing:border-box; }
.Pball { position:absolute; left:262px; top:276px; width:44px; height:44px; background:INK; }
.Pup { position:absolute; left:640px; top:820px; width:260px; height:6px; background:INK; transform-origin:0% 50%; }
.Pupx { position:absolute; left:380px; top:610px; font-family:"Newsreader", serif; font-size:180px; line-height:1; }
"""), f"""
      {title(P, "Os 4 modelos tradicionais")}
      {tabs}
      {sh}
      {txt(P, "pub", "1º MODELO PUBLICADO", 1180, 300, 30, font="mono", w=560, align="center")}
      <div class="{P}ball" id="{P}ball"></div>
      {stamp(P, "mac", "escada que só desce", 1050, 430, fs=54)}
      <div class="{P}up" id="{P}up"></div>
      <div class="{P}upx" id="{P}upx">×</div>
      {box(P, "nv", "NÃO VOLTA", 160, 520, 300, 80, fs=34, inv=True, fill=False)}
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          for (let i = 0; i < 4; i++) pop("#Pt" + i, @quatro+i*0.15);
          lit("#Pt0", @cascata); bump("#Pt0", @cascata, 1.08);
          fade("#Ppub", @publicado-0.3);
          const stt = [@requisitos, @projeto, @implementação, @teste, @implantação, @manutenção];
          stt.forEach((t, i) => { slide("#Ps" + i, t - 0.15, -40, { d: 0.4 }); if (i > 0) drawY("#Pe" + (i - 1), t - 0.3, 0.25); });
          fade("#Pball", @macete);
          stampIn("#Pmac", @macete+0.2, -2);
          // ball hops down every step
          for (let i = 1; i < 6; i++) {
            const t = @desce + (i - 1) * 0.42;
            tl.to(q("#Pball"), { x: i * 250, duration: 0.3, ease: "power1.inOut" }, t);
            tl.to(q("#Pball"), { y: i * 86, duration: 0.3, ease: "bounce.out" }, t + 0.06);
          }
          tl.fromTo(q("#Pup"), { scaleX: 0, rotation: 212 }, { scaleX: 1, rotation: 212, duration: 0.4, ease: "power3.out" }, @volta-0.8);
          tl.fromTo(q("#Pupx"), { opacity: 0, scale: 2 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.in" }, @volta-0.3);
          stampIn("#Pnv", @volta, 2);
""")

# ---------------------------------------------------------------- 12
P = "f12-"
FR[12] = ("cascata-vd", "", f"""
      {title(P, "Cascata: prós e contras")}
      {procon(P, [("l0", "≡", "Documentação em cada fase"), ("l1", "#", "Organizado e fácil de gerenciar")],
                 [("r0", "~", "Projetos raramente são sequenciais"), ("r1", "?", "Cliente não sabe tudo no início"), ("r2", "×", "Pouca flexibilidade")],
                 y0=340, gap=110).replace("≡", "1")}
      {stamp(P, "hook", "organizada, porém rígida", 470, 720, fs=56, tag="GANCHO")}
""", PROCON_JS + """
          slide("#Pl0", @documentação, -60); slide("#Pl1", @organizado, -60);
          slide("#Pr0", @raramente, 60); slide("#Pr1", @dificuldade, 60); slide("#Pr2", @flexibilidade, 60);
          stampIn("#Phook", @mudanças, -2);
""")

# ---------------------------------------------------------------- 13
P = "f13-"
cx, cy, rx, ry = 960, 500, 520, 240
ring = ""
names = ["COMUNICAÇÃO", "PLANEJAMENTO<br>RÁPIDO", "MODELAGEM<br>RÁPIDA", "CONSTRUÇÃO DO<br>PROTÓTIPO", "ENTREGA E<br>FEEDBACK"]
pos = []
for i in range(5):
    a = math.radians(-90 + 72 * i)
    x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
    pos.append((round(x), round(y)))
    ring += box(P, f"n{i}", names[i], round(x - 170), round(y - 54), 340, 108, fs=26)
FR[13] = ("prototipacao", C("""
.Pwire { position:absolute; left:790px; top:380px; width:340px; height:230px; border:5px solid INK; background:PAPER; box-sizing:border-box; }
.Pw { position:absolute; background:INK; }
.Pwd { position:absolute; border:3px dashed INK; box-sizing:border-box; }
.Pver { position:absolute; left:790px; top:330px; width:340px; text-align:center; font-family:"DM Mono", monospace; font-size:30px; letter-spacing:0.1em; }
.Pdotm { position:absolute; width:30px; height:30px; background:INK; margin:-15px 0 0 -15px; }
"""), f"""
      {title(P, "Prototipação", tag="EVOLUCIONÁRIO · ITERATIVO")}
      {ring}
      <div class="{P}wire" id="{P}wire">
        <div class="{P}w" id="{P}w1" style="left:0;right:0;top:0;height:34px"></div>
        <div class="{P}wd" id="{P}w2" style="left:16px;top:52px;width:90px;height:150px"></div>
        <div class="{P}w" id="{P}w3" style="left:124px;top:56px;width:180px;height:12px"></div>
        <div class="{P}w" id="{P}w4" style="left:124px;top:82px;width:140px;height:12px"></div>
        <div class="{P}wd" id="{P}w5" style="left:124px;top:110px;width:180px;height:60px"></div>
        <div class="{P}w" id="{P}w6" style="left:204px;top:180px;width:100px;height:28px"></div>
      </div>
      <div class="{P}ver" id="{P}ver"><span id="{P}v1">v1</span><span id="{P}v2" style="position:absolute;left:0;right:0">v2</span><span id="{P}v3" style="position:absolute;left:0;right:0">v3</span></div>
      <div class="{P}dotm" id="{P}dot" style="left:{pos[0][0] + 196}px;top:{pos[0][1]}px"></div>
      {stamp(P, "mac", "o rascunho que o cliente testa", 520, 790, fs=50)}
""", f"""
          pop("#Pq", 0.05, {{ s: 0.9 }});
          pop("#Pwire", @evolucionário, {{ s: 0.8 }});
          ["#Pw2", "#Pw3", "#Pw4", "#Pw5", "#Pw6"].forEach((s) => tl.set(q(s), {{ opacity: 0 }}, 0));
          tl.set(qa("#Pv2, #Pv3"), {{ opacity: 0 }}, 0);
          fade("#Pver", @volta);
          const nt = [@comunicação, @planejamento, @modelagem, @construção, @entrega];
          nt.forEach((t, i) => pop("#Pn" + i, t));
          fade("#Pdot", @comunicação);
          const P5 = {[[x + 196, y] for (x, y) in pos]};
          // dot runs around the ring once per spoken step, then a fast lap at the feedback
          nt.forEach((t, i) => {{ if (i > 0) tl.to(q("#Pdot"), {{ x: P5[i][0] - P5[0][0], y: P5[i][1] - P5[0][1], duration: 0.35, ease: "power2.inOut" }}, t - 0.2); lit("#Pn" + i, t + 0.1, 0.3); }});
          tl.to(q("#Pdot"), {{ x: 0, y: 0, duration: 0.35, ease: "power2.inOut" }}, @refina);
          // the sketch grows each lap
          tl.to(qa("#Pw2, #Pw3"), {{ opacity: 1, duration: 0.3 }}, @completo);
          tl.to(q("#Pv1"), {{ opacity: 0, duration: 0.2 }}, @completo); tl.to(q("#Pv2"), {{ opacity: 1, duration: 0.2 }}, @completo);
          tl.to(qa("#Pw4, #Pw5"), {{ opacity: 1, duration: 0.3 }}, @feedback);
          tl.to(q("#Pv2"), {{ opacity: 0, duration: 0.2 }}, @refina); tl.to(q("#Pv3"), {{ opacity: 1, duration: 0.2 }}, @refina);
          tl.to(q("#Pw6"), {{ opacity: 1, duration: 0.3 }}, @refina+0.3);
          bump("#Pwire", @refina+0.3, 1.06);
          stampIn("#Pmac", @rascunho, -2);
""")

# ---------------------------------------------------------------- 14
P = "f14-"
FR[14] = ("prototipacao-vd", "", f"""
      {title(P, "Prototipação: prós e contras")}
      {procon(P, [("l0", "~", "Flexível"), ("l1", "!", "Fácil detectar erros e faltas"), ("l2", "+", "Usuário participa"), ("l3", "=", "Cliente mais satisfeito")],
                 [("r0", "$", "Caro"), ("r1", "–", "Documentação deficiente"), ("r2", "!", "Cliente quer o produto já"), ("r3", "?", "Nº de voltas incerto")],
                 y0=340, gap=118)}
      {txt(P, "foot", "gancho: muito FEEDBACK, pouca DOCUMENTAÇÃO", 150, 830, 30, font="mono", w=1620, align="center")}
""", PROCON_JS + """
          slide("#Pl0", @flexível, -60); slide("#Pl1", @erros, -60); slide("#Pl2", @participa, -60); slide("#Pl3", @satisfeito, -60);
          slide("#Pr0", @caro, 60); slide("#Pr1", @deficiente, 60); slide("#Pr2", @exigir, 60); slide("#Pr3", @voltas, 60);
          fade("#Pfoot", @voltas+0.6);
""")

# ---------------------------------------------------------------- 15
P = "f15-"
FR[15] = ("incremental", C("""
.Pax { position:absolute; background:INK; }
.Pbar { position:absolute; width:150px; border:4px solid INK; border-bottom:none; box-sizing:border-box; background:PAPER; transform-origin:50% 100%; display:flex; align-items:flex-start; justify-content:center; padding-top:10px; font-family:"DM Mono", monospace; font-size:28px; }
.Pbar.Pinv { background:INK; color:PAPER; }
.Ppz { position:absolute; left:1180px; top:400px; width:440px; height:440px; border:5px dashed rgba(31,43,224,0.5); box-sizing:border-box; }
.Psl { position:absolute; width:212px; height:212px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Newsreader", serif; font-size:90px; border:4px solid PAPER; box-sizing:border-box; }
.Pall { position:absolute; left:870px; top:390px; width:240px; height:120px; border:4px solid INK; box-sizing:border-box; display:flex; align-items:center; justify-content:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:28px; letter-spacing:0.08em; background:PAPER; }
.Pstrike { position:absolute; left:850px; top:476px; width:280px; height:8px; background:INK; transform-origin:0% 50%; }
"""), f"""
      {box(P, "eq1", "CASCATA", 240, 200, 340, 80, fs=32)}
      {txt(P, "pl", "+", 600, 188, 90)}
      {box(P, "eq2", "PROTOTIPAÇÃO", 670, 200, 420, 80, fs=32)}
      {txt(P, "eqs", "=", 1110, 188, 90)}
      {box(P, "eq3", "INCREMENTAL", 1190, 200, 480, 80, fs=36, inv=True, fill=False)}
      <div class="{P}ax" id="{P}axy" style="left:200px;top:340px;width:6px;height:500px;transform-origin:50% 100%"></div>
      <div class="{P}ax" id="{P}axx" style="left:200px;top:834px;width:920px;height:6px;transform-origin:0% 50%"></div>
      {txt(P, "lx", "TEMPO", 980, 850, 26, font="mono")}
      {txt(P, "ly", "FUNÇÕES", 220, 330, 26, font="mono")}
      <div class="{P}bar {P}inv" id="{P}b1" style="left:260px;top:684px;height:150px">1</div>
      <div class="{P}bar" id="{P}b2" style="left:450px;top:574px;height:260px">2</div>
      <div class="{P}bar" id="{P}b3" style="left:640px;top:464px;height:370px">3</div>
      {txt(P, "nuc", "NÚCLEO", 236, 630, 28, font="lab", extra="font-weight:600;letter-spacing:0.12em;")}
      <div class="{P}all" id="{P}all">TUDO DE<br>UMA VEZ</div><div class="{P}strike" id="{P}stk"></div>
      <div class="{P}pz" id="{P}pz"></div>
      <div class="{P}sl" id="{P}z1" style="left:1188px;top:408px">1</div>
      <div class="{P}sl" id="{P}z2" style="left:1400px;top:408px">2</div>
      <div class="{P}sl" id="{P}z3" style="left:1188px;top:620px">3</div>
      <div class="{P}sl" id="{P}z4" style="left:1400px;top:620px">4</div>
      {stamp(P, "mac", "fatia por fatia", 1210, 316, fs=48)}
""", """
          pop("#Peq3", @incremental, { s: 0.8 });
          pop("#Peq1", @cascata); pop("#Ppl", @cascata+0.2);
          pop("#Peq2", @prototipação); pop("#Peqs", @prototipação+0.2);
          drawY("#Paxy", @vez-0.8, 0.5); drawX("#Paxx", @vez-0.6, 0.6); fade("#Plx", @vez-0.4); fade("#Ply", @vez-0.4);
          pop("#Pall", @tudo); tl.fromTo(q("#Pstk"), { scaleX: 0, rotation: -14 }, { scaleX: 1, rotation: -14, duration: 0.3, ease: "power3.out" }, @pequenos-0.2);
          drawY("#Pb1", @primeira, 0.5); rise("#Pnuc", @núcleo);
          drawY("#Pb2", @soma-0.3, 0.5); drawY("#Pb3", @soma+0.1, 0.5);
          fade("#Ppz", @soma);
          const sl = [["#Pz1", -300, -200], ["#Pz2", 300, -200], ["#Pz3", -300, 200], ["#Pz4", 300, 200]];
          sl.forEach(([s, dx, dy], i) => tl.fromTo(q(s), { opacity: 0, x: dx, y: dy, rotation: 20 }, { opacity: 1, x: 0, y: 0, rotation: 0, duration: 0.45, ease: "back.out(1.4)" }, @pizza + i * 0.42));
          stampIn("#Pmac", @fatia, -2);
""")

# ---------------------------------------------------------------- 16
P = "f16-"
FR[16] = ("incremental-vd", "", f"""
      {title(P, "Incremental: prós e contras")}
      {procon(P, [("l0", "»", "Entrega rápida"), ("l1", "–", "Menos riscos"), ("l2", "~", "Flexível"), ("l3", "#", "Gerenciamento eficiente"), ("l4", "=", "Qualidade em cada módulo")],
                 [("r0", "+", "Integração complexa e cara"), ("r1", "?", "Tempo total difícil de estimar"), ("r2", "×", "Cliente sem visão geral"), ("r3", "!", "Mudanças geram retrabalho")],
                 y0=330, gap=104).replace("»", "1")}
""", PROCON_JS + """
          slide("#Pl0", @rápida, -60); slide("#Pl1", @riscos, -60); slide("#Pl2", @flexibilidade, -60); slide("#Pl3", @gerenciamento, -60); slide("#Pl4", @qualidade, -60);
          slide("#Pr0", @integrar, 60); slide("#Pr1", @estimar, 60); slide("#Pr2", @visão, 60); slide("#Pr3", @retrabalho, 60);
""")

# ---------------------------------------------------------------- 17
P = "f17-"
# Archimedean spiral in a 760x560 box centred on (380, 280)
pts = []
N = 400
for k in range(N + 1):
    th = k / N * 3.2 * 2 * math.pi
    r = 8 + 75 * th / (2 * math.pi)
    pts.append((380 + r * math.cos(th) * 1.25, 280 + r * math.sin(th) * 0.95))
path = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
L = sum(math.dist(pts[i], pts[i + 1]) for i in range(N))
quads = [("O", "OBJETIVOS", 1010, 250), ("R", "RISCOS", 1610, 250), ("D", "DESENVOLVER", 1610, 720), ("P", "PLANEJAR", 1010, 720)]
qh = ""
for i, (L1, lab, x, y) in enumerate(quads):
    qh += box(P, f"q{i}", L1, x, y, 96, 96, fs=64, font="serif")
    qh += txt(P, f"ql{i}", lab, x - 40 if i in (0, 3) else x - 80, y + 104, 26, font="lab", w=240, align="center", extra="font-weight:600;letter-spacing:0.08em;")
FR[17] = ("espiral", C("""
.Psv { position:absolute; left:1000px; top:250px; width:760px; height:560px; overflow:visible; }
.Psv path { fill:none; stroke:INK; stroke-width:6; stroke-linecap:square; }
.Paxh { position:absolute; left:960px; top:528px; width:840px; height:4px; background:rgba(31,43,224,0.55); transform-origin:50% 50%; }
.Paxv { position:absolute; left:1378px; top:220px; width:4px; height:620px; background:rgba(31,43,224,0.55); transform-origin:50% 50%; }
.Pseal { position:absolute; left:160px; top:230px; width:640px; height:150px; border:5px solid INK; background:PAPER; box-sizing:border-box; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px; }
.Pseal b { font-family:"Newsreader", serif; font-weight:400; font-size:62px; line-height:1; }
.Pseal span { font-family:"DM Mono", monospace; font-size:30px; letter-spacing:0.16em; }
"""), f"""
      {title(P, "Modelo espiral")}
      <div class="{P}seal" id="{P}seal"><b>Barry Boehm</b><span id="{P}yr">1988</span></div>
      {stamp(P, "risk", "RISCO", 330, 440, fs=110, tag="PALAVRA-CHAVE")}
      {box(P, "it", "ITERAÇÃO DA<br>PROTOTIPAGEM", 160, 660, 300, 120, fs=26)}
      {txt(P, "plus", "+", 482, 664, 90, extra="z-index:2;")}
      {box(P, "ct", "CONTROLE DA<br>CASCATA", 550, 660, 300, 120, fs=26)}
      <div class="{P}axh" id="{P}axh"></div><div class="{P}axv" id="{P}axv"></div>
      <svg class="{P}sv" viewBox="0 0 760 560"><path id="{P}sp" d="{path}" stroke-dasharray="{L:.0f}" stroke-dashoffset="{L:.0f}"/></svg>
      {qh}
""", f"""
          pop("#Pq", 0.05, {{ s: 0.9 }});
          pop("#Pseal", @boehm); tl.fromTo(q("#Pyr"), {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, @mil);
          stampIn("#Prisk", @risco, -3);
          pop("#Pit", @iteração); pop("#Pplus", @controle-0.2); pop("#Pct", @controle);
          bump("#Pit", @volta-0.6, 1.06); bump("#Pct", @volta-0.5, 1.06);
          drawX("#Paxh", @volta-0.4, 0.5); drawY("#Paxv", @volta-0.4, 0.5);
          tl.fromTo(q("#Psp"), {{ strokeDashoffset: {L:.0f} }}, {{ strokeDashoffset: 0, duration: D - @volta, ease: "none" }}, @volta);
          const ql = [@r-0.35, @r, @d, @p];
          ql.forEach((t, i) => pop("#Pq" + i, t, {{ s: 0.4 }}));
          const lw = [@objetivos, @riscos, @desenvolver, @planejar];
          lw.forEach((t, i) => {{ lit("#Pq" + i, t); rise("#Pql" + i, t); }});
          shake(@planejar+0.3);
""")

# ---------------------------------------------------------------- 18
P = "f18-"
FR[18] = ("espiral-vd", C("""
.Pbig { position:absolute; left:1140px; top:690px; width:90px; height:170px; border:5px solid INK; box-sizing:border-box; background:PAPER;
  background-image: repeating-linear-gradient(0deg, transparent 0 18px, INK 18px 26px); background-size:50px 100%; background-repeat:no-repeat; background-position:15px 0; }
.Psmall { position:absolute; left:1540px; top:790px; width:80px; height:70px; border:5px solid INK; box-sizing:border-box; background:PAPER; }
.Pnox { position:absolute; left:1530px; top:720px; font-family:"Newsreader", serif; font-size:150px; line-height:1; }
"""), f"""
      {title(P, "Espiral: prós e contras")}
      {procon(P, [("l0", "=", "Abordagem realista"), ("l1", "–", "Reduz riscos antes do problema"), ("l2", "#", "Estimativas mais realistas"), ("l3", "+", "Não separa desenv. e manutenção")],
                 [("r0", "!", "Exige analista experiente"), ("r1", "?", "Difícil convencer o cliente"), ("r2", "×", "Não serve para sistemas pequenos")],
                 y0=330, gap=104)}
      <div class="{P}big" id="{P}big"></div>
      {box(P, "gp", "GRANDE PORTE", 1250, 740, 260, 80, fs=28, inv=True, fill=False)}
      <div class="{P}small" id="{P}sm"></div><div class="{P}nox" id="{P}nox">×</div>
""", PROCON_JS + """
          slide("#Pl0", @realista, -60); slide("#Pl1", @reduz, -60); slide("#Pl2", @estimativas, -60); slide("#Pl3", @separa, -60);
          slide("#Pr0", @analista, 60); slide("#Pr1", @convencer, 60); slide("#Pr2", @pequenos, 60);
          pop("#Psm", @pequenos+0.2); tl.fromTo(q("#Pnox"), { opacity: 0, scale: 2 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.in" }, @pequenos+0.5);
          drawY("#Pbig", @grande-0.2, 0.5); stampIn("#Pgp", @grande, -2);
""")

# ---------------------------------------------------------------- 19
P = "f19-"
sit = ["Requisitos claros e estáveis", "Cliente não sabe o que quer", "Entregar rápido, em partes", "Sistema grande e arriscado"]
mod = ["CASCATA", "PROTOTIPAÇÃO", "INCREMENTAL", "ESPIRAL"]
icn = ['<i style="left:12px;top:12px;width:22px;height:12px"></i><i style="left:30px;top:30px;width:22px;height:12px"></i><i style="left:48px;top:48px;width:22px;height:12px"></i>',
       '<i style="left:10px;top:10px;width:64px;height:10px"></i><u style="left:10px;top:28px;width:24px;height:44px"></u><u style="left:40px;top:28px;width:34px;height:20px"></u>',
       '<i style="left:10px;top:10px;width:30px;height:30px"></i><i style="left:44px;top:10px;width:30px;height:30px"></i><i style="left:10px;top:44px;width:30px;height:30px"></i><u style="left:44px;top:44px;width:30px;height:30px"></u>',
       '<svg viewBox="0 0 84 84" style="position:absolute;inset:0"><path d="M42,42 L48,42 L48,50 L34,50 L34,32 L58,32 L58,60 L24,60 L24,22 L68,22 L68,70 L14,70 L14,12" fill="none" stroke="#1F2BE0" stroke-width="5"/></svg>']
r19 = ""
for i in range(4):
    y = 230 + i * 160
    r19 += box(P, f"s{i}", sit[i], 160, y, 820, 120, fs=40, font="body", fill=False)
    r19 += arrow(P, f"a{i}", 1000, y + 58, 120)
    r19 += f'<div class="{P}mi" id="{P}i{i}" style="left:1150px;top:{y + 18}px">{icn[i]}</div>'
    r19 += box(P, f"m{i}", mod[i], 1260, y, 500, 120, fs=40)
FR[19] = ("qual-modelo", C("""
.Pmi { position:absolute; width:84px; height:84px; }
.Pmi i { position:absolute; background:INK; }
.Pmi u { position:absolute; border:3px dashed INK; box-sizing:border-box; }
"""), f"""
      {question(P, "Qual modelo escolher?")}
      {r19}
""", """
          pop("#Pq", 0.05, { s: 0.85 });
          const st = [@claros, @sabe, @rápido, @grande];
          const mt = [@cascata, @prototipação, @incremental, @espiral];
          st.forEach((t, i) => slide("#Ps" + i, t - 0.3, -60));
          mt.forEach((t, i) => { drawX("#Pa" + i, t - 0.35, 0.3); pop("#Pi" + i, t - 0.1); pop("#Pm" + i, t); lit("#Pm" + i, t + 0.15); });
          shake(@espiral+0.4);
""")

# ---------------------------------------------------------------- 20
P = "f20-"
left = [("k0", "CRISE DE 68", "P · R · Q"), ("k1", "REQUISITOS", "o quê × como"), ("k2", "MODELO + PLANEJ.", "= processo")]
right = [("k3", "CASCATA", "escada"), ("k4", "PROTOTIPAÇÃO", "rascunho"), ("k5", "INCREMENTAL", "pizza"), ("k6", "ESPIRAL", "risco")]
ch = ""
for i, (id, a, b) in enumerate(left):
    y = 220 + i * 170
    ch += f'<div class="{P}ck" id="{P}{id}" style="left:150px;top:{y}px;width:820px;height:150px"><span class="{P}ca">{a}</span><span class="{P}cb" id="{P}{id}b">{b}</span></div>'
for i, (id, a, b) in enumerate(right):
    y = 220 + i * 126
    ch += f'<div class="{P}ck" id="{P}{id}" style="left:1010px;top:{y}px;width:760px;height:110px"><span class="{P}ca">{a}</span><span class="{P}cb" id="{P}{id}b">{b}</span></div>'
FR[20] = ("cola", C("""
.Pck { position:absolute; border:4px solid INK; background:PAPER; box-sizing:border-box; display:flex; align-items:center; justify-content:space-between; padding:0 30px; }
.Pca { font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:30px; letter-spacing:0.1em; white-space:nowrap; }
.Pcb { background:INK; color:PAPER; padding:6px 22px 10px; font-family:"Newsreader", serif; font-size:52px; line-height:1.05; white-space:nowrap; }
.Pbye { position:absolute; left:0; right:0; top:752px; text-align:center; font-family:"Newsreader", serif; font-size:110px; line-height:1; font-style:italic; }
"""), f"""
      {title(P, "Sua cola final", tag="REVISE ANTES DA PROVA")}
      {ch}
      <div class="{P}bye" id="{P}bye">Boa prova!</div>
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          const kt = [@crise, @funcional, @modelo, @cascata, @prototipação, @incremental, @espiral];
          kt.forEach((t, i) => { slide("#Pk" + i, t - 0.25, i < 3 ? -60 : 60); tl.fromTo(q("#Pk" + i + "b"), { opacity: 0, scale: 1.7 }, { opacity: 1, scale: 1, duration: 0.35, ease: "power4.in" }, t + 0.25); });
          tl.fromTo(q("#Pbye"), { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.9, ease: "power3.out" }, @boa);
""")
