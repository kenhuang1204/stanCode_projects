"""
File: fire.py
Name: 黃科諺
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the filename of a greenland image with fire
    :return: img, a new image with fire highlighted and the other pixels gray-scaled
    """
    highlighted = SimpleImage(filename)
    for pixel in highlighted:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red=255
            pixel.green=0
            pixel.blue=0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlighted


def main():
    """
    Input: img, a greenland image with or without fire
    Output: img, a new image with fire highlighted and the other pixels gray-scaled
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()




if __name__ == '__main__':
    main()
