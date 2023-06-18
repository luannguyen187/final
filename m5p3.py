#Luan Nguyen

#May 11th 2023

#draw and paint square

color = input('Enter the color: ')
length = input('Enter the length: ')

import turtle
Luan = turtle.Turtle()

Luan.pencolor(color)
Luan.pensize(length)

Luan.forward(90)
Luan.right(90)
Luan.forward(90)

turtle.exitonclick()

Luan.fillcolor(color)
Luan.begin_fill()
for num in range(1,4):
    Luan.left(90)
    Luan.forward(90)
    turtle.speed(1)

Luan.end_fill()

