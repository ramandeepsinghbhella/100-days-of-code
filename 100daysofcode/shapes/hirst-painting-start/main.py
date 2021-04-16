import turtle

import colorgram
from turtle import Turtle, Screen
import random
timmy = Turtle()
turtle.colormode(255)

screen = Screen()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
timmy.pu()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pd()

for color in colors:
    rgb_colors.append(color.rgb)

for go in range(1, 11):

    for draw in range(1, 11):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.pu()
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()
