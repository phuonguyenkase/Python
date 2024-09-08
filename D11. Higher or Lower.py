import game_data
import art
import random

continue_game = True
scores = 0
highest_score = 0

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def rules(person_a, person_b, answer):
    global continue_game, scores, highest_score
    print(art.logo)
    if (person_a > person_b and answer == 'A') or (person_b > person_a and answer == 'B'):
        scores += 1
        print(f"You're right! Current score: {scores}")
    else:
        print(f"Sorry that's wrong. Final score: {scores}")
        if scores > highest_score:
            highest_score = scores
        print(f"Your highest score is: {highest_score}")
        continue_game = False

print(art.logo)

while continue_game:
    A = random.choice(game_data.data)
    B = random.choice(game_data.data)
    while A == B:
        B = random.choice(game_data.data)

    print(f"Compare A: {format_data(A)}")
    print(art.vs)
    print(f"Compare B: {format_data(B)}")

    choice = input("Who has more followers? Type 'A' or 'B' ").title()
    rules(A["follower_count"], B["follower_count"], choice)

    if continue_game:
        A = B
    else:
        play_next = input("Do you want to play next? Type 'Yes' or 'No'").title()
        if play_next == "Yes":
            print("\n" * 20)
            print(art.logo)
            continue_game = True
        else:
            print("Thank you for playing!")
