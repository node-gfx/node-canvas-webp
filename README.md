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

It's relatively straightforward to add `canvas.createWEBPStream()`, but I haven't
implemented it yet.

:warning: **libwebp compatibility**  
I'm still figuring out the best way to distribute this so users don't have to
build and install libwebp.

* I built the win32 and win64 libraries because the ones Google distributes
  appear to be built with mingw instead of MSVC.

* I built the linux library because the one Google distributes appears to be
  built with `-fno-pic` (or otherwise had a PIC-related issue). I built it on
  Ubuntu 16.06 with GCC 5.4. I think that means it's incompatible with any
  distro that uses ld older than 2.26.1 (including Ubuntu 14), but
  forward-compatible (e.g. Ubuntu 18 should work).
  I've momentarily given up on getting travis to use a newer GCC or building it
  with an older GCC (https://travis-ci.org/zbjornson/node-canvas-webp).

* I have not built or tested the mac version. It probably needs to be built.

* More info: https://developers.google.com/speed/webp/docs/compiling.