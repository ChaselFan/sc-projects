"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=10

window=GWindow()
click=0
oval = GOval(SIZE, SIZE)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(function)


def function(event):
    global click
    click += 1
    c = click % 2
    if c == 1:
        window.add(oval,event.x-oval.width/2,event.y-oval.height/2)
    elif c == 0:

        line = GLine(oval.x+oval.width/2, oval.y+oval.height/2, event.x, event.y)
        window.get_object_at(oval.x,oval.y)
        window.add(line)



if __name__ == "__main__":
    main()
