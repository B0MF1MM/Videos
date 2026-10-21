from fw import box, txt, arrow, stamp, question, title, procon, INK

FR = {}

# ---------------------------------------------------------------- 01
P = "f01-"
FR[1] = ("prova-amanha", """
.Pcal { position:absolute; left:210px; top:190px; width:350px; height:380px; border:5px solid INK; background:PAPER; }
.Pcal-top { position:absolute; left:0; right:0; top:0; height:82px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"DM Mono", monospace; font-size:32px; letter-spacing:0.18em; }
.Pcal-ring { position:absolute; top:-26px; width:16px; height:46px; background:INK; }
.Pcal-day { position:absolute; left:0; right:0; top:110px; text-align:center; font-family:"Newsreader", serif; font-size:150px; line-height:1; }
.Pcal-word { position:absolute; left:30px; right:30px; top:282px; height:68px; }
.Ptitle1, .Ptitle2 { position:absolute; left:660px; font-family:"Newsreader", serif; font-size:132px; line-height:1; white-space:nowrap; letter-spacing:-0.02em; }
.Ptitle1 { top:196px; } .Ptitle2 { top:332px; font-style:italic; }
.Pbreath { position:absolute; left:668px; top:494px; display:flex; align-items:center; gap:22px; font-family:"DM Mono", monospace; font-size:32px; letter-spacing:0.2em; }
.Pbsq { width:34px; height:34px; border:4px solid INK; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      <div class="{P}cal" id="{P}cal">
        <div class="{P}cal-ring" style="left:70px"></div><div class="{P}cal-ring" style="left:264px"></div>
        <div class="{P}cal-top">PROVA</div>
        <div class="{P}cal-day">!</div>
        {box(P, "amanha", "AMANHÃ", 30, 282, 280, 68, fs=34, cls=P + "cal-word")}
      </div>
      <div class="{P}title1" id="{P}t1">Engenharia</div>
      <div class="{P}title2" id="{P}t2">de Software</div>
      <div class="{P}breath" id="{P}br"><div class="{P}bsq" id="{P}bsq"></div>RESPIRA.</div>
      {box(P, "c1", "PERGUNTA", 230, 640, 420, 130, fs=40)}
      {arrow(P, "a1", 664, 703, 74)}
      {box(P, "c2", "RESPOSTA", 750, 640, 420, 130, fs=40)}
      {arrow(P, "a2", 1184, 703, 74)}
      {box(P, "c3", "MACETE", 1270, 640, 420, 130, fs=40)}
""", """
          tl.fromTo(q("#Pcal"), { opacity: 0, y: -260, rotation: -8 }, { opacity: 1, y: 0, rotation: -2, duration: 0.8, ease: "bounce.out" }, 0.05);
          lit("#Pamanha", @amanhã);
          bump("#Pcal", @amanhã+0.2, 1.05);
          wipe("#Pt1", @engenharia, 0.7);
          wipe("#Pt2", @software, 0.7);
          rise("#Pbr", @respira);
          tl.to(q("#Pbsq"), { scale: 1.35, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: 3 }, @respira+0.1);
          pop("#Pc1", @pergunta); drawX("#Pa1", @resposta-0.3, 0.3);
          pop("#Pc2", @resposta); drawX("#Pa2", @macete-0.3, 0.3);
          pop("#Pc3", @macete); lit("#Pc3", @macete+0.3);
          shake(@macete+0.35);
          bump("#Pc1", @esquecer-0.6, 1.05); bump("#Pc2", @esquecer-0.4, 1.05); bump("#Pc3", @esquecer-0.2, 1.08);
""")

# ---------------------------------------------------------------- 02
P = "f02-"
gears = ""
for i, gx in enumerate((620, 900, 1180)):
    gears += f'<div class="{P}gear" id="{P}g{i}" style="left:{gx}px"><i></i><i class="{P}r"></i></div>'
meters = ""
for i, (lab, sign) in enumerate((("QUALIDADE", "+"), ("PRAZO", "–"), ("CUSTO", "–"))):
    x = 230 + i * 330
    meters += (f'<div class="{P}meter" id="{P}m{i}" style="left:{x}px"><div class="{P}bar" id="{P}b{i}"></div></div>'
               f'<div class="{P}msign" id="{P}s{i}" style="left:{x}px">{sign}</div>'
               f'<div class="{P}mlab" id="{P}l{i}" style="left:{x - 20}px">{lab}</div>')
