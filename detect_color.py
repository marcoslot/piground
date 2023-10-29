#!/usr/bin/python3
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

def get_dominant_colors(image_path, n_colors=5):
    # Load image using PIL
    image = Image.open(image_path)
    np_image = np.array(image)

    # Flatten the image data
    pixels = np_image.reshape(-1, 3)

    # Remove alpha if exists
    if np_image.shape[2] == 4:
        pixels = pixels[:, :3]

    # Apply KMeans clustering with fixed seed
    kmeans = KMeans(n_clusters=n_colors, n_init='auto', random_state=0)
    kmeans.fit(pixels)

    # Get RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert to integer from float
    dominant_colors = [tuple(map(int, color)) for color in colors]

    # Combine colors and bin counts and then sort by bin count
    #labels = kmeans.labels_
    #bin_counts = np.bincount(labels)
    #combined = zip(dominant_colors, bin_counts)
    #sorted_combined = sorted(combined, key=lambda t: t[1], reverse=True)
    #dominant_colors = [color for color, bin_count in sorted_combined]

    return dominant_colors

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = 'camera-latest.png'

    main_colors = get_dominant_colors(image_path)
    print(main_colors)
