import click
from PIL import Image
from colorama import Fore
from src.my_ascii_pic import resize_image, image_to_grayscale, get_ascii_char

# Use click for CLI configuration
@click.command()
@click.option("--file_path", "-f", default="", show_default=True, 
              help="Enter the file path and image name")
@click.option("--output_file", "-o", default="./", show_default=True,
              help="Enter file output path. Must include file name (with .txt) and path")

def main(file_path: str, output_file: str, new_width: int=100):
    try:
        image = Image.open(file_path)
        resized_image = resize_image(image)
        grayscale_image = image_to_grayscale(resized_image)
        ascii_image = get_ascii_char(grayscale_image)

        # format
        pixel_count = len(ascii_image)
        ascii_image = "\n".join([(ascii_image[index:(index+new_width)]) for index in range(0, pixel_count, new_width)])

        with open(output_file, "w") as file:
            file.write(ascii_image)
    except:
        print(file_path, " is not a valid pathname to an image")



# run script
main()