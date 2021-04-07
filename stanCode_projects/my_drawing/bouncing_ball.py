"""
File: bouncing_ball.py
Name: 黃科諺
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
vy = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(fall)


def fall(mouse):
    global vy
    global ball
    global count
    if ball.x == START_X and ball.y == START_Y:
        count += 1
        if count <= 3:
            while True:
                ball.move(VX, vy)
                if ball.x >= window.width - SIZE:
                    window.remove(ball)
                    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                    ball.filled = True
                    ball.fill_color = 'black'
                    window.add(ball)
                    break
                if ball.y >= window.height - SIZE:
                    vy = -abs(vy * REDUCE)
                else:
                    vy += GRAVITY
                pause(DELAY)


if __name__ == "__main__":
    main()
