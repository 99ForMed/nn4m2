var canvas = document.getElementById("speechBoxRectangle");
var ctx = canvas.getContext("2d");
var squareWidth = 20;

// Set the style for the lines
ctx.strokeStyle = 'darkorange';
ctx.lineWidth = 2;

// Fill the area between lines
ctx.fillStyle = '#1e1e1e';
ctx.beginPath();
ctx.moveTo(0, 0);
ctx.lineTo(squareWidth, squareWidth);
ctx.lineTo(0, squareWidth);
ctx.closePath();
ctx.fill();

// Draw line from top left to bottom right
ctx.beginPath();
ctx.moveTo(0, 0);
ctx.lineTo(squareWidth, squareWidth);
ctx.stroke();


// Draw line from top left to bottom left
ctx.beginPath();
ctx.moveTo(ctx.lineWidth/2, 0);
ctx.lineTo(ctx.lineWidth/2, squareWidth);
ctx.stroke();
