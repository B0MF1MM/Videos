import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbkit import scene, code_win, lcd, LCD_CSS, lines_hl, hl

NOTE_CSS = """  .nt { position: absolute; left: 1120px; width: 680px; }
  .nt b { position: absolute; left: 26px; top: 16px; font-family: "Hanken Grotesk", sans-serif; font-size: 30px; }
  .nt span { position: absolute; left: 26px; top: 62px; width: 630px; font-family: "Hanken Grotesk", sans-serif; font-size: 24px; line-height: 1.4; color: #B9C2DA; }
"""
def note(nid, top, h, color, cls, title, text, left=1120, width=680):
    return ('<div id="@%s" class="k-card nt" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-color:%s"><b class="%s">%s</b><span>%s</span></div>\n'
            % (nid, left, top, width, h, color, cls, title, text))

# 10 map -----------------------------------------------------------
L = ["const int pinoPotenciometro = A0;", "const int pinoLED = 9;", "int leitura = 0, intensidade = 0;",
     "void setup() {", "  pinMode(pinoLED, OUTPUT);", "  Serial.begin(9600);", "}", "void loop() {",
     "  leitura = analogRead(pinoPotenciometro);", "  intensidade = map(leitura, 0, 1023, 0, 255);",
     "  analogWrite(pinoLED, intensidade);", "  Serial.print(\"Leitura: \");", "  Serial.println(leitura);",
     "  delay(500);", "}"]
