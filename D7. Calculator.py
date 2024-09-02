import art
print(art.logo)

def add(n1, n2):
    """+"""
    return n1 + n2

def subtract(n1, n2):
    """-"""
    return n1 - n2

def multiple(n1, n2):
    """*"""
    return n1 * n2

def divide(n1, n2):
    """/"""
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

def calculator(): #tạo 1 cái function bự luôn vl
    continue_calculate = True
    num1 = float(input("What's the first number?"))

    while continue_calculate:
        for i in operation:
            print(i)
        operations= input("Pick an operation: ")
        num2 = float(input("What's the next number?"))
        answer = operation[operations](num1,num2) #operation[operations] là để extract cái value trong dictionary
        print(f"{num1} {operations} {num2} = {answer}")

        choice = input(f"Type 'Yes' to continue calculating with {answer}, or type 'New' to start a new calculation. Maybe 'No' to end").lower()
        if choice == "yes":
            num1 = answer
        elif choice == "no":
            continue_calculate = False
            print("Thank you, see you soon")
        else:
            continue_calculate = False
            print("\n" * 20)
            calculator()

calculator()
