import os
import argparse
from collections import Counter
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_dominant_color(image, k=10):
    """
    Get the dominant color of an image using k-means clustering.

    Parameters:
    - image: PIL.Image object
    - k: Number of clusters for k-means

    Returns:
    - dominant_color: Tuple representing the dominant RGB color
    """
    # Resize image to reduce processing time
    image = image.resize((100, 100))
    
    # Convert image to RGB or RGBA if not already in that mode
    if image.mode not in ['RGB', 'RGBA']:
        image = image.convert('RGBA')
    
    # Convert image to numpy array
    image_np = np.array(image)
    
    # Remove fully transparent pixels (if any)
    if image.mode == 'RGBA':
        pixels = np.array([pixel[:3] for pixel in image_np.reshape((-1, 4)) if pixel[3] != 0])
    else:
        pixels = image_np.reshape((-1, 3))
    
    # Use k-means to cluster the pixel colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    
    # Get the cluster centers and counts
    counts = Counter(kmeans.labels_)
    centers = kmeans.cluster_centers_
    
    # Get the most common cluster center
    dominant_color = centers[counts.most_common(1)[0][0]]
    
    # Convert to integer
    dominant_color = tuple(int(c) for c in dominant_color)
    
    return dominant_color

def closest_color(requested_color):
    """
    Find the closest predefined color to the requested color.

    Parameters:
    - requested_color: Tuple representing an RGB color

    Returns:
    - closest_color_name: String name of the closest color
    """
    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "grey": (128, 128, 128),
        "brown": (165, 42, 42),
        "sepia": (112, 66, 20),
        "bronze": (205, 127, 50),
        "rosewood": (101, 0, 11),
        "blue": (0, 0, 255),
        "mauve": (224, 176, 255),
        "tan": (210, 180, 140),
        "old_rose": (192, 128, 129),
        "sky_blue": (135, 206, 235),
        "gold": (255, 215, 0),
        "maroon": (128, 0, 0),
        "indigo": (75, 0, 130),
        "celadon": (172, 225, 175),
        "forest_green": (34, 139, 34),
        "green": (0, 128, 0),
        "blue_violet": (138, 43, 226),
        "lavender": (230, 230, 250),
        "carmine": (150, 0, 24),
        "red": (255, 0, 0),
        "pink": (255, 192, 203),
        "peach": (255, 229, 180),
        "amber": (255, 191, 0),
        "yellow": (255, 255, 0),
        "aquamarine": (127, 255, 212),
        "plum": (142, 69, 133),
        "umber": (99, 81, 71),
        "olive": (128, 128, 0),
        "yellow_green": (154, 205, 50),
        "lime": (0, 255, 0),
        "rust": (183, 65, 14),
        "salmon": (250, 128, 114),
        "orange": (255, 165, 0),
        "copper": (184, 115, 51),
        "ruby": (224, 17, 95),
        "magenta": (255, 0, 255),
        "cerise": (222, 49, 99),
        "azure": (0, 127, 255),
        "pale_blue": (175, 238, 238),
        "bisque": (255, 228, 196),
        "ocher": (204, 119, 34),
        "sage": (188, 184, 138),
        "ivory": (255, 255, 240),
        "slate": (112, 128, 144),
        "rice": (255, 247, 219),
        "graphite": (36, 36, 36),
        "iron": (67, 70, 75),
        "pewter": (143, 143, 143),
        "cloud": (201, 226, 255),
        "smoke": (115, 130, 118),
        "ash": (135, 142, 138),
        "propose": (65, 68, 81),
        "fog": (207, 214, 207),
        "dove": (192, 192, 192),
        "lead": (119, 136, 153),
        "fossil": (210, 208, 203)
    }
    
    min_distance = float('inf')
    closest_color_name = None
    
    for color_name, color_value in colors.items():
        distance = sum((requested_color[i] - color_value[i]) ** 2 for i in range(3))
        if distance < min_distance:
            min_distance = distance
            closest_color_name = color_name
    
    # Adjust the threshold to be less strict
    threshold = 10000
    if min_distance > threshold:
        return "miscellaneous"
    
    return closest_color_name

def process_images(source_folder, destination_folder_base='./colors'):
    """
    Process images in the source folder and sort them by their dominant color.

    Parameters:
    - source_folder: Path to the source folder containing images
    - destination_folder_base: Base path for destination folders
    """
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder_base):
        os.makedirs(destination_folder_base)
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(source_folder, filename)
            try:
                image = Image.open(image_path)
                
                if image.mode == 'P' and 'transparency' in image.info:
                    image = image.convert('RGBA')

                dominant_color = get_dominant_color(image)
                closest = closest_color(dominant_color)
                
                destination_folder = os.path.join(destination_folder_base, closest)
                
                # Create the destination color folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                destination_path = os.path.join(destination_folder, filename)
                
                print(f"Moving {filename} to {closest} folder")
                image.save(destination_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Sort images into folders by their dominant color.")
    parser.add_argument('source_folder', help="Path to the source folder containing images")
    parser.add_argument('--destination_folder_base', default='./colors', help="Base path for destination folders")
    
    args = parser.parse_args()
    process_images(args.source_folder, args.destination_folder_base)

if __name__ == "__main__":
    main()
