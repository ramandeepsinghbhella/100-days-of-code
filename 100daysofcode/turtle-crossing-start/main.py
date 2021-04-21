import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
car.create_car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.01)
    screen.update()
    car.move_cars()
    for car_dis in car.cars:
        if car_dis.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.goto(0, -280)
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()