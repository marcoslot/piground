PROJECT_ID = 'eminent-tesla-402318'

import sys
import vertexai
from vertexai.vision_models import ImageTextModel, Image

def caption_image(image_path):
    vertexai.init(project=PROJECT_ID)
    model = ImageTextModel.from_pretrained("imagetext@001")

    source_image = Image.load_from_file(location=image_path)

    captions = model.get_captions(
        image=source_image,
        # Optional:
        number_of_results=1,
        language="en",
    )

    return captions[0]

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = 'camera.png'

    caption = caption_image(image_path)

    print(caption)
