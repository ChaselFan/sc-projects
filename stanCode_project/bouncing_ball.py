"""
File: 
Name:
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
ball=GOval(SIZE,SIZE)
t=0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled=True
    ball.fill_color='black'
    window.add(ball,START_X,START_Y)
    onmouseclicked(function)

def function(e):
    global ball
    global VX
    global GRAVITY
    global t
    t+=1
    if t==1:
        while ball.x<=window.width:
            ball.move(5,VX)
            VX+=GRAVITY
            if ball.y>=window.height:
                VX = -VX
                VX*=0.9
            pause(DELAY)
        ball.x=START_X
        ball.y=START_Y

if __name__ == "__main__":
    main()
