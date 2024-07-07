import vertexai
from vertexai.vision_models import ImageTextModel, Image
import base64
import requests
import sys
import os

PROJECT_ID = 'eminent-tesla-402318'
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def caption_image_old(image_path):
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

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def caption_image(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {OPENAI_KEY}"
    }

    payload = {
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What are the main objects in this image? Do not describe the surroundings. If the object is an image or figurine or toy, only describe what the object portrays. Do not mention that it's an image, or toy, or figurine. Do give some details around colors, shape, etc."
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 200
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = 'camera.png'

    caption = caption_image(image_path)

    print(caption)
