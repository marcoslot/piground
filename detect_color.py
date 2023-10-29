#!/usr/bin/python3
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

def get_dominant_colors(image_path, n_colors=5):
    # Load image using PIL
    image = Image.open(image_path)
    image = image.resize((320, 240))  # Reduce size for faster processing
    np_image = np.array(image)

    # Flatten the image data
    pixels = np_image.reshape(-1, 3)

    # Remove alpha if exists
    if np_image.shape[2] == 4:
        pixels = pixels[:, :3]

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_colors, n_init=10)
    kmeans.fit(pixels)

    # Get RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert to integer from float
    return [tuple(map(int, color)) for color in colors]

def color_contrast(color_tuple):
    min_val = 255
    max_val = 0
    for val in color_tuple:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val 

    return max_val - min_val

def get_main_color(image_path):
    colors = get_dominant_colors(image_path)
    main_color = max(colors, key=color_contrast)

    return main_color

def color_tuple_to_hex(color_tuple):
    return '%02x%02x%02x' % color_tuple

def get_main_color_hex(image_path):
    main_color_tuple = get_main_color(image_path)
    main_color_hex = color_tuple_to_hex(main_color_tuple)
    return main_color_hex

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = 'camera-latest.png'

    main_color_hex= get_main_color_hex(image_path)
    print(main_color_hex)
