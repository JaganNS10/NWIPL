(function () {
  'use strict';
  var d = document;

  /* Mobile menu + dropdowns */
  var burger = d.querySelector('.burger'), menu = d.getElementById('menu');
  function closeSubs(except) {
    d.querySelectorAll('.has-sub.open').forEach(function (li) {
      if (li !== except) { li.classList.remove('open'); li.querySelector('.sub-btn').setAttribute('aria-expanded', 'false'); }
    });
  }
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      d.body.style.overflow = open ? 'hidden' : '';
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a') && !e.target.closest('.sub-btn')) {
        menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); d.body.style.overflow = '';
      }
    });
  }
  d.querySelectorAll('.sub-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.parentElement, open = !li.classList.contains('open');
      closeSubs(li);
      li.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
    });
  });
  d.addEventListener('click', function (e) { if (!e.target.closest('.has-sub')) closeSubs(); });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSubs(); });

  /* Toast dismiss */
  d.querySelectorAll('[data-dismiss]').forEach(function (b) {
    b.addEventListener('click', function () { b.parentElement.remove(); });
  });

  /* Reveal on scroll */
  var rv = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (items) {
      items.forEach(function (it) { if (it.isIntersecting) { it.target.classList.add('in'); io.unobserve(it.target); } });
    }, { threshold: 0.12 });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* Home hero slideshow */
  var slides = d.querySelectorAll('.hero-slides img');
  if (slides.length > 1 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var i = 0;
    setInterval(function () {
      slides[i].classList.remove('on'); i = (i + 1) % slides.length; slides[i].classList.add('on');
    }, 6000);
  }

  /* Lightbox */
  var zoomables = Array.prototype.slice.call(d.querySelectorAll('img[data-zoom]')), lb, cur = 0;
  function show(n) {
    cur = (n + zoomables.length) % zoomables.length;
    lb.querySelector('img').src = zoomables[cur].currentSrc || zoomables[cur].src;
    lb.querySelector('img').alt = zoomables[cur].alt;
  }
  function close() { if (lb) { lb.remove(); lb = null; d.body.style.overflow = ''; } }
  zoomables.forEach(function (img, n) {
    img.addEventListener('click', function () {
      lb = d.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-label', 'Image viewer');
      lb.innerHTML = '<img alt=""><button class="x" aria-label="Close">&times;</button><button class="p" aria-label="Previous">&lsaquo;</button><button class="n" aria-label="Next">&rsaquo;</button>';
      d.body.appendChild(lb); d.body.style.overflow = 'hidden'; show(n);
      lb.addEventListener('click', function (e) {
        if (e.target.classList.contains('p')) show(cur - 1);
        else if (e.target.classList.contains('n')) show(cur + 1);
        else if (e.target.tagName !== 'IMG') close();
      });
    });
  });
  d.addEventListener('keydown', function (e) {
    if (!lb) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
  });

  /* Wardrobe slider */
  d.querySelectorAll('[data-slider]').forEach(function (s) {
    var main = s.querySelector('.slider-main img'), cap = s.querySelector('.s-cap'),
        thumbs = Array.prototype.slice.call(s.querySelectorAll('.slider-thumbs button')), idx = 0;
    function go(n) {
      idx = (n + thumbs.length) % thumbs.length;
      var t = thumbs[idx];
      main.style.opacity = 0;
      setTimeout(function () { main.src = t.dataset.src; main.alt = t.dataset.cap; cap.textContent = t.dataset.cap; main.style.opacity = 1; }, 150);
      thumbs.forEach(function (b) { b.classList.remove('on'); }); t.classList.add('on');
      t.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
    }
    thumbs.forEach(function (b, n) { b.addEventListener('click', function () { go(n); }); });
    s.querySelector('.s-prev').addEventListener('click', function () { go(idx - 1); });
    s.querySelector('.s-next').addEventListener('click', function () { go(idx + 1); });
    s.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') go(idx - 1);
      if (e.key === 'ArrowRight') go(idx + 1);
    });
  });
})();
