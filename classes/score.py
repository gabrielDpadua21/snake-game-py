from turtle import Turtle
ALIGINMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.print_score()


    def increment(self):
        self.score += 1
        self.print_score()


    def print_score(self):
        self.clear()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGINMENT, font=FONT)
        self.hideturtle()
