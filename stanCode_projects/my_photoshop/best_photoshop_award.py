"""
File: best_photoshop_award.py
Name: 黃科諺
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
BLACK = 120


def main():
    """
    Luffy is one of my favorite character in the animation One Piece. The gesture of my picture is similar to Luffy's signature gesture, and I like it.
    """
    bg = SimpleImage("image_contest/Luffy.jpg")
    figure = SimpleImage("image_contest/figure.jpg")
    result = combine(bg, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: img, an image of Luffy
    :param figure_img: img, an image of Kenny
    :return: img, a new image with the green screen replaced by the background
    """
    background_img.make_as_big_as(figure_img)
    for pixel in background_img:
        pixel.red *= 1.1
        pixel.green *= 1.1
        pixel.blue *= 1.1
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            bg_pixel=background_img.get_pixel(x, y)
            new_pixel=figure_img.get_pixel(x, y)

            avg = (new_pixel.red + new_pixel.green + new_pixel.blue)//3
            total = new_pixel.red + new_pixel.green + new_pixel.blue
            if new_pixel.green > avg*1.2 and total > BLACK:
                new_pixel.red = bg_pixel.red
                new_pixel.green = bg_pixel.green
                new_pixel.blue = bg_pixel.blue
    return figure_img



if __name__ == '__main__':
    main()
