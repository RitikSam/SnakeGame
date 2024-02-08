from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect  collection with walls
    if snake.head.xcor() > 297 or snake.head.xcor() < -297 or snake.head.ycor() > 297 or snake.head.ycor() < -297:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False

    # Detect the collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
