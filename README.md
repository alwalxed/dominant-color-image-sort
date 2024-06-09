# Image Color Sorter

A Python script to sort images into folders based on their dominant color.

## Features

- Supports multiple image formats: PNG, JPG, JPEG, BMP, GIF, TIFF.
- Uses k-means clustering to determine the dominant color.
- Maps the dominant color to the closest predefined color name.
- Organizes images into folders named after the dominant color.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/alwalxed/image-color-sorter.git
   cd image-color-sorter
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To sort images by their dominant color and move them to corresponding folders, run the following command:

```
python -m image_color_sorter.sorter /path/to/source/folder --destination_folder_base /path/to/destination/folder
```

## Example

```
python -m image_color_sorter.sorter ./images --destination_folder_base ./sorted_images
```

This command will process all images in the ./images folder and sort them into subfolders in the ./sorted_images directory based on their dominant colors.

## License

This project is licensed under the MIT License. See the LICENSE file for details
