# import turtle
# kase = turtle.Turtle()

from turtle import Turtle, Screen
#object = class()
kase = Turtle()
print(kase)
kase.shape("turtle") #change shape into turtle
kase.color("DarkRed") #We cannot assign a value to a function (method) like kase.color() = "DarkRed"
kase.width(5)

#object.attribute
my_screen = Screen() #create object
print(my_screen.canvheight)

#function (or object) is sth object can do and attribute is sth object has
for i in range(0,3):
    kase.forward(100)
    kase.left(120) #rùa vẽ hình tam giác

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        kase.color(c)
        kase.forward(steps)
        kase.right(30) #quay phải 1 góc 30 độ

kase.up()
kase.goto(0, -100)
kase.down()
kase.begin_fill()
kase.left(50)
kase.forward(133)
kase.circle(50, 200)
kase.right(140)
kase.circle(50, 200)
kase.forward(133)
kase.end_fill()
# Hide the turtle
kase.hideturtle()


#object.method
my_screen.exitonclick() #hiện màn hình và khi bấm click sẽ tắt

#https://pypi.org/ tìm suộc đã có sẵn
#PrettyTable: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

#install package using settings -> my project -> Python Interpreter
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
