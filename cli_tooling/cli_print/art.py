import random
from pathlib import Path
from ascii_magic import AsciiArt

def main():

    # Set up the file path to the images directory
    images = Path(__file__).resolve().parent / 'images'

    # Randomly select an image path
    image_path = random.choice(
        [x for x in images.iterdir()] # iterate over image filepaths
        )

    # Generate ascii art
    my_art = AsciiArt.from_image(image_path)

    # Print to terminal
    my_art.to_terminal()
