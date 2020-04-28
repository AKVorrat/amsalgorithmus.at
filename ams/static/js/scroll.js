
function scrollToId(id) {
    const el = document.getElementById(id);
    let target = el.getBoundingClientRect().top;
    let pos = window.pageYOffset || document.documentElement.scrollTop;
    let frame = 1;
    const up = (target < 0);

    function scrollFrame() {
        const x = (frame / 60);
        target = el.getBoundingClientRect().top;
        pos += target * x;
        const vh = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
        if ((target > 0 && up) 
            || (target < 0 && !up) 
            || (target < vh && !up && pos >= (document.body.scrollHeight - vh))){
            window.scrollTo(0, pos + target);
        } else {
            window.scrollTo(0, pos);
            requestAnimFrame(scrollFrame);
        }
        frame++;
    }
    scrollFrame();
}

var scrollTos = document.getElementsByClassName('scrollto');
for (var st of scrollTos) {
    st.removeAttribute('href');
    st.style.cursor = 'pointer';
}
