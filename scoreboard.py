from turtle import Turtle

FONT = ("Times New Roman", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color("white")
        self.penup()
        self.goto(0,380)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font = FONT)

    def final_score(self):
        self.score += 1
        self.update_score()
        if self.score > self.highest_score:  # Update the highest score
            self.highest_score = self.score

    def reset(self):
        self.clear()
        self.score = 0  # Reset the current score to 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Your highest score is {self.highest_score}. Thank you for playing", align="center", font = FONT)

#cách để hiện highest score bên góc trái
