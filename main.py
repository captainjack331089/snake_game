from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SLEEP_TIME_EASY = 0.1
SLEEP_TIME_MID = 0.07
SLEEP_TIME_HIGH = 0.05
SLEEP_TIME_CRAZY = 0.03

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

status = 1
while status:
    screen.update()
    if scoreboard.score <= 8:
        time.sleep(SLEEP_TIME_EASY)
    elif scoreboard.score <= 15:
        time.sleep(SLEEP_TIME_MID)
    elif scoreboard.score <= 22:
        time.sleep(SLEEP_TIME_HIGH)
    else:
        time.sleep(SLEEP_TIME_CRAZY)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 305 or snake.head.ycor() < -305:
        scoreboard.game_over()
        status = 0

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            status = 0

screen.exitonclick()
