window.onload = function() {


  var demandDetails = document.getElementsByClassName('demand');

  for (let el of demandDetails) {
    el.getElementsByClassName('demand__detail')[0].style.display = 'none';
    var moreBt = document.createElement("div");
    moreBt.classList.add('demand__more')
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
    lightbox.classList.add('lightbox')
    
    var lightboxContent = `
    <div class="lightbox__ground"></div>
    <div class="lightbox__content">
      <div class="lightbox__closebt">×</div>
      <h4 class="lightbox--demand__preheader">Forderung im Detail:</h4>
      <div class="lightbox--demand__title">${demand.title}</div>
      <div class="lightbox--demand__summary">${demand.summary}</div>
      <div class="lightbox--demand__detail">${demand.detail}</div>
    </div>
    `
    lightbox.innerHTML = lightboxContent;

    document.getElementsByTagName('body')[0].append(lightbox)
    document.getElementsByClassName('lightbox__ground')[0].onclick = function() {
      destroyLightbox(lightbox)
    };
    document.getElementsByClassName('lightbox__closebt')[0].onclick = function() {
      destroyLightbox(lightbox)
    };

  }

  function destroyLightbox(el) {
      el.remove();
  }

}