from turtle import Turtle
import random
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 1.3, stretch_wid = 1.3)
        self.color("lightpink")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self, loser_side):
        radian_angle = math.radians(random.uniform(30,60))
        self.goto(0,0)
        self.move_speed = 0.1
        if loser_side == "left":
            self.x_move = 10 * math.cos(radian_angle)
            self.y_move = 10 * math.sin(radian_angle)
        else:  # Serve to right side
            self.x_move = -10 * math.cos(radian_angle)
            self.y_move = 10 * math.sin(radian_angle)