FR[2] = ("o-que-e", """
.Pruler { position:absolute; left:300px; top:390px; width:1320px; height:6px; background:INK; transform-origin:0% 50%; }
.Ptick { position:absolute; top:376px; width:4px; height:34px; background:INK; }
.Pgear { position:absolute; top:330px; width:120px; height:120px; }
.Pgear i { position:absolute; inset:18px; border:8px solid INK; background:PAPER; box-sizing:border-box; }
.Pgear i.Pr { transform:rotate(45deg); }
.Paspect { position:absolute; left:0; right:0; top:262px; text-align:center; font-family:"DM Mono", monospace; font-size:28px; letter-spacing:0.16em; }
.Pmeter { position:absolute; top:560px; width:180px; height:250px; border:4px solid INK; box-sizing:border-box; background:PAPER; }
.Pbar { position:absolute; left:10px; right:10px; bottom:10px; height:226px; background:INK; transform-origin:50% 100%; }
.Pmsign { position:absolute; top:488px; width:180px; text-align:center; font-family:"Newsreader", serif; font-size:84px; line-height:0.8; }
.Pmlab { position:absolute; top:822px; width:220px; text-align:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:28px; letter-spacing:0.1em; }
.Pcb { position:absolute; left:1240px; top:560px; width:480px; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {question(P, "O que é Engenharia de Software?")}
      <div class="{P}aspect" id="{P}asp">TODOS OS ASPECTOS DA PRODUÇÃO</div>
      {box(P, "esp", "ESPECIFICAÇÃO", 110, 350, 300, 86, fs=28)}
      <div class="{P}ruler" id="{P}ruler"></div>
      {gears}
      {box(P, "man", "MANUTENÇÃO", 1510, 350, 300, 86, fs=28)}
      {meters}
      {box(P, "cb", "CUSTO-BENEFÍCIO", 1240, 560, 480, 100, fs=34, inv=True, fill=False)}
      {txt(P, "cbt", "+ – –", 1240, 680, 120, w=480, align="center")}
      {txt(P, "cbs", "mais qualidade, menos prazo, menos custo", 1210, 830, 26, font="mono", w=540, align="center")}
""", """
          pop("#Pq", 0.1, { s: 0.85 });
          rise("#Pasp", @disciplina);
          pop("#Pesp", @especificação);
          drawX("#Pruler", @especificação+0.2, 1.6);
          ["#Pg0", "#Pg1", "#Pg2"].forEach((g, i) => {
            pop(g, @todos+i*0.2);
            tl.fromTo(q(g), { rotation: 0 }, { rotation: (i % 2 ? -1 : 1) * 360, duration: D - @todos, ease: "none" }, @todos);
          });
          pop("#Pman", @manutenção);
          lit("#Pesp", @manutenção+0.4); lit("#Pman", @manutenção+0.6);
          ["0", "1", "2"].forEach((k, i) => { fade("#Pm" + k, @objetivo+i*0.12); fade("#Pl" + k, @objetivo+i*0.12); });
          tl.set(qa("#Pb0, #Pb1, #Pb2"), { scaleY: 0.5 }, 0);
          pop("#Pcb", @custo-benefício, { s: 0.8 });
          tl.to(q("#Pb0"), { scaleY: 1, duration: 0.8, ease: "back.out(1.6)" }, @qualidade);
          pop("#Ps0", @qualidade);
          tl.to(q("#Pb1"), { scaleY: 0.18, duration: 0.8, ease: "power3.out" }, @prazo);
          pop("#Ps1", @prazo);
          tl.to(q("#Pb2"), { scaleY: 0.18, duration: 0.8, ease: "power3.out" }, @custo);
          pop("#Ps2", @custo);
          stampIn("#Pcbt", @custo+0.3, 0);
          fade("#Pcbs", @custo+0.6);
""")

# ---------------------------------------------------------------- 03
P = "f03-"
papers = ""
for i, (dx, dy, r) in enumerate(((0, 0, -12), (40, 18, 9), (-30, 34, 20), (60, -10, -24), (14, 50, 4))):
    papers += f'<div class="{P}paper" id="{P}p{i}" data-r="{r}" style="left:{250 + dx}px;top:{430 + dy}px;"><i></i><i></i><i></i></div>'
prq = ""
for i, (L, lab) in enumerate((("P", "PRAZO<br>ESTOURADO"), ("R", "REQUISITO<br>IGNORADO"), ("Q", "QUALIDADE<br>BAIXA"))):
    x = 340 + i * 460
    prq += box(P, f"L{i}", L, x, 560, 210, 190, fs=150, font="serif", fill=True)
    prq += txt(P, f"W{i}", lab, x - 60, 770, 32, font="lab", w=330, align="center", extra="white-space:normal;font-weight:600;letter-spacing:0.08em;")
FR[3] = ("crise", """
.Pline { position:absolute; left:160px; top:360px; width:1600px; height:5px; background:INK; transform-origin:0% 50%; }
.Pdot { position:absolute; top:344px; width:36px; height:36px; background:INK; }
.Ppaper { position:absolute; width:96px; height:120px; border:4px solid INK; background:PAPER; box-sizing:border-box; padding:16px 12px; display:flex; flex-direction:column; gap:12px; }
.Ppaper i { display:block; height:5px; background:INK; }
.Pyear { position:absolute; left:820px; top:226px; width:280px; text-align:center; font-family:"Newsreader", serif; font-size:100px; line-height:1; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {title(P, "Por que surgiu?", tag="A CRISE DO SOFTWARE")}
      <div class="{P}line" id="{P}line"></div>
      <div class="{P}dot" id="{P}d1" style="left:330px"></div>
      <div class="{P}dot" id="{P}d2" style="left:942px"></div>
      {txt(P, "y60", "ANOS 60", 260, 300, 32, font="mono")}
      {papers}
      {txt(P, "ama", "AMADOR ·<br>DESORGANIZADO", 440, 446, 30, font="lab", extra="font-weight:600;letter-spacing:0.08em;")}
      <div class="{P}year" id="{P}yr">1968</div>
      {txt(P, "otan", "OTAN · ALEMANHA", 790, 396, 32, font="mono", w=340, align="center")}
      {stamp(P, "crise", "Crise do Software", 1230, 410, fs=58, tag=None)}
      {txt(P, "mtag", "MACETE", 150, 640, 28, font="mono", extra="transform-origin:0 50%;")}
      {prq}
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          drawX("#Pline", 0.3, 1.2);
          pop("#Pd1", @nos); rise("#Py60", @sessenta);
          for (let i = 0; i < 5; i++) {
            tl.fromTo(q("#Pp" + i), { opacity: 0, scale: 0.6, rotation: +q("#Pp" + i).dataset.r }, { opacity: 1, scale: 1, rotation: +q("#Pp" + i).dataset.r, duration: 0.5, ease: "back.out(1.7)" }, @programar+i*0.12);
            tl.to(q("#Pp" + i), { y: -6, rotation: "+=6", duration: 0.12, ease: "sine.inOut", yoyo: true, repeat: 9 }, @amador+i*0.05);
          }
          wipe("#Pama", @amador, 0.8);
          pop("#Pd2", @mil);
          tl.fromTo(q("#Pyr"), { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, @mil);
          wipe("#Potan", @otan, 0.6);
          stampIn("#Pcrise", @crise, -3);
          rise("#Pmtag", @macete);
          pop("#PL0", @p); pop("#PL1", @r); pop("#PL2", @q);
          lit("#PL0", @prazo); rise("#PW0", @prazo);
          lit("#PL1", @requisito); rise("#PW1", @requisito);
          lit("#PL2", @qualidade); rise("#PW2", @qualidade);
          shake(@qualidade+0.4);
""")

