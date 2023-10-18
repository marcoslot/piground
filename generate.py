import sys
import os
import openai

def generate_image(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    images = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = images['data'][0]['url']

    return image_url

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise ValueError("no prompt specified")

    prompt = ' '.join(sys.argv[1:])

    image_url = generate_image(prompt)
    print(image_url)
