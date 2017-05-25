"""
Name: ThankGod Ofurum
Function: Use recursion and turtle to draw shape of a fractal
tree
"""
import turtle
import random
from fractions import Fraction

#Fractal Tree function
def FracTree(branchLen, t):
    if branchLen > 10:
        ran = random.randint(1, 9)
        t.pensize(branchLen * .1) #reduce width of pen per branch
        t.forward(branchLen)
        t.right(45)
        FracTree(branchLen * (float(Fraction(ran, 10))),t) #recursion on branch
        t.left(90)
        FracTree(branchLen * (float(Fraction(ran, 10))),t) #recursion on branch
        t.dot(10, "green")
        t.right(45)
        FracTree(branchLen * (float(Fraction(ran, 10))),t) #recursion on branch
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #Window color
    myWin.bgcolor("cyan")
    myWin.title("Turtle Fractal Tree")
    t.setheading(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("brown")
    t.speed(0)
    t.shape("turtle")
    FracTree(150, t)
    myWin.exitonclick()

main()