# ---------------------------------------------------------------- 04
P = "f04-"
phases = [("PLANEJAMENTO", "Planeje", 960, 255), ("ANÁLISE", "Analise", 1420, 400), ("DESIGN", "Desenhe", 1420, 640),
          ("DESENVOLVIMENTO", "Desenvolva", 960, 780), ("TESTES E INTEGRAÇÃO", "Teste", 500, 640), ("MANUTENÇÃO", "Mantenha", 500, 400)]
ph = ""
for i, (lab, verb, cx, cy) in enumerate(phases):
    x, y = cx - 190, cy - 62
    ph += (f'<div class="{P}ph" id="{P}ph{i}" style="left:{x}px;top:{y}px">'
           f'<div class="{P}num">{i + 1}</div><div class="{P}plab">{lab}</div>'
           f'<div class="{P}verb" id="{P}v{i}">{verb}</div></div>')
FR[4] = ("ciclo-de-vida", """
.Pring { position:absolute; left:500px; top:255px; width:920px; height:525px; border:5px dashed rgba(31,43,224,0.45); border-radius:50%; box-sizing:border-box; }
.Pph { position:absolute; width:380px; height:124px; border:4px solid INK; background:PAPER; box-sizing:border-box; }
.Pnum { position:absolute; left:0; top:0; width:44px; height:44px; background:INK; color:PAPER; font-family:"DM Mono", monospace; font-size:28px; display:flex; align-items:center; justify-content:center; }
.Pplab { position:absolute; left:56px; right:8px; top:8px; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:26px; letter-spacing:0.08em; white-space:nowrap; }
.Pverb { position:absolute; left:0; right:0; top:46px; height:70px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Newsreader", serif; font-size:52px; }
.Pcenter { position:absolute; left:760px; top:430px; width:400px; text-align:center; }
.Pcursor { position:absolute; width:26px; height:26px; background:INK; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      <div class="{P}ring" id="{P}ring"></div>
      {ph}
      {txt(P, "sdlc", "SDLC", 760, 430, 104, w=400, align="center")}
      {txt(P, "sub", "CICLO DE VIDA", 760, 548, 28, font="mono", w=400, align="center")}
      {stamp(P, "mac", "fase = verbo", 1530, 120, fs=44)}
      {stamp(P, "rec", "e recomeça", 1500, 790, fs=40, tag=None)}
""".replace("↺", "").replace("e recomeça ", "e recomeça"), """
          pop("#Psdlc", 0.1, { s: 0.7 }); rise("#Psub", 0.4);
          fade("#Pring", @ciclo, 0.8);
          tl.fromTo(q("#Pring"), { rotation: 0 }, { rotation: 40, duration: D, ease: "none" }, 0);
          for (let i = 0; i < 6; i++) { pop("#Pph" + i, @seis+i*0.18); tl.set(q("#Pv" + i), { clipPath: "inset(0% 100% 0% 0%)" }, 0); }
          stampIn("#Pmac", @macete, -2);
          const vt = [@planeje, @analise, @desenhe, @desenvolva, @teste, @mantenha];
          vt.forEach((t, i) => { tl.to(q("#Pv" + i), { clipPath: "inset(0% 0% 0% 0%)", duration: 0.35, ease: "power2.inOut" }, t); bump("#Pph" + i, t, 1.06); });
          tl.to(q("#Pring"), { opacity: 1, duration: 0.1 }, @ciclo#2);
          [0, 1, 2, 3, 4, 5, 0].forEach((k, i) => bump("#Pph" + k, @ciclo#2+0.2+i*0.32, 1.07));
          stampIn("#Prec", @recomeça, 2);
""")

