from art import guess_game
import random

print(guess_game)
print("Welcome to Emmanuel's guessing game")
print("Instruction: Pick a number between 1 and 100")

numbers = []

for no in range(1, 101):
    numbers.append(no)

random_no = random.choice(numbers)

print(f"The random number selected is {random_no}")

keep_going = True
difficulty = input('Choose a difficulty: easy or hard\n').lower()
lives = 0
if difficulty == "easy":
    lives += 10
elif difficulty == "hard":
    lives += 5
else:
    print("Invalid input")
    keep_going = False

while keep_going:
    print(f'you have {lives} attempts remaining to guess the number')
    guessed_number = int(input("Make a guess: "))
    if guessed_number > random_no:
        lives -= 1
        print("too high")
    elif guessed_number < random_no:
        lives -= 1
        print("too low")
    elif guessed_number == random_no:
        print(f"you got it! The answer was {random_no}")
        keep_going = False
    if lives == 0:
        keep_going = False
        print('Game over, you ran out of attempts')