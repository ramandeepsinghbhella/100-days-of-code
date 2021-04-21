from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 270)
        self.hideturtle()
        self.level_no = 1
        self.update_level()

    def update_level(self):
        self.write(f"LEVEL {self.level_no}", move=False, align="left", font=("Arial", 8, "normal"))

    def increase_level(self):
        self.level_no += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
