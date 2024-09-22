from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

left_paddle = Paddle((350,0))
right_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(left_paddle.up,"Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    score.update_score()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -320 and ball.distance(right_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position(loser_side = "left")
        score.right_score()
        if score.leftscore == 5:
            score.winner("right")
            game_is_on = False

    if ball.xcor() < -380:
        ball.reset_position(loser_side = "right")
        score.left_score()
        if score.leftscore == 5:
            score.winner("left")
            game_is_on = False

screen.exitonclick()
