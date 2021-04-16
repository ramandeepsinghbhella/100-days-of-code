from turtle import Turtle, Screen
import random
screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
colors = ["cornflower blue", "olive", "red", "light sky blue", "maroon"]
direction = [0, 90, 180, 270]
timmy.width(10)
timmy.speed(3)
for key in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))









screen.exitonclick()
