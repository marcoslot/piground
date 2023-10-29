import sys
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) >= 2:
    image_path = sys.argv[1]
else:
    image_path = 'camera-latest.png'

variations = openai.Image.create_variation(
    image=open(image_path, "rb"),
    n=1,
    size="1024x1024"
)

print(variations)
