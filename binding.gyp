{
  "conditions": [
    ['OS=="win"', {
      "variables": {
        "GTK_Root%": "C:/GTK"
      }
    }]
  ],
  "targets": [
    {
      "target_name": "canvaswebp",
      "sources": [
        "webp.cc"
      ],
      "include_dirs" : [
          "<!(node -e \"require('nan')\")",
          "<!(node find_canvas.js)",
          "libwebp"
      ],
      "cflags": [
        "-std=c++14"
      ],
      "cflags_cc!": [
        "-std=gnu++0x" # Allow -std=c++14 to prevail
      ],
      "xcode_settings": {
        "GCC_VERSION": "com.apple.compilers.llvm.clang.1_0",
        "CLANG_CXX_LANGUAGE_STANDARD": "c++14",
        "CLANG_CXX_LIBRARY": "libc++",
      },
      "conditions": [
        ['OS=="win"', {
          "libraries": [
            '-lC:/Users/zachb/git/canvas-webp/node_modules/canvas/build/Release/canvas.lib',
            '-lC:/Users/zachb/git/canvas-webp/libwebp/win64/libwebp.lib',
            '-l<(GTK_Root)/lib/cairo.lib',
            '-l<(GTK_Root)/lib/libpng.lib',
            '-l<(GTK_Root)/lib/pangocairo-1.0.lib',
            '-l<(GTK_Root)/lib/pango-1.0.lib',
            '-l<(GTK_Root)/lib/freetype.lib',
            '-l<(GTK_Root)/lib/glib-2.0.lib',
            '-l<(GTK_Root)/lib/gobject-2.0.lib'
          ],
          "include_dirs": [
            '<(GTK_Root)/include',
            '<(GTK_Root)/include/cairo',
            '<(GTK_Root)/include/pango-1.0',
            '<(GTK_Root)/include/glib-2.0',
            '<(GTK_Root)/include/freetype2',
            '<(GTK_Root)/lib/glib-2.0/include'
          ],
          "copies": [{
            "destination": "<(PRODUCT_DIR)",
            "files": [
              'C:/Users/zachb/git/canvas-webp/libwebp/win64/libwebp.lib'
            ]
          }]
        }, { # not windows
          "libraries": [
            "<!@(pkg-config cairo --libs)"
          ],
          "include_dirs": [
            "<!@(pkg-config cairo --cflags-only-I | sed s/-I//g"
          ]
        }]
      ]
    }
  ]
}
