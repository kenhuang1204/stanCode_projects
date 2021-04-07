"""
File: green_screen.py
Name: 黃科諺
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: img, an image that is to replace the green screen
    :param figure_img: img, the original image with a green screen
    :return: img, a new image with the green screen replaced by the background
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            bg_pixel=background_img.get_pixel(x, y)
            new_pixel=figure_img.get_pixel(x, y)

            bigger = max(new_pixel.red, new_pixel.blue)
            if new_pixel.green > bigger*2:
                new_pixel.red = bg_pixel.red
                new_pixel.green = bg_pixel.green
                new_pixel.blue = bg_pixel.blue
    return figure_img


def main():
    """
    Input: img, an image with a green screen
    Output: img, a new image with the green screen replaced by another background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
