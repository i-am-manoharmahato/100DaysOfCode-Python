import turtle
from turtle import *
import random

timmy = Turtle()

timmy.pensize(15)
timmy.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


turtle_headings = [0, 90, 180, 270]


def move_random():
    timmy.fd(30)
    timmy.seth(random.choice(turtle_headings))


for moves in range(200):
    timmy.pencolor(random_color())
    move_random()


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()