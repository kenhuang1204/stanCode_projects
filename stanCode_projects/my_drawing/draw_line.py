"""
File: draw_line.py
Name: 黃科諺
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()
SIZE = 5
count = 0
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global count
    global oval
    count += 1
    if count % 2 == 1:
        oval = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        window.add(oval)
    else:
        window.remove(oval)
        line = GLine(oval.x+SIZE/2, oval.y+SIZE/2, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
