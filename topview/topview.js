"use strict";

var canv = document.getElementById('canv').getContext('2d');
canv.fillStyle = "blue";
canv.strokeStyle = "gray";
// mdl = {};

for(var x=4; x<100; x+=20){
    for(var y=4; y<100; y+=10){
//    a = x; b = Math.sin(x) * 10;
//    canv.strokeRect(x,y,x+2,y+2);
      canv.strokeRect(x, y, 1, 1);
    };
};

document.write("| success!");
