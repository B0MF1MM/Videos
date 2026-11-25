import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbkit import scene, code_win, lcd, LCD_CSS, lines_hl, hl

# 01 ---------------------------------------------------------------
scene("01-abertura", """
<div id="@k" class="k-kicker" style="left:0;top:150px;width:1920px;text-align:center">REVISÃO PARA A PROVA</div>
<div id="@t" class="k-title" style="left:0;top:200px;width:1920px;text-align:center;font-size:104px">Sistemas <em>Embarcados</em></div>
<div id="@f1" class="k-chip k-c-cyan" style="left:250px;top:430px;font-size:34px">SENSOR · lê</div>
<div id="@a1" class="k-code k-mute" style="left:560px;top:428px;font-size:44px">→</div>
<div id="@f2" class="k-chip k-c-yel" style="left:640px;top:430px;font-size:34px;background:#2A2410">MICROCONTROLADOR · decide</div>
<div id="@a2" class="k-code k-mute" style="left:1230px;top:428px;font-size:44px">→</div>
<div id="@f3" class="k-chip k-c-pink" style="left:1320px;top:430px;font-size:34px;background:#2E1420">ATUADOR · age</div>
<div id="@c1" class="k-card" style="left:330px;top:560px;width:1260px;height:110px;border-color:#7FE39A">
  <div class="k-body" style="left:36px;top:30px;font-size:34px"><b class="k-c-green">vai cair código</b> · todos os códigos do resumo, linha por linha</div>
</div>
<div id="@c2" class="k-card" style="left:330px;top:700px;width:1260px;height:110px;border-color:#B49BFF">
  <div class="k-body" style="left:36px;top:30px;font-size:34px"><b class="k-c-violet">discursiva</b> · proposta completa de irrigação automática</div>
</div>
""", """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("t"), C.a + 0.3);
K.pop(tl, $("f1"), C.b + 3.0);
K.fade(tl, $("a1"), C.b + 3.6);
K.pop(tl, $("f2"), C.b + 3.9);
K.fade(tl, $("a2"), C.b + 4.8);
K.pop(tl, $("f3"), C.b + 5.1);
K.rise(tl, $("c1"), C.c + 1.0);
K.rise(tl, $("c2"), C.d + 0.4);
""", sfx="b:pop@3.0*0.2, c:pop@1.0*0.25, d:chime@0.4*0.3")

# 02 ---------------------------------------------------------------
Q = [("1", "arquitetura", "cyan"), ("2", "analogRead · map · PWM", "green"), ("3", "LDR + divisor", "cyan"),
     ("4", "ADC 10 bits", "cyan"), ("5", "UART", "pink"), ("6", "I2C", "pink"), ("7", "atuador + driver", "pink"),
     ("8", "dashboard · IoT", "pink"), ("9", "ROI · Payback", "yel"), ("10", "discursiva: irrigação", "violet")]
