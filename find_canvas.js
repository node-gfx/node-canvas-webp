// Reports the path to e.g. node_modules/canvas/src/
const canvasPath = require.resolve("canvas");
// version 1.x's entry is /lib/canvas.js, version 2.x is /index.js
const is1x = require("canvas").createCanvas === undefined;
const srcPath = require("path").resolve(canvasPath, is1x ? "../../" : "../");
process.stdout.write(srcPath);
