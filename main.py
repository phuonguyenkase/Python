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

#Cái đống cực hình làm bữa day 15 đã được làm sẵn rồi giờ ghi code ra thôi
