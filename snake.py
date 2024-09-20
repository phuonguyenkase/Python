from turtle import Turtle
from random_color import Random_color
MOVE_DISTANCE = 20
DIRECTION = [0,90,180,270]

class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]

    def create(self):
        for i in range(3):
            self.add_block((-20 * i, 0))

    def add_block(self, position):
        color_generator = Random_color()
        color = color_generator.random_color() #generate random color
        my_turtle = Turtle("square")
        my_turtle.color(color)
        my_turtle.width(15)
        my_turtle.penup()
        my_turtle.goto(position)
        self.snake.append(my_turtle)

    def extend(self):
        last_block = self.snake[-1]
        new_position = (last_block.xcor(), last_block.ycor())
        self.add_block(new_position)

    def move(self): #function
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)  # Move old segments off-screen
        self.snake.clear()  # Clear the snake list
        self.create()  # Recreate the snake
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DIRECTION[3]:
            self.head.setheading(DIRECTION[1])

    def down(self):
        if self.head.heading() != DIRECTION[1]:
            self.head.setheading(DIRECTION[3])

    def left(self):
        if self.head.heading() != DIRECTION[0]:
            self.head.setheading(DIRECTION[2])

    def right(self):
        if self.head.heading() != DIRECTION[2]:
            self.head.setheading(DIRECTION[0])
