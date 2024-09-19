from turtle import Turtle, Screen
screen = Screen()
import random

screen.setup(800,700)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue","violet","purple"]
y_positions = [-330,-220,-110,0,110,220,330]
our_racers = []

is_race_on = False
if user_bet in colors:
    is_race_on = True
else:
    print("Your guest is inapproriate. Try again")

for i in range(7):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(-370, y_positions[i])
    our_racers.append(my_turtle)

while is_race_on:
    for i in our_racers:
        if i.xcor() > 370:
            is_race_on = False
            winner = i.pencolor()
            if user_bet == winner:
                print(f"Félicitations. You just win the race with {winner} turtle")
            else:
                print(f"Ouch! You just lose the race. The winner is {winner} turtle")
                
        rand_distance = random.randint(0,15)
        i.forward(rand_distance)

screen.exitonclick()