# ---------------------------------------------------------------- 05
P = "f05-"
FR[5] = ("requisito", """
.Phd { position:absolute; left:250px; top:330px; width:110px; height:110px; border:5px solid INK; background:PAPER; box-sizing:border-box; }
.Pbd { position:absolute; left:225px; top:452px; width:160px; height:190px; background:INK; }
.Pballoon { position:absolute; left:420px; top:250px; width:300px; height:150px; border:4px solid INK; background:PAPER; box-sizing:border-box; display:flex; flex-direction:column; justify-content:center; gap:10px; padding-left:24px; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:30px; letter-spacing:0.08em; }
.Pmon { position:absolute; left:1300px; top:300px; width:420px; height:300px; border:5px solid INK; background:PAPER; box-sizing:border-box; }
.Pmon-bar { position:absolute; left:0; right:0; top:0; height:48px; background:INK; color:PAPER; font-family:"DM Mono", monospace; font-size:28px; letter-spacing:0.16em; display:flex; align-items:center; padding-left:18px; }
.Pdoc { position:absolute; left:40px; width:340px; height:62px; border:4px solid INK; background:PAPER; box-sizing:border-box; display:flex; align-items:center; gap:14px; padding-left:14px; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:28px; letter-spacing:0.08em; }
.Pdoc i { width:22px; height:30px; border:3px solid INK; box-sizing:border-box; }
.Pstand { position:absolute; left:1480px; top:600px; width:60px; height:46px; background:INK; }
.Pbridge { position:absolute; left:760px; top:470px; width:440px; height:6px; background:INK; transform-origin:50% 50%; }
.Ptri-l, .Ptri-r { position:absolute; top:457px; width:0; height:0; border-top:16px solid transparent; border-bottom:16px solid transparent; }
.Ptri-l { left:744px; border-right:28px solid INK; } .Ptri-r { left:1186px; border-left:28px solid INK; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {question(P, "O que é requisito?")}
      <div class="{P}hd" id="{P}hd"></div><div class="{P}bd" id="{P}bd"></div>
      <div class="{P}balloon" id="{P}bal"><span id="{P}b1">? PROBLEMA</span><span id="{P}b2">◎ OBJETIVO</span></div>
      {txt(P, "usr", "USUÁRIO", 190, 660, 34, font="lab", w=230, align="center", extra="font-weight:600;letter-spacing:0.12em;")}
      <div class="{P}mon" id="{P}mon"><div class="{P}mon-bar">SISTEMA</div>
        <div class="{P}doc" id="{P}d1" style="top:72px"><i></i>CONTRATO</div>
        <div class="{P}doc" id="{P}d2" style="top:146px"><i></i>NORMA</div>
        <div class="{P}doc" id="{P}d3" style="top:220px"><i></i>ESPECIFICAÇÃO</div>
      </div><div class="{P}stand" id="{P}st"></div>
      <div class="{P}bridge" id="{P}br"></div><div class="{P}tri-l" id="{P}tl"></div><div class="{P}tri-r" id="{P}tr"></div>
      {txt(P, "req", "requisito", 760, 380, 76, w=440, align="center", extra="font-style:italic;")}
      {txt(P, "cap", "CONDIÇÃO OU CAPACIDADE", 760, 500, 26, font="mono", w=440, align="center")}
      {box(P, "pre", "o usuário PRECISA", 190, 740, 620, 110, fs=50, font="serif")}
      {box(P, "pro", "o sistema PROVÊ", 1110, 740, 620, 110, fs=50, font="serif")}
      {txt(P, "mtag", "MACETE", 880, 770, 30, font="mono", w=160, align="center")}
""".replace("◎ ", "! "), """
          pop("#Pq", 0.05, { s: 0.85 });
          rise("#Phd", @condição); rise("#Pbd", @condição+0.1);
          tl.fromTo(q("#Pbr"), { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "power3.inOut" }, @capacidade);
          pop("#Ptl", @capacidade+0.6); pop("#Ptr", @capacidade+0.6);
          rise("#Preq", @capacidade+0.2); fade("#Pcap", @capacidade+0.5);
          rise("#Pusr", @usuário);
          pop("#Pbal", @problema-0.2, { s: 0.7 }); tl.set(q("#Pb2"), { opacity: 0 }, 0);
          tl.fromTo(q("#Pb1"), { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.3 }, @problema);
          tl.to(q("#Pb2"), { opacity: 1, duration: 0.3 }, @objetivo);
          slide("#Pmon", @sistema, 80); fade("#Pst", @sistema);
          pop("#Pd1", @contrato); pop("#Pd2", @norma); pop("#Pd3", @especificação);
          fade("#Pmtag", @macete);
          pop("#Ppre", @precisa-0.5); lit("#Ppre", @precisa);
          pop("#Ppro", @provê-0.5); lit("#Ppro", @provê);
          shake(@provê+0.3);
""")

# ---------------------------------------------------------------- 06
P = "f06-"
st6 = ""
names = ["ELICITAÇÃO", "ANÁLISE E<br>NEGOCIAÇÃO", "DEFINIÇÃO E<br>DOCUMENTAÇÃO", "VALIDAÇÃO"]
verbs = ["escuta", "acerta", "escreve", "confere"]
for i in range(4):
    x = 130 + i * 430
    st6 += (f'<div class="{P}stn" id="{P}s{i}" style="left:{x}px"><div class="{P}snum">{i + 1}</div>'
            f'<div class="{P}sname">{names[i]}</div></div>')
    st6 += box(P, f"v{i}", verbs[i], x, 520, 360, 96, fs=52, font="serif", inv=False)
    st6 += f'<div class="{P}ic" id="{P}i{i}" style="left:{x + 140}px">{["<b></b><b></b><b></b>", "<u></u><u class=r></u>", "<s></s><s></s><s></s>", "<em></em>"][i]}</div>'
    if i < 3:
        st6 += arrow(P, f"a{i}", x + 366, 370, 54)
