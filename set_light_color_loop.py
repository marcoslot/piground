#!/usr/bin/python3
import os
import math
import time
from detect_color import get_main_color, color_tuple_to_hex
from hue import set_lights_color

def color_distance(left,right):
    rd = abs(left[0] - right[0])
    gd = abs(left[1] - right[1])
    bd = abs(left[2] - right[2])
    return math.sqrt(rd**2 + gd**2 + bd**2)

if __name__ == "__main__":
    image_path = f"/tmp/camera-color.png"
    last_color = (0,0,0)

    while True:
        os.system(f"fswebcam -q -r 640x480 --skip 1 --no-banner --png 9 {image_path}")
        color_tuple = get_main_color(image_path)

        if color_distance(color_tuple, last_color) > 40:
            hex_color = color_tuple_to_hex(color_tuple)
            last_color = color_tuple
            print(hex_color)
            set_lights_color(hex_color)

        time.sleep(1)
