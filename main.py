from turtle import Screen
from time import sleep
from classes.snake import Snake
from classes.food import Food
from classes.score import Score

GAME_OVER_MESSAGE = "FUCK YOU, LOSER"
ALIGINMENT = "center"
FONT = ("Courier", 32, "normal")


def validate_wall_colision(snake):
    if snake.head.xcor() > 280:
        return True

    if snake.head.xcor() < -280:
        return True

    if snake.head.ycor() > 280:
        return True

    if snake.head.ycor() < -280:
        return True

    return False


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    GAME_START = True
    snake = Snake()
    food = Food()
    score = Score()

    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


    while GAME_START:
        screen.update()
        SPEED = 0.1
        sleep(SPEED)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            SPEED = SPEED + 0.1
            sleep(SPEED)
            score.increment()
        if validate_wall_colision(snake):
            GAME_START = False
            score.game_over()


    screen.exitonclick()
