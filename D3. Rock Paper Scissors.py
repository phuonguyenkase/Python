import random
rock = '''
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
'''
paper = '''
   _______
---'   ____)____
         ______)
         _______)
        _______)
---.__________)
'''
scissors = '''
   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)
'''
game_image = [rock, paper, scissors] #Tạo 1 list từ variable sẵn có


player = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors\n"))
if player == 0:
   print(game_image[player])
elif player == 1:
   print(game_image[player])
else:
   print(game_image[player])


print("Computer choose: ")
random_number = random.randint(0,2)
if random_number == 0:
   print(game_image[player])
elif random_number == 1:
   print(game_image[player])
else:
   print(game_image[player])


if player >= 3 or int(player) < 0:
   print("Invalid. You need to type an invalid number")
elif player == random_number:
   print("It's a draw")
elif (player == 0 and random_number == 2) or \
       (player == 1 and random_number == 0) or \
       (player == 2 and random_number == 1):
   print("You win!")
else:
   print("You lose!")
