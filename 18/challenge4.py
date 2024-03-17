from turtle import Turtle, Screen
import turtle_functions as t

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.width(10)
tim.speed(10)

while True:
    t.random_walk(tim)

screen.exitonclick()