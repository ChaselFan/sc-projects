"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect,GPolygon,GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window=GWindow(width=550,height=550,title='Pikachu')
    ball=GOval(550,550)
    ball.filled=True
    ball.fill_color='red'
    window.add(ball,0,0)
    ball2=GRect(550,275)
    ball2.filled=True
    ball2.fill_color='white'
    window.add(ball2,0,275)
    ball3=GOval(550,550)
    window.add(ball3)
    ball4=GRect(550,50)
    ball4.filled=True
    ball4.fill_color='black'
    window.add(ball4,0,250)
    tail=GRect(40,20)
    tail.filled=True
    tail.fill_color='gold'
    tail.color='gold'
    window.add(tail, 350, 325)
    tail2 = GRect(20, 60)
    tail2.filled = True
    tail2.fill_color = 'gold'
    tail2.color = 'gold'
    window.add(tail2,370,280)
    tail = GRect(40,20)
    tail.filled = True
    tail.fill_color = 'gold'
    tail.color = 'gold'
    window.add(tail, 370, 280)
    tail = GRect(30,50)
    tail.filled = True
    tail.fill_color = 'gold'
    tail.color = 'gold'
    window.add(tail, 390, 260)
    tail = GRect(100, 50)
    tail.filled = True
    tail.fill_color = 'gold'
    tail.color = 'gold'
    window.add(tail, 390, 230)
    body = GRect(130, 180)
    body.filled = True
    body.fill_color = 'gold'
    window.add(body, 212, 200)
    body2 = GRect(100, 100)
    body2.filled = True
    body2.fill_color = 'gold'
    body2.color = 'gold'
    window.add(body2,220,287)
    body3=GPolygon()
    body3.add_vertex((214,220))
    body3.add_vertex((193,330))
    body3.add_vertex((220,330))
    body3.filled=True
    body3.fill_color='gold'
    body3.color='gold'
    window.add(body3)
    body3 = GPolygon()
    body3.add_vertex((340, 220))
    body3.add_vertex((343, 330))
    body3.add_vertex((358,330))
    body3.filled = True
    body3.fill_color = 'gold'
    body3.color = 'gold'
    window.add(body3)
    l_leg = GOval(100, 90)
    l_leg.filled = True
    l_leg.fill_color = 'gold'
    l_leg.color='gold'
    window.add(l_leg, 190, 300)
    r_leg = GOval(100, 90)
    r_leg.filled = True
    r_leg.fill_color = 'gold'
    r_leg.color = 'gold'
    window.add(r_leg, 260, 300)
    body2 = GRect(100, 100)
    body2.filled = True
    body2.fill_color = 'gold'
    body2.color = 'gold'
    window.add(body2, 220, 287)
    body3 = GPolygon()
    body3.add_vertex((214, 220))
    body3.add_vertex((193, 330))
    body3.add_vertex((220, 330))
    body3.filled = True
    body3.fill_color = 'gold'
    body3.color = 'gold'
    window.add(body3)
    body4 = GPolygon()
    body4.add_vertex((340, 220))
    body4.add_vertex((343, 330))
    body4.add_vertex((358, 330))
    body4.filled = True
    body4.fill_color = 'gold'
    body4.color = 'gold'
    window.add(body4)
    l_leg = GOval(100, 90)
    l_leg.filled = True
    l_leg.fill_color = 'gold'
    l_leg.color = 'gold'
    window.add(l_leg, 190, 300)
    l_hand = GOval(40, 125)
    l_hand.filled = True
    l_hand.fill_color = 'gold'
    window.add(l_hand, 200, 225)
    l_leg2=GOval(20,60)
    l_leg2.filled=True
    l_leg2.fill_color='gold'
    window.add(l_leg2,210,340)
    l_leg3=GLine(217,340,217,360)
    window.add(l_leg3)
    l_leg4=GLine(222,340,222,360)
    window.add(l_leg4)
    r_leg = GOval(100, 90)
    r_leg.filled = True
    r_leg.fill_color = 'gold'
    r_leg.color = 'gold'
    window.add(r_leg, 260, 300)
    r_hand = GOval(40, 125)
    r_hand.filled = True
    r_hand.fill_color = 'gold'
    window.add(r_hand, 310, 225)
    r_leg2 = GOval(20, 60)
    r_leg2.filled = True
    r_leg2.fill_color = 'gold'
    window.add(r_leg2, 320, 340)
    r_leg3=GLine(327,340,327,360)
    window.add(r_leg3)
    r_leg4=GLine(332,340,332,360)
    window.add(r_leg4)
    l_ear = GOval(100, 30)
    l_ear.filled = True
    l_ear.fill_color = 'gold'
    window.add(l_ear, 135, 110)
    l_ear2=GPolygon()
    l_ear2.add_vertex((120,125))
    l_ear2.add_vertex((145,115))
    l_ear2.add_vertex((145,135))
    l_ear2.filled=True
    l_ear2.fill_color='black'
    window.add(l_ear2)
    r_ear=GOval(30,100)
    r_ear.filled=True
    r_ear.fill_color='gold'
    window.add(r_ear,300,25)
    r_ear2=GPolygon()
    r_ear2.add_vertex((315,10))
    r_ear2.add_vertex((305,35))
    r_ear2.add_vertex((325,35))
    r_ear2.filled=True
    r_ear2.fill_color='black'
    window.add(r_ear2)
    face4 = GOval(152, 156)
    face4.filled = True
    face4.fill_color = 'gold'
    window.add(face4, 199, 100)
    face2 = GOval(90, 100)
    face2.filled = True
    face2.fill_color = 'gold'
    window.add(face2, 195, 140)
    face3 = GOval(90, 100)
    face3.filled = True
    face3.fill_color = 'gold'
    window.add(face3, 265, 140)
    face=GOval(150,155)
    face.filled=True
    face.fill_color='gold'
    face.color='gold'
    window.add(face,200,100)
    l_eye=GOval(30,30)
    l_eye.filled=True
    l_eye.fill_color='black'
    window.add(l_eye,225,150)
    l_eye2=GOval(15,15)
    l_eye2.filled=True
    l_eye2.fill_color='white'
    window.add(l_eye2,235,150)
    r_eye = GOval(30, 30)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye, 295, 150)
    r_eye2 = GOval(15, 15)
    r_eye2.filled = True
    r_eye2.fill_color = 'white'
    window.add(r_eye2, 298, 153)
    nose=GOval(5,5)
    nose.filled=True
    nose.fill_color='black'
    window.add(nose,270,190)
    l_face=GOval(33,33)
    l_face.filled=True
    l_face.fill_color='tomato'
    window.add(l_face,200,190)
    l_face = GOval(33, 33)
    l_face.filled = True
    l_face.fill_color = 'tomato'
    window.add(l_face, 320, 190)
    mouth=GPolygon()
    mouth.add_vertex((260,205))
    mouth.add_vertex((285,205))
    mouth.add_vertex((272,240))
    mouth.filled=True
    mouth.fill_color='darkred'
    window.add(mouth)

if __name__ == '__main__':
    main()
