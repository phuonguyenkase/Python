import MENU


def total_money():
    print("Please insert coins.")
    try:
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.1
        total += int(input("How many nickles?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
    except ValueError:
        print("Seems like you type invalid things. Try again with numeric number")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.1
        total += int(input("How many nickles?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
    return total

def enough_money(user_choice, user_money):
    if user_choice in MENU.MENU:  # Check if the coffee choice exists in the menu
        coffee_cost = MENU.MENU[coffee_choice]["cost"]

        if user_money >= coffee_cost:
            change = round(user_money - coffee_cost, 2)
            return f"Here is ${change} in change.\nHere is your {user_choice} ☕. Enjoy!"
        else:
            return "Sorry, that's not enough money. Money refunded."

def enough_resources(drink):
    for item in MENU.MENU[drink]["ingredients"]:
        if MENU.MENU[drink]["ingredients"][item] > MENU.resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            MENU.resources[item] -= MENU.MENU[drink]["ingredients"][item]
    return True

coffee = True

while coffee:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "report":
        print("\n".join(f"{key}: {value}" for key, value in MENU.resources.items()))
    elif coffee_choice in MENU.MENU:
        if enough_resources(coffee_choice):
            print(enough_money(coffee_choice,total_money()))
    else:
        print("Invalid choice. Please select from espresso, latte, or cappuccino.")
