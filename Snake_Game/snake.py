from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.lst = []
        self.create_snake()
        self.head = self.lst[0]

    def create_snake(self):
        for each in STARTING_POS:
            self.add_tail(each)

    def add_tail(self, each):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.shapesize(stretch_len=0.95, stretch_wid=0.95)
        snake.goto(each)
        self.lst.append(snake)

    def reset(self):
        for each in self.lst:
            each.goto(1000, 1000)
        self.lst.clear()
        self.create_snake()
        self.head = self.lst[0]

    def extend(self):
        self.add_tail(self.lst[-1].position())

    def move(self):
        for item in range(len(self.lst) - 1, 0, -1):
            x_pos = self.lst[item - 1].xcor()
            y_pos = self.lst[item - 1].ycor()
            self.lst[item].goto(x_pos, y_pos)
        self.head.forward(MOVING_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

