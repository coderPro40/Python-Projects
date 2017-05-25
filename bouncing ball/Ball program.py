"""
Name of Programmer:ThankGod Ofurum
The function of this program is to create a graphical
image of a moving circle. Users click on the GUI to
create the circle which moves automatically
"""

from graphics import *
from time import sleep

"""GUI Properties"""
win = GraphWin("Bouncy Ball")
colorWin = win.setBackground("Cyan")

"""Circle properties"""
dx = 1
dy = 1
Radius = 30
Center = win.getMouse()
circle = Circle(Center, Radius)
circle.setFill("Red")
circle.draw(win)

"""Continueous loop for circle"""
for count in range(2000):
    circle.move(dx, dy)
    Center._move(dx, dy)
    sleep(0.025)
    pointOne = Center.getX()
    pointTwo = Center.getY()
    if pointOne >= 170:
        dx = -1
    elif pointOne <=30:
        dx = 1
    elif pointTwo >= 170:
        dy = -1
    elif pointTwo <= 30:
        dy = 1
    else:
        dx = (dx)
        dy = (dy)
        
"""Command for termonating interface"""
Close = win._onClick(win.close())

    
    







