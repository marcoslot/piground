#!/usr/bin/python3
from phue import Bridge
from pprint import pprint

b = Bridge('192.168.87.212')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
lights = b.get_light_objects()

for light in lights:
    if "Fugato" in light.name:
        light.on = False
