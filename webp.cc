#include <nan.h>
#include "encode.h"

#include "Canvas.h"
#include "cairo.h"
#include <stdint.h>

using v8::Object;
using v8::Local;

void free_webp(char* data, void* hint) {
  WebPFree(data);
}

NAN_METHOD(canvasToBufferWebp) {
  Canvas *canvas = Nan::ObjectWrap::Unwrap<Canvas>(info[0]->ToObject(Nan::GetCurrentContext()).ToLocalChecked());
  float quality = static_cast<float>(info[1]->NumberValue(Nan::GetCurrentContext()).FromMaybe(75.0)); // 0 to 100
  bool lossless = info[2]->BooleanValue(info.GetIsolate());

  cairo_surface_t *surface = canvas->surface();
  cairo_format_t format = cairo_image_surface_get_format(surface);
  unsigned char* data = cairo_image_surface_get_data(surface);
  unsigned int width = cairo_image_surface_get_width(surface);
  unsigned int height = cairo_image_surface_get_height(surface);
  unsigned int stride = cairo_image_surface_get_stride(surface);

  uint8_t* out = NULL;
  size_t outSize;

  if (format == CAIRO_FORMAT_ARGB32) {
    if (lossless) {
      outSize = WebPEncodeLosslessBGRA(data, width, height, stride, &out);
    } else {
      outSize = WebPEncodeBGRA(data, width, height, stride, quality, &out);
    }
  } else if (format == CAIRO_FORMAT_RGB24) {
    if (lossless) {
      outSize = WebPEncodeLosslessBGR(data, width, height, stride, &out);
    } else {
      outSize = WebPEncodeBGR(data, width, height, stride, quality, &out);
    }
  } else {
    return Nan::ThrowError("Can only encode ARGB32 and RGB24 canvases.");
  }

  if (outSize == 0) {
    return Nan::ThrowError("Error encoding.");
  }

  Local<Object> buf = Nan::NewBuffer(reinterpret_cast<char*>(out), outSize, free_webp, 0).ToLocalChecked();
  info.GetReturnValue().Set(buf);
}

NAN_MODULE_INIT(CWInit) {
  NAN_EXPORT(target, canvasToBufferWebp);
}

NODE_MODULE(canvaswebp, CWInit);
