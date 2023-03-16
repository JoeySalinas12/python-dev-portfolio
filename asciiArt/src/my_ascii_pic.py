from PIL import Image


def resize_image(image, new_width = 100):
    # Resize image
    width, height = image.size
    # Change the last number depending on the size of the original image
    ratio = height/width/1.8
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# convert each pixel to grayscale
def image_to_grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# covert pixels to ascii characters
def get_ascii_char(image):
    '''
        // is the operation for floor divison. This guarantees that we get an integer as the result. 
    So "pixel//25" divides the intensity of the pixel by 25 and rounds it to the smallest integer.
    The important thing to notice is that he is using the result of "pixel//25" (e.g. let's say 3)
    to choose an element from the list of ASCII charachters he made earlier (so in our example, it
    would choose the 4th element, which is "%"). This is also why ASCII charachters were listed in
    descending intensity at the start.
    '''
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    pixels = image.getdata()
    ascii_length = len(ascii_chars)
    # adjust the divisor of the // opertion to adjust granularity in txt image
    ascii_line = "".join([ascii_chars[pixel//35] for pixel in pixels])
    return(ascii_line)

def change_color(image):
    for row in image:
        print(len(row))


# def print_ascii_matrix(ascii_matrix, text_color):
#     for row in ascii_matrix:
#         line = [p+p+p for p in row]
#         print(text_color + "".join(line))

#     print(Style.RESET_ALL)
