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

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 20       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title='breakout')

        # make a ball that is black
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.reset_ball()

        self.brick_height = BRICK_HEIGHT
        self.brick_rows = BRICK_ROWS
        self.brick_spacing = BRICK_SPACING
        self.brick_cols=BRICK_COLS


        # Create a paddle.
        # Center a filled ball in the graphical window.
        # Default initial velocity for the ball.
        # Initialize our mouse listeners.
        # Draw bricks

    # it check that is the ball touching the paddle
    def ball_touch_paddle(self):
        if self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height+1) is self.p:
            return self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height+1)

    # it check that is the ball touching the brick
    def ball_touch_brick(self):
        obj = self.window.get_object_at(self.ball.x+self.ball.width/2 , self.ball.y-1)
        if obj is not None and obj is not self.p:
            return self.window.get_object_at(self.ball.x+self.ball.width/2 , self.ball.y-1)

    # set the ball in the middle of window
    def reset_ball(self):
        self.set_ball_position()
        while self.out_of_window():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    # it check that is the out of the window
    def out_of_window(self):
        if self.ball.y + self.ball.height >= self.window.height:
            return True

    # this is the position of the ball
    def set_ball_position(self):
        self.ball.x=self.window.width/2-self.ball.width/2
        self.ball.y=self.window.height/2-self.ball.height/2

    # the moving speed of the ball
    def set_ball_velocity(self):
        self.dx=random.randint(3,MAX_X_SPEED)
        self.dy=INITIAL_Y_SPEED
        if random.random()>0.5:
            self.dx=-self.dx

    # it make a paddle
    def make_a_paddle(self,width=PADDLE_WIDTH,height=PADDLE_HEIGHT):
        self.p = GRect(width,height)
        self.p.filled=True
        self.p.fill_color='black'
        self.window.add(self.p, self.window.width/2-self.p.width/2, self.window.height-PADDLE_OFFSET)

    # it make (BRICK_ROW*BRICK_COLS) bricks and fill color
    def brick(self,width=BRICK_WIDTH,height=BRICK_HEIGHT,space=BRICK_SPACING):
        self.__w=width
        self.__h=height
        self.__s=space
        b_x=0
        b_y=BRICK_OFFSET
        for j in range(BRICK_ROWS):
            for i in range(BRICK_COLS):
                brick=GRect(BRICK_WIDTH,BRICK_HEIGHT)
                brick.filled=True
                if j == 0:
                    brick.fill_color='dark blue'
                elif j==1:
                    brick.fill_color = 'medium blue'
                elif j == 2:
                    brick.fill_color = 'blue'
                elif j==3:
                    brick.fill_color = 'royal blue'
                elif j==4:
                    brick.fill_color = 'dodger blue'
                elif j==5:
                    brick.fill_color = 'light sky blue'
                elif j==6:
                    brick.fill_color = 'sky blue'
                elif j==7:
                    brick.fill_color = 'light blue'
                elif j==8:
                    brick.fill_color = 'powder blue'
                elif j==9:
                    brick.fill_color = 'snow'
                if j==0:
                    self.window.add(brick,b_x,b_y)
                    b_x+=BRICK_SPACING+BRICK_WIDTH
                else:
                    if i==0:
                        b_x=0
                    self.window.add(brick,b_x,b_y+(BRICK_SPACING+BRICK_HEIGHT)*(j))
                    b_x+=BRICK_SPACING+BRICK_WIDTH

