var oldHref = document.location.href;
window.onload = function() {

    document.getElementById('bigPetitionBt').onclick( function(e) {
      console.log(e);
    })

    var bodyList = document.querySelector("body")
    var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
          if (oldHref != document.location.href) {
              oldHref = document.location.href;
              console.log(document.location);
              if (document.location.hash == "#unterschreiben") {
                showPetition();
              } 
          }
      });
    });

    var config = {
        childList: true,
        subtree: true
    };
    observer.observe(bodyList, config);
};

function showPetition() {
  console.log('petition!');
}