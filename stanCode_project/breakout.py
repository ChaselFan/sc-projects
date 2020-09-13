"""
File : break.py
Name : Chasel Fan
-----------------------
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
import random

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
P_Y_SPEED=-5


t=0
graphics = BreakoutGraphics()
live=NUM_LIVES
brick_n=graphics.brick_rows*graphics.brick_cols

def main():

    # Add animation loop here!
    # make paddle and bricks
    graphics.make_a_paddle()
    graphics.brick()
    onmouseclicked(function)


def function(event):
    onmousemoved(function2)
    global t
    global graphics
    global live
    global brick_n
    t+=1
    if brick_n is not 0:
        if t > 0:
            while True:
                if brick_n==0:
                    # you break all the bricks and you will see 'YOU WON'
                    graphics.window.clear()
                    rect=GRect(graphics.window.width,graphics.window.height)
                    rect.filled=True
                    rect.fill_color='black'
                    graphics.window.add(rect)
                    label = GLabel('YOU　WON')
                    label.font = '-50'
                    label_x = 50
                    label_y = graphics.window.width / 2 + label.width / 2
                    label.color = 'white'
                    graphics.window.add(label, label_x, label_y)
                    break
                # you have 3 lives
                if graphics.out_of_window():
                    live -= 1
                    if live > 0:
                        graphics.reset_ball()
                        onmouseclicked(function)
                        break
                    else:
                        # you have no live and you will see 'YOU LOSE'
                        graphics.window.clear()
                        r=GRect(graphics.window.width,graphics.window.height)
                        r.filled=True
                        r.fill_color='black'
                        graphics.window.add(r)
                        label3 = GLabel('YOU　LOSE')
                        label3.font = '-50'
                        label_x3 = 50
                        label_y3 = graphics.window.width / 2 + label3.width / 2
                        label3.color='white'
                        graphics.window.add(label3, label_x3, label_y3)
                        break
                # the ball move dx and dy
                graphics.ball.move(graphics.dx, graphics.dy)
                # The ball bounces against the wall
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    graphics.dx = -graphics.dx
                if graphics.ball.y <= 0:
                    graphics.dy *= -1
                # the ball break the brick by remove
                if graphics.ball_touch_brick() is not None:
                    obj = graphics.ball_touch_brick()
                    graphics.window.remove(obj)
                    graphics.dy = -graphics.dy
                    brick_n-=1
                # The ball bounces against the paddle
                if graphics.ball_touch_paddle()==graphics.p:
                    graphics.dy = P_Y_SPEED
                    graphics.ball.move(graphics.dx, graphics.dy)
                pause(FRAME_RATE)


def function2(mouse):
    # the paddle will follow the mouse
    graphics.p.x=mouse.x-graphics.p.width/2


if __name__ == '__main__':
    main()