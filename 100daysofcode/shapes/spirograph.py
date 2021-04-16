from turtle import Turtle, Screen
import random
screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
colors = ["cornflower blue", "olive", "red", "light sky blue", "maroon"]
timmy.speed(0)
angle = 1
for key in range(1, 40):

    timmy.color(random.choice(colors))
    timmy.setheading(angle)
    timmy.circle(100)
    angle += 10









screen.exitonclick()