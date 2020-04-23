window.requestAnimFrame = (function () {
  return (
    window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    function (callback) {
      window.setTimeout(callback, 1000 / 60);
    }
  );
})();

function animate() {
  requestAnimFrame(animate);
  animDraw();
}

var canvases = []
var pixelSize = 25;
var drawRadius = 2;

function setup() {
  containers = document.getElementsByClassName('pixelate-container');
  canvases = [];
  for (let cont of containers) {
    c = cont.getElementsByClassName('pixelate')[0];
    var rect = cont.getBoundingClientRect();
    c.width = rect.width;
    c.height = rect.height;
    canvases.push({ canvas: c, container: cont, change: false });
    var context = c.getContext('2d');
    context.fillStyle = '#FCFCFC';
    context.fillRect(0, 0, c.width, c.height);
  }
}

function animDraw() {
  for (let obj of canvases) {
    c = obj.canvas;
    var context = c.getContext('2d');
    context.fillStyle = "#FCFCFC20";
    context.fillRect(0, 0, c.width, c.height);
    obj.container.style.background = 'url(' + c.toDataURL() + ')';
  }
}

function draw(event) {
  for (let obj of canvases) {
    c = obj.canvas;
    if (c != event.target) {continue}
    var pos = getMousePos(c, event);
    pos = quantizePos(pos);
    var context = c.getContext("2d");
    for (var x = -drawRadius; x < drawRadius; x++) {
      for (var y = -drawRadius; y < drawRadius; y++) {
        if (Math.random() > 0.8) {
          drawPixel(
            {
              x: pos.x + x,
              y: pos.y + y,
            },
            context
          );
        }
      }
    }
  }
}

function getMousePos(canvas, evt) {
  var rect = canvas.getBoundingClientRect();
  return {
    x: evt.clientX - rect.left,
    y: evt.clientY - rect.top,
  };
}

function quantizePos(pos) {
  return {
    x: Math.ceil(pos.x / pixelSize),
    y: Math.ceil(pos.y / pixelSize),
  };
}

function drawPixel(pos, context) {
  context.fillStyle = "#969DA8";
  context.globalAlpha = 0.2;
  context.fillRect(pos.x * pixelSize, pos.y * pixelSize, pixelSize, pixelSize);
  context.globalAlpha = 1;
}

setup();
animate();
window.onresize = setup;
