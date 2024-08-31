#Warm Up:
def calculate_love_score(name1, name2):
    combine_name = name1.lower() + name2.lower()
    true_count = combine_name.count("t") + combine_name.count("r") + combine_name.count("u") + combine_name.count("e")
    love_count = combine_name.count("l") + combine_name.count("o") + combine_name.count("v") + combine_name.count("e")
    print(f"{true_count}{love_count}")

calculate_love_score("Kase", "French")

#Game begins:
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount):
    cipher = ""
    for i in original_text:
        if i in alphabet:
            if direction == "encode":
                position = alphabet.index(i) + shift_amount
            else:
                position = alphabet.index(i) - shift_amount

            position %= len(alphabet)
            cipher += alphabet[position]
        else:
            cipher += i
    print(f"Here is the {direction} result: {cipher}")

continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift)

    play_or_not = input("Do you want to play again?\n").lower()[0]
    if play_or_not == "n":
        continue_game = False
        print("Thank You!")
