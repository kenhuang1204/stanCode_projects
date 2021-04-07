"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 2000 / 120 # 120 frames per second.
graphics = BreakoutGraphics()


def main():
    graphics.window.add(graphics.life)
    graphics.window.add(graphics.score_text)
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
                    graphics.window.remove(graphics.paddle)
                    graphics.window.remove(graphics.ball)
                    graphics.window.remove(graphics.life)
                    congrats = GLabel('You Win!')
                    congrats.font = 'Courier-30'
                    graphics.window.add(congrats, x=(graphics.window.width-congrats.width)/2, y=(graphics.window.height-congrats.height)/2)
                    break


if __name__ == '__main__':
    main()