FR[6] = ("fases-requisitos", """
.Pstn { position:absolute; top:300px; width:360px; height:150px; border:4px solid INK; background:PAPER; box-sizing:border-box; }
.Psnum { position:absolute; left:0; top:0; width:46px; height:46px; background:INK; color:PAPER; font-family:"DM Mono", monospace; font-size:28px; display:flex; align-items:center; justify-content:center; }
.Psname { position:absolute; left:0; right:0; top:40px; bottom:0; display:flex; align-items:center; justify-content:center; text-align:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:30px; letter-spacing:0.06em; line-height:1.15; }
.Pic { position:absolute; top:636px; width:80px; height:80px; border:4px solid INK; box-sizing:border-box; background:PAPER; }
.Pic b { position:absolute; bottom:12px; width:10px; background:INK; }
.Pic b:nth-child(1) { left:14px; height:20px; } .Pic b:nth-child(2) { left:31px; height:40px; } .Pic b:nth-child(3) { left:48px; height:28px; }
.Pic u { position:absolute; top:34px; width:26px; height:6px; background:INK; left:8px; } .Pic u.r { left:auto; right:8px; }
.Pic s { display:block; margin:12px 12px 0; height:5px; background:INK; }
.Pic em { position:absolute; left:16px; top:14px; width:22px; height:38px; border-right:7px solid INK; border-bottom:7px solid INK; transform:rotate(40deg); }
.Pger { position:absolute; left:560px; top:770px; width:800px; height:90px; border:4px dashed INK; box-sizing:border-box; display:flex; align-items:center; justify-content:center; gap:20px; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:30px; letter-spacing:0.08em; background:PAPER; }
.Pger span { font-family:"DM Mono", monospace; font-weight:400; font-size:26px; letter-spacing:0.04em; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {title(P, "Fases de requisitos", tag="JUNTO AO CLIENTE")}
      {st6}
      {txt(P, "mtag", "MACETE ↓", 1650, 470, 26, font="mono").replace(" ↓", "")}
      <div class="{P}ger" id="{P}ger">5ª · GERENCIAMENTO <span id="{P}gs">acompanha as mudanças</span></div>
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          const st = [@elicitação, @análise, @definição, @validação];
          st.forEach((t, i) => { pop("#Ps" + i, t); if (i > 0) drawX("#Pa" + (i - 1), t - 0.3, 0.3); });
          fade("#Pmtag", @macete);
          const vt = [@escuta, @acerta, @escreve, @confere];
          vt.forEach((t, i) => { pop("#Pv" + i, t); lit("#Pv" + i, t + 0.2); pop("#Pi" + i, t + 0.1); bump("#Ps" + i, t, 1.05); });
          tl.fromTo(qa("#Pi0 b"), { scaleY: 0.3 }, { scaleY: 1, duration: 0.25, ease: "sine.inOut", yoyo: true, repeat: 7, stagger: 0.08, transformOrigin: "50% 100%" }, @escuta+0.2);
          shake(@confere+0.4);
          rise("#Pger", @quinta); fade("#Pgs", @mudanças-0.3);
""")

# ---------------------------------------------------------------- 07
P = "f07-"
FR[7] = ("funcional", """
.Pdiv { position:absolute; left:958px; top:240px; width:5px; height:480px; background:INK; transform-origin:50% 0%; }
.Pform { position:absolute; left:230px; top:380px; width:520px; height:300px; border:5px solid INK; background:PAPER; box-sizing:border-box; }
.Pfbar { position:absolute; left:0; right:0; top:0; height:44px; background:INK; color:PAPER; font-family:"DM Mono", monospace; font-size:26px; letter-spacing:0.14em; display:flex; align-items:center; padding-left:16px; }
.Pfl { position:absolute; left:30px; font-family:"DM Mono", monospace; font-size:26px; }
.Pfield { position:absolute; left:180px; width:300px; height:44px; border:3px solid INK; box-sizing:border-box; }
.Pfill-in { position:absolute; left:8px; top:13px; height:12px; background:INK; transform-origin:0% 50%; }
.Pbtn { position:absolute; left:180px; top:206px; width:300px; height:60px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:28px; letter-spacing:0.1em; }
.Picon { position:absolute; left:1060px; width:110px; height:110px; border:4px solid INK; box-sizing:border-box; background:PAPER; }
.Pneedle { position:absolute; left:51px; top:20px; width:8px; height:46px; background:INK; transform-origin:50% 100%; }
.Pdial { position:absolute; left:14px; right:14px; top:58px; height:8px; background:INK; }
.Ppage s { display:block; margin:16px 18px 0; height:6px; background:INK; }
.Pui i { position:absolute; width:30px; height:30px; background:INK; top:38px; }
.Pilab { position:absolute; left:1200px; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:36px; letter-spacing:0.08em; white-space:nowrap; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {question(P, "Funcional ou não funcional?")}
      <div class="{P}div" id="{P}div"></div>
      {txt(P, "lh", "O QUE", 230, 250, 96, extra="font-weight:400;")}
      {txt(P, "lhs", "o sistema faz", 590, 290, 38, font="mono")}
      <div class="{P}form" id="{P}form"><div class="{P}fbar">CADASTRO</div>
        <div class="{P}fl" style="top:72px">NOME</div><div class="{P}field" style="top:64px"><div class="{P}fill-in" id="{P}f1" style="width:220px"></div></div>
        <div class="{P}fl" style="top:136px">E-MAIL</div><div class="{P}field" style="top:128px"><div class="{P}fill-in" id="{P}f2" style="width:260px"></div></div>
        <div class="{P}btn" id="{P}btn">CADASTRAR</div></div>
      {txt(P, "rh", "COMO", 1060, 250, 96)}
      {txt(P, "rhs", "o sistema funciona", 1390, 290, 38, font="mono")}
      <div class="{P}icon" id="{P}ic1" style="top:380px"><div class="{P}dial"></div><div class="{P}needle" id="{P}nd"></div></div>
      <div class="{P}ilab" id="{P}il1" style="top:414px">RÁPIDO</div>
      <div class="{P}icon {P}page" id="{P}ic2" style="top:510px"><s></s><s></s><s></s><s></s></div>
      <div class="{P}ilab" id="{P}il2" style="top:544px">DOCUMENTADO</div>
      <div class="{P}icon {P}ui" id="{P}ic3" style="top:640px"><i style="left:14px"></i><i style="left:58px"></i></div>
      <div class="{P}ilab" id="{P}il3" style="top:674px">FÁCIL DE USAR</div>
      {box(P, "m1", "funcionalidade", 190, 760, 600, 100, fs=52, font="serif")}
      {box(P, "m2", "qualidade", 1130, 760, 600, 100, fs=52, font="serif")}
      {txt(P, "mtag", "MACETE", 860, 790, 30, font="mono", w=200, align="center")}
""", """
          pop("#Pq", 0.05, { s: 0.85 });
          drawY("#Pdiv", @funcional, 0.6);
          rise("#Plh", @funcional#3); fade("#Plhs", @faz);
          pop("#Pform", @faz+0.2, { s: 0.9 });
          drawX("#Pf1", @cliente, 0.6); drawX("#Pf2", @próprio, 0.6);
          bump("#Pbtn", @cadastro, 1.12);
          rise("#Prh", @não#2); fade("#Prhs", @como);
          pop("#Pic1", @rápido-0.2); rise("#Pil1", @rápido);
          tl.fromTo(q("#Pnd"), { rotation: -70 }, { rotation: 70, duration: 0.6, ease: "back.out(2)" }, @rápido);
          pop("#Pic2", @documentado-0.2); rise("#Pil2", @documentado);
          pop("#Pic3", @fácil-0.2); rise("#Pil3", @fácil);
          fade("#Pmtag", @macete);
          pop("#Pm1", @funcionalidade-0.3); lit("#Pm1", @funcionalidade+0.1);
          pop("#Pm2", @qualidade-0.3); lit("#Pm2", @qualidade+0.1);
          shake(@qualidade+0.4);
""")

