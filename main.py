import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

# Colorgram recognize colors
# import colorgram
#
# colors = colorgram.extract("hirst_image.jpg", 15)
#
#
# def get_colors():
#     colors_list_rgb = []
#     for i in colors:
#         rgb = i.rgb
#         red = rgb.r
#         green = rgb.g
#         blue = rgb.b
#         col_list = (red, green, blue)
#         colors_list_rgb.append(col_list)
#     return colors_list_rgb
# print(get_colors())

colors_list_new = [(199, 168, 94), (129, 179, 191), (163, 58, 78), (234, 221, 121), (49, 113, 167), (241, 217, 222),
                   (104, 87, 83), (143, 187, 119), (216, 151, 171), (67, 125, 76), (94, 124, 180), (85, 165, 94)]

# 10 x 10 rows of spots
#  20 dots in size, spaced at 50

tim = Turtle()
tim.shape("turtle")
tim.color("orange")
tim.hideturtle()

tim.setheading(215)
tim.penup()
tim.forward(350)
tim.setheading(0)
tim.speed(0)


def make_row():
    for i in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list_new))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.backward(500)


for j in range(10):
    make_row()


screen = Screen()
screen.exitonclick()
