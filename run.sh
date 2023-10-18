#!/bin/sh
fswebcam -q -r 1280x720 --no-banner camera.jpg
python3 vertex.py 2>/dev/null
