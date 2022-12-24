from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_coor = 0
        y_coor = 0
        for i in range(3):
            new_snake = Turtle()
            new_snake.penup()
            new_snake.color("white")
            new_snake.shape("square")
            new_snake.setposition(x_coor, y_coor)
            x_coor -= 20
            self.segments.append(new_snake)

    def move(self):
        for segm_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segm_num - 1].xcor()
            new_y = self.segments[segm_num - 1].ycor()
            self.segments[segm_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

