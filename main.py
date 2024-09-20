from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800,800)
screen.bgcolor("black")
screen.title("My Snake Game Time!!!")
screen.tracer(0) #này như froze màn hình until we update

snake = Snake()
food = Food()
score = Scoreboard()

def setup_controls(): #to manage the loop again when you want to play again
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def continue_or_not():
    play_next = screen.textinput("YOU LOSEEE!!!", "Do you want to play next? Yes or No ").title()
    if play_next == "Yes":
        score.reset()
        snake.reset()
        setup_controls()
        return True
    else:
        score.game_over()
        return False

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)  # ngủ trong 0.3s
    snake.move()
    setup_controls()
    if snake.head.distance(food) < 20:
        food.refresh()
        score.final_score()
        snake.extend()
    if (snake.head.xcor() > 380 or snake.head.xcor() < -380) or (snake.head.ycor() > 380 or snake.head.ycor() < -380):
        game_is_on = continue_or_not()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 17:
            game_is_on = continue_or_not()
            break

screen.exitonclick()
