const Canvas = require("canvas");
require(".");
const fs = require("fs");

// 1.x : 2.x
const c = typeof Canvas === "function" ? new Canvas(200, 200) : Canvas.createCanvas(200, 200);
const ctx = c.getContext("2d");
ctx.fillStyle = "green";
ctx.fillRect(0, 0, 50, 50);
ctx.beginPath();
ctx.fillStyle = "blue";
ctx.fillRect(10, 10, 20, 20);
ctx.beginPath();
ctx.fillStyle = "red";
ctx.fillRect(50, 50, 100, 150);

const buff = c.toBuffer("image/webp", {lossless: true});
fs.writeFileSync("./img.webp", buff);
console.log("done");
