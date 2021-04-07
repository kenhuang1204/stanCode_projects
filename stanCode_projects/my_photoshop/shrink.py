"""
File: shrink.py
Name: 黃科諺
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the filename of the image to be shrink
    :return img: SimpleImage, a shrink image with half the original width and half the original height
    """
    img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(shrink_img.width):
        for y in range(shrink_img.height):
            shrink_pixel = shrink_img.get_pixel(x, y)
            old_pixel = img.get_pixel(x*2, y*2)

            shrink_pixel.red = old_pixel.red
            shrink_pixel.green = old_pixel.green
            shrink_pixel.blue = old_pixel.blue
    return shrink_img


def main():
    """
    Input: img, an image to be shrink
    Output: img, a shrink image with half the original width and half the original height
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
