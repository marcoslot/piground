PROJECT_ID = 'eminent-tesla-402318'

import sys
import vertexai
from vertexai.vision_models import ImageTextModel, Image

if len(sys.argv) >= 2:
    image_filename = sys.argv[1]
else:
    image_filename = 'camera.jpg'

if __name__ == "__main__":
    vertexai.init(project=PROJECT_ID)
    model = ImageTextModel.from_pretrained("imagetext@001")

    source_image = Image.load_from_file(location=image_filename)

    captions = model.get_captions(
        image=source_image,
        # Optional:
        number_of_results=1,
        language="en",
    )
    print(captions[0])
