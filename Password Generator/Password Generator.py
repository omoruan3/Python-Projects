import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


new_letters = random.sample(letters, nr_letters)
new_symbols = random.sample(symbols, nr_symbols)
new_numbers = random.sample(numbers, nr_numbers)

password = []
for l in new_letters:
    password += l

for s in new_symbols:
    password += s

for n in new_numbers:
    password += n
    random.shuffle(password)

new_password = ''
for p in password:
    new_password += p

# alternate conversion from list to string
#new_password = ''.join(random.sample(password, len(password)))

print(f"Your generated password is: {new_password}")