body = '<div id="@k" class="k-chip k-c-green" style="left:120px;top:110px;font-size:24px;background:#13241A">QUESTÃO 2 · POTENCIÔMETRO → LED</div>\n'
body += code_win("win", "potenciometro.ino", L, 120, 170, 940, font=23, lh=40)
X0, X1 = 1160, 1740
body += """
<div id="@fm" class="k-code" style="left:1120px;top:180px;font-size:25px">map(valor, <span class="k-c-cyan">deMin, deMax</span>, <span class="k-c-pink">paraMin, paraMax</span>)</div>
<div id="@sa" style="position:absolute;left:0;top:0">
  <div class="sl k-c-cyan" style="top:260px">analogRead · 0 a 1023</div>
  <div class="bar" style="top:300px;background:linear-gradient(90deg,#182238,#4FD6EE)"></div>
  <div class="sv" style="left:%dpx;top:340px">0</div><div class="sv" style="left:%dpx;top:340px">512</div><div class="sv" style="left:%dpx;top:340px">1023</div>
</div>
<div id="@sb" style="position:absolute;left:0;top:0">
  <div class="sl k-c-pink" style="top:430px">analogWrite · 0 a 255</div>
  <div class="bar" style="top:470px;background:linear-gradient(90deg,#182238,#FF6F9C)"></div>
  <div class="sv" style="left:%dpx;top:510px">0</div><div class="sv" style="left:%dpx;top:510px">127</div><div class="sv" style="left:%dpx;top:510px">255</div>
</div>
<svg class="k-svg"><path id="@ar" class="arrow" d="M %d 330 L %d 466 M %d 452 L %d 466 L %d 452" stroke="#FFD24A"/></svg>
<div id="@ex" class="k-anno k-c-yel" style="left:1500px;top:372px;font-size:22px">512 → 127</div>
<div id="@inv" class="k-anno" style="left:1120px;top:580px;font-size:21px"><span class="k-c-cyan">map</span>(solo, <span class="k-c-yel">4095, 1500</span>, 0, 100)
faixa invertida: seco (4095) → 0 %%</div>
<div id="@ans" class="k-chip k-c-green" style="left:1120px;top:700px;font-size:24px;background:#13241A">Q2 → C · map = conversão proporcional</div>
""" % (X0 - 30, (X0 + X1) // 2 - 40, X1 - 60, X0 - 30, (X0 + X1) // 2 - 40, X1 - 50,
       (X0 + X1) // 2, (X0 + X1) // 2, (X0 + X1) // 2 - 12, (X0 + X1) // 2, (X0 + X1) // 2 + 12)
js = 'K.fade(tl, $("k"), C.a);\nK.rise(tl, $("win"), C.a + 0.3);\n'
js += lines_hl([("c0", "C.a + 1.2", "C.b"), ("c1", "C.a + 1.8", "C.b"), ("c4", "C.b", "C.c"), ("c5", "C.b + 2.0", "C.c"),
                ("c8", "C.c", "C.d"), ("c9", "C.d", "C.e + 4"), ("c10", "C.d + 2.0", "C.e + 4"),
                ("c11", "C.f", "C.f + 4.5"), ("c12", "C.f", "C.f + 4.5"), ("c13", "C.f + 2.4", "C.f + 4.5")])
js += """
K.fade(tl, $("sa"), C.c + 0.4);
K.fade(tl, $("sb"), C.d + 0.6);
K.wipe(tl, $("fm"), C.d + 3.0);
K.draw(tl, $("ar"), C.e + 0.4, { d: 0.6 });
K.pop(tl, $("ex"), C.e + 1.0);
K.wipe(tl, $("inv"), C.e + 5.2);
K.pop(tl, $("ans"), C.f + 1.0);
"""
scene("10-map", body, js, sfx="d:pop@3.0*0.2, e:whoosh-short@0.4*0.2, f:pop@1.0*0.25",
      css="""  .sl { position: absolute; left: 1120px; white-space: nowrap; font-family: "DM Mono", monospace; font-size: 24px; }
  .bar { position: absolute; left: %dpx; width: %dpx; height: 26px; border-radius: 13px; }
  .sv { position: absolute; width: 80px; text-align: center; font-family: "DM Mono", monospace; font-size: 21px; color: #B9C2DA; }
""" % (X0, X1 - X0))

# 11 serial --------------------------------------------------------
body = """
<div id="@k" class="k-chip k-c-cyan" style="left:120px;top:120px;font-size:26px">COMUNICAÇÃO SERIAL COM O PC</div>
<div id="@c1" class="k-card" style="left:120px;top:190px;width:820px;height:300px;border-color:#4FD6EE">
  <div class="k-code" style="left:24px;top:24px;font-size:27px;line-height:62px">%s
<span class="k-mute">// 9600 bits/s · ESP32: 115200</span>
%s   <span class="k-mute">// mesma linha</span>
%s <span class="k-mute">// pula linha</span></div>
</div>
<div id="@mon" class="k-win" style="left:1000px;top:190px;width:800px;height:300px"><div class="k-win-bar"><i style="left:22px;background:#FF6F9C"></i><i style="left:46px;background:#FFD24A"></i><i style="left:70px;background:#7FE39A"></i><span>Monitor Serial · 9600 baud</span></div>
  <div id="@out" class="k-code" style="left:24px;top:70px;font-size:28px;line-height:46px;color:#7FE39A">Leitura: 512
Leitura: 518
Leitura: 530</div></div>
<div id="@bd" class="k-card" style="left:120px;top:530px;width:820px;height:260px;border-color:#FF6F9C">
  <div class="k-h2 k-c-pink" style="left:30px;top:24px;font-size:30px">velocidades diferentes</div>
  <div class="k-code" style="left:30px;top:90px;font-size:28px">9600 ≠ 115200</div>
  <div class="k-code k-mute" style="left:30px;top:150px;font-size:28px">→ ÿ�x�Ð� (lixo)</div>
</div>
<div id="@pl" class="k-card" style="left:1000px;top:530px;width:800px;height:260px;border-color:#7FE39A">
  <div class="k-h2 k-c-green" style="left:30px;top:20px;font-size:30px">Serial Plotter · gráfico</div>
  <svg width="740" height="160" style="position:absolute;left:30px;top:80px"><path id="@pw" d="M 0 120 C 60 120, 80 40, 140 50 S 220 130, 280 110 S 360 20, 430 40 S 520 140, 600 90 S 690 30, 740 60" stroke="#7FE39A" stroke-width="4" fill="none"/><path d="M 0 70 L 740 70" stroke="#FF6F9C" stroke-width="2" stroke-dasharray="10 8"/></svg>
</div>
""" % (hl("Serial.begin(9600);"), hl('Serial.print("Leitura: ");'), hl("Serial.println(leitura);"))
scene("11-serial", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("c1"), C.b);
K.rise(tl, $("mon"), C.c);
K.wipe(tl, $("out"), C.c + 1.2, { d: 1.6 });
K.rise(tl, $("bd"), C.d);
K.rise(tl, $("pl"), C.e);
K.draw(tl, $("pw"), C.e + 0.6, { d: 1.6 });
""", sfx="b:pop@0.2*0.2, c:typing@1.2*0.2, d:pop@0.2*0.2, e:pop@0.2*0.2")

# 12 gas -----------------------------------------------------------
L = ["int sensorValue = 0;", "void setup() {", "  pinMode(8, OUTPUT);   // LED", "  pinMode(9, OUTPUT);   // buzzer",
     "  Serial.begin(9600);", "}", "void loop() {", "  sensorValue = analogRead(A0);", "  Serial.println(sensorValue, DEC);",
     "  if (sensorValue > 500) {", "    digitalWrite(8, HIGH);", "    digitalWrite(9, HIGH);", "  } else {",
     "    digitalWrite(8, LOW);", "    digitalWrite(9, LOW);", "  }", "}"]
body = code_win("win", "sensor_gas.ino", L, 120, 150, 920, font=23, lh=40)
body += """
<div id="@mt" style="position:absolute;left:0;top:0">
  <div class="k-anno k-mute" style="left:1120px;top:150px;font-size:22px">leitura do A0</div>
  <div style="position:absolute;left:1120px;top:210px;width:680px;height:34px;border-radius:17px;background:#182238;border:2px solid #2A3656"></div>
  <div id="@fill" style="position:absolute;left:1122px;top:212px;width:676px;height:30px;border-radius:15px;background:linear-gradient(90deg,#4FD6EE,#FF6F9C);transform-origin:0 50%%"></div>
  <div style="position:absolute;left:%dpx;top:196px;width:4px;height:62px;background:#FFD24A"></div>
  <div class="k-anno k-c-yel" style="left:%dpx;top:262px;font-size:20px">limiar 500</div>
</div>
<div id="@led" class="ic" style="left:1150px;top:340px;border-color:#FF6F9C">LED · 8</div>
<div id="@bz" class="ic" style="left:1480px;top:340px;border-color:#FFD24A">buzzer · 9</div>
<div id="@pd" class="k-anno k-c-green" style="left:1120px;top:450px;font-size:23px">padrão limiar: ler → comparar → acionar</div>
<div id="@mq" class="k-card" style="left:1120px;top:530px;width:680px;height:300px;border-color:#B49BFF">
  <div class="k-h2 k-c-violet" style="left:26px;top:18px;font-size:28px">sensores MQ</div>
  <div class="k-body" style="left:26px;top:66px;width:640px;font-size:23px;line-height:1.55">gás ↑ → resistência ↓ → tensão no AO ↑<br><b>MQ-135</b> qualidade do ar<br><b>MQ-4</b> metano · <b>MQ-5</b> GLP (gás de cozinha)<br><span class="k-mute">precisa pré-aquecer e calibrar</span></div>
</div>
""" % (1120 + 680 * 500 // 1023, 1120 + 680 * 500 // 1023 - 60)
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c2", "C.b", "C.c"), ("c3", "C.b + 1.0", "C.c"), ("c7", "C.c", "C.d"), ("c8", "C.c + 2.6", "C.d"),
       ("c9", "C.d", "C.e"), ("c10", "C.d + 2.0", "C.d + 4.2"), ("c11", "C.d + 2.0", "C.d + 4.2"),
       ("c13", "C.d + 4.2", "C.e"), ("c14", "C.d + 4.2", "C.e")])
js += """
K.fade(tl, [$("mt"), $("led"), $("bz")], C.b + 0.4);
tl.set($("fill"), { scaleX: 0.3 }, 0);
tl.to($("fill"), { scaleX: 0.42, duration: 1.5, ease: "power1.inOut" }, C.c + 0.4);
tl.to($("fill"), { scaleX: 0.72, duration: 1.0, ease: "power2.out" }, C.d + 1.2);
tl.to([$("led"), $("bz")], { backgroundColor: "#4A2030", boxShadow: "0 0 40px rgba(255,111,156,0.6)", duration: 0.3 }, C.d + 2.2);
tl.to($("fill"), { scaleX: 0.35, duration: 1.0, ease: "power2.out" }, C.d + 3.4);
tl.to([$("led"), $("bz")], { backgroundColor: "#182238", boxShadow: "0 0 0px rgba(255,111,156,0)", duration: 0.3 }, C.d + 4.4);
K.wipe(tl, $("pd"), C.d + 5.0);
K.rise(tl, $("mq"), C.e);
"""
scene("12-gas", body, js, sfx="d:pop@2.2*0.3, e:pop@0.2*0.2",
      css="  .ic { position: absolute; width: 280px; height: 80px; border-radius: 16px; border: 3px solid; background: #182238; font-family: 'DM Mono', monospace; font-size: 26px; line-height: 74px; text-align: center; color: #EEF1F8; }\n")

# 13 tmp36 ---------------------------------------------------------
L = ["int leitura = analogRead(ps);", "float tensao = leitura * (5.0 / 1023);", "float tempC = (tensao - 0.5) * 100.0;",
     "lcd.clear();", "lcd.setCursor(0, 0);", "lcd.print(\"Temp Atual: \");", "lcd.print(tempC, 1);", "lcd.print(\" C\");",
     "lcd.setCursor(0, 1);", "if (fabs(tempC - ta) < 0.1) lcd.print(\"Igual a: \");",
     "else if (tempC > ta)        lcd.print(\"Acima de: \");", "else                        lcd.print(\"Abaixo de: \");",
     "lcd.print(ta, 1);"]
body = code_win("win", "temperatura_lcd.ino", L, 120, 160, 1000, font=22, lh=40)
body += """
<div id="@ex" class="k-card" style="left:1170px;top:160px;width:630px;height:230px;border-color:#FFD24A">
  <div class="k-code" style="left:26px;top:22px;font-size:25px;line-height:62px">leitura = 153
tensão  = 153×5/1023 = <span class="k-c-yel">0,75 V</span>
tempC   = (0,75−0,5)×100 = <span class="k-c-yel">25,0</span></div>
</div>
%s
<div id="@fb" class="k-anno" style="left:1170px;top:640px;font-size:22px"><span class="k-c-cyan">fabs</span> = valor absoluto (sem sinal)
|25,0 − 22,0| = 3,0 → não é igual
25,0 > 22,0 → <span class="k-c-yel">"Acima de: "</span></div>
""" % lcd("lc", 1170, 430, "Temp Atual: 25.0", "Acima de: 22.0C", cell=36)
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c0", "C.b", "C.c"), ("c1", "C.b", "C.c"), ("c2", "C.c", "C.d"),
       ("c4", "C.d", "C.e"), ("c5", "C.d", "C.e"), ("c6", "C.d + 1.6", "C.e"), ("c7", "C.d + 3.0", "C.e"),
       ("c8", "C.e", "C.e + 8"), ("c9", "C.e + 2.0", "C.e + 8"), ("c10", "C.e + 4.6", "C.e + 8"), ("c11", "C.e + 4.6", "C.e + 8")])
js += """
K.rise(tl, $("ex"), C.b + 0.6);
K.rise(tl, $("lc"), C.d);
tl.set($("lcr1"), { opacity: 0 }, 0);
tl.to($("lcr1"), { opacity: 1, duration: 0.3 }, C.e + 0.6);
K.wipe(tl, $("fb"), C.e + 2.4);
"""
scene("13-tmp36", body, js, sfx="b:pop@0.6*0.2, d:pop*0.2, e:pop@0.6*0.2", css=LCD_CSS)

# 14 pir -----------------------------------------------------------
LA = ["void setup() {", "  pinMode(2, INPUT);", "  pinMode(LED_BUILTIN, OUTPUT);", "}", "void loop() {",
      "  int s = digitalRead(2);", "  if (s == HIGH) digitalWrite(LED_BUILTIN, HIGH);", "  else           digitalWrite(LED_BUILTIN, LOW);",
      "  delay(10);", "}"]
LB = ["void loop() {", "  int movimento = digitalRead(pinoPIR);", "  if (movimento == HIGH) {", "    for (int i = 0; i < 3; i++) {",
      "      digitalWrite(pinoLED, HIGH);", "      delay(1000);", "      digitalWrite(pinoLED, LOW);", "      delay(500);",
      "    }", "  } else {", "    digitalWrite(pinoLED, LOW);", "  }", "}"]
body = '<div id="@k" class="k-chip k-c-violet" style="left:120px;top:110px;font-size:24px">SENSOR PIR · saída digital: HIGH = movimento</div>\n'
body += code_win("wa", "pir_simples.ino", LA, 120, 170, 860, font=21, lh=36, pre="a")
body += code_win("wb", "pir_pisca3.ino", LB, 1010, 170, 790, font=21, lh=36, pre="b")
body += """
<div id="@fr" class="k-anno" style="left:120px;top:600px;font-size:24px"><span class="k-c-violet">for</span> (<span class="k-c-cyan">int i = 0</span>; <span class="k-c-yel">i &lt; 3</span>; <span class="k-c-green">i++</span>)
 <span class="k-c-cyan">início</span>     <span class="k-c-yel">condição</span>  <span class="k-c-green">passo</span>  → 3 voltas</div>
<div id="@led" style="position:absolute;left:1700px;top:110px;width:46px;height:46px;border-radius:23px;background:#FF6F9C;box-shadow:0 0 30px #FF6F9C"></div>
<div id="@mac" class="k-macete" style="left:120px;top:740px;width:1680px;font-size:30px"><u>if</u> decide · <u>for</u> repete um nº de vezes · <u>loop</u> recomeça tudo</div>
"""
js = 'K.fade(tl, $("k"), C.a);\nK.rise(tl, $("wa"), C.b);\n' + lines_hl([("a1", "C.b + 0.8", "C.c"), ("a5", "C.b + 1.6", "C.c"), ("a6", "C.b + 3.2", "C.c"), ("a7", "C.b + 6.2", "C.c")])
js += '\nK.rise(tl, $("wb"), C.c);\n' + lines_hl([("b2", "C.c + 0.6", "C.d"), ("b3", "C.c + 1.6", "C.e"), ("b4", "C.c + 3.0", "C.c + 4.6"), ("b5", "C.c + 3.0", "C.c + 4.6"), ("b6", "C.c + 4.6", "C.d"), ("b7", "C.c + 4.6", "C.d")])
js += """
tl.set($("led"), { opacity: 0 }, 0);
for (var i = 0; i < 3; i++) {
  tl.set($("led"), { opacity: 1 }, C.c + 1.0 + i * 1.5);
  tl.set($("led"), { opacity: 0 }, C.c + 2.0 + i * 1.5);
}
K.wipe(tl, $("fr"), C.d + 0.4);
K.macete(tl, $("mac"), C.e);
"""
scene("14-pir", body, js, sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, e:pop*0.3")

# 15 pir lcd -------------------------------------------------------
L = ["const int pp = 4;  const int ledA = 13;", "int ultE = LOW;    int eventos = 0;", "void loop() {",
     "  int estado = digitalRead(pp);", "  digitalWrite(ledA, estado);", "  if (estado == HIGH && ultE == LOW) {",
     "    eventos++;", "    lcd.clear(); lcd.setCursor(0, 0);", "    lcd.print(\"Move Detectado\");",
     "    lcd.setCursor(0, 1); lcd.print(\"total = \");", "    lcd.print(eventos);",
     "  } else if (estado == LOW && ultE == HIGH) {", "    lcd.clear(); lcd.setCursor(0, 0);", "    lcd.print(\"Area Livre!\");",
     "  }", "  ultE = estado;", "  delay(100);", "}"]
body = code_win("win", "pir_lcd.ino", L, 120, 140, 960, font=21, lh=36)
body += """
<svg id="@sig" class="k-svg"><path d="M 1140 300 L 1220 300 L 1220 210 L 1380 210 L 1380 300 L 1480 300 L 1480 210 L 1640 210 L 1640 300 L 1780 300" stroke="#B49BFF" stroke-width="5" fill="none"/></svg>
<div class="k-anno k-mute" style="left:1140px;top:150px;font-size:20px" id="@sl">estado do PIR</div>
<div id="@u1" class="k-chip k-c-green" style="left:1170px;top:320px;font-size:20px;background:#13241A">↑ +1</div>
<div id="@u2" class="k-chip k-c-green" style="left:1430px;top:320px;font-size:20px;background:#13241A">↑ +1</div>
<div id="@d1" class="k-chip k-c-pink" style="left:1330px;top:380px;font-size:20px;background:#2E1420">↓ livre</div>
%s
%s
<div id="@al" class="k-macete k-alert" style="left:1120px;top:690px;width:680px;font-size:22px">pinMode(2, INPUT) configura o pino 2, mas a leitura é no <b>4</b> (pp). Correto: pinMode(pp, INPUT).</div>
""" % (lcd("l1", 1120, 450, "Move Detectado", "total = 2", cell=38), lcd("l2", 1120, 450, "Area Livre!", "", cell=38))
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c1", "C.b", "C.c"), ("c3", "C.b + 1.0", "C.c"), ("c5", "C.c", "C.d"), ("c6", "C.c + 2.4", "C.d"),
       ("c8", "C.c + 3.4", "C.d"), ("c11", "C.d", "C.e"), ("c13", "C.d + 1.6", "C.e"), ("c15", "C.e", "C.e + 3.0"), ("c0", "C.e + 3.4", "C.e + 9")])
js += """
K.fade(tl, [$("sig"), $("sl")], C.b + 0.6);
tl.set([$("l2")], { opacity: 0 }, 0);
K.pop(tl, [$("u1"), $("u2")], C.c + 0.6, { s: 0.8 });
K.rise(tl, $("l1"), C.c + 3.4);
K.pop(tl, $("d1"), C.d + 0.6);
tl.to($("l1"), { opacity: 0, duration: 0.2 }, C.d + 1.8);
tl.to($("l2"), { opacity: 1, duration: 0.2 }, C.d + 1.8);
K.pop(tl, $("al"), C.e + 3.4);
"""
scene("15-pir-lcd", body, js, sfx="c:pop@0.6*0.2, d:pop@0.6*0.2, e:pop@3.4*0.25", css=LCD_CSS)

# 16 lcd i2c -------------------------------------------------------
L = ["#include <Wire.h>", "#include <LiquidCrystal_I2C.h>", "LiquidCrystal_I2C lcd(0x20, 16, 2);", "void setup() {",
     "  lcd.init();", "  lcd.backlight();", "  lcd.setCursor(0, 0);", "  lcd.print(\"Sistemas\");", "  lcd.setCursor(0, 1);",
     "  lcd.print(\"Embarcados\");", "  delay(1000);", "}", "void loop() {", "  lcd.scrollDisplayRight();", "  delay(300);", "}"]
body = code_win("win", "lcd_i2c.ino", L, 120, 150, 900, font=23, lh=40)
body += """
<div id="@args" class="k-anno" style="left:1080px;top:150px;font-size:23px">lcd(<span class="k-c-yel">0x20</span>, <span class="k-c-cyan">16</span>, <span class="k-c-green">2</span>)
  endereço  colunas  linhas</div>
%s
<div id="@co" style="position:absolute;left:0;top:0">
  <div class="k-chip k-c-yel" style="left:1060px;top:300px;font-size:20px;background:#2A2410">(0,0)</div>
  <div class="k-chip k-c-yel" style="left:1060px;top:364px;font-size:20px;background:#2A2410">(0,1)</div>
</div>
<div id="@cl" class="k-anno k-mute" style="left:1080px;top:510px;font-size:22px">setCursor(<span class="k-c-cyan">coluna</span>, <span class="k-c-green">linha</span>) · começa do 0</div>
<div id="@sc" class="k-anno k-c-cyan" style="left:1080px;top:580px;font-size:22px">scrollDisplayRight() → 1 coluna p/ direita
delay(300) → velocidade</div>
<div id="@ad" class="k-macete" style="left:1080px;top:700px;width:720px;font-size:24px">Aceso e sem texto? Endereço errado: <u>0x20 · 0x27 · 0x3F</u> → scanner I2C</div>
""" % lcd("lc", 1150, 300, "Sistemas", "Embarcados", cell=38)
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c0", "C.b", "C.c"), ("c1", "C.b", "C.c"), ("c2", "C.b + 4.0", "C.c"),
       ("c4", "C.c", "C.d"), ("c5", "C.c + 1.6", "C.d"), ("c6", "C.d", "C.e"), ("c7", "C.d + 3.0", "C.e"), ("c8", "C.d + 4.6", "C.e"), ("c9", "C.d + 6.4", "C.e"),
       ("c13", "C.e", "C.f"), ("c14", "C.e + 2.6", "C.f")])
js += """
K.wipe(tl, $("args"), C.b + 4.4);
K.rise(tl, $("lc"), C.c);
tl.set([$("lcr0"), $("lcr1")], { opacity: 0 }, 0);
K.fade(tl, $("co"), C.d + 1.0);
tl.to($("lcr0"), { opacity: 1, duration: 0.2 }, C.d + 3.0);
tl.to($("lcr1"), { opacity: 1, duration: 0.2 }, C.d + 6.4);
K.fade(tl, $("cl"), C.d + 1.6);
K.wipe(tl, $("sc"), C.e + 0.4);
for (var i = 1; i <= 8; i++) tl.set([$("lcr0"), $("lcr1")], { x: i * 38 }, C.e + 1.0 + i * 0.4);
tl.set([$("lcr0"), $("lcr1")], { x: 0 }, C.f);
K.macete(tl, $("ad"), C.f + 0.4);
"""
scene("16-lcd-i2c", body, js, sfx="c:pop@0.2*0.2, e:click-soft@1.0*0.2, f:pop@0.4*0.3", css=LCD_CSS)

# 17 lcd + dht -----------------------------------------------------
LA = ["#include <LiquidCrystal.h>", "LiquidCrystal lcd(12, 11, 5, 4, 3, 2);", "//                RS  E  D4 D5 D6 D7", "void setup() {", "  lcd.begin(16, 2);", "}"]
LB = ["#include <DHT.h>", "#define DHTPIN A5", "#define DHTTYPE DHT11", "DHT dht(DHTPIN, DHTTYPE);", "void loop() {",
      "  float h = dht.readHumidity();", "  float t = dht.readTemperature();", "  lcd.print(t, 1);", "  delay(2000);   // mínimo do DHT11", "}"]
body = code_win("wa", "lcd_paralelo.ino", LA, 120, 160, 840, font=22, lh=38, pre="a")
body += code_win("wb", "dht11.ino", LB, 1000, 160, 800, font=22, lh=38, pre="b")
body += """
<div id="@n1" class="k-anno k-c-cyan" style="left:120px;top:490px;font-size:22px">sem módulo I2C: 6 pinos (RS, E, D4–D7)
inicia com lcd.begin(16, 2)</div>
%s
<div id="@al" class="k-macete k-alert" style="left:1000px;top:640px;width:800px;font-size:26px">DHT11: no mínimo <b>2 s</b> entre leituras · valores inteiros</div>
""" % lcd("lc", 120, 620, "Temp: 28.0 C", "Umid: 37.0 %", cell=38)
js = 'K.rise(tl, $("wa"), C.b);\n' + lines_hl([("a1", "C.b + 1.6", "C.c"), ("a2", "C.b + 3.0", "C.c"), ("a4", "C.b + 7.0", "C.c")])
js += '\nK.wipe(tl, $("n1"), C.b + 4.0);\nK.rise(tl, $("wb"), C.c);\n' + lines_hl([("b0", "C.c + 0.6", "C.d"), ("b2", "C.c + 1.2", "C.d"), ("b3", "C.c + 2.4", "C.d"),
       ("b5", "C.d + 2.2", "C.e"), ("b6", "C.d", "C.e"), ("b8", "C.e", "C.e + 5")])
js += '\nK.rise(tl, $("lc"), C.d + 1.0);\nK.pop(tl, $("al"), C.e + 0.6);\n'
scene("17-lcd-dht", body, js, sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, e:pop@0.6*0.25", css=LCD_CSS)

# 18 atuador -------------------------------------------------------
body = """
<div id="@k" class="k-chip k-c-pink" style="left:120px;top:120px;font-size:26px;background:#2E1420">QUESTÃO 7 · ATUADORES</div>
<div id="@mcu" class="bk" style="left:120px;top:250px;border-color:#FFD24A"><b class="k-c-yel">microcontrolador</b><span>pino GPIO: só ~20–40 mA</span></div>
<div id="@pump" class="bk" style="left:1300px;top:250px;border-color:#FF6F9C"><b class="k-c-pink">bomba / motor</b><span>centenas de mA · 12 V</span></div>
<svg class="k-svg"><path id="@dir" d="M 620 330 L 1290 330" stroke="#FF6F9C" stroke-width="5" stroke-dasharray="14 10" fill="none"/>
<path id="@x" d="M 930 290 L 1000 370 M 1000 290 L 930 370" stroke="#FF6F9C" stroke-width="10" fill="none" stroke-linecap="round"/></svg>
<div id="@rl" class="bk" style="left:710px;top:470px;border-color:#7FE39A"><b class="k-c-green">relé · transistor · driver</b><span>circuito intermediário</span></div>
<div id="@src" class="bk" style="left:1300px;top:470px;border-color:#8C97B5"><b>fonte própria</b><span>energia da carga</span></div>
<svg class="k-svg"><path id="@p1" class="arrow" d="M 370 410 L 370 550 L 700 550 M 684 538 L 700 550 L 684 562" stroke="#FFD24A"/><path id="@p2" class="arrow" d="M 1210 550 L 1270 550 L 1270 380 L 1294 380 M 1280 368 L 1294 380 L 1280 392" stroke="#7FE39A"/></svg>
<div id="@cm" class="k-anno k-c-yel" style="left:390px;top:480px;font-size:20px">comando</div>
<div id="@lg" class="k-card" style="left:120px;top:690px;width:900px;height:130px;border-color:#7FE39A"><div class="k-body" style="left:30px;top:22px;font-size:28px;line-height:1.5">módulo relé: <b class="k-c-yel">LOW → liga</b> · <b class="k-c-mute">HIGH → desliga</b><br><span class="k-mute" style="font-size:24px">lógica invertida</span></div></div>
<div id="@al" class="k-macete k-alert" style="left:1060px;top:690px;width:740px;font-size:24px">A carga pode estar na <b>rede elétrica</b> (110/220 V): cuidado!</div>
<div id="@ans" class="k-chip k-c-green" style="left:1500px;top:120px;font-size:26px;background:#13241A">Q7 → alternativa D</div>
"""
scene("18-atuador", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, [$("mcu"), $("pump")], C.b, { s: 0.6 });
tl.set($("x"), { opacity: 0 }, 0);
K.fade(tl, $("dir"), C.b + 4.0);
K.pop(tl, $("x"), C.c);
K.rise(tl, $("rl"), C.c + 1.6);
K.draw(tl, $("p1"), C.d, { d: 0.6 });
K.fade(tl, $("cm"), C.d + 0.4);
K.rise(tl, $("src"), C.d + 2.0);
K.draw(tl, $("p2"), C.d + 3.0, { d: 0.6 });
K.rise(tl, $("lg"), C.e);
K.pop(tl, $("al"), C.f);
K.pop(tl, $("ans"), C.f + 2.0);
""", sfx="c:pop*0.3, d:whoosh-short@0.2*0.2, e:pop@0.2*0.2, f:pop*0.3",
css="""  .bk { position: absolute; width: 500px; height: 160px; border-radius: 20px; border: 3px solid; background: #182238; }
  .bk b { position: absolute; left: 28px; top: 28px; font-family: "Hanken Grotesk", sans-serif; font-size: 34px; }
  .bk span { position: absolute; left: 28px; top: 92px; font-family: "DM Mono", monospace; font-size: 22px; color: #B9C2DA; }
""")

