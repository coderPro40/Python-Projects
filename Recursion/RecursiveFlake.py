"""
Name: ThankGod Ofurum
Function: Use recursion and turtle to draw shape of a snow
flake
"""
import turtle

def SnowFl(t, order, size):
    #Base case
    if order == 0:      
        t.forward(size)

    #Recursive case    
    else:
        SnowFl(t, order-1, size/3)
        t.left(60)
        SnowFl(t, order-1, size/3)
        t.right(120)
        SnowFl(t, order-1, size/3)
        t.left(60)
        SnowFl(t, order-1, size/3)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #Screen color & title
    myWin.bgcolor("orange")
    myWin.title("Turtle SnowFlake")
    t.speed(0)
    t.color("white")
    #Hexagon
    for i in range(3):
        SnowFl(t, 3, 200)
        t.right(120)
    myWin.exitonclick()

main()
