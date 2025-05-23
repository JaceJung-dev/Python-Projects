import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")
BASEDIR = os.path.dirname(__file__)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(f"{BASEDIR}/score_data.txt", mode="r") as score_data:
            self.high_score = int(score_data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{BASEDIR}/score_data.txt", mode="w") as score_data:
                score_data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!\nScore: {self.score}", align=ALIGNMENT, font=FONT)
