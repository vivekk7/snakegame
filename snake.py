from turtle import Turtle,Screen
"""Creates snake using turtle class"""
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Creates snake of length 3"""
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)

    def extend(self):
        """Extends the snake each time it feeds."""
        self.add_segment(self.snake[-1].position())

    def move(self):
        """Moves the snake forward."""
        for each in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[each - 1].xcor()
            new_y = self.snake[each - 1].ycor()
            self.snake[each].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Reorients snake to move up."""
        if self.head.heading() != 270 :
            self.head.setheading(90)

    def down(self):
        """Reorients snake to move down."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Reorients snake to move left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Reorients snake to move right."""
        if self.head.heading() != 180:
            self.head.setheading(0)