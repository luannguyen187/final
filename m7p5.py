import turtle
import random
def drawSquaret (t,sz):
    """Get turtle t to draw a square of sz side"""
    for i in range (4):
        t.toward (sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(5)


shapes = [[360,3,20],[360,360,1],[720,5,20]]

for i in range (5):
    drawSquaret (alex,20)
    alex.penup()
    alex.forward(20)
    alex.pendown()

turtle.speed(1)

wn.exotonclick()
