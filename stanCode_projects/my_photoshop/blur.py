"""
File: blur.py
Name: 黃科諺
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, an image to be blurred
    :return: img, a blurred image
    """
    blurred = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)
            new_pixel = blurred.get_pixel(x, y)

            if x==0:
                if y==0:
                    old_pixel6 = img.get_pixel(x + 1, y)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    old_pixel9 = img.get_pixel(x + 1, y + 1)
                    new_pixel.red= (old_pixel.red + old_pixel6.red + old_pixel8.red + old_pixel9.red)//4
                    new_pixel.green = (old_pixel.green + old_pixel6.green + old_pixel8.green + old_pixel9.green) // 4
                    new_pixel.blue = (old_pixel.blue + old_pixel6.blue + old_pixel8.blue + old_pixel9.blue) // 4
                elif y==(img.height-1):
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel3 = img.get_pixel(x + 1, y - 1)
                    old_pixel6 = img.get_pixel(x + 1, y)
                    new_pixel.red = (old_pixel.red + old_pixel2.red + old_pixel3.red + old_pixel6.red) // 4
                    new_pixel.green = (old_pixel.green + old_pixel2.green + old_pixel3.green + old_pixel6.green) // 4
                    new_pixel.blue = (old_pixel.blue + old_pixel2.blue + old_pixel3.blue + old_pixel6.blue) // 4
                else:
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel3 = img.get_pixel(x + 1, y - 1)
                    old_pixel6 = img.get_pixel(x + 1, y)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    old_pixel9 = img.get_pixel(x + 1, y + 1)
                    new_pixel.red = (old_pixel.red + old_pixel2.red + old_pixel3.red + old_pixel6.red + old_pixel8.red + old_pixel9.red) // 6
                    new_pixel.green = (old_pixel.green + old_pixel2.green + old_pixel3.green + old_pixel6.green + old_pixel8.green + old_pixel9.green) // 6
                    new_pixel.blue = (old_pixel.blue + old_pixel2.blue + old_pixel3.blue + old_pixel6.blue + old_pixel8.blue + old_pixel9.blue) // 6
            elif x==(img.width-1):
                if y==0:
                    old_pixel4 = img.get_pixel(x - 1, y)
                    old_pixel7 = img.get_pixel(x - 1, y + 1)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    new_pixel.red= (old_pixel.red + old_pixel4.red + old_pixel7.red + old_pixel8.red)//4
                    new_pixel.green = (old_pixel.green + old_pixel4.green + old_pixel7.green + old_pixel8.green) // 4
                    new_pixel.blue = (old_pixel.blue + old_pixel4.blue + old_pixel7.blue + old_pixel8.blue) // 4
                elif y==(img.height-1):
                    old_pixel1 = img.get_pixel(x - 1, y - 1)
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel4 = img.get_pixel(x - 1, y)
                    new_pixel.red = (old_pixel.red + old_pixel1.red + old_pixel2.red + old_pixel4.red) // 4
                    new_pixel.green = (old_pixel.green + old_pixel1.green + old_pixel2.green + old_pixel4.green) // 4
                    new_pixel.blue = (old_pixel.blue + old_pixel1.blue + old_pixel2.blue + old_pixel4.blue) // 4
                else:
                    old_pixel1 = img.get_pixel(x - 1, y - 1)
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel4 = img.get_pixel(x - 1, y)
                    old_pixel7 = img.get_pixel(x - 1, y + 1)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    new_pixel.red = (old_pixel.red + old_pixel1.red + old_pixel2.red + old_pixel4.red + old_pixel7.red + old_pixel8.red) // 6
                    new_pixel.green = (old_pixel.green + old_pixel1.green + old_pixel2.green + old_pixel4.green + old_pixel7.green + old_pixel8.green) // 6
                    new_pixel.blue = (old_pixel.blue + old_pixel1.blue + old_pixel2.blue + old_pixel4.blue + old_pixel7.blue + old_pixel8.blue) // 6
            else:
                if y==0:
                    old_pixel4 = img.get_pixel(x - 1, y)
                    old_pixel6 = img.get_pixel(x + 1, y)
                    old_pixel7 = img.get_pixel(x - 1, y + 1)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    old_pixel9 = img.get_pixel(x + 1, y + 1)
                    new_pixel.red = (old_pixel.red + old_pixel4.red + old_pixel6.red + old_pixel7.red + old_pixel8.red + old_pixel9.red) // 6
                    new_pixel.green = (old_pixel.green + old_pixel4.green + old_pixel6.green + old_pixel7.green + old_pixel8.green + old_pixel9.green) // 6
                    new_pixel.blue = (old_pixel.blue + old_pixel4.blue + old_pixel6.blue + old_pixel7.blue + old_pixel8.blue + old_pixel9.blue) // 6
                elif y==(img.height-1):
                    old_pixel1 = img.get_pixel(x - 1, y - 1)
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel3 = img.get_pixel(x + 1, y - 1)
                    old_pixel4 = img.get_pixel(x - 1, y)
                    old_pixel6 = img.get_pixel(x + 1, y)
                    new_pixel.red = (old_pixel.red + old_pixel1.red + old_pixel2.red + old_pixel3.red + old_pixel4.red + old_pixel6.red) // 6
                    new_pixel.green = (old_pixel.green + old_pixel1.green + old_pixel2.green + old_pixel3.green + old_pixel4.green + old_pixel6.green) // 6
                    new_pixel.blue = (old_pixel.blue + old_pixel1.blue + old_pixel2.blue + old_pixel3.blue + old_pixel4.blue + old_pixel6.blue) // 6
                else:
                    old_pixel1 = img.get_pixel(x - 1, y - 1)
                    old_pixel2 = img.get_pixel(x, y - 1)
                    old_pixel3 = img.get_pixel(x + 1, y - 1)
                    old_pixel4 = img.get_pixel(x - 1, y)
                    old_pixel6 = img.get_pixel(x + 1, y)
                    old_pixel7 = img.get_pixel(x - 1, y + 1)
                    old_pixel8 = img.get_pixel(x, y + 1)
                    old_pixel9 = img.get_pixel(x + 1, y + 1)
                    new_pixel.red = (old_pixel.red + old_pixel1.red + old_pixel2.red + old_pixel3.red + old_pixel4.red + old_pixel6.red + old_pixel7.red + old_pixel8.red + old_pixel9.red) // 9
                    new_pixel.green = (old_pixel.green + old_pixel1.green + old_pixel2.green + old_pixel3.green + old_pixel4.green + old_pixel6.green + old_pixel7.green + old_pixel8.green + old_pixel9.green) // 9
                    new_pixel.blue = (old_pixel.blue + old_pixel1.blue + old_pixel2.blue + old_pixel3.blue + old_pixel4.blue + old_pixel6.blue + old_pixel7.blue + old_pixel8.blue + old_pixel9.blue) // 9
    return blurred


def main():
    """
    Input: img, an old image to be blurred
    Output: img, a blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
