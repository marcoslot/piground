#!/usr/bin/python3
import os
from detect_color import get_main_color_hex
from hue import set_lights_color

def set_lights_color_from_image(image_path):
    os.system(f"fswebcam -q -r 1280x720 --skip 1 --no-banner --png 9 {image_path}")

    hex_color = get_main_color_hex(image_path)
    print(hex_color)

    set_lights_color(hex_color)


if __name__ == "__main__":
    camera_image_path = f"/tmp/camera-color.png"
    set_lights_color_from_image(camera_image_path)
