from turtle import Turtle, Screen
from random import randint

def random_color(turtle):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.color((r,g,b))

tim = Turtle()
screen = Screen()
screen.colormode(255)

sides = 3
while sides < 20:
    angle = 360 / sides
    random_color(tim)

    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
    
    sides +=1




screen.exitonclick()
