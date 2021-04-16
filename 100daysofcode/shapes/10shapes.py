from turtle import Turtle, Screen
import random
screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
timmy.right(90)
timmy.pu()
timmy.forward(250)
timmy.left(90)
timmy.pd()
colors = ["cornflower blue", "olive", "red", "light sky blue", "maroon"]
for key in range(3, 11):
    for run in range(0, key):
        timmy.color(random.choice(colors))
        angle = 360/key
        timmy.forward(100)
        timmy.left(angle)
        timmy.forward(100)







screen.exitonclick()