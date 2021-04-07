"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

NUM_LIVES = 3
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 5        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
BALL_OFFSET = 150

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, title='Breakout'):

        self.paddle_offset = paddle_offset
        self.ball_radius = ball_radius
        self.count = 0
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.ball_upper = brick_rows * (brick_height + brick_spacing)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_controller)

        self.is_game_start = True

        # Life text.
        self.lives = NUM_LIVES
        self.life = GLabel(f'Lives: {self.lives}', x=1, y=20)

        # Draw bricks.
        for i in range(brick_rows):
            for j in range (brick_cols):
                self.brick = GRect(brick_width, brick_height, x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))
                self.brick.filled = True
                if i < brick_rows/5:
                    self.brick.fill_color = 'red'
                elif i < brick_rows * 2 / 5:
                    self.brick.fill_color = 'orange'
                elif i < brick_rows * 3 / 5:
                    self.brick.fill_color = 'yellow'
                elif i < brick_rows * 4 / 5:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    def ball_detect(self):
        thing1 = self.window.get_object_at(self.ball.x, self.ball.y)
        thing2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        thing3 = self.window.get_object_at(self.ball.x, self.ball.y + + 2 * self.ball_radius)
        thing4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + + 2 * self.ball_radius)
        if thing1 is None:
            if thing2 is None:
                if thing3 is None:
                    if thing4 is None:
                        self.move_ball()
                    elif thing4 is self.paddle:
                        self.paddle_bounce()
                    elif thing4 is self.life:
                        self.move_ball()
                    else:
                        self.bounce()
                        self.window.remove(thing4)
                        self.count += 1
                elif thing3 is self.paddle:
                    self.paddle_bounce()
                elif thing3 is self.life:
                    self.move_ball()
                else:
                    self.bounce()
                    self.window.remove(thing3)
                    self.count += 1
            elif thing2 is self.paddle:
                self.paddle_bounce()
            elif thing2 is self.life:
                self.move_ball()
            else:
                self.bounce()
                self.window.remove(thing2)
                self.count += 1
        elif thing1 is self.paddle:
            self.paddle_bounce()
        elif thing1 is self.life:
            self.move_ball()
        else:
            self.bounce()
            self.window.remove(thing1)
            self.count += 1

    def paddle_bounce(self):
        if self.__dy > 0:
            self.__dy = - self.__dy
            self.ball.move(self.__dx, self.__dy)
        else:
            self.ball.move(self.__dx, self.__dy)

    def bounce(self):
        self.__dy = - self.__dy
        self.ball.move(self.__dx, self.__dy)

    def game_start(self, mouse):
        if self.is_game_start:
            self.set_ball_position()
            self.is_game_start = False

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)
        if self.ball.x < 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        if self.ball.y < 0:
            self.__dy = -self.__dy

    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = self.window.height/2 - self.ball_radius
        self.window.add(self.ball)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def paddle_controller(self, mouse):
        mouse_in_screen = self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2
        if mouse_in_screen:
            self.paddle.x = mouse.x - self.paddle.width / 2
        if mouse.y == self.window.height - self.paddle_offset:
            self.paddle.y = mouse.y - self.paddle.height / 2