# ---------------------------------------------------------------- 08
P = "f08-"
cards = [("c0", "PESQUISAR", 210, 640), ("c1", "RESERVAR", 210, 720), ("c2", "RENOVAR", 210, 800),
         ("c3", "INTERFACE INTUITIVA", 1080, 600), ("c4", "VÁRIOS IDIOMAS", 1080, 680), ("c5", "MUITOS USUÁRIOS", 1080, 760),
         ("c6", "NO AR 24/7", 1420, 600)]
cs = ""
for (id, t, x, y) in cards:
    cs += f'<div class="{P}card" id="{P}{id}" style="left:{x}px;top:{y}px">{t}</div>'
FR[8] = ("biblioteca", """
.Pbin { position:absolute; top:520px; height:350px; border:5px solid INK; border-top:none; box-sizing:border-box; }
.Pbinlab { position:absolute; top:488px; height:52px; padding:0 22px; display:flex; align-items:center; background:PAPER; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:32px; letter-spacing:0.12em; border:4px solid INK; }
.Pcard { position:absolute; width:320px; height:62px; border:4px solid INK; background:PAPER; box-sizing:border-box; display:flex; align-items:center; justify-content:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:26px; letter-spacing:0.06em; white-space:nowrap; }
.Pseg { position:absolute; left:1420px; top:680px; width:320px; height:62px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:26px; letter-spacing:0.06em; }
.Pxo { position:absolute; left:300px; top:560px; font-family:"Newsreader", serif; font-size:200px; line-height:1; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {title(P, "A pegadinha da biblioteca", tag="SLIDE 10 · BIBLIOTECA ONLINE")}
      <div class="{P}bin" id="{P}bin1" style="left:170px;width:720px"></div>
      <div class="{P}binlab" id="{P}bl1" style="left:200px">FUNCIONAL</div>
      <div class="{P}bin" id="{P}bin2" style="left:1040px;width:740px"></div>
      <div class="{P}binlab" id="{P}bl2" style="left:1070px">NÃO FUNCIONAL</div>
      {cs}
      <div class="{P}xo" id="{P}xo" data-layout-allow-overlap>×</div>
      <div class="{P}seg" id="{P}seg">SEGURANÇA DOS DADOS</div>
      {stamp(P, "peg", "pegadinha!", 1180, 250, fs=64, tag=None)}
      {txt(P, "is", "parece função, mas é qualidade", 1000, 372, 32, font="mono", w=760, align="center")}
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          drawY("#Pbin1", @biblioteca, 0.5); fade("#Pbl1", @biblioteca+0.2);
          drawY("#Pbin2", @biblioteca+0.2, 0.5); fade("#Pbl2", @biblioteca+0.4);
          const drop = (id, t) => tl.fromTo(q(id), { opacity: 0, y: -380, rotation: -6 }, { opacity: 1, y: 0, rotation: 0, duration: 0.55, ease: "bounce.out" }, t);
          drop("#Pc0", @pesquisar); drop("#Pc1", @reservar); drop("#Pc2", @renovar);
          bump("#Pbl1", @funcional, 1.1);
          drop("#Pc3", @interface); drop("#Pc4", @idiomas); drop("#Pc5", @usuários); drop("#Pc6", @tempo);
          bump("#Pbl2", @funcional#2, 1.1);
          stampIn("#Ppeg", @pegadinha, -3);
          // the trap card first flies toward FUNCIONAL...
          tl.fromTo(q("#Pseg"), { opacity: 0, x: -760, y: -560 }, { opacity: 1, x: -760, y: -380, duration: 0.5, ease: "power3.out" }, @segurança);
          tl.to(q("#Pseg"), { x: -900, y: -30, rotation: -4, duration: 0.6, ease: "power2.inOut" }, @parece);
          tl.fromTo(q("#Pxo"), { opacity: 0, scale: 2 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.in" }, @mas);
          // ...and is redirected into NÃO FUNCIONAL
          tl.to(q("#Pseg"), { x: 0, y: 0, rotation: 0, duration: 0.9, ease: "power3.inOut" }, @qualidade);
          fade("#Pis", @parece);
          bump("#Pbl2", @funcional#3, 1.14); shake(@funcional#3+0.1);
""")

