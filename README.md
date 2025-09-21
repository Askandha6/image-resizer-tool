# image-resizer-tool
Batch Image Resizer & Converter
This Python script resizes and converts images in bulk using the Pillow library.
It is useful when you need to standardize image sizes or convert them into a specific format (JPEG, PNG, WEBP, etc.).
Resize all images in a given folder to a fixed size.
Convert images into any supported format (JPEG, PNG, WEBP, etc.).
Automatically creates the output folder if it doesn’t exist.
Skips invalid or unsupported files gracefully.

Python 3.7+
Pillow (PIL fork)
Install dependencies:
Copy code
Bash
pip install pillow
Place your input images inside a folder (e.g., input_images/).
Run the script with the desired parameters.
Example:
Copy code
Python
from batch_resize_convert import batch_resize_convert

input_folder = "input_images"      # folder containing images
output_folder = "output_images"    # folder to save resized/converted images

# Resize to 400x400 and convert to PNG
batch_resize_convert(input_folder, output_folder, size=(400, 400), output_format="PNG")

project/
│── batch_resize_convert.py
│── input_images/
│    ├── photo1.jpg
│    ├── photo2.jpeg
│    ├── image.png
│── output_images/
│    ├── photo1.png
│    ├── photo2.png
│    ├── image.png
⚙ Function Parameters

batch_resize_convert(input_folder, output_folder, size=(800, 600), output_format="JPEG")
input_folder → Path to folder with original images
output_folder → Path where processed images will be saved
size → Tuple (width, height) for resizing
output_format → Target format ("JPEG", "PNG", "WEBP", etc.)
 Output
Input: photo.jpg (1920x1080)
Output: photo.png (400x400)