# 19 rele codigos --------------------------------------------------
LA = ["int porta_rele1 = 7;", "int porta_rele2 = 8;", "void setup() {", "  pinMode(porta_rele1, OUTPUT);", "  pinMode(porta_rele2, OUTPUT);", "}",
      "void loop() {", "  digitalWrite(porta_rele1, LOW);   // liga 1", "  digitalWrite(porta_rele2, HIGH);  // desliga 2", "  delay(2000);",
      "  digitalWrite(porta_rele1, HIGH);  // desliga 1", "  digitalWrite(porta_rele2, LOW);   // liga 2", "  delay(2000);", "}"]
LB = ["leitura1 = digitalRead(porta_botao1);", "if (leitura1 != 0) {            // apertou?", "  while (digitalRead(porta_botao1) != 0) {",
      "    delay(100);                 // espera soltar", "  }", "  estadorele1 = !estadorele1;   // inverte",
      "  digitalWrite(porta_rele1, estadorele1);", "}"]
body = code_win("wa", "rele_alterna.ino", LA, 120, 150, 880, font=21, lh=36, pre="a")
body += code_win("wb", "rele_botao.ino", LB, 1030, 150, 770, font=20, lh=38, pre="b")
body += """
<div id="@lp" style="position:absolute;left:0;top:0">
  <div id="@g1" class="lmp" style="left:1060px;top:560px"></div><div class="k-anno k-mute" style="left:1150px;top:572px;font-size:20px">lâmpada 1</div>
  <div id="@g2" class="lmp" style="left:1420px;top:560px"></div><div class="k-anno k-mute" style="left:1510px;top:572px;font-size:20px">lâmpada 2</div>
</div>
<div id="@nt" class="k-macete" style="left:1030px;top:700px;width:770px;font-size:26px"><u>!</u> = NÃO lógico: !1 = 0 · !0 = 1 → cada clique troca</div>
"""
js = 'K.rise(tl, $("wa"), C.b);\n' + lines_hl([("a0", "C.b + 2.0", "C.c"), ("a1", "C.b + 3.4", "C.c"), ("a7", "C.c", "C.c + 3.4"), ("a8", "C.c", "C.c + 3.4"),
       ("a10", "C.c + 3.4", "C.d"), ("a11", "C.c + 3.4", "C.d")])
js += """
K.fade(tl, $("lp"), C.c);
tl.set([$("g1"), $("g2")], { opacity: 0.25 }, 0);
tl.set($("g1"), { opacity: 1 }, C.c + 0.4);
tl.set($("g1"), { opacity: 0.25 }, C.c + 3.4);
tl.set($("g2"), { opacity: 1 }, C.c + 3.4);
tl.to($("lp"), { opacity: 0, duration: 0.3 }, C.d - 0.2);
K.rise(tl, $("wb"), C.d);
""" + lines_hl([("b0", "C.d + 1.6", "C.d + 3.4"), ("b1", "C.d + 2.0", "C.d + 3.4"), ("b2", "C.d + 3.4", "C.d + 5.4"), ("b3", "C.d + 3.4", "C.d + 5.4"), ("b5", "C.d + 5.4", "C.e + 4")]) + """
K.macete(tl, $("nt"), C.e);
"""
scene("19-rele-cod", body, js, sfx="b:pop@0.2*0.2, c:click-soft@0.4*0.25, d:pop@0.2*0.2, e:pop*0.3",
      css="  .lmp { position: absolute; width: 70px; height: 70px; border-radius: 35px; background: #FFD24A; box-shadow: 0 0 40px #FFD24A; }\n")
