from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    snake_body = []

    def __init__(self):
        self.set_snake_body()
        self.head = self.snake_body[0]


    def set_snake_body(self) -> None:
        for positions in INITIAL_POSITIONS:
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
        self.snake_body[0].forward(MOVE_DISTANCE)


    def move_up(self) -> None:
        self.head.setheading(UP)


    def move_down(self) -> None:
        self.head.setheading(DOWN)


    def move_left(self) -> None:
        self.head.setheading(LEFT)


    def move_right(self) -> None:
        self.head.setheading(RIGHT)
