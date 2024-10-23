import sys
from PIL import Image

def print_image_in_terminal(image_path):
    try:
        img = Image.open(image_path)
    except IOError:
        print(f"Unable to open image: {image_path}")
        return

    width, height = img.size
    img = img.resize((width, height))

    img = img.convert('RGB')

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            # Use ANSI escape codes to set the background color
            print(f"\033[48;2;{r};{g};{b}m \033[48;2;{r};{g};{b}m ", end="")
        print("\033[0m")  # Reset color at the end of each line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ./main.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        print_image_in_terminal(image_path)
