"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 2000 / 120 # 120 frames per second.
graphics = BreakoutGraphics()


def main():
    graphics.window.add(graphics.life)
    onmouseclicked(game_start)


def game_start(mouse):
    if graphics.lives >= 1:
        if graphics.is_game_start:
            graphics.set_ball_position()
            graphics.is_game_start = False
            while True:
                pause(FRAME_RATE)
                graphics.ball_detect()
                if graphics.ball.y > graphics.window.height:
                    graphics.lives -= 1
                    graphics.life.text = 'Lives: ' + str(graphics.lives)
                    graphics.is_game_start = True
                    break
                if graphics.count == graphics.brick_rows * graphics.brick_cols:
                    break


if __name__ == '__main__':
    main()
