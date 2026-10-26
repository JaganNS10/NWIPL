(function () {
  var nav = document.getElementById('nwNav');
  if (!nav) return;
  function onScroll() { nav.classList.toggle('nw-nav-solid', window.scrollY > 10); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
})();