# ---------------------------------------------------------------- 09
P = "f09-"
pil = ""
pnames = ["ESPECIFICAÇÃO", "DESIGN E<br>IMPLEMENTAÇÃO", "VALIDAÇÃO", "EVOLUÇÃO"]
pq = ["o que fazer?", "como fazer?", "está correto?", "adaptar no tempo"]
for i in range(4):
    x = 230 + i * 390
    pil += (f'<div class="{P}pil" id="{P}p{i}" style="left:{x}px"><div class="{P}pname">{pnames[i]}</div>'
            f'<div class="{P}pq" id="{P}pq{i}">{pq[i]}</div></div>')
FR[9] = ("processo", """
.Proof { position:absolute; left:190px; top:470px; width:1540px; height:62px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"DM Mono", monospace; font-size:30px; letter-spacing:0.2em; transform-origin:50% 50%; }
.Ppil { position:absolute; top:532px; width:290px; height:300px; border:4px solid INK; border-top:none; background:PAPER; box-sizing:border-box; transform-origin:50% 100%;
  background-image: repeating-linear-gradient(90deg, transparent 0 44px, rgba(31,43,224,0.18) 44px 48px); }
.Ppname { position:absolute; left:0; right:0; top:20px; text-align:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:27px; letter-spacing:0.06em; line-height:1.15; background:PAPER; padding:6px 0; }
.Ppq { position:absolute; left:16px; right:16px; bottom:22px; height:82px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Newsreader", serif; font-size:38px; font-style:italic; }
.Pbase { position:absolute; left:190px; top:832px; width:1540px; height:16px; background:INK; transform-origin:50% 50%; }
.Pchip { position:absolute; top:376px; height:56px; padding:0 22px; border:4px solid INK; background:PAPER; display:flex; align-items:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:28px; letter-spacing:0.08em; box-sizing:border-box; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {question(P, "O que é processo de software?")}
      {box(P, "conj", "conjunto estruturado", 190, 268, 640, 90, fs=54, font="serif")}
      <div class="{P}chip" id="{P}k1" style="left:190px">ATIVIDADES</div>
      <div class="{P}chip" id="{P}k2" style="left:430px">MÉTODOS</div>
      <div class="{P}chip" id="{P}k3" style="left:640px">PRÁTICAS</div>
      {arrow(P, "ar", 880, 312, 120)}
      {box(P, "dm", "DESENVOLVER<br>E MANTER", 1040, 268, 420, 130, fs=34)}
      <div class="{P}roof" id="{P}roof">4 PILARES</div>
      {pil}
      <div class="{P}base" id="{P}base"></div>
""", """
          pop("#Pq", 0.05, { s: 0.85 });
          pop("#Pconj", @conjunto); lit("#Pconj", @estruturado);
          pop("#Pk1", @atividades); pop("#Pk2", @métodos); pop("#Pk3", @práticas);
          drawX("#Par", @pessoas, 0.5); pop("#Pdm", @desenvolver);
          drawX("#Pbase", @pilares-0.4, 0.6);
          tl.fromTo(q("#Proof"), { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power3.inOut" }, @pilares);
          const pt = [@especificação, @design, @validação, @evolução];
          const qt = [@fazer, @fazer#2, @correto, @adaptar];
          pt.forEach((t, i) => { tl.fromTo(q("#Pp" + i), { scaleY: 0 }, { scaleY: 1, duration: 0.55, ease: "back.out(1.4)" }, t); tl.set(q("#Ppq" + i), { opacity: 0 }, 0); });
          qt.forEach((t, i) => { tl.fromTo(q("#Ppq" + i), { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "power4.in", immediateRender: false }, t); });
          shake(@adaptar+0.4);
""")

