from turtle import Turtle, Screen
import turtle_functions as t

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(10)

for i in range(0, 360, 15):
    tim.color(t.random_color())
    tim.setheading(i)
    tim.circle(100)

screen.exitonclick()