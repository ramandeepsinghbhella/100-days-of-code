from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
car_x_pos = [-280, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 280]
car_y_pos = -250
start = 0
end = 10
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, car_y_pos=car_y_pos, end=end, start=start):
        for car in range(100):
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=.5, stretch_len=1)
            new_car.penup()
            self.cars.append(new_car)

        for arrange in range(10):
            for same_x in range(start, end):
                self.cars[same_x].goto(random.choice(car_x_pos), car_y_pos)
            start += 10
            end += 10
            car_y_pos += 50

    def move_cars(self):
        for move in self.cars:
            move.forward(self.car_speed)
            if move.xcor() > 300:
                move.goto(-300, move.ycor())
                move.forward(self.car_speed)

    def level_up(self, MOVE_INCREMENT = MOVE_INCREMENT):
        self.car_speed += MOVE_INCREMENT
