import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 0.3,stretch_wid = 0.3)
        self.color("lightblue")
        self.speed(0)
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        self.goto(x, y)
