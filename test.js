const Canvas = require("canvas");
require(".");
const fs = require("fs");

// 1.x : 2.x
const c = typeof Canvas === "function" ? new Canvas(200, 200) : Canvas.createCanvas(200, 200);
const ctx = c.getContext("2d");

const colors = ["green", "blue", "red", "cyan", "yellow", "orange", "purple"];
for (const color of colors) {
	ctx.beginPath();
	ctx.fillStyle = color;
	ctx.fillRect(Math.random() * 50, Math.random() * 50, Math.random() * 150, Math.random() * 150);
}

let buff;
console.time("webp");
buff = c.toBuffer("image/webp", {lossless: true});
console.timeEnd("webp");
console.log("webp:", buff.byteLength);
fs.writeFileSync("test.webp", buff);

console.time("png");
buff = c.toBuffer("image/png");
console.timeEnd("png");
console.log("png:", buff.byteLength);
fs.writeFileSync("test.png", buff);

console.log("OK");
