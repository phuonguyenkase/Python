from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftscore = 0
        self.rightscore = 0

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.leftscore, align = "center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightscore, align="center", font=("Courier", 80, "normal"))

    def right_score(self):
        self.rightscore += 1
        self.update_score()

    def left_score(self):
        self.leftscore += 1
        self.update_score()

    def winner(self, winner):
        self.clear()
        self.goto(0, 0)
        if winner == "left":
            self.write("The left side wins!", align="center", font=("Courier", 40, "normal"))
        else:
            self.write("The right side wins!", align="center", font=("Courier", 40, "normal"))
