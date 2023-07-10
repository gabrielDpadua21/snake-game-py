from turtle import Turtle
import os
ALIGINMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER_MESSAGE = "FUCK YOU, LOSER"
FILE_PATH = "./score.txt"

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.get_high_score()
        self.color("white")
        self.print_score()


    def increment(self):
        self.score += 1
        self.print_score()


    def print_score(self):
        self.clear()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} | HIGH SCORE: {self.high_score}", align=ALIGINMENT, font=FONT)
        self.hideturtle()


    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(GAME_OVER_MESSAGE, align=ALIGINMENT, font=FONT)
        self.set_high_score()


    def get_high_score(self):
        try:
            with open(FILE_PATH, mode="r") as file:
                for line in file.readlines():
                    self.high_score = int(line)
        except FileNotFoundError:
            self.high_score = 0


    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as file:
                file.write(f"{self.high_score}")
