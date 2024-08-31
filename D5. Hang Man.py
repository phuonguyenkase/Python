import random
lives = 6
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
chosen_word = random.choice(word_list) #giống sql còn ko import phía trên luôn
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
display = ""
words_guessed = []

while not game_over:
    print(f"************************** You have {lives}/6 LIVES LEFT ***************************")
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        if guess not in words_guessed:
            lives -= 1
            print(stages[lives])
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            if lives == 0:
                game_over = True
                print(f"***********************YOU LOSE********************** \n The answer is: {chosen_word}")
        else:
            print(f"You have already guest {guess}. Try again")

    words_guessed.append(guess)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
