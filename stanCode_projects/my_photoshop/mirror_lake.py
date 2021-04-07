"""
File: mirror_lake.py
Name: 黃科諺
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the filename of an image
    :return: img, a new image with twice the original height, same width, and a reflected olg image in the lower half
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height*2)
    for x in range (img.width):
        for y in range (img.height):
            old_pixel=img.get_pixel(x, y)

            new_pixel1=new_img.get_pixel(x, y)
            new_pixel2=new_img.get_pixel(x, new_img.height-1-y)

            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue

            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    return new_img


def main():
    """
    Input: img, an image with given width and height
    Output: img, a new image with twice the original height, same width, and a reflected olg image in the lower half
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
