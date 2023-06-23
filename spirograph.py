import turtle
from turtle import *
import random

tim = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


tim.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.pencolor(random_color())
        tim.circle(80)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(3)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
