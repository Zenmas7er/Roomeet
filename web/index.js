// wait for the content of the window element 
// to load, then performs the operations. 
// This is considered best practice. 
window.addEventListener('load', ()=>{ 
		
	resize(); // Resizes the canvas once the window loads 
	document.addEventListener('mousedown', startPainting); 
	document.addEventListener('mouseup', stopPainting); 
	document.addEventListener('mousemove', sketch); 
	window.addEventListener('resize', resize); 
}); 
	
const canvas = document.querySelector('#canvas'); 

// Context for the canvas for 2 dimensional operations 
const ctx = canvas.getContext('2d'); 
	
// Resizes the canvas to the available size of the window. 
function resize(){ 
    ctx.canvas.width = window.innerWidth; 
    ctx.canvas.height = window.innerHeight; 
} 
	
// Stores the initial position of the cursor 
let coord = {x:0 , y:0}; 

// This is the flag that we are going to use to 
// trigger drawing 
let paint = false; 
	
// Updates the coordianates of the cursor when 
// an event e is triggered to the coordinates where 
// the said event is triggered. 
function getPosition(event){ 
    coord.x = event.clientX - canvas.offsetLeft; 
    coord.y = event.clientY - canvas.offsetTop; 
} 

// The following functions toggle the flag to start 
// and stop drawing 
function startPainting(event){ 
    paint = true; 
    getPosition(event); 
} 
function stopPainting(){ 
    paint = false; 
}

// Records starting points of the cursor for the Rectangle tool
// var StartX = coord.x;
// var StartY = coord.y;

// function componentToHex(c) {
//     var hex = c.toString(16);
//     return hex.length == 1 ? "0" + hex : hex;
// }
  
// function rgbToHex(r, g, b) {
//     return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
// }

// Alert test to see what hexadecimal color is coming out
// alert( tx.strokeStyle = getRGB(document.getElementById('red').value, document.getElementById('green').value, document.getElementById('blue')));
	
function sketch(event){ 
    if (!paint) 
        return; 
    ctx.beginPath(); 

    // Sets the end of the lines drawn 
    // to a round shape. 
    if (document.getElementById('radio1').checked) {
        rate_value = document.getElementById('radio1').value;
        ctx.lineCap = 'round';
        ctx.strokeStyle = 'rgb(' + document.getElementById('red').value + ',' + document.getElementById('green').value + ',' + document.getElementById('blue').value +')';
        ctx.lineWidth = document.getElementById('tipsize').value;   
    }

    if (document.getElementById('radio2').checked) {
        rate_value = document.getElementById('radio2').value;
        ctx.lineCap = 'square';
        ctx.strokeStyle = 'rgb(' + document.getElementById('red').value + ',' + document.getElementById('green').value + ',' + document.getElementById('blue').value +')';
        ctx.lineWidth = document.getElementById('tipsize').value;   
    }

    if (document.getElementById('radio3').checked) {
        rate_value = document.getElementById('radio3').value;
        ctx.lineCap = 'round';
        ctx.strokeStyle = 'White';
        ctx.lineWidth = 2 * document.getElementById('tipsize').value;   
    }

    if (document.getElementById('radio4').checked) {
        rate_value = document.getElementById('radio4').value;
        ctx.strokeStyle = 'rgb(' + document.getElementById('red').value + ',' + document.getElementById('green').value + ',' + document.getElementById('blue').value +')';
        ctx.lineWidth = document.getElementById('tipsize').value;

    }
        
    // The cursor to start drawing 
    // moves to this coordinate 
    ctx.moveTo(coord.x, coord.y); 

    // The position of the cursor 
    // gets updated as we move the 
    // mouse around. 
    getPosition(event); 

    // A line is traced from start 
    // coordinate to this coordinate 
    ctx.lineTo(coord.x , coord.y); 
        
    // Draws the line. 
    ctx.stroke(); 
} 
