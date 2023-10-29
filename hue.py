#!/usr/bin/python3
import sys
from phue import Bridge
from pprint import pprint

b = Bridge('192.168.87.212')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

def convert_color(hexCode):
    R = int(hexCode[:2],16)
    G = int(hexCode[2:4],16)
    B = int(hexCode[4:6],16)

    total = R + G + B

    if R == 0:
        firstPos = 0
    else:
        firstPos = R / total
                            
    if G == 0:
        secondPos = 0
    else:
        secondPos = G / total

    return [firstPos, secondPos]

def set_lights_color(hex_color):
    lights = b.get_light_objects()

    for light in lights:
        if "Fugato" in light.name:
            light.on = True
            light.xy = convert_color(hex_color)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        hex_color = sys.argv[1]
    else:
        hex_color = 'ff0000'

    set_lights_color(hex_color)
