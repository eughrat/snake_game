import time
from turtle import Screen
import datetime

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def write_to_score_sheet(score):
    username = screen.textinput(title="Player Name", prompt="Please enter your name: ")
    with open("score_sheet.txt", "a") as f:
        f.write(f"\nname: {username},date: {datetime.datetime.now()}, score: {score}")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        print("omomomom")

    # DETECT COLLISION WITH BORDER
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        write_to_score_sheet(scoreboard.score)
        scoreboard.reset()

#     DETECT COLLISION WITH SNAKE
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            write_to_score_sheet(scoreboard.score)
            scoreboard.reset()




screen.exitonclick()