# ---------------------------------------------------------------- 10
P = "f10-"
FR[10] = ("modelo-processo", """
.Pcard { position:absolute; top:210px; width:560px; height:220px; border:5px solid INK; background:PAPER; box-sizing:border-box; }
.Pchead { position:absolute; left:0; right:0; top:0; height:74px; background:INK; color:PAPER; display:flex; align-items:center; justify-content:center; font-family:"Newsreader", serif; font-size:52px; }
.Pcl { position:absolute; left:0; right:0; text-align:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:30px; letter-spacing:0.08em; }
.Pvs { position:absolute; left:860px; top:262px; width:200px; text-align:center; font-family:"Newsreader", serif; font-size:110px; line-height:1; }
.Precipe { position:absolute; left:200px; top:480px; width:250px; height:200px; border:4px solid INK; background:PAPER; box-sizing:border-box; padding:46px 20px 0; }
.Precipe s { display:block; height:5px; background:INK; margin-bottom:20px; }
.Precipe span { position:absolute; left:0; right:0; top:8px; text-align:center; font-family:"DM Mono", monospace; font-size:26px; letter-spacing:0.12em; }
.Pic { position:absolute; top:500px; width:150px; height:150px; border:4px solid INK; background:PAPER; box-sizing:border-box; }
.Phand { position:absolute; left:69px; top:28px; width:6px; height:48px; background:INK; transform-origin:50% 100%; }
.Phand2 { position:absolute; left:69px; top:48px; width:6px; height:28px; background:INK; transform-origin:50% 100%; }
.Phat { position:absolute; left:30px; top:24px; width:82px; height:56px; background:INK; }
.Phat2 { position:absolute; left:42px; top:80px; width:58px; height:40px; border:5px solid INK; border-top:none; box-sizing:border-box; }
.Pscale-b { position:absolute; left:20px; top:58px; width:102px; height:6px; background:INK; transform-origin:50% 50%; }
.Pscale-p { position:absolute; left:66px; top:64px; width:10px; height:56px; background:INK; }
.Pilab { position:absolute; top:662px; width:190px; text-align:center; font-family:"Hanken Grotesk", sans-serif; font-weight:600; font-size:26px; letter-spacing:0.08em; }
.Pop { position:absolute; top:756px; font-family:"Newsreader", serif; font-size:84px; line-height:1; }
""".replace("INK", INK).replace("PAPER", "#F0EBDE"), f"""
      {title(P, "Modelo × Processo")}
      <div class="{P}card" id="{P}cm" style="left:220px"><div class="{P}chead">Modelo</div>
        <div class="{P}cl" id="{P}cm1" style="top:96px">TEÓRICO</div><div class="{P}cl" id="{P}cm2" style="top:146px">POSSÍVEIS AÇÕES</div></div>
      <div class="{P}vs" id="{P}vs">×</div>
      <div class="{P}card" id="{P}cp" style="left:1140px"><div class="{P}chead">Processo</div>
        <div class="{P}cl" id="{P}cp1" style="top:96px">PRÁTICO</div><div class="{P}cl" id="{P}cp2" style="top:146px">PRAZOS E MÉTRICAS</div></div>
      <div class="{P}recipe" id="{P}rec"><span>RECEITA</span><s></s><s></s><s></s><s style="width:60%"></s></div>
      {txt(P, "eqm", "= modelo", 200, 694, 34, font="mono", w=250, align="center")}
      {txt(P, "plus", "+", 500, 520, 110)}
      <div class="{P}ic" id="{P}i1" style="left:640px"><div class="{P}hand" id="{P}h1"></div><div class="{P}hand2" id="{P}h2"></div></div>
      <div class="{P}ic" id="{P}i2" style="left:840px"><div class="{P}hat"></div><div class="{P}hat2"></div></div>
      <div class="{P}ic" id="{P}i3" style="left:1040px"><div class="{P}scale-b" id="{P}sb"></div><div class="{P}scale-p"></div></div>
      <div class="{P}ilab" id="{P}l1" style="left:620px">HORÁRIO</div>
      <div class="{P}ilab" id="{P}l2" style="left:820px">COZINHEIRO</div>
      <div class="{P}ilab" id="{P}l3" style="left:1020px">QUANTIDADE</div>
      {arrow(P, "ar", 1230, 573, 130)}
      {box(P, "proc", "processo", 1400, 520, 330, 110, fs=56, font="serif")}
      {box(P, "e1", "MODELO", 230, 750, 400, 100, fs=38)}
      <div class="{P}op" id="{P}o1" style="left:660px">+</div>
      {box(P, "e2", "PLANEJAMENTO", 740, 750, 520, 100, fs=38)}
      <div class="{P}op" id="{P}o2" style="left:1292px">=</div>
      {box(P, "e3", "PROCESSO", 1380, 750, 340, 100, fs=38, inv=True, fill=False)}
""", """
          pop("#Pq", 0.05, { s: 0.9 });
          slide("#Pcm", @modelo, -80);
          rise("#Pcm1", @teórico); rise("#Pcm2", @possíveis);
          pop("#Pvs", @processo-0.2); slide("#Pcp", @processo, 80);
          rise("#Pcp1", @prático); rise("#Pcp2", @prazos);
          pop("#Prec", @bolo); tl.fromTo(qa("#Prec s"), { scaleX: 0 }, { scaleX: 1, duration: 0.3, stagger: 0.12, transformOrigin: "0% 50%" }, @receita);
          fade("#Peqm", @modelo#2);
          pop("#Pplus", @horário-0.3);
          pop("#Pi1", @horário); rise("#Pl1", @horário);
          tl.fromTo(q("#Ph1"), { rotation: 0 }, { rotation: 720, duration: D - @horário, ease: "none" }, @horário);
          tl.fromTo(q("#Ph2"), { rotation: 0 }, { rotation: 60, duration: D - @horário, ease: "none" }, @horário);
          pop("#Pi2", @cozinheiro); rise("#Pl2", @cozinheiro);
          pop("#Pi3", @quantidade); rise("#Pl3", @quantidade);
          tl.fromTo(q("#Psb"), { rotation: -14 }, { rotation: 14, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 3 }, @quantidade);
          drawX("#Par", @vira, 0.4); pop("#Pproc", @processo#2); lit("#Pproc", @processo#2+0.3);
          pop("#Pe1", @modelo#3); pop("#Po1", @mais); pop("#Pe2", @planejamento); pop("#Po2", @igual);
          stampIn("#Pe3", @processo#3, 0);
""")
