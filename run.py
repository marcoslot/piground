#!/usr/bin/python3
import os
from recognize import caption_image
from generate import generate_image
from show import display_image_fullscreen
import urllib.request
from datetime import datetime

unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()

camera_image_path = f"images/camera-{unix_timestamp}.png"
generated_image_path = f"images/generated-{unix_timestamp}.png"

os.system(f"fswebcam -q -r 1280x720 --skip 1 --no-banner --png 9 {camera_image_path}")

caption = caption_image(camera_image_path)

# take the content out of drawings
caption = caption.replace("a drawing of ", "")
caption = caption.replace("a piece of paper with ", "")

caption = f"a drawing of {caption}"

print(caption)

generated_image_url = generate_image(caption)
print(generated_image_url)

urllib.request.urlretrieve(generated_image_url, generated_image_path)
print(generated_image_path)

display_image_fullscreen(generated_image_path)
