from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_coor = 0
y_coor = 0

for i in range(3):
    new_snake = Turtle()
    new_snake.penup()
    new_snake.color("white")
    new_snake.shape("square")
    new_snake.setposition(x_coor,y_coor)
    x_coor -= 20






screen.exitonclick()