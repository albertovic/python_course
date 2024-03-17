import random

angles = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk(turtle):
    turtle.color(random_color())
    turtle.setheading(random.choice(angles))
    turtle.forward(20)
