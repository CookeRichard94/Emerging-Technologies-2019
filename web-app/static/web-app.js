
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
 
var painting = document.getElementById('canvasDiv');
var paint_style = getComputedStyle(painting);
canvas.width = parseInt(paint_style.getPropertyValue('width'));
canvas.height = parseInt(paint_style.getPropertyValue('height'));

var mouse = {x: 0, y: 0};
 
canvas.addEventListener('mousemove', function(e) {
  mouse.x = e.pageX - this.offsetLeft;
  mouse.y = e.pageY - this.offsetTop;
}, false);

ctx.lineWidth = 3;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = '#00CC99';
 
canvas.addEventListener('mousedown', function(e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);
 
    canvas.addEventListener('mousemove', onPaint, false);
}, false);
 
canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);
 
var onPaint = function() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};

function erase() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

function saveImage(){
    var canvas = document.getElementById("myCanvas");
    var dataURL=canvas.toDataURL();
    console.log(dataURL);
    $.ajax({
      type: 'POST',
      url: '/predictedNumber',
      data: {
        imgBase64: dataURL
      }
    }).done(function(e){
      console.log('SENT');
    });
  };