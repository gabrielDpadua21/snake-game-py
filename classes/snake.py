from turtle import Turtle
from random import randint

class Snake:

    snake_body = []
    initial_position = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.set_snake_body()


    def set_snake_body(self) -> None:
        for positions in self.initial_position:
            body = Turtle("square")
            body.penup()
            body.color("white")
            body.goto(positions)
            self.snake_body.append(body)


    def move(self) -> None:
        for body in range((len(self.snake_body) -1), 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        turn = randint(0, 1)
        if turn == 0:
            self.snake_body[0].left(90)
        else:
            self.snake_body[0].forward(20)
