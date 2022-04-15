window.onload = function() {
  var hero = document.getElementById('hero');
  hero.onclick = function() {
    if (! document.getElementById('bigPetitionBt')) {
      location.href = '/';
    }
  };

  var demandDetails = document.getElementsByClassName('demand');

  
  for (let el of demandDetails) {
    el.getElementsByClassName('demand__detail')[0].classList.add('demand__detail-nojs')
    var moreBt = document.getElementById('template_moreBt').cloneNode(true);
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
    var demandLightbox = document.getElementById('template_demandLightbox').cloneNode(true);

    demandLightbox.getElementsByClassName('js-lightbox--demand__title')[0].innerHTML = demand.title
    demandLightbox.getElementsByClassName('js-lightbox--demand__summary')[0].innerHTML = demand.summary
    demandLightbox.getElementsByClassName('js-lightbox--demand__detail')[0].innerHTML = demand.detail

    document.getElementsByTagName('body')[0].append(demandLightbox)
    demandLightbox.getElementsByClassName('js-lightbox__ground')[0].onclick = function() {
      destroyLightbox(demandLightbox)
    };
    demandLightbox.getElementsByClassName('js-lightbox__closebt')[0].onclick = function() {
      destroyLightbox(demandLightbox)
    };

  }

  function destroyLightbox(el) {
      el.remove();
  }

}