COL = {"cyan": "#4FD6EE", "green": "#7FE39A", "pink": "#FF6F9C", "yel": "#FFD24A", "violet": "#B49BFF"}
body = ""
for i, (n, t, c) in enumerate(Q):
    x = 120 + (i % 5) * 336
    y = 220 + (i // 5) * 220
    body += ('<div id="@q%s" class="k-card" style="left:%dpx;top:%dpx;width:300px;height:180px;border-color:%s">'
             '<div class="k-body" style="left:24px;top:20px;font-size:24px;color:#8C97B5;font-family:\'DM Mono\',monospace">QUESTÃO %s</div>'
             '<div class="k-body k-c-%s" style="left:24px;top:70px;width:260px;font-size:30px;font-weight:600;line-height:1.2">%s</div></div>\n'
             % (n, x, y, COL[c], n, c, t))
body += '<div id="@cod" class="k-macete" style="left:120px;top:690px;width:1680px;font-size:32px">+ <u>código</u>: todos os exemplos do resumo (vai cair diferente do que caiu)</div>'
scene("02-mapa", body, """
K.fade(tl, [$("q1"), $("q2"), $("q3"), $("q4"), $("q5"), $("q6"), $("q7"), $("q8"), $("q9"), $("q10")], C.a + 0.2, { s: 0.08, d: 0.3 });
tl.set([$("q1"), $("q2"), $("q3"), $("q4"), $("q5"), $("q6"), $("q7"), $("q8"), $("q9"), $("q10")], { opacity: 0.25 }, C.a + 1.4);
tl.to([$("q1"), $("q4"), $("q3")], { opacity: 1, duration: 0.3, stagger: 1.2 }, C.b);
tl.to($("q2"), { opacity: 1, duration: 0.3 }, C.c);
tl.to([$("q5"), $("q6"), $("q7"), $("q8")], { opacity: 1, duration: 0.3, stagger: 0.9 }, C.d);
tl.to([$("q9"), $("q10")], { opacity: 1, duration: 0.3, stagger: 1.6 }, C.e);
K.macete(tl, $("cod"), C.e + 3.6);
""", sfx="b:click-soft*0.25, c:click-soft*0.25, d:click-soft*0.25, e:pop@3.6*0.3")

# 03 ---------------------------------------------------------------
scene("03-arquitetura", """
<div id="@k" class="k-chip k-c-cyan" style="left:120px;top:120px;font-size:26px">QUESTÃO 1 · ARQUITETURA</div>
<div id="@cy" class="k-h2" style="left:120px;top:190px;font-size:50px">perceber <span class="k-mute">→</span> <span class="k-c-yel">pensar</span> <span class="k-mute">→</span> <span class="k-c-pink">agir</span></div>
<div id="@b1" class="k-card bx" style="left:120px;border-color:#4FD6EE"><div class="tg k-c-cyan">ENTRADA</div><div class="nm">sensor</div><div class="ds">percebe o mundo:<br>temperatura, luz, umidade</div></div>
<div id="@b2" class="k-card bx" style="left:700px;border-color:#FFD24A"><div class="tg k-c-yel">PROCESSAMENTO</div><div class="nm">microcontrolador</div><div class="ds">lê o sensor e decide,<br>seguindo o <b class="k-c-yel">firmware</b></div></div>
<div id="@b3" class="k-card bx" style="left:1280px;border-color:#FF6F9C"><div class="tg k-c-pink">SAÍDA</div><div class="nm">atuador</div><div class="ds">LED, buzzer, relé, motor,<br>sinalizador</div></div>
<svg class="k-svg"><path id="@p1" class="arrow" d="M 646 430 L 694 430 M 680 418 L 694 430 L 680 442" stroke="#8C97B5"/><path id="@p2" class="arrow" d="M 1226 430 L 1274 430 M 1260 418 L 1274 430 L 1260 442" stroke="#8C97B5"/></svg>
<div id="@ex" class="k-anno k-mute" style="left:120px;top:600px;font-size:24px">ex.: sensor mede 31 °C → ESP32 lê → regra "temp > 24 °C" → compressor liga</div>
<div id="@al" class="k-macete k-alert" style="left:120px;top:690px;width:1680px;font-size:30px">Firmware é <b>software gravado no chip</b>, não é peça física. Hardware é o corpo; firmware é o cérebro.</div>
<div id="@ans" class="k-chip k-c-green" style="left:1500px;top:120px;font-size:26px;background:#13241A">Q1 → alternativa C</div>
""", """
K.fade(tl, $("k"), C.a);
K.wipe(tl, $("cy"), C.b);
K.rise(tl, $("b1"), C.c);
K.draw(tl, $("p1"), C.d - 0.3, { d: 0.3 });
K.rise(tl, $("b2"), C.d);
K.draw(tl, $("p2"), C.e - 0.3, { d: 0.3 });
K.rise(tl, $("b3"), C.e);
K.fade(tl, $("ex"), C.e + 2.0);
K.pop(tl, $("al"), C.f);
K.pop(tl, $("ans"), C.f + 3.0);
""", sfx="c:pop@0.2*0.25, d:pop@0.2*0.25, e:pop@0.2*0.25, f:pop*0.3",
css="""  .bx { top: 300px; width: 520px; height: 260px; }
  .bx .tg { position: absolute; left: 30px; top: 24px; font-family: "DM Mono", monospace; font-size: 24px; letter-spacing: 0.1em; }
  .bx .nm { position: absolute; left: 30px; top: 66px; font-family: "Hanken Grotesk", sans-serif; font-weight: 700; font-size: 44px; color: #EEF1F8; }
  .bx .ds { position: absolute; left: 30px; top: 140px; width: 470px; font-family: "Hanken Grotesk", sans-serif; font-size: 27px; line-height: 1.4; color: #B9C2DA; }
""")

# 04 ---------------------------------------------------------------
def row(rid, top, title, lt, lh_, rt, rh, lc, rc):
    return ('<div id="@%s" class="k-card rw" style="top:%dpx"><div class="ti">%s</div>'
            '<div class="cl" style="left:330px"><b class="%s">%s</b><span>%s</span></div>'
            '<div class="cl" style="left:1000px"><b class="%s">%s</b><span>%s</span></div></div>\n'
            % (rid, top, title, lc, lt, lh_, rc, rt, rh))
body = row("r1", 190, "uso", "sistema embarcado", "função específica · baixo consumo · tempo real",
           "computador comum", "vários programas · SO completo · flexível", "k-c-cyan", "k-c-mute")
body += row("r2", 370, "chip", "microcontrolador", "CPU + memória + periféricos no mesmo chip",
            "microprocessador", "memória e periféricos externos · roda SO", "k-c-yel", "k-c-mute")
body += row("r3", 550, "placas", "Arduino · ESP32", "microcontroladores · ESP32 tem Wi-Fi e Bluetooth",
            "Raspberry Pi", "computador de placa única · roda Linux", "k-c-green", "k-c-violet")
body += '<div id="@mac" class="k-macete" style="left:120px;top:740px;width:1680px;font-size:30px">A melhor tecnologia é a que <u>atende aos requisitos</u> do projeto.</div>'
scene("04-conceitos", body, """
K.rise(tl, $("r1"), C.b);
K.rise(tl, $("r2"), C.c);
K.rise(tl, $("r3"), C.d);
K.macete(tl, $("mac"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop*0.3",
css="""  .rw { left: 120px; width: 1680px; height: 150px; }
  .rw .ti { position: absolute; left: 30px; top: 54px; font-family: "DM Mono", monospace; font-size: 26px; color: #8C97B5; text-transform: uppercase; letter-spacing: 0.1em; }
  .rw .cl { position: absolute; top: 26px; width: 640px; }
  .rw .cl b { display: block; font-family: "Hanken Grotesk", sans-serif; font-size: 36px; font-weight: 700; }
  .rw .cl span { display: block; margin-top: 8px; font-family: "Hanken Grotesk", sans-serif; font-size: 25px; color: #B9C2DA; }
""")

# 05 ---------------------------------------------------------------
L = ["void setup() {", "  pinMode(13, OUTPUT);     // pino 13 = saída", "}", "void loop() {",
     "  digitalWrite(13, HIGH);  // acende", "  delay(1000);             // espera 1 s",
     "  digitalWrite(13, LOW);   // apaga", "  delay(1000);             // espera 1 s", "}"]
body = code_win("win", "pisca_led.ino", L, 120, 180, 940, font=28, lh=46)
body += """
<div id="@n1" class="k-card nt" style="top:180px;border-color:#4FD6EE"><b class="k-c-cyan">setup()</b><span>roda <u>uma vez</u> ao ligar · configura pinos e serial</span></div>
<div id="@n2" class="k-card nt" style="top:320px;border-color:#7FE39A"><b class="k-c-green">loop()</b><span>repete <u>para sempre</u> · a lógica do sistema</span></div>
<div id="@n3" class="k-anno" style="left:1120px;top:470px;font-size:23px"><span class="k-c-cyan">pinMode</span>(pino, OUTPUT/INPUT)
<span class="k-c-cyan">digitalWrite</span>(pino, <span class="k-c-yel">HIGH</span>=5 V / <span class="k-c-yel">LOW</span>=0 V)</div>
<div id="@n4" class="k-anno" style="left:1120px;top:580px;font-size:23px"><span class="k-c-cyan">digitalRead</span>(pino) → 1 ou 0
<span class="k-c-cyan">delay</span>(ms) → 1000 = 1 s</div>
<div id="@led" style="position:absolute;left:1500px;top:720px;width:90px;height:90px;border-radius:45px;background:#3A1420;border:4px solid #FF6F9C"></div>
<div id="@glow" style="position:absolute;left:1500px;top:720px;width:90px;height:90px;border-radius:45px;background:#FF6F9C;box-shadow:0 0 60px #FF6F9C"></div>
<div id="@ll" class="k-anno k-mute" style="left:1620px;top:742px;font-size:22px">pino 13</div>
"""
js = """
K.rise(tl, $("win"), C.a);
K.rise(tl, $("n1"), C.b);
""" + lines_hl([("c0", "C.b", "C.c"), ("c1", "C.b + 1.6", "C.c"), ("c3", "C.c", "C.d")]) + """
K.rise(tl, $("n2"), C.c);
K.wipe(tl, $("n3"), C.d);
""" + lines_hl([("c1", "C.d", "C.d + 2.5"), ("c4", "C.d + 2.5", "C.e"), ("c6", "C.d + 4.5", "C.e")]) + """
K.wipe(tl, $("n4"), C.e);
""" + lines_hl([("c5", "C.e + 3.0", "C.f"), ("c7", "C.e + 3.0", "C.f")]) + """
tl.set($("glow"), { opacity: 0 }, 0);
K.fade(tl, [$("led"), $("ll")], C.f);
for (var i = 0; i < 3; i++) {
  tl.set($("glow"), { opacity: 1 }, C.f + 0.4 + i * 1.4);
  tl.set($("glow"), { opacity: 0 }, C.f + 1.1 + i * 1.4);
}
"""
scene("05-estrutura", body, js, sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, f:click-soft@0.4*0.2",
      css="  .nt { left: 1120px; width: 680px; height: 118px; }\n  .nt b { position: absolute; left: 28px; top: 18px; font-family: 'DM Mono', monospace; font-size: 32px; }\n  .nt span { position: absolute; left: 28px; top: 66px; font-family: 'Hanken Grotesk', sans-serif; font-size: 24px; color: #B9C2DA; }\n")

# 06 ---------------------------------------------------------------
def col(cid, left, color, cls, name, wave, items, ex):
    lis = "".join('<div class="it">%s</div>' % t for t in items)
    return ('<div id="@%s" class="k-card dc" style="left:%dpx;border-color:%s"><div class="nm %s">%s</div>'
            '<svg width="220" height="60" style="position:absolute;left:560px;top:28px"><path d="%s" stroke="%s" stroke-width="5" fill="none"/></svg>'
            '<div class="ls">%s</div><div id="@%sx" class="ex %s">%s</div></div>\n'
            % (cid, left, color, cls, name, wave, color, lis, cid, cls, ex))
body = col("dg", 120, "#B49BFF", "k-c-violet", "DIGITAL", "M 0 50 L 40 50 L 40 10 L 90 10 L 90 50 L 130 50 L 130 10 L 180 10 L 180 50 L 220 50",
           ["2 estados: <b>HIGH</b> ou <b>LOW</b>", "0 V ou 5 V", "pinos D0 a D13", "lê: <code>digitalRead()</code>", "escreve: <code>digitalWrite()</code>"],
           "LED · relé · botão · buzzer")
body += col("an", 980, "#7FE39A", "k-c-green", "ANALÓGICO", "M 0 30 C 25 -5, 50 -5, 75 30 S 125 65, 150 30 S 200 -5, 220 20",
            ["valores <b>contínuos</b>", "0 a 5 V → <b>0 a 1023</b>", "pinos A0 a A5", "lê: <code>analogRead()</code>", "escreve só via PWM"],
            "LDR · potenciômetro · umidade do solo")
body += '<div id="@mac" class="k-macete" style="left:120px;top:760px;width:1680px;font-size:30px">Interruptor = <u>digital</u> (liga/desliga). Dimmer = <u>analógico</u> (todos os níveis).</div>'
scene("06-dig-anal", body, """
K.rise(tl, $("dg"), C.b);
K.rise(tl, $("an"), C.c);
tl.set([$("dgx"), $("anx")], { opacity: 0 }, 0);
tl.to([$("dgx"), $("anx")], { opacity: 1, duration: 0.4, stagger: 2.2 }, C.d + 0.4);
K.macete(tl, $("mac"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, e:pop*0.3",
css="""  .dc { top: 180px; width: 820px; height: 540px; }
  .dc .nm { position: absolute; left: 32px; top: 30px; font-family: "DM Mono", monospace; font-size: 40px; letter-spacing: 0.08em; }
  .dc .ls { position: absolute; left: 32px; top: 120px; width: 760px; }
  .dc .it { font-family: "Hanken Grotesk", sans-serif; font-size: 30px; line-height: 64px; color: #EEF1F8; border-bottom: 1px solid #2A3656; }
  .dc .it code { font-family: "DM Mono", monospace; color: #4FD6EE; }
  .dc .ex { position: absolute; left: 32px; top: 460px; font-family: "DM Mono", monospace; font-size: 26px; }
""")

# 07 ---------------------------------------------------------------
X0, X1 = 200, 1700
def xp(v):
    return X0 + (X1 - X0) * v / 1023.0
ticks = ""
for v, lab in [(0, "0"), (256, "256"), (512, "512"), (768, "768"), (1023, "1023")]:
    ticks += '<div class="tk" style="left:%dpx">%s</div>' % (xp(v) - 60, lab)
for v, lab in [(0, "0 V"), (512, "2,5 V"), (1023, "5 V")]:
    ticks += '<div class="tv" style="left:%dpx">%s</div>' % (xp(v) - 60, lab)
body = """
<div id="@k" class="k-chip k-c-cyan" style="left:120px;top:120px;font-size:26px">QUESTÃO 4 · CONVERSOR ADC</div>
<div id="@b" class="k-h2" style="left:120px;top:190px;font-size:48px">10 bits → 2<sup>10</sup> = <span class="k-c-yel">1024 níveis</span> → <span class="k-c-cyan">0 a 1023</span></div>
<div id="@sc" style="position:absolute;left:0;top:0">
  <div style="position:absolute;left:%dpx;top:370px;width:%dpx;height:36px;border-radius:18px;background:linear-gradient(90deg,#182238,#4FD6EE)"></div>
  %s
</div>
<div id="@mk" style="position:absolute;left:%dpx;top:340px;width:6px;height:96px;margin-left:-3px;background:#FFD24A;border-radius:3px"></div>
<div id="@mkl" class="k-chip k-c-yel" style="left:%dpx;top:280px;font-size:26px;background:#2A2410">leitura = 850</div>
<div id="@st" class="k-anno k-mute" style="left:200px;top:470px;font-size:22px">cada degrau ≈ 4,9 mV (5 V ÷ 1023)</div>
<div id="@fm" class="k-card" style="left:120px;top:540px;width:1040px;height:230px;border-color:#FFD24A">
  <div class="k-body" style="left:32px;top:26px;font-size:28px">850 <b>não</b> são 850 volts. Para voltar à tensão:</div>
  <div class="k-code" style="left:32px;top:90px;font-size:36px;line-height:1.5">V = leitura × 5 / 1023
  = 850 × 5 / 1023 = <span class="k-c-yel">4,15 V</span></div>
</div>
<div id="@e32" class="k-card" style="left:1200px;top:540px;width:600px;height:230px;border-color:#7FE39A">
  <div class="k-h2 k-c-green" style="left:30px;top:24px;font-size:34px">ESP32</div>
  <div class="k-body" style="left:30px;top:84px;width:540px;font-size:28px;line-height:1.45">ADC de <b>12 bits</b><br>0 a <b>4095</b> · máximo <b>3,3 V</b></div>
</div>
<div id="@ans" class="k-chip k-c-green" style="left:1500px;top:120px;font-size:26px;background:#13241A">Q4 → alternativa A</div>
""" % (X0, X1 - X0, ticks, xp(850), xp(850) - 110)
scene("07-adc", body, """
K.fade(tl, $("k"), C.a);
K.wipe(tl, $("b"), C.b);
K.fade(tl, $("sc"), C.c);
K.fade(tl, $("st"), C.c + 3.6);
tl.set([$("mk"), $("mkl")], { opacity: 0 }, 0);
tl.fromTo($("mk"), { x: -1250, opacity: 0 }, { x: 0, opacity: 1, duration: 1.0, ease: "power3.out" }, C.d);
tl.to($("mkl"), { opacity: 1, duration: 0.3 }, C.d + 0.8);
K.rise(tl, $("fm"), C.d + 2.4);
K.rise(tl, $("e32"), C.e);
K.pop(tl, $("ans"), C.e + 4.0);
""", sfx="b:pop@0.2*0.2, d:whoosh-short*0.2, e:pop@0.2*0.25",
css="""  .tk { position: absolute; top: 420px; width: 120px; text-align: center; font-family: "DM Mono", monospace; font-size: 24px; color: #4FD6EE; }
  .tv { position: absolute; top: 330px; width: 120px; text-align: center; font-family: "DM Mono", monospace; font-size: 22px; color: #8C97B5; }
""")

# 08 ---------------------------------------------------------------
body = """
<div id="@k" class="k-chip k-c-cyan" style="left:120px;top:120px;font-size:26px">QUESTÃO 3 · LDR + DIVISOR DE TENSÃO</div>
<svg id="@cir" class="k-svg"><g stroke="#8C97B5" stroke-width="4" fill="none">
  <path d="M 400 220 L 400 260"/><path d="M 400 380 L 400 470"/><path d="M 400 590 L 400 650"/><path d="M 400 470 L 560 470"/>
  <path d="M 360 650 L 440 650 M 375 665 L 425 665 M 390 680 L 410 680"/></g>
  <rect x="360" y="260" width="80" height="120" rx="10" fill="#182238" stroke="#FFD24A" stroke-width="4"/>
  <path d="M 372 300 L 428 300 M 372 340 L 428 340" stroke="#FFD24A" stroke-width="3" stroke-dasharray="8 6"/>
  <rect x="370" y="470" width="60" height="120" rx="8" fill="#182238" stroke="#4FD6EE" stroke-width="4"/>
  <circle cx="400" cy="470" r="8" fill="#7FE39A"/>
</svg>
<div class="lb" style="left:420px;top:196px">5 V</div>
<div class="lb k-c-yel" style="left:460px;top:300px">LDR</div>
<div class="lb k-c-cyan" style="left:450px;top:510px">R fixo 10 kΩ</div>
<div class="lb" style="left:460px;top:640px">GND</div>
<div id="@a0" class="k-chip k-c-green" style="left:570px;top:448px;font-size:26px;background:#13241A">→ A0 (ADC)</div>
<div id="@sun" style="position:absolute;left:180px;top:270px;width:90px;height:90px;border-radius:45px;background:#FFD24A;box-shadow:0 0 50px #FFD24A"></div>
<div id="@n1" class="k-card nt" style="top:190px;border-color:#FFD24A"><b class="k-c-yel">sensor de luz</b><span>resistência muda com a luz · <u>mais luz → menos resistência</u></span></div>
<div id="@n2" class="k-card nt" style="top:330px;border-color:#4FD6EE"><b class="k-c-cyan">divisor de tensão</b><span>o Arduino só lê tensão → LDR + resistor fixo</span></div>
<div id="@n3" class="k-card nt" style="top:470px;border-color:#7FE39A"><b class="k-c-green">luz muda → tensão muda</b><span>o ponto do meio vai ao A0 · o ADC converte</span></div>
<div id="@cd" class="k-win" style="left:860px;top:620px;width:940px;height:200px"><div class="k-win-bar"><i style="left:22px;background:#FF6F9C"></i><i style="left:46px;background:#FFD24A"></i><i style="left:70px;background:#7FE39A"></i><span>ldr.ino</span></div>
<div class="k-code" style="left:10px;top:62px;font-size:24px;line-height:40px"><span class="ln">%s</span><span class="ln">%s</span><span class="ln">%s</span></div></div>
<div id="@q" class="k-chip k-c-green" style="left:120px;top:760px;font-size:26px;background:#13241A">Q3 → B · quem decide é o microcontrolador</div>
""" % (hl("int luz = analogRead(A0);"), hl("if (luz < 300) digitalWrite(8, HIGH);  // pouca luz"), hl("else          digitalWrite(8, LOW);"))
scene("08-ldr", body, """
K.fade(tl, $("k"), C.a);
K.fade(tl, $("cir"), C.a + 0.4);
K.rise(tl, $("n1"), C.b);
tl.set($("sun"), { opacity: 0.25 }, 0);
tl.to($("sun"), { opacity: 1, duration: 0.6 }, C.b + 2.0);
tl.to($("sun"), { opacity: 0.25, duration: 0.6 }, C.b + 4.0);
K.rise(tl, $("n2"), C.c);
K.rise(tl, $("n3"), C.d);
K.pop(tl, $("a0"), C.d + 3.0);
K.rise(tl, $("cd"), C.e);
K.pop(tl, $("q"), C.e + 4.4);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@3.0*0.25, e:pop@4.4*0.25",
css="""  .lb { position: absolute; font-family: "DM Mono", monospace; font-size: 24px; color: #B9C2DA; }
  .nt { left: 860px; width: 940px; height: 118px; }
  .nt b { position: absolute; left: 28px; top: 16px; font-family: "Hanken Grotesk", sans-serif; font-size: 32px; }
  .nt span { position: absolute; left: 28px; top: 66px; font-family: "Hanken Grotesk", sans-serif; font-size: 25px; color: #B9C2DA; }
""")

# 09 ---------------------------------------------------------------
def pwm(duty, y, w=640, per=128, h=70):
    d, x = "", 0
    on = per * duty
    d = "M 0 %d" % (y + h)
    while x < w:
        if duty == 0:
            d += " L %d %d" % (min(w, x + per), y + h)
        elif duty >= 1:
            d += " L %d %d L %d %d" % (x, y, min(w, x + per), y)
        else:
            d += " L %d %d L %d %d L %d %d L %d %d" % (x, y, x + on, y, x + on, y + h, min(w, x + per), y + h)
        x += per
    return d
rows = [(0.25, "64", "25 %", 0.3), (0.5, "127", "50 %", 0.55), (1.0, "255", "100 %", 1.0)]
body = """
<div id="@k" class="k-chip k-c-green" style="left:120px;top:120px;font-size:26px;background:#13241A">SAÍDA · analogWrite = PWM</div>
<div id="@b" class="k-card" style="left:120px;top:190px;width:1680px;height:96px;border-color:#7FE39A"><div class="k-body" style="left:30px;top:26px;font-size:30px">Não é saída analógica real: o pino <b class="k-c-green">liga e desliga muito rápido</b> (sinal digital pulsado)</div></div>
"""
for i, (dty, v, pc, op) in enumerate(rows):
    y = 330 + i * 150
    body += ('<div id="@w%d" style="position:absolute;left:0;top:0"><div class="vl">analogWrite(9, <b class="k-c-yel">%s</b>)</div>'
             '<svg style="position:absolute;left:560px;top:%dpx" width="660" height="90"><path d="%s" stroke="#7FE39A" stroke-width="4" fill="none" transform="translate(0,-%d)"/></svg>'
             '<div class="pc" style="top:%dpx">%s ligado</div>'
             '<div class="ld" style="top:%dpx;opacity:%s"></div></div>\n'
             % (i, v, y, pwm(dty, y + 8), y, y + 22, pc, y + 6, op))
    body = body.replace('<div class="vl">', '<div class="vl" style="top:%dpx">' % (y + 20), 1)
body += """
<div id="@dc" class="k-anno k-c-yel" style="left:1540px;top:330px;font-size:23px">% do tempo ligado
= ciclo de trabalho
(duty cycle)</div>
<div id="@pins" class="k-macete" style="left:120px;top:780px;width:1680px;font-size:30px">0 a 255 (8 bits) · só nos pinos com <u>~</u> no Uno: 3, 5, 6, 9, 10, 11</div>
"""
scene("09-pwm", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("b"), C.b);
K.fade(tl, [$("w0"), $("w1"), $("w2")], C.c + 0.6, { s: 1.6 });
K.wipe(tl, $("dc"), C.d + 0.6);
K.macete(tl, $("pins"), C.e);
""", sfx="b:pop@0.2*0.2, c:click-soft@0.6*0.2, e:pop*0.3",
css="""  .vl { position: absolute; left: 120px; white-space: nowrap; font-family: "DM Mono", monospace; font-size: 30px; color: #4FD6EE; }
  .pc { position: absolute; left: 1250px; font-family: "DM Mono", monospace; font-size: 26px; color: #B9C2DA; }
  .ld { position: absolute; left: 1430px; width: 70px; height: 70px; border-radius: 35px; background: #FF6F9C; box-shadow: 0 0 40px #FF6F9C; }
""")
