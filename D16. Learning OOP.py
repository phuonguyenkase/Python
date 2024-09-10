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

#From here I had redone the D12 project using OOP:
from coffe_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

my_coffee_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

machine_is_ready = True

while machine_is_ready:
    guess_choice = input(f"What would you like? {menu.get_items()}: ")
    if guess_choice == "report":
        coffe_maker.report()
        my_coffee_machine.report()
    elif guess_choice == "off":
        machine_is_ready = False
        print("It's such a productive day! See you soon!")
    else:
        drink = menu.find_drink(guess_choice)
        if coffe_maker.is_resource_sufficient(drink):
            if my_coffee_machine.make_payment(drink.cost): #này tự tính tiền cho mình luôn
                coffe_maker.make_coffee(drink)
                my_coffee_machine.amount_of_tip()

#Cái đống cực hình làm bữa day 12 đã được làm sẵn rồi giờ ghi code ra thôi
