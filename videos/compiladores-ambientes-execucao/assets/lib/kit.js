/* Kit de animação compartilhado. Tudo é função do tempo da timeline (seek-safe). */
(function () {
  if (window.K) return;
  var HIDE = "inset(-20% 100% -20% -2%)", SHOW = "inset(-20% -2% -20% -2%)";
  function arr(x) { return Array.isArray(x) ? x : [x]; }

  var K = {
    // cria a timeline pausada da cena, registra e ancora a duração
    scene: function (id, D, total) {
      var tl = gsap.timeline({ paused: true });
      window.__timelines = window.__timelines || {};
      window.__timelines[id] = tl;
      tl.to({}, { duration: D }, 0);
      var $ = function (s) { return document.getElementById("s" + id + "-" + s); };
      var cam = $("cam"), prog = $("prog");
      if (cam) tl.fromTo(cam, { scale: 1 }, { scale: 1.03, duration: D, ease: "none" }, 0);
      if (prog && total) {
        var n = parseInt(id, 10);
        tl.fromTo(prog, { width: (n - 1) / total * 1760 }, { width: n / total * 1760, duration: D, ease: "none" }, 0);
      }
      return { tl: tl, $: $ };
    },
    // entra subindo
    rise: function (tl, els, t, o) {
      o = o || {};
      tl.fromTo(arr(els), { y: o.y == null ? 36 : o.y, opacity: 0 },
        { y: 0, opacity: 1, duration: o.d || 0.55, ease: "power3.out", stagger: o.s || 0 }, t);
    },
    // entra vindo do lado
    slide: function (tl, els, t, o) {
      o = o || {};
      tl.fromTo(arr(els), { x: o.x == null ? -60 : o.x, opacity: 0 },
        { x: 0, opacity: 1, duration: o.d || 0.55, ease: "power3.out", stagger: o.s || 0 }, t);
    },
    // aparece com mola
    pop: function (tl, els, t, o) {
      o = o || {};
      tl.fromTo(arr(els), { scale: o.from || 0.4, opacity: 0 },
        { scale: 1, opacity: 1, duration: o.d || 0.55, ease: "back.out(1.8)", stagger: o.s || 0 }, t);
    },
    fade: function (tl, els, t, o) {
      o = o || {};
      tl.fromTo(arr(els), { opacity: 0 }, { opacity: 1, duration: o.d || 0.5, ease: "power2.out", stagger: o.s || 0 }, t);
    },
    // revela da esquerda para a direita
    wipe: function (tl, els, t, o) {
      o = o || {};
      tl.fromTo(arr(els), { clipPath: HIDE }, { clipPath: SHOW, duration: o.d || 0.6, ease: o.ease || "power3.out", stagger: o.s || 0 }, t);
    },
    // sai
    out: function (tl, els, t, o) {
      o = o || {};
      tl.to(arr(els), { opacity: 0, y: o.y || 0, duration: o.d || 0.35, ease: "power2.in", stagger: o.s || 0 }, t);
    },
    dim: function (tl, els, t, to) {
      tl.to(arr(els), { opacity: to == null ? 0.3 : to, duration: 0.4, ease: "power2.out" }, t);
    },
    // pulso de destaque
    pulse: function (tl, els, t, o) {
      o = o || {};
      tl.to(arr(els), { scale: o.k || 1.12, duration: 0.16, ease: "power2.out" }, t);
      tl.to(arr(els), { scale: 1, duration: 0.4, ease: "power3.out" }, t + 0.16);
    },
    // destaca uma linha de código (classe .hl) num intervalo
    hl: function (tl, el, t0, t1) {
      tl.set(el, { className: el.className.replace(/\s*hl\b/, "") + " hl" }, t0);
      if (t1 != null) tl.set(el, { className: el.className.replace(/\s*hl\b/, "") }, t1);
    },
    // máquina de escrever num elemento de texto simples
    type: function (tl, el, t, cps) {
      var full = el.getAttribute("data-text") || el.textContent;
      el.setAttribute("data-text", full);
      el.textContent = "";
      var d = full.length / (cps || 28);
      tl.to({ p: 0 }, { p: 1, duration: d, ease: "none", onUpdate: function () {
        el.textContent = full.slice(0, Math.round(this.progress() * full.length));
      } }, t);
      tl.set({}, {}, t + d);
      return d;
    },
    // desenha um traço SVG
    draw: function (tl, els, t, o) {
      o = o || {};
      arr(els).forEach(function (p, i) {
        var len = p.getTotalLength ? p.getTotalLength() : 1000;
        p.style.strokeDasharray = len + " " + len;
        tl.fromTo(p, { opacity: 0 }, { opacity: 1, duration: 0.01 }, t + i * (o.s || 0));
        tl.fromTo(p, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: o.d || 0.6, ease: o.ease || "power2.inOut" }, t + i * (o.s || 0));
      });
    },
    // cartão de macete: entra batendo
    macete: function (tl, el, t) {
      tl.fromTo(el, { scale: 1.25, rotation: -3, opacity: 0 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.5, ease: "back.out(2.2)" }, t);
      tl.to(el, { rotation: -1, duration: 0.25, ease: "power2.out" }, t + 0.5);
      tl.to(el, { rotation: 0, duration: 0.4, ease: "power2.out" }, t + 0.75);
    },
    // move um "token" de um lugar a outro (voa)
    fly: function (tl, el, t, x, y, o) {
      o = o || {};
      tl.to(el, { x: x, y: y, scale: o.scale || 1, duration: o.d || 0.7, ease: o.ease || "power3.inOut" }, t);
    }
  };
  window.K = K;
})();
