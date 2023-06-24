import turtle
from turtle import *
import random

# The below module will extract the colours from our image
# And use those colours to dra a diagram.

# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 20)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     current_color = (r, g, b)
#     rgb_colors.append(current_color)
#

color_list = [(253, 251, 247), (253, 249, 252), (232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189),
              (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252),
              (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209),
              (11, 97, 62)]

tim = Turtle()
turtle.colormode(255)
tim.shape("arrow")
tim.speed("fastest")

# x_pos, y_pos = tim.pos()

# Starting from the (0, 0) position
for ypos in range(0, 400, 40):
    for xpos in range(0, 400, 40):
        color = random.choice(color_list)
        tim.setpos(xpos, ypos)
        tim.dot(20, color)
        tim.penup()

tim.hideturtle()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
