from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("lightpink")
my_turtle.width(5) #or pensize(15)
my_turtle.speed(0) #or "fastest"

#No1:
for i in range(100):
    for color in ["darkslateblue", "lightpink", "Lightseagreen"]:
        my_turtle.color(color)
        my_turtle.forward(i)
        my_turtle.left(30)

#No2:
my_turtle.up()
my_turtle.goto(-250,250)
for i in range(20):
    my_turtle.forward(10)
    if i % 2 == 0:
        my_turtle.pendown()
    else:
        my_turtle.penup()

#No3:
def draw_shape(num_sides):
  angle = 360 / num_sides
  for i in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
    
my_turtle.penup()
my_turtle.goto(-50,150)
my_turtle.pendown()

color = ["darkslateblue", "lightpink", "Lightseagreen", "MediumPurple3", "cornflowerblue"]

for shape_sides in range(3,11):
    my_turtle.color(random.choice(color))
    draw_shape(shape_sides)

#No4:
directions = [0,90,180,270]
for i in range(100):
    my_turtle.color(random.choice(color))
    my_turtle.forward(25)
    my_turtle.setheading(random.choice(directions)) #for north south east west

screen = Screen()
screen.exitonclick()

#import turtle as t (alias like in sql)
