import art
import random
print(art.logo)

print("Welcome to the Number Guessing Name!")

def comparing(heart, ran_num):
    while heart > 0:
        number = int(input('Make a guess: '))
        if number < ran_num:
            print("Too low. \nGuess again")
            heart -= 1
            print(f"You have {heart} attempts remaining to guess the number")
        elif number > ran_num:
            print("Too high. \nGuess again")
            heart -= 1
            print(f"You have {heart} attempts remaining to guess the number")
        else:
            print(f"You got it! The answer was {ran_num}")
            return

        if heart == 0:
            print(f"Game over! The correct number was {ran_num}.")

continue_game = True

while continue_game:
    print("I'm thinking of number between 1 and 100")
    random_number = random.randint(1, 100)
    difficult_level = input("Choose a difficulty. Type 'easy' or 'hard': ").title()

    if difficult_level == "Easy":
        print("You have 10 attempts remaining to guess the number")
        lives = 10
        comparing(lives, random_number)
    else:
        print("You have 5 attempts remaining to guess the number")
        lives = 5
        comparing(lives, random_number)

    choice = input("Do you want to play again. Yes or No ").title()
    if choice == "Yes":
        continue
    else:
        print("See you soon. Hope you enjoy the game")
        continue_game = False
