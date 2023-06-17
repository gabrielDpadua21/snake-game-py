from turtle import Turtle, Screen


if __name__ == '__main__':
    screen = Screen()
    initial_position = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    
    for index in range(len(initial_position)):
        snake_body.append(Turtle("square"))
        snake_body[index].color("white")
        snake_body[index].goto(initial_position[index])

    
    screen.exitonclick()