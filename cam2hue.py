#!/usr/bin/python3
import os
import math
import time
import fire
import logging
from colorsys import rgb_to_hls
from detect_color import get_dominant_colors
from hue import set_lights_color, set_lights_colors, is_any_light_on

def color_distance(left_color,right_color):
    rd = abs(left_color[0] - right_color[0])
    gd = abs(left_color[1] - right_color[1])
    bd = abs(left_color[2] - right_color[2])
    return math.sqrt(rd**2 + gd**2 + bd**2)

def color_list_distance(left_list,right_list):
    max_distance = 0

    # calculate the maximum distance between lists
    for (left_color, right_color) in zip(left_list, right_list):
        distance = color_distance(left_color, right_color)
        if distance > max_distance:
            max_distance = distance

    return max_distance

def color_difference(color_tuple):
    min_val = 255
    max_val = 0
    for val in color_tuple:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val 

    return max_val - min_val

def color_magnitude(color_tuple):
    min_val = 255
    max_val = 0
    for val in color_tuple:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val 

    return max_val / min_val

def color_tuple_to_hex(color_tuple):
    return '%02x%02x%02x' % color_tuple

def cam2hue(image_path="/tmp/camera-color.png",loop=False):
    last_colors = []

    while True:
        if is_any_light_on() or not loop:
            os.system(f"fswebcam -q -r 320x240 --skip 2 --no-banner --png 9 {image_path}")
            dominant_colors = get_dominant_colors(image_path, n_colors=5)
            print(dominant_colors)

            high_contrast_colors = list(filter(lambda c: color_difference(c) > 20 and color_magnitude(c) > 3, dominant_colors))
            #high_contrast_colors = list(filter(lambda c: rgb_to_hls(*c)[2] > 0.1 and rgb_to_hls(*c)[1] > 0.1, dominant_colors))

            # Sort by hue
            high_contrast_colors = sorted(high_contrast_colors, key=lambda c: rgb_to_hls(*c)[0])

            if (len(high_contrast_colors) > 0 and
                (len(high_contrast_colors) != len(last_colors) or
                 color_list_distance(high_contrast_colors, last_colors) > 40)):

                hex_colors = list(map(color_tuple_to_hex, high_contrast_colors))
                logging.info(hex_colors)
                set_lights_colors(hex_colors)

                last_colors = high_contrast_colors

        if not loop:
            break

        time.sleep(2)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    image_path = f"/tmp/camera-color.png"
    fire.Fire(cam2hue)
