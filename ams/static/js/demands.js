window.onload = function() {
  var hero = document.getElementById('hero');
  hero.onclick = function() {
    location.href = '/';
  };

  var demandDetails = document.getElementsByClassName('demand');

  for (let el of demandDetails) {
    el.getElementsByClassName('demand__detail')[0].classList.add('demand__detail-nojs')
    var moreBt = document.createElement("div");
    moreBt.classList.add('demand__more', 'text-display')
    moreBt.append("mehr");
    el.append(moreBt);
    moreBt.onclick = function() {
      showDemandDetail(el)
    };
  }
  

  function showDemandDetail(el) {
    var demand = {
      title: el.getElementsByClassName('demand__title')[0].innerHTML,
      summary: el.getElementsByClassName('demand__summary')[0].innerHTML,
      detail: el.getElementsByClassName('demand__detail')[0].innerHTML
    }
    var lightbox = document.createElement("div");
    lightbox.classList.add('js-lightbox')
    
    var lightboxContent = `
    <div class="js-lightbox__ground"></div>
    <div class="js-lightbox__content">
      <div class="js-lightbox__closebt">×</div>
      <h4 class="js-lightbox--demand__preheader">Forderung im Detail:</h4>
      <div class="js-lightbox--demand__title">${demand.title}</div>
      <div class="js-lightbox--demand__summary"><div class="text-display">${demand.summary}</div></div>
      <div class="js-lightbox--demand__detail">${demand.detail}</div>
    </div>
    `
    lightbox.innerHTML = lightboxContent;

    document.getElementsByTagName('body')[0].append(lightbox)
    document.getElementsByClassName('js-lightbox__ground')[0].onclick = function() {
      destroyLightbox(lightbox)
    };
    document.getElementsByClassName('js-lightbox__closebt')[0].onclick = function() {
      destroyLightbox(lightbox)
    };

  }

  function destroyLightbox(el) {
      el.remove();
  }

}
