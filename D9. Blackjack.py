import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
player_cards = []

def deal_card():
    return random.choice(cards)

def blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if cards == 11 and sum(cards) > 21:
        cards.append(1)
        cards.remove(11)

    return sum(cards)

def rules(c_cards, p_cards):
    player_score = blackjack(p_cards)
    computer_score = blackjack(c_cards)

    if player_score < 21 and len(p_cards) == 5:
        return "You are so lucky. Good job! YOU WIN!"
    elif computer_score == 0:
        return "Computer just has BLACKJACK! YOU LOSE!"
    elif player_score == 0:
        return "You just have BLACK JACK! YOU WIN!"
    elif computer_score == player_score:
        return "It's a draw"
    elif player_score > 21:
        return "Your age is over 21. YOU LOSE!"
    elif player_score > 21:
        return "The computer's age is over 21. YOU WIN!"
    elif computer_score > player_score:
        return "YOU LOSE!"
    else:
        return "YOU WIN!"

def play_game():
    player_cards.clear()
    computer_cards.clear()

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    continue_game = True

    while continue_game:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        while sum(computer_cards) < 16:
            computer_cards.append(deal_card())

        choice = input("Do you want to have another card. Yes or No\n").title()

        if choice == "Yes":
            player_cards.append(random.choice(cards))
            continue
        else:
            continue_game = False
            print(f"Your final hand: {player_cards}, final score: {blackjack(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {blackjack(computer_cards)}")
            print(rules(computer_cards,player_cards))

while input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").title() == "Yes":
    print("\n" * 20)
    play_game()
