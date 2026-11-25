import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbkit import scene, code_win, lcd, LCD_CSS, lines_hl, hl

BOX_CSS = """  .bk { position: absolute; border-radius: 20px; border: 3px solid; background: #182238; }
  .bk b { position: absolute; left: 24px; top: 20px; font-family: "Hanken Grotesk", sans-serif; font-size: 30px; }
  .bk span { position: absolute; left: 24px; top: 70px; font-family: "DM Mono", monospace; font-size: 20px; line-height: 1.45; color: #B9C2DA; white-space: pre-line; }
"""

# 20 tone + ohm ----------------------------------------------------
L = ["void setup() { Serial.begin(9600); }", "void loop() {", "  Serial.println(\"A frequencia é de: 50 Hz\");", "  tone(6, 50);   // 50 Hz no pino 6", "  delay(2000);", "}"]
body = code_win("win", "tone.ino", L, 120, 160, 860, font=22, lh=40)
sq = "M 0 90 " + " ".join("L %d 90 L %d 20 L %d 20 L %d 90" % (x, x, x + 40, x + 40) for x in range(0, 640, 80))
body += """
<div id="@osc" class="k-card" style="left:120px;top:520px;width:860px;height:290px;border-color:#FFD24A">
  <div class="k-h2 k-c-yel" style="left:28px;top:18px;font-size:28px">osciloscópio</div>
  <svg width="800" height="140" style="position:absolute;left:30px;top:90px"><path d="M 0 55 L 800 55 M 400 0 L 400 140" stroke="#2A3656" stroke-width="2"/><path id="@wv" d="%s" stroke="#FFD24A" stroke-width="4" fill="none" transform="translate(80,10)"/></svg>
</div>
<div id="@oh" class="k-card" style="left:1040px;top:160px;width:760px;height:430px;border-color:#7FE39A">
  <div class="k-h2 k-c-green" style="left:30px;top:24px;font-size:34px">Lei de Ohm · V = R × I</div>
  <div id="@calc" class="k-code" style="left:30px;top:100px;font-size:27px;line-height:1.65">pino: 5 V
LED vermelho: 2 V · 20 mA
R = (5 − 2) / 0,02
R = <span class="k-c-yel">150 Ω</span></div>
</div>
<div id="@t1" class="k-chip k-c-pink" style="left:1040px;top:630px;font-size:24px;background:#2E1420">sem resistor → o LED queima</div>
<div id="@t2" class="k-chip k-c-cyan" style="left:1040px;top:710px;font-size:24px">perna maior = anodo (+)</div>
""" % sq
js = 'K.rise(tl, $("win"), C.b);\n' + lines_hl([("c2", "C.b + 1.0", "C.c"), ("c3", "C.b + 2.0", "C.c"), ("c4", "C.b + 4.6", "C.c")])
js += """
K.rise(tl, $("osc"), C.b + 3.0);
K.draw(tl, $("wv"), C.b + 3.6, { d: 1.4 });
K.rise(tl, $("oh"), C.c);
K.wipe(tl, $("calc"), C.d, { d: 1.4 });
K.pop(tl, $("t1"), C.e);
K.pop(tl, $("t2"), C.e + 2.2);
"""
scene("20-tone-ohm", body, js, sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, e:pop*0.25")

# 21 UART ----------------------------------------------------------
body = """
<div id="@k" class="k-chip k-c-pink" style="left:120px;top:120px;font-size:26px;background:#2E1420">QUESTÃO 5 · UART</div>
<div id="@as" class="k-h2" style="left:120px;top:190px;font-size:44px">serial <span class="k-c-pink">assíncrona</span> · <span class="k-mute">sem fio de clock</span></div>
<div id="@d1" class="bk" style="left:200px;top:320px;width:420px;height:300px;border-color:#FFD24A"><b class="k-c-yel">Arduino</b></div>
<div id="@d2" class="bk" style="left:1300px;top:320px;width:420px;height:300px;border-color:#4FD6EE"><b class="k-c-cyan">PC / GPS / Bluetooth</b></div>
<div class="pn" id="@t1" style="left:540px;top:400px">TX</div><div class="pn" id="@r1" style="left:540px;top:520px">RX</div>
<div class="pn" id="@r2" style="left:1320px;top:400px">RX</div><div class="pn" id="@t2" style="left:1320px;top:520px">TX</div>
<svg class="k-svg"><path id="@l1" class="arrow" d="M 620 425 C 900 425, 1020 425, 1310 425 M 1294 413 L 1310 425 L 1294 437" stroke="#FFD24A"/><path id="@l2" class="arrow" d="M 1310 545 C 1020 545, 900 545, 620 545 M 636 533 L 620 545 L 636 557" stroke="#4FD6EE"/></svg>
<div id="@cz" class="k-anno k-mute" style="left:800px;top:455px;font-size:22px">TX de um → RX do outro</div>
<div id="@bd" class="k-macete" style="left:120px;top:680px;width:1100px;font-size:28px">Os dois lados com o <u>mesmo baud rate</u> (ex.: 9600) · ponto a ponto</div>
<div id="@ans" class="k-chip k-c-green" style="left:1300px;top:700px;font-size:26px;background:#13241A">Q5 → alternativa D</div>
"""
scene("21-uart", body, """
K.fade(tl, $("k"), C.a);
K.wipe(tl, $("as"), C.b);
K.rise(tl, [$("d1"), $("d2")], C.c, { s: 0.3 });
K.pop(tl, [$("t1"), $("r1"), $("r2"), $("t2")], C.c + 1.0, { s: 0.3 });
K.draw(tl, $("l1"), C.c + 4.0, { d: 0.6 });
K.draw(tl, $("l2"), C.c + 4.8, { d: 0.6 });
K.fade(tl, $("cz"), C.c + 5.4);
K.macete(tl, $("bd"), C.d);
K.pop(tl, $("ans"), C.e + 3.0);
""", sfx="c:pop@1.0*0.2, d:pop*0.3, e:pop@3.0*0.25",
css=BOX_CSS + "  .pn { position: absolute; width: 80px; height: 50px; border-radius: 10px; background: #0D1322; border: 2px solid #8C97B5; font-family: 'DM Mono', monospace; font-size: 24px; line-height: 46px; text-align: center; color: #EEF1F8; }\n")

# 22 I2C -----------------------------------------------------------
devs = [("lcd", "LCD 16×2", "0x27", 760), ("tmp", "sensor temp.", "0x48", 1130), ("rtc", "relógio RTC", "0x68", 1500)]
body = """
<div id="@k" class="k-chip k-c-pink" style="left:120px;top:120px;font-size:26px;background:#2E1420">QUESTÃO 6 · I2C</div>
<div id="@mst" class="bk" style="left:120px;top:300px;width:400px;height:220px;border-color:#FFD24A"><b class="k-c-yel">mestre</b><span>microcontrolador
chama pelo endereço</span></div>
<svg class="k-svg"><path id="@sda" d="M 520 360 L 1800 360" stroke="#7FE39A" stroke-width="6"/><path id="@scl" d="M 520 450 L 1800 450" stroke="#B49BFF" stroke-width="6"/></svg>
<div id="@ls" class="k-anno k-c-green" style="left:540px;top:300px;font-size:22px">SDA · dados</div>
<div id="@lc" class="k-anno k-c-violet" style="left:540px;top:470px;font-size:22px">SCL · clock</div>
"""
for did, name, addr, x in devs:
    body += ('<div id="@%s" style="position:absolute;left:0;top:0"><svg class="k-svg"><path d="M %d 360 L %d 560 M %d 450 L %d 560" stroke="#8C97B5" stroke-width="3"/></svg>'
             '<div id="@%sb" class="bk" style="left:%dpx;top:560px;width:300px;height:140px;border-color:#4FD6EE"><b class="k-c-cyan">%s</b><span>endereço %s</span></div></div>\n'
             % (did, x + 120, x + 120, x + 180, x + 180, did, x, name, addr))
body += """
<div id="@pk" class="k-chip k-c-yel" style="left:560px;top:330px;font-size:22px;background:#2A2410">0x27?</div>
<div id="@e32" class="k-chip k-c-cyan" style="left:120px;top:760px;font-size:24px">ESP32: SDA = GPIO 21 · SCL = GPIO 22</div>
<div id="@ans" class="k-chip k-c-green" style="left:1500px;top:120px;font-size:26px;background:#13241A">Q6 → alternativa C</div>
"""
scene("22-i2c", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("mst"), C.b);
K.draw(tl, [$("sda"), $("scl")], C.b + 0.4, { d: 0.8 });
K.fade(tl, [$("ls"), $("lc")], C.b + 1.2, { s: 2.0 });
K.rise(tl, [$("lcd"), $("tmp"), $("rtc")], C.c, { s: 0.5 });
tl.set($("pk"), { opacity: 0 }, 0);
tl.to($("pk"), { opacity: 1, duration: 0.2 }, C.d + 1.8);
tl.to($("pk"), { x: 300, duration: 1.0, ease: "power1.inOut" }, C.d + 2.0);
tl.to($("pk"), { opacity: 0, duration: 0.2 }, C.d + 3.0);
tl.to([$("tmpb"), $("rtcb")], { opacity: 0.3, duration: 0.3 }, C.d + 3.0);
tl.to($("lcdb"), { borderColor: "#FFD24A", boxShadow: "0 0 40px rgba(255,210,74,0.5)", duration: 0.3 }, C.d + 3.0);
tl.to([$("tmpb"), $("rtcb")], { opacity: 1, duration: 0.3 }, C.e);
K.pop(tl, $("e32"), C.e + 6.0);
K.pop(tl, $("ans"), C.e + 8.0);
""", sfx="b:whoosh-short@0.4*0.2, c:pop@0.2*0.2, d:click-soft@3.0*0.3, e:pop@6.0*0.25", css=BOX_CSS)

# 23 protocolos ----------------------------------------------------
def pc(pid, left, color, cls, name, items):
    li = "".join("<div>%s</div>" % i for i in items)
    return ('<div id="@%s" class="k-card pr" style="left:%dpx;border-color:%s"><div class="nm %s">%s</div><div class="li">%s</div></div>\n'
            % (pid, left, color, cls, name, li))
body = pc("u", 120, "#FF6F9C", "k-c-pink", "UART", ["assíncrona", "<b>TX</b> e <b>RX</b> (2 fios)", "velocidade: baud rate", "ponto a ponto", "ex.: PC, GPS, Bluetooth"])
body += pc("s", 690, "#FFD24A", "k-c-yel", "SPI", ["síncrona", "<b>MOSI, MISO, SCK, SS</b> (4)", "rápida", "um SS por dispositivo · sem endereço", "ex.: cartão SD, RFID"])
body += pc("i", 1260, "#7FE39A", "k-c-green", "I2C", ["síncrona", "<b>SDA</b> e <b>SCL</b> (2 fios)", "100 / 400 kbps", "vários por <b>endereço</b>", "ex.: LCD, BMP180, RTC"])
body += '<div id="@mac" class="k-macete" style="left:120px;top:720px;width:1680px;font-size:30px">SDA/SCL = <u>I2C</u> · TX/RX = <u>UART</u> · MOSI/MISO = <u>SPI</u></div>'
scene("23-protocolos", body, """
K.rise(tl, $("u"), C.b);
K.rise(tl, $("s"), C.c);
K.rise(tl, $("i"), C.d);
K.macete(tl, $("mac"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop*0.3",
css="""  .pr { top: 170px; width: 540px; height: 500px; }
  .pr .nm { position: absolute; left: 30px; top: 26px; font-family: "DM Mono", monospace; font-size: 48px; }
  .pr .li { position: absolute; left: 30px; top: 120px; width: 480px; }
  .pr .li div { font-family: "Hanken Grotesk", sans-serif; font-size: 27px; line-height: 68px; border-bottom: 1px solid #2A3656; color: #EEF1F8; }
""")

# 24 esp32 ---------------------------------------------------------
body = """
<div id="@chip" class="k-card" style="left:120px;top:170px;width:700px;height:420px;border-color:#4FD6EE">
  <div class="k-h2 k-c-cyan" style="left:32px;top:26px;font-size:48px">ESP32</div>
  <div class="k-body" style="left:32px;top:110px;width:640px;font-size:30px;line-height:1.7">Wi-Fi + Bluetooth integrados<br>2 núcleos (dual core)<br>trabalha em <b class="k-c-yel">3,3 V</b><br>ADC de 12 bits (0 a 4095)</div>
</div>
<div id="@p1" class="k-card pw" style="top:170px;border-color:#FF6F9C"><b class="k-c-pink">GPIO 6 a 11</b><span>não usar · memória flash</span></div>
<div id="@p2" class="k-card pw" style="top:300px;border-color:#FFD24A"><b class="k-c-yel">GPIO 34, 35, 36, 39</b><span>só entrada</span></div>
<div id="@p3" class="k-card pw" style="top:430px;border-color:#7FE39A"><b class="k-c-green">Wi-Fi ligado → ADC1</b><span>GPIO 32 a 39 · o ADC2 não funciona</span></div>
<div id="@dv" class="k-card" style="left:120px;top:630px;width:1680px;height:170px;border-color:#B49BFF">
  <div class="k-body" style="left:32px;top:26px;font-size:28px">sensor de <b>5 V</b> → <b class="k-c-violet">divisor de tensão</b> (ex.: 10 kΩ + 20 kΩ) → <b class="k-c-yel">≤ 3,3 V</b> no pino</div>
  <div class="k-code" style="left:32px;top:90px;font-size:26px">5 V × 20k / (10k + 20k) = <span class="k-c-yel">3,3 V</span></div>
</div>
"""
scene("24-esp32", body, """
K.rise(tl, $("chip"), C.a + 0.3);
K.rise(tl, $("p1"), C.c);
K.rise(tl, $("p2"), C.c + 4.0);
K.rise(tl, $("p3"), C.d);
K.rise(tl, $("dv"), C.e);
""", sfx="c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop@0.2*0.2",
css="""  .pw { left: 880px; width: 920px; height: 110px; }
  .pw b { position: absolute; left: 28px; top: 14px; font-family: "DM Mono", monospace; font-size: 32px; }
  .pw span { position: absolute; left: 28px; top: 62px; font-family: "Hanken Grotesk", sans-serif; font-size: 25px; color: #B9C2DA; }
""")

# 25 esp32 codigo --------------------------------------------------
def cc(cid, top, color, cls, title, lines, h):
    code = "\n".join(hl(l) for l in lines)
    return ('<div id="@%s" class="k-card" style="left:120px;top:%dpx;width:1680px;height:%dpx;border-color:%s">'
            '<div class="k-h2 %s" style="left:30px;top:18px;font-size:28px">%s</div>'
            '<div class="k-code" style="left:30px;top:66px;font-size:24px;line-height:1.5">%s</div></div>\n'
            % (cid, top, h, color, cls, title, code))
body = cc("i1", 160, "#FF6F9C", "k-c-pink", "interrupção · a ISR é curta e roda na hora do evento",
          ["attachInterrupt(digitalPinToInterrupt(14), botaoISR, FALLING);", "void IRAM_ATTR botaoISR() { cont++; }   // só marca o evento"], 180)
body += cc("i2", 360, "#FFD24A", "k-c-yel", "millis() / timer · sem travar o loop (delay trava)",
           ["if (millis() - tAnterior >= 1000) {   // passou 1 s?", "  tAnterior = millis();   // lê e envia }"], 180)
body += cc("i3", 560, "#7FE39A", "k-c-green", "deep sleep · dorme e acorda sozinho",
           ["esp_sleep_enable_timer_wakeup(10ULL * 1000000ULL);  // 10 s em µs", "esp_deep_sleep_start();"], 180)
body += '<div id="@cs" class="k-chip k-c-green" style="left:120px;top:770px;font-size:26px;background:#13241A">ativo: 80–260 mA → deep sleep: 10–150 µA · ideal para bateria</div>'
scene("25-esp32-cod", body, """
K.rise(tl, $("i1"), C.b);
K.rise(tl, $("i2"), C.c);
K.rise(tl, $("i3"), C.d);
K.pop(tl, $("cs"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop*0.25")

# 26 IoT -----------------------------------------------------------
nodes = [("n1", "sensores", "medem", "#4FD6EE", "k-c-cyan"), ("n2", "ESP32", "processa + Wi-Fi", "#FFD24A", "k-c-yel"),
         ("n3", "servidor", "HTTP / MQTT", "#FF6F9C", "k-c-pink"), ("n4", "banco", "guarda", "#B49BFF", "k-c-violet"),
         ("n5", "dashboard", "mostra + alerta", "#7FE39A", "k-c-green")]
body = '<div id="@k" class="k-chip k-c-pink" style="left:120px;top:120px;font-size:26px;background:#2E1420">QUESTÃO 8 · IoT E DASHBOARD</div>\n'
arrows = ""
for i, (nid, t, s, col, cls) in enumerate(nodes):
    x = 120 + i * 344
    body += '<div id="@%s" class="bk" style="left:%dpx;top:200px;width:300px;height:150px;border-color:%s"><b class="%s">%s</b><span>%s</span></div>\n' % (nid, x, col, cls, t, s)
    if i < 4:
        arrows += '<path id="@a%d" class="arrow" d="M %d 275 L %d 275 M %d 265 L %d 275 L %d 285" stroke="#8C97B5"/>' % (i, x + 304, x + 340, x + 330, x + 340, x + 330)
body += '<svg class="k-svg">%s</svg>\n' % arrows
body += """
<div id="@db" class="k-card" style="left:120px;top:400px;width:1100px;height:380px;border-color:#7FE39A">
  <div class="k-h2 k-c-green" style="left:30px;top:20px;font-size:28px">painel em tempo real</div>
  <div class="gg"><b class="k-c-cyan">24,6 °C</b><span>temperatura</span></div>
  <div class="gg" style="left:300px"><b class="k-c-green">41 %</b><span>umidade do solo</span></div>
  <svg width="420" height="170" style="position:absolute;left:600px;top:90px"><path d="M 0 140 L 60 120 L 120 130 L 180 80 L 240 95 L 300 50 L 360 70 L 420 30" stroke="#4FD6EE" stroke-width="4" fill="none"/></svg>
  <div class="k-chip k-c-pink" style="left:30px;top:290px;font-size:22px;background:#2E1420">alerta: solo seco</div>
  <div class="k-chip k-c-yel" style="left:330px;top:290px;font-size:22px;background:#2A2410">ligar bomba (remoto)</div>
</div>
<div id="@al" class="k-macete k-alert" style="left:1260px;top:400px;width:540px;font-size:24px">O dashboard <b>não mede</b> e não substitui sensor nem firmware.</div>
<div id="@ans" class="k-chip k-c-green" style="left:1260px;top:640px;font-size:26px;background:#13241A">Q8 → alternativa B</div>
"""
scene("26-iot", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, [$("n1"), $("n2")], C.b, { s: 1.2 });
K.fade(tl, $("a0"), C.b + 0.8);
K.fade(tl, $("a1"), C.c);
K.rise(tl, [$("n3"), $("n4")], C.c + 0.2, { s: 2.6 });
K.fade(tl, $("a2"), C.c + 2.6);
K.fade(tl, $("a3"), C.d);
K.rise(tl, $("n5"), C.d + 0.2);
K.rise(tl, $("db"), C.d + 1.4);
K.pop(tl, $("al"), C.e);
K.pop(tl, $("ans"), C.e + 4.0);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@1.4*0.2, e:pop*0.3",
css=BOX_CSS + """  .gg { position: absolute; left: 30px; top: 90px; width: 240px; height: 170px; border-radius: 16px; background: #0D1322; border: 2px solid #2A3656; }
  .gg b { position: absolute; left: 20px; top: 30px; font-family: "DM Mono", monospace; font-size: 44px; }
  .gg span { position: absolute; left: 20px; top: 110px; font-family: "Hanken Grotesk", sans-serif; font-size: 22px; color: #8C97B5; }
""")

# 27 http ----------------------------------------------------------
L = ["#include <WiFi.h>", "#include <HTTPClient.h>", "void setup() {", "  Serial.begin(115200);", "  WiFi.begin(ssid, senha);",
     "  while (WiFi.status() != WL_CONNECTED) {", "    delay(500); Serial.print(\".\");", "  }", "}", "void loop() {",
     "  HTTPClient http;", "  http.begin(site + \"temp=\" + String(25.4));", "  int codigo = http.GET();   // 200 = OK",
     "  Serial.println(codigo);", "  http.end();", "  delay(10000);              // a cada 10 s", "}"]
body = code_win("win", "envio_wifi.ino", L, 120, 140, 1000, font=22, lh=38)
body += """
<div id="@n1" class="k-card nt" style="top:140px;height:150px;border-color:#4FD6EE"><b class="k-c-cyan">conectar</b><span>WiFi.begin(rede, senha) e o while espera WL_CONNECTED</span></div>
<div id="@n2" class="k-card nt" style="top:320px;height:150px;border-color:#FFD24A"><b class="k-c-yel">enviar</b><span>monta a URL com os valores e faz um GET para o servidor</span></div>
<div id="@n3" class="k-card nt" style="top:500px;height:150px;border-color:#7FE39A"><b class="k-c-green">conferir e repetir</b><span>200 = OK · http.end() fecha · espera 10 s</span></div>
"""
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c0", "C.a + 1.6", "C.b"), ("c1", "C.a + 1.6", "C.b"), ("c4", "C.b + 2.4", "C.c"), ("c5", "C.b + 4.0", "C.c"),
       ("c11", "C.c + 0.4", "C.d"), ("c12", "C.c + 3.0", "C.d"), ("c12", "C.d", "C.d + 2.0"), ("c14", "C.d + 2.0", "C.d + 6"), ("c15", "C.d + 4.0", "C.d + 7")])
js += '\nK.rise(tl, $("n1"), C.b);\nK.rise(tl, $("n2"), C.c);\nK.rise(tl, $("n3"), C.d);\n'
scene("27-http", body, js, sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2",
      css="""  .nt { left: 1170px; width: 630px; }
  .nt b { position: absolute; left: 26px; top: 16px; font-family: "Hanken Grotesk", sans-serif; font-size: 30px; }
  .nt span { position: absolute; left: 26px; top: 64px; width: 580px; font-family: "Hanken Grotesk", sans-serif; font-size: 24px; line-height: 1.4; color: #B9C2DA; }
""")

# 28 ROI -----------------------------------------------------------
body = """
<div id="@k" class="k-chip k-c-yel" style="left:120px;top:120px;font-size:26px;background:#2A2410">QUESTÃO 9 · ROI E PAYBACK</div>
<div id="@r" class="k-card fm" style="left:120px;border-color:#FFD24A"><b class="k-c-yel">ROI · percentual</b><div class="k-code ft">ROI = (benefício − investimento)
      ÷ investimento × 100</div></div>
<div id="@p" class="k-card fm" style="left:980px;border-color:#4FD6EE"><b class="k-c-cyan">Payback · tempo</b><div class="k-code ft">Payback = investimento
          ÷ benefício líquido mensal</div></div>
<div id="@ex" class="k-card" style="left:120px;top:430px;width:1680px;height:280px;border-color:#7FE39A">
  <div class="k-body" style="left:32px;top:24px;font-size:27px">investimento <b>R$ 8.000</b> · economia <b>R$ 1.000/mês</b> · custo <b>R$ 200/mês</b> → líquido <b class="k-c-green">R$ 800/mês</b></div>
  <div id="@pb" class="k-code" style="left:32px;top:100px;font-size:32px">Payback = 8.000 ÷ 800 = <span class="k-c-cyan">10 meses</span></div>
  <div id="@ro" class="k-code" style="left:32px;top:170px;font-size:32px">ROI 12 m = (9.600 − 8.000) ÷ 8.000 = <span class="k-c-yel">20 %</span></div>
</div>
<div id="@mac" class="k-macete" style="left:120px;top:740px;width:1680px;font-size:28px">ROI = <u>%</u> · Payback = <u>tempo</u> · ROI positivo não garante que o sistema não falhe</div>
<div id="@ans" class="k-chip k-c-green" style="left:1500px;top:120px;font-size:26px;background:#13241A">Q9 → alternativa C</div>
"""
scene("28-roi", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("r"), C.b);
K.rise(tl, $("p"), C.c);
K.rise(tl, $("ex"), C.d);
tl.set([$("pb"), $("ro")], { opacity: 0 }, 0);
tl.to($("pb"), { opacity: 1, duration: 0.4 }, C.d + 8.0);
tl.to($("ro"), { opacity: 1, duration: 0.4 }, C.e);
K.macete(tl, $("mac"), C.f);
K.pop(tl, $("ans"), C.f + 3.0);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop*0.25, f:pop*0.3",
css="""  .fm { top: 190px; width: 820px; height: 200px; }
  .fm b { position: absolute; left: 30px; top: 22px; font-family: "Hanken Grotesk", sans-serif; font-size: 34px; }
  .fm .ft { left: 30px; top: 86px; font-size: 27px; line-height: 1.5; }
""")

# 29 KPIs ----------------------------------------------------------
def kc(cid, left, top, color, cls, title, text):
    return ('<div id="@%s" class="k-card kc" style="left:%dpx;top:%dpx;border-color:%s"><b class="%s">%s</b><span>%s</span></div>\n'
            % (cid, left, top, color, cls, title, text))
body = kc("k1", 120, 170, "#4FD6EE", "k-c-cyan", "latência · disponibilidade", "latência = detecção + processamento + comunicação + acionamento<br>disponibilidade = tempo funcionando ÷ tempo total × 100")
body += kc("k2", 980, 170, "#FFD24A", "k-c-yel", "acurácia × precisão", "acurácia: perto do valor real<br>precisão: repete o mesmo valor<br>real 25 °C, lê 28 / 28,1 / 27,9 → preciso, pouco acurado")
body += kc("k3", 120, 480, "#7FE39A", "k-c-green", "requisitos", "funcional: <strong>o que</strong> faz (detectar presença)<br>não funcional: <strong>como</strong> (consumo, custo, em até 100 ms)")
body += kc("k4", 980, 480, "#FF6F9C", "k-c-pink", "trade-off · protótipo ≠ produto", "melhorar uma coisa piora outra<br>produto: placa própria (PCB), certificação, testes")
scene("29-kpi", body, """
K.rise(tl, $("k1"), C.b);
K.rise(tl, $("k2"), C.c);
K.rise(tl, $("k3"), C.d);
K.rise(tl, $("k4"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop@0.2*0.2",
css="""  .kc { width: 820px; height: 280px; }
  .kc b { position: absolute; left: 30px; top: 24px; font-family: "Hanken Grotesk", sans-serif; font-size: 34px; }
  .kc span { position: absolute; left: 30px; top: 88px; width: 760px; font-family: "Hanken Grotesk", sans-serif; font-size: 25px; line-height: 1.6; color: #D5DBEA; }
""")

# 30 Q10 arquitetura ----------------------------------------------
body = """
<div id="@k" class="k-chip k-c-violet" style="left:120px;top:120px;font-size:26px">QUESTÃO 10 · IRRIGAÇÃO AUTOMÁTICA</div>
<div id="@s" class="bk" style="left:120px;top:250px;width:420px;height:200px;border-color:#4FD6EE"><b class="k-c-cyan">ENTRADA</b><span>sensor de umidade do solo
(+ temperatura, chuva)</span></div>
<div id="@m" class="bk" style="left:750px;top:250px;width:420px;height:200px;border-color:#FFD24A"><b class="k-c-yel">PROCESSAMENTO</b><span>ESP32
Wi-Fi integrado</span></div>
<div id="@o" class="bk" style="left:1380px;top:250px;width:420px;height:200px;border-color:#FF6F9C"><b class="k-c-pink">SAÍDA</b><span>relé / driver →
bomba ou válvula solenoide
+ fonte própria</span></div>
<div id="@c" class="bk" style="left:750px;top:560px;width:1050px;height:220px;border-color:#7FE39A"><b class="k-c-green">COMUNICAÇÃO · MONITORAMENTO REMOTO</b><span>Wi-Fi → plataforma IoT (HTTP / MQTT)
dashboard: umidade, estado da bomba, histórico
alertas · acionamento manual remoto</span></div>
<svg class="k-svg"><path id="@a1" class="arrow" d="M 544 350 L 744 350 M 730 338 L 744 350 L 730 362" stroke="#8C97B5"/><path id="@a2" class="arrow" d="M 1174 350 L 1374 350 M 1360 338 L 1374 350 L 1360 362" stroke="#8C97B5"/><path id="@a3" class="arrow" d="M 960 454 L 960 554 M 948 540 L 960 554 L 972 540" stroke="#8C97B5"/></svg>
"""
scene("30-q10-arq", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("s"), C.b);
K.draw(tl, $("a1"), C.c - 0.2, { d: 0.3 });
K.rise(tl, $("m"), C.c);
K.draw(tl, $("a2"), C.d - 0.2, { d: 0.3 });
K.rise(tl, $("o"), C.d);
K.draw(tl, $("a3"), C.e - 0.2, { d: 0.3 });
K.rise(tl, $("c"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop@0.2*0.2", css=BOX_CSS)

# 31 Q10 codigo ---------------------------------------------------
L = ["const int SOLO = 34;   // ADC1", "const int RELE = 26;   // relé liga com LOW", "bool bomba = false;", "void setup() {",
     "  pinMode(RELE, OUTPUT);", "  digitalWrite(RELE, HIGH);   // começa desligada", "}", "void loop() {",
     "  int leitura = analogRead(SOLO);               // 0..4095", "  int umidade = map(leitura, 4095, 1500, 0, 100);",
     "  if (umidade < 30) bomba = true;     // seco: liga", "  if (umidade > 60) bomba = false;    // úmido: desliga",
     "  digitalWrite(RELE, bomba ? LOW : HIGH);", "  enviarDashboard(umidade, bomba);    // Wi-Fi", "  delay(2000);", "}"]
body = code_win("win", "irrigacao.ino", L, 120, 140, 1060, font=22, lh=38)
gx, gy, gw, gh = 1230, 200, 570, 300
def yv(u): return gy + gh - u * gh / 100.0
pts = [(0, 55), (60, 42), (120, 31), (150, 29), (200, 45), (250, 62), (300, 58), (360, 44), (420, 33), (450, 29), (500, 47), (570, 61)]
curve = "M " + " L ".join("%d %d" % (gx + x, yv(u)) for x, u in pts)
body += """
<svg id="@gr" class="k-svg">
  <rect x="%d" y="%d" width="%d" height="%d" fill="#182238" stroke="#2A3656" stroke-width="2" rx="12"/>
  <path d="M %d %d L %d %d" stroke="#FF6F9C" stroke-width="2" stroke-dasharray="10 8"/>
  <path d="M %d %d L %d %d" stroke="#7FE39A" stroke-width="2" stroke-dasharray="10 8"/>
  <path id="@cv" d="%s" stroke="#4FD6EE" stroke-width="4" fill="none"/>
  <rect id="@on1" x="%d" y="%d" width="%d" height="22" fill="#FFD24A" rx="4"/>
  <rect id="@on2" x="%d" y="%d" width="%d" height="22" fill="#FFD24A" rx="4"/>
</svg>
<div class="k-anno k-c-pink" style="left:1240px;top:%dpx;font-size:18px">30 %% liga</div>
<div class="k-anno k-c-green" style="left:1240px;top:%dpx;font-size:18px">60 %% desliga</div>
<div id="@bl" class="k-anno k-c-yel" style="left:1230px;top:545px;font-size:20px">bomba ligada</div>
<div id="@hs" class="k-card" style="left:1230px;top:610px;width:570px;height:190px;border-color:#FFD24A"><div class="k-body" style="left:26px;top:20px;width:520px;font-size:25px;line-height:1.45"><b class="k-c-yel">histerese</b>: entre 30 %% e 60 %% nada muda · a bomba não fica ligando e desligando</div></div>
""" % (gx, gy, gw, gh, gx, yv(30), gx + gw, yv(30), gx, yv(60), gx + gw, yv(60), curve,
       gx + 150, gy + gh + 14, 100, gx + 450, gy + gh + 14, 100, yv(30) - 44, yv(60) - 44)
js = 'K.rise(tl, $("win"), C.a);\n' + lines_hl([("c8", "C.b", "C.c"), ("c9", "C.b + 2.6", "C.c"), ("c10", "C.c", "C.d"), ("c11", "C.c + 3.0", "C.d"),
       ("c12", "C.e", "C.e + 3.0"), ("c13", "C.e + 3.0", "C.e + 7"), ("c1", "C.e", "C.e + 3.0")])
js += """
K.fade(tl, $("gr"), C.b + 1.0);
K.draw(tl, $("cv"), C.b + 1.4, { d: 2.4 });
tl.set([$("on1"), $("on2"), $("bl")], { opacity: 0 }, 0);
tl.to([$("on1"), $("on2"), $("bl")], { opacity: 1, duration: 0.3 }, C.c + 1.4);
K.rise(tl, $("hs"), C.d);
"""
scene("31-q10-cod", body, js, sfx="c:pop@1.4*0.2, d:pop@0.2*0.25")

# 32 Q10 resposta -------------------------------------------------
steps = [("s1", "objetivo e requisitos", "acompanhar o solo, controlar a água, monitorar remotamente"),
         ("s2", "arquitetura e componentes", "sensor de umidade · ESP32 · relé/driver + bomba/válvula · fonte · Wi-Fi"),
         ("s3", "funcionamento", "liga < 30 %, desliga > 60 % · envia dados · dashboard · comando remoto"),
         ("s4", "testes e custo", "calibração do sensor · testes · ROI e Payback")]
body = '<div id="@k" class="k-chip k-c-violet" style="left:120px;top:120px;font-size:26px">COMO ESCREVER A DISCURSIVA</div>\n'
for i, (sid, t, d) in enumerate(steps):
    body += ('<div id="@%s" class="k-card st" style="top:%dpx"><div class="nn">%d</div><b>%s</b><span>%s</span></div>\n'
             % (sid, 190 + i * 160, i + 1, t, d))
scene("32-q10-resp", body, """
K.fade(tl, $("k"), C.a);
K.rise(tl, $("s1"), C.b);
K.rise(tl, $("s2"), C.c);
K.rise(tl, $("s3"), C.d);
K.rise(tl, $("s4"), C.e);
""", sfx="b:pop@0.2*0.2, c:pop@0.2*0.2, d:pop@0.2*0.2, e:pop@0.2*0.2",
css="""  .st { left: 120px; width: 1680px; height: 136px; border-color: #B49BFF; }
  .st .nn { position: absolute; left: 28px; top: 34px; width: 68px; height: 68px; border-radius: 34px; background: #1E1838; border: 2px solid #B49BFF; font-family: "DM Mono", monospace; font-size: 34px; line-height: 64px; text-align: center; color: #B49BFF; }
  .st b { position: absolute; left: 130px; top: 22px; font-family: "Hanken Grotesk", sans-serif; font-size: 34px; color: #EEF1F8; }
  .st span { position: absolute; left: 130px; top: 76px; font-family: "Hanken Grotesk", sans-serif; font-size: 26px; color: #B9C2DA; }
""")

# 33 cola ---------------------------------------------------------
cards = [("q1", 120, 170, "#4FD6EE", "k-c-cyan", "arquitetura", "sensor = entrada · MCU = processamento · atuador = saída"),
         ("q2", 980, 170, "#7FE39A", "k-c-green", "analógico", "analogRead 0–1023 · analogWrite 0–255 · map converte"),
         ("q3", 120, 410, "#FF6F9C", "k-c-pink", "protocolos", "UART: TX, RX, baud rate · I2C: SDA, SCL, endereço"),
         ("q4", 980, 410, "#FFD24A", "k-c-yel", "atuador · negócio", "carga pesada → relé/driver (liga com LOW) · ROI % · Payback tempo")]
body = ""
for cid, x, y, col, cls, t, d in cards:
    body += ('<div id="@%s" class="k-card cc" style="left:%dpx;top:%dpx;border-color:%s"><b class="%s">%s</b><span>%s</span></div>\n'
             % (cid, x, y, col, cls, t, d))
body += '<div id="@end" class="k-title" style="left:0;top:330px;width:1920px;text-align:center;font-size:120px">Boa <em>prova!</em></div>'
scene("33-cola", body, """
K.pop(tl, $("q1"), C.b);
K.pop(tl, $("q2"), C.c);
K.pop(tl, $("q3"), C.d);
K.pop(tl, $("q4"), C.e);
K.dim(tl, [$("q1"), $("q2"), $("q3"), $("q4")], C.f, 0.12);
K.pop(tl, $("end"), C.f + 0.2);
""", sfx="b:pop@0.1*0.2, c:pop@0.1*0.2, d:pop@0.1*0.2, e:pop@0.1*0.2, f:chime@0.2*0.35",
css="""  .cc { width: 820px; height: 210px; }
  .cc b { position: absolute; left: 30px; top: 26px; font-family: "Hanken Grotesk", sans-serif; font-size: 38px; }
  .cc span { position: absolute; left: 30px; top: 96px; width: 760px; font-family: "Hanken Grotesk", sans-serif; font-size: 27px; line-height: 1.45; color: #D5DBEA; }
""")
