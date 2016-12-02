#!/usr/bin/env python
# -*- coding: utf-8 -*-


def primitives(device, draw):
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    x = padding
    draw.ellipse((x, top, x + shape_width, bottom), outline="red", fill="black")
    x += shape_width + padding
    draw.rectangle((x, top, x + shape_width, bottom), outline="blue", fill="black")
    x += shape_width + padding
    draw.polygon([(x, bottom), (x + shape_width / 2, top), (x + shape_width, bottom)], outline="green", fill="black")
    x += shape_width + padding
    draw.line((x, bottom, x + shape_width, top), fill="yellow")
    draw.line((x, top, x + shape_width, bottom), fill="yellow")
    x += shape_width + padding
    draw.text((x, top), 'Hello', fill="cyan")
    draw.text((x, top + 20), 'World!', fill="purple")


# These datasets are purely to prevent regression bugs from creeping in
demo_ssd1306 = [
    255, 1, 1, 1, 1, 1, 1, 1, 1, 129, 193, 65, 193, 129, 1, 1, 241, 241, 17,
    17, 1, 1, 241, 241, 17, 17, 1, 129, 193, 65, 193, 129, 33, 225, 225, 129,
    225, 225, 1, 13, 113, 129, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    129, 113, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 225, 29, 225, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 253, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    253, 1, 1, 1, 1, 1, 129, 97, 25, 9, 5, 5, 5, 5, 5, 9, 25, 97, 129, 1, 1, 1,
    1, 1, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 4, 7, 3, 4, 4, 7, 7, 4, 4, 4,
    4, 7, 7, 4, 4, 0, 5, 5, 5, 7, 3, 4, 7, 7, 0, 7, 7, 0, 0, 0, 3, 28, 224, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 28, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    248, 7, 0, 7, 248, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 240, 14, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 14, 240, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 0, 192, 56, 7, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 126, 1, 0, 0, 0, 1, 126, 128, 0, 0, 0, 0,
    0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255,
    0, 192, 63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 192, 0,
    255, 255, 0, 0, 0, 0, 94, 94, 0, 64, 127, 127, 69, 124, 56, 64, 64, 127,
    127, 65, 65, 12, 4, 76, 120, 124, 68, 0, 56, 124, 68, 124, 56, 2, 30, 112,
    62, 112, 30, 0, 0, 0, 0, 0, 0, 0, 0, 1, 14, 112, 128, 112, 14, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 31, 0, 0, 0, 0, 0, 0, 0, 31, 224, 0, 0,
    0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255,
    0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    128, 112, 14, 1, 14, 112, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 248, 7,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 248, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 28, 3, 0, 0, 0, 0, 0, 3, 28, 224, 0, 0, 0,
    0, 0, 0, 0, 0, 128, 126, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 126, 128,
    0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255,
    0, 1, 126, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 126, 1,
    0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 56, 7, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 224, 31, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 224, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 192, 56, 7, 0, 0, 0, 255, 255, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 176, 142, 129, 128, 128, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 128, 128, 129, 142, 176, 128, 184, 167, 160, 160, 160,
    160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 167,
    184, 128, 191, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160,
    160, 160, 160, 160, 160, 160, 160, 191, 128, 128, 128, 128, 128, 128, 131,
    140, 136, 144, 144, 176, 144, 144, 136, 140, 131, 128, 128, 128, 128, 128,
    128, 255
]

demo_sh1106 = [
    {'command': [176, 2, 16]}, {'data': [255, 1, 1, 1, 1, 1, 129, 97, 25, 9, 5, 5, 5, 5, 5, 9, 25, 97, 129, 1, 1, 1, 1, 1, 253, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 253, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 225, 29, 225, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 113, 129, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 129, 113, 13, 1, 225, 225, 129, 225, 225, 33, 129, 193, 65, 193, 129, 1, 17, 17, 241, 241, 1, 1, 17, 17, 241, 241, 1, 1, 129, 193, 65, 193, 129, 1, 1, 1, 1, 1, 1, 1, 1, 255]},
    {'command': [177, 2, 16]}, {'data': [255, 0, 0, 0, 240, 14, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 14, 240, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 248, 7, 0, 7, 248, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 28, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 28, 3, 0, 0, 0, 7, 7, 0, 7, 7, 4, 3, 7, 5, 5, 5, 0, 4, 4, 7, 7, 4, 4, 4, 4, 7, 7, 4, 4, 3, 7, 4, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 255]},
    {'command': [178, 2, 16]}, {'data': [255, 0, 192, 63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 192, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 128, 126, 1, 0, 0, 0, 1, 126, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 0, 192, 56, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255]},
    {'command': [179, 2, 16]}, {'data': [255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 224, 31, 0, 0, 0, 0, 0, 0, 0, 31, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 14, 112, 128, 112, 14, 1, 0, 0, 0, 0, 0, 0, 0, 0, 30, 112, 62, 112, 30, 2, 56, 124, 68, 124, 56, 0, 68, 124, 120, 76, 4, 12, 65, 65, 127, 127, 64, 64, 56, 124, 69, 127, 127, 64, 0, 94, 94, 0, 0, 0, 0, 255]},
    {'command': [180, 2, 16]}, {'data': [255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 248, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 248, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 112, 14, 1, 14, 112, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255]},
    {'command': [181, 2, 16]}, {'data': [255, 0, 1, 126, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 126, 1, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 128, 126, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 126, 128, 0, 0, 0, 0, 0, 0, 0, 0, 224, 28, 3, 0, 0, 0, 0, 0, 3, 28, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255]},
    {'command': [182, 2, 16]}, {'data': [255, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 56, 7, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 224, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 224, 0, 0, 0, 0, 192, 56, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 56, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255]},
    {'command': [183, 2, 16]}, {'data': [255, 128, 128, 128, 128, 128, 128, 131, 140, 136, 144, 144, 176, 144, 144, 136, 140, 131, 128, 128, 128, 128, 128, 128, 191, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 191, 128, 184, 167, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 167, 184, 128, 176, 142, 129, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 129, 142, 176, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 255]}
]
