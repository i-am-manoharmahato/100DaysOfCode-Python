from turtle import *
import random

timmy = Turtle()
timmy.shape("arrow")
timmy.shapesize(1, 1, 1)
timmy.color("green")

# print(timmy)
timmy.pensize(1)
timmy.speed(2)

turtle_colors = ['forest green', 'dark goldenrod', 'indian red', 'teal', 'dark salmon']


def draw_shape(number_of_sides):
    angle = int(360 / number_of_sides)
    for _ in range(number_of_sides):
        timmy.fd(100)
        timmy.right(angle)


for sides in range(3, 10):
    timmy.color(random.choice(turtle_colors))
    draw_shape(sides)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()