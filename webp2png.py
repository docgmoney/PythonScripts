import os
from PIL import Image

def convert_webp_to_png(input_file, output_dir):
    # Open the .webp image
    with Image.open(input_file) as img:
        # Get the filename without the extension
        filename = os.path.splitext(os.path.basename(input_file))[0]
        # Set the output file path
        output_file = os.path.join(output_dir, filename + ".png")
        # Save it as .png with the same quality
        img.save(output_file, 'PNG', quality=95)

if __name__ == "__main__":
    input_file = input("Enter the path to the .webp file: ")
    output_dir = input("Enter the directory path where you want to save the .png file: ")

    convert_webp_to_png(input_file, output_dir)
