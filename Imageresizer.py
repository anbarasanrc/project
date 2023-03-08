from PIL import Image
import os

# Define the input and output directories
input_dir = "input"
output_dir = "output"

# Define the target image size
target_size = (800, 800)

# Loop over the files in the input directory
for filename in os.listdir(input_dir):
    # Open the image file
    with Image.open(os.path.join(input_dir, filename)) as img:
        # Resize the image while preserving aspect ratio
        img.thumbnail(target_size)
        # Save the resized image to the output directory
        img.save(os.path.join(output_dir, filename))
