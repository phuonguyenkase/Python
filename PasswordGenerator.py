letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
#Easy Level:
pw_easy = ''
for char in range(0,nr_letters):
    pw_easy += random.choice(letters)
for char in range(0,nr_numbers):
    pw_easy += random.choice(numbers)
for char in range(0,nr_symbols):
    pw_easy += random.choice(symbols)

print(pw_easy)

#Hard level: từ list mới qua var nhờ for loop
pw_hard = []
for char in range(0,nr_letters):
    pw_hard.append(random.choice(letters))
for char in range(0,nr_symbols):
    pw_hard.append(random.choice(symbols))
for char in range(0,nr_numbers):
    pw_hard.append(random.choice(numbers))

print(pw_hard)
random.shuffle(pw_hard) #random shuffle cho list
password = f"{"".join(pw_hard)}" #Chuyển list thành string và "" là cái nối giữa các var trong list lại
print(f"Your password should be: {password}")
