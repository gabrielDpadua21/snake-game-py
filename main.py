from turtle import Turtle, Screen
from time import sleep
from random import randint


if __name__ == '__main__':
    screen = Screen()
    initial_position = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    GAME_START = True


    for positions in initial_position:
        body = Turtle("square")
        body.penup()
        body.color("white")
        body.goto(positions)
        snake_body.append(body)


    while GAME_START:
        screen.update()
        sleep(0.1)
        for body in range((len(snake_body) -1), 0, -1):
            new_x = snake_body[body - 1].xcor()
            new_y = snake_body[body - 1].ycor()
            snake_body[body].goto(new_x, new_y)
        turn = randint(0, 1)
        if turn == 0:
            snake_body[0].left(90)
        else:
            snake_body[0].forward(20)

    screen.exitonclick()
