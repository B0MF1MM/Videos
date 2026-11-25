"""Ajudantes para gerar as cenas (tools/src/*.html) deste vídeo."""
import html, os, re

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")

KW = r"void|int|float|const|bool|byte|char|long|unsigned|if|else|for|while|return|true|false|static|volatile|String"
CONST = r"HIGH|LOW|OUTPUT|INPUT_PULLUP|INPUT|LED_BUILTIN|FALLING|RISING|CHANGE|WL_CONNECTED|DHT11"
API = (r"pinMode|digitalWrite|digitalRead|analogRead|analogWrite|delay|map|millis|tone|fabs|"
       r"Serial|begin|println|print|lcd|init|backlight|clear|setCursor|scrollDisplayRight|scrollDisplayLeft|"
       r"dht|readTemperature|readHumidity|attachInterrupt|digitalPinToInterrupt|IRAM_ATTR|"
       r"esp_sleep_enable_timer_wakeup|esp_deep_sleep_start|WiFi|status|HTTPClient|http|GET|end|"
       r"LiquidCrystal_I2C|LiquidCrystal|DHT|enviarDashboard")
TOK = re.compile(r'(?P<com>//.*$)|(?P<str>"[^"]*")|(?P<pre>#include|#define)|(?P<inc><[A-Za-z_0-9.]+\.h>)|'
                 r'(?P<kw>\b(?:' + KW + r')\b)|(?P<cst>\b(?:' + CONST + r')\b)|(?P<api>\b(?:' + API + r')\b)|'
                 r'(?P<num>\b0x[0-9A-Fa-f]+\b|\b\d+(?:\.\d+)?\b)')
CLS = {"com": "k-mute", "str": "k-c-green", "pre": "k-c-pink", "inc": "k-c-green", "kw": "k-c-violet",
       "cst": "k-c-yel", "api": "k-c-cyan", "num": "k-c-orange"}


def hl(line):
    out, pos = [], 0
    for m in TOK.finditer(line):
        out.append(html.escape(line[pos:m.start()], quote=False))
        out.append('<span class="%s">%s</span>' % (CLS[m.lastgroup], html.escape(m.group(0), quote=False)))
        pos = m.end()
    out.append(html.escape(line[pos:], quote=False))
    return "".join(out)


def code_win(wid, fname, lines, left, top, width, font=24, lh=36, pre="c"):
    """Janela de código; cada linha recebe id @<pre><i>."""
    spans = "".join('<span class="ln" id="@%s%d">%s</span>' % (pre, i, hl(l) or " ") for i, l in enumerate(lines))
    height = 66 + len(lines) * lh + 22
    return ('<div id="@%s" class="k-win" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">\n'
            '  <div class="k-win-bar"><i style="left:22px;background:#FF6F9C"></i><i style="left:46px;background:#FFD24A"></i>'
            '<i style="left:70px;background:#7FE39A"></i><span>%s</span></div>\n'
            '  <div class="k-code" style="left:10px;top:66px;font-size:%dpx;--lh:%dpx">%s</div>\n</div>'
            % (wid, left, top, width, height, fname, font, lh, spans))


def lcd(lid, left, top, l1="", l2="", cell=38, ids=False):
    """Display 16x2 desenhado por células (cada linha num wrapper @<lid>r0/@<lid>r1)."""
    rows = []
    for r, txt in enumerate((l1, l2)):
        txt = txt.ljust(16)[:16]
        cells = "".join('<b style="left:%dpx">%s</b>' % (i * cell, html.escape(ch) if ch != " " else "&nbsp;") for i, ch in enumerate(txt))
        rows.append('<div class="lr" id="@%sr%d" style="top:%dpx">%s</div>' % (lid, r, 30 + r * 64, cells))
    w = 16 * cell + 60
    return ('<div id="@%s" class="lcd" style="left:%dpx;top:%dpx;width:%dpx;height:178px">'
            '<div class="lcdin" style="width:%dpx">%s</div></div>' % (lid, left, top, w, 16 * cell, "".join(rows)))


LCD_CSS = """  .lcd { position: absolute; border-radius: 16px; background: #1B3A1F; border: 4px solid #2E5E33; box-shadow: inset 0 0 30px rgba(0,0,0,0.5); }
  .lcdin { position: absolute; left: 30px; top: 0; height: 178px; overflow: hidden; }
  .lr { position: absolute; left: 0; height: 56px; width: 2000px; }
  .lr b { position: absolute; top: 0; width: 34px; height: 56px; background: #24502A; border-radius: 3px; font-family: "DM Mono", monospace; font-weight: 400; font-size: 34px; line-height: 56px; text-align: center; color: #C8F7C5; }
"""


def scene(sid, body, script, sfx="", css=""):
    s = ""
    if sfx:
        s += "<!--sfx: %s-->\n" % sfx
    s += "<style>\n  .k-code .ln { line-height: var(--lh, 36px); }\n" + css + "</style>\n"
    s += body.strip() + "\n<script>\n" + script.strip() + "\n</script>\n"
    open(os.path.join(SRC, sid + ".html"), "w", encoding="utf-8").write(s)


def lines_hl(pairs):
    """pairs: [(linha, t0, t1)] -> chamadas K.hl."""
    return "\n".join('K.hl(tl, $("%s"), %s, %s);' % p for p in pairs)
