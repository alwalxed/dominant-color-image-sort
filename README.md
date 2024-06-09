# Dominant Color Image Sort 🖼️🎨

A handy Python script that takes a folder of images and sorts them into named folders based on their dominant color. Useful if you want to group random images by a single pattern, in this case: their dominant color.


## 🌟 Features

- Supports multiple image formats: PNG, JPG, JPEG, BMP, GIF, TIFF.
- Uses k-means clustering to determine the dominant color.
- Maps the dominant color to the closest predefined color name.
- Organizes images into folders named after the dominant color.


## 🚀 Installation

Clone the repository:
```
git clone https://github.com/alwalxed/dominant-color-image-sort.git
cd dominant-color-image-sort
```

Install the required dependencies:
```
pip install -r requirements.txt
```


## 💡 Usage

To sort images by their dominant color and move them to corresponding folders, run the following command:

```
python -m image_color_sorter.sorter /path/to/input/folder --destination_folder_base /path/to/output/folder
```


## 🔍 Example

```
python -m image_color_sorter.sorter ./images --destination_folder_base ./sorted_images
```

This command will process all images in the ./images folder and sort them into subfolders in the ./sorted_images directory based on their dominant colors.


## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/alwalxed/dominant-color-image-sort/blob/main/LICENSE) file for details.


## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create your feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.
6. Your contribution will be reviewed, and once approved, it will be merged into the main branch.

Please make sure to update tests as appropriate.
