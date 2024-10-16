from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]  #the three initials block the body of the snake
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segments(position)

    def add_segments(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()  # rende invisibile la linea sottile
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position())

    def reset(self):
        for self.segment in self.segments:
            self.segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.head.heading != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.head.heading != RIGHT:
            self.segments[0].setheading(LEFT)



