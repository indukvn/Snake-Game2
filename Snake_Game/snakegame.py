from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=550)
screen.bgcolor("black")
screen.title("Snake_Game")

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.incre_score()

    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        scoreboard.reset()
        snake.reset()

    for each in snake.lst[1:]:
        if snake.head.distance(each) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
