import os
import sys
import random
from PIL import Image, ImageDraw, ImageOps

def tint_image(src: Image, color: tuple=(255, 255, 255)):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    result = ImageOps.colorize(gray, (0, 0, 0, 0), color)
    result.putalpha(alpha)
    return result

colors = [
    ["Black", (25, 25, 25)], #191919
    ["Gray", (76, 76, 76)], #4c4c4c
    ["Light Gray", (153, 153, 153)], #999999
    ["White", (242, 242, 242)], #f2f2f2
    ["Pink", (242, 127, 165)], #f27fa5
    ["Magenta", (178, 76, 216)], #b24cd8
    ["Purple", (127, 63, 178)], #7f3fb2
    ["Blue", (51, 76, 178)], #334cb2
    ["Cyan", (76, 127, 153)], #4c7f99
    ["Light Blue", (102, 153, 216)], #4c7f99
    ["Green", (102, 127, 51)], #667f33
    ["Lime", (127, 204, 25)], #7fcc19
    ["Yellow", (229, 229, 51)], #e5e533
    ["Orange", (216, 127, 51)], #d87f33
    ["Brown", (102, 76, 51)], #664c33
    ["Red", (153, 51, 51)] #993333
]

layers = random.randint(0, 6)
shadow = Image.open(os.path.join(os.path.dirname(__file__), "img/shadow.png"))
color = random.choice(colors)
banner = Image.new("RGBA", shadow.size, color[1])
print(f"Created new flag with background color {color[0]}")

if layers != 0:
    for i in range(layers):
        n = random.randint(1, 38)
        p = Image.open(os.path.join(os.path.dirname(__file__), "img/pattern_" + str(n).zfill(2) + ".png"))
        c = random.choice(colors)
        pattern = tint_image(p, c[1])
        pattern.convert("RGBA")
        banner = Image.alpha_composite(banner, pattern)
        print(f"Added pattern {n} to banner with color {c[0]}")

banner = Image.alpha_composite(banner, shadow)
banner.save(os.path.join(os.path.dirname(__file__), "output.png"))
print(f"Generated banner with {layers+1} layers")
