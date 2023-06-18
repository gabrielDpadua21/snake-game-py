from turtle import Screen
from time import sleep
from classes.snake import Snake


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    GAME_START = True
    snake = Snake()


    while GAME_START:
        screen.update()
        sleep(0.1)
        snake.move()

    screen.exitonclick()
