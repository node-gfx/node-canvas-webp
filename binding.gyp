{
  "variables": {
    "Canvas_Src%": "<!(node find_canvas.js)"
  },
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
          "<(Canvas_Src)/src",
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
        # Canvas dependencies:
        ['OS=="win"', {
          "libraries": [
            '-l<(GTK_Root)/lib/cairo.lib'
          ],
          "include_dirs": [
            '<(GTK_Root)/include',
            '<(GTK_Root)/include/cairo',
            '<(GTK_Root)/include/pango-1.0',
            '<(GTK_Root)/include/glib-2.0',
            '<(GTK_Root)/include/freetype2',
            '<(GTK_Root)/lib/glib-2.0/include'
          ]
        }, { # not windows
          "libraries": [
            "<!@(pkg-config cairo --libs)",
            "<!@(pkg-config pangocairo --libs)"
          ],
          "include_dirs": [
            "<!@(pkg-config cairo --cflags-only-I | sed s/-I//g)",
            "<!@(pkg-config pangocairo --cflags-only-I | sed s/-I//g)"
          ]
        }],
        # Canvas:
        ['OS=="win"', {
          "libraries": ['-l<(Canvas_Src)/build/Release/canvas.lib']
        }, {
          "libraries": ["<(Canvas_Src)/build/Release/canvas.node"]
        }],
        # The libwebp library:
        ['OS=="win"', {
          "conditions": [
            ['target_arch=="ia32"', {
              "libraries": ['-l../libwebp/win32/libwebp.lib']
            }, {
              "libraries": ['-l../libwebp/win64/libwebp.lib']
            }]
          ]
        }],
        ['OS=="linux"', {
          "libraries": ["../libwebp/linux-x86_64/libwebp.a"]
        }],
        ['OS=="mac"', {
          "libraries": ["../libwebp/mac/libwebp.a"]
        }]
      ]
    }
  ]
}
