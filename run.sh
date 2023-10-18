#!/bin/sh
fswebcam -q -r 1280x720 --skip 1 --no-banner --png 9 camera.png

CAPTION=$(python3 recognize.py camera.png 2>/dev/null)
echo $CAPTION

HEX_COLOR=$(python3 detect_color.py $CAPTION)
echo $HEX_COLOR

#python3 hue.py $HEX_COLOR

GENERATED_IMAGE_URL=$(python3 generate.py a drawing of $CAPTION)
echo $GENERATED_IMAGE_URL

curl -s -o generated.png "$GENERATED_IMAGE_URL"

python3 show.py generated.png
