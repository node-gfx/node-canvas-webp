This module enables WebP encoding of canvases:

```js
const Canvas = require("canvas");
require("canvas-webp");

const canvas = Canvas.createCanvas(w, h);
// Do stuff with your canvas...

// Encode using default settings (lossless: true)
const buff = canavs.toBuffer("image/webp");
// Encode using custom settings:
const buff = canvas.toBuffer("image/webp", {lossless: true}); // quality does not apply
const buff = canvas.toBuffer("image/webp", {lossless: false, quality: zeroToOne});
```

Compatible with node-canvas 1.x and 2.x.
