#!/bin/sh
fswebcam -q -r 1280x720 --no-banner camera.jpg
CAPTION=$(python3 vertex.py 2>/dev/null)
echo $CAPTION

HEX_COLOR=$(python3 color.py $CAPTION)
echo $HEX_COLOR

python3 hue.py $HEX_COLOR
