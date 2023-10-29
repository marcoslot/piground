#!/usr/bin/python3
import os
import fire
from recognize import caption_image
from generate import generate_image
from show import display_image_fullscreen
import urllib.request
from datetime import datetime

def cam2img():
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()

    camera_image_path = f"images/camera-{unix_timestamp}.png"
    generated_image_path = f"images/generated-{unix_timestamp}.png"

    os.system(f"fswebcam -q -r 1280x720 --skip 1 --no-banner --png 9 {camera_image_path}")

    caption = caption_image(camera_image_path)

    # take the content out of drawings
    caption = caption.replace("a drawing of ", "")
    caption = caption.replace("a piece of paper with ", "")
    caption = caption.replace(" is ", " that is ")

    #caption = f"a drawing of {caption}"
    caption = f"make a drawing of: {caption}"

    print(caption)

    generated_image_url = generate_image(caption)
    print(generated_image_url)

    urllib.request.urlretrieve(generated_image_url, generated_image_path)
    print(generated_image_path)

    os.symlink(camera_image_path, "camera-latest-tmp.png")
    os.rename("camera-latest-tmp.png", "camera-latest.png")
    os.symlink(generated_image_path, "generated-latest-tmp.png")
    os.rename("generated-latest-tmp.png", "generated-latest.png")

    display_image_fullscreen(generated_image_path)

if __name__ == "__main__":
    fire.Fire(cam2img)
