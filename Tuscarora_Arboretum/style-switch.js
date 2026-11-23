/* Tuscarora Arboretum — design-style switcher (pilot, Nov 23, 2026).
   The choice lives in localStorage key "peptopia-style" and is applied
   as the data-style attribute on <html> (see style-themes.css). An
   inline snippet in each page's <head> applies it before first paint;
   this file re-applies it and wires the paintbrush dropdown.
   Choosing "Peptopia" removes the key and the attribute — the wing
   renders exactly as built. */
(function () {
  var KEY = 'peptopia-style';
  var STYLES = [
    ['peptopia', 'Peptopia', 'The current look'],
    ['bauhaus', 'Bauhaus', 'Geometry · primary color · form follows function'],
    ['fauvism', 'Fauvism', 'Wild color · emotion over accuracy'],
    ['midcentury', 'Mid-Century Modern', 'Walnut & teal · atomic-age warmth']
  ];
  var DOTS = {
    peptopia: 'linear-gradient(135deg,#F06000,#06B6D4)',
    bauhaus: 'conic-gradient(#D92323 0 33%,#FFC500 0 66%,#005CA9 0)',
    fauvism: 'linear-gradient(135deg,#E8442E,#FFC20E 55%,#0E7C3A)',
    midcentury: 'linear-gradient(135deg,#1F7A72,#E3A72F 55%,#CC5E2A)'
  };
  function current() {
    try { return localStorage.getItem(KEY) || 'peptopia'; } catch (e) { return 'peptopia'; }
  }
  function apply(s) {
    var de = document.documentElement;
    if (s && s !== 'peptopia') { de.setAttribute('data-style', s); }
    else { de.removeAttribute('data-style'); }
  }
  apply(current());
  function build(wrap) {
    var btn = wrap.querySelector('.style-brush-btn');
    if (!btn || wrap.querySelector('.style-menu')) { return; }
    var menu = document.createElement('div');
    menu.className = 'style-menu';
    menu.hidden = true;
    menu.setAttribute('role', 'menu');
    var html = '<div class="style-menu-title">Design Style</div>';
    STYLES.forEach(function (st) {
      html += '<button type="button" class="style-opt" role="menuitemradio" aria-checked="false" data-style-val="' + st[0] + '">' +
        '<span class="dot" style="background:' + DOTS[st[0]] + '"></span>' +
        '<span><span class="nm">' + st[1] + '</span><span class="ds">' + st[2] + '</span></span>' +
        '<span class="cur"></span></button>';
    });
    menu.innerHTML = html;
    wrap.appendChild(menu);
    function mark() {
      var c = current();
      menu.querySelectorAll('.style-opt').forEach(function (o) {
        var on = o.getAttribute('data-style-val') === c;
        o.setAttribute('aria-checked', on ? 'true' : 'false');
        o.querySelector('.cur').textContent = on ? 'Current' : '';
      });
    }
    function close() { menu.hidden = true; btn.setAttribute('aria-expanded', 'false'); }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var willOpen = menu.hidden;
      document.querySelectorAll('.style-menu').forEach(function (m) { m.hidden = true; });
      menu.hidden = !willOpen;
      btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      if (willOpen) { mark(); }
    });
    menu.addEventListener('click', function (e) {
      var o = e.target.closest('.style-opt');
      if (!o) { return; }
      var v = o.getAttribute('data-style-val');
      try {
        if (v === 'peptopia') { localStorage.removeItem(KEY); }
        else { localStorage.setItem(KEY, v); }
      } catch (err) {}
      apply(v);
      mark();
      close();
    });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) { close(); } });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { close(); } });
    mark();
  }
  function init() { document.querySelectorAll('.style-pick').forEach(build); }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); }
  else { init(); }
})();
