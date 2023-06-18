from turtle import Screen
from time import sleep
from classes.snake import Snake


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    GAME_START = True
    snake = Snake()

    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


    while GAME_START:
        screen.update()
        sleep(0.1)
        snake.move()

    screen.exitonclick()
