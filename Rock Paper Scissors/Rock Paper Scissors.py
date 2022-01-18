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

print('Welcome to Rock, Paper and Scissors by your guy BIG DICK MANU')

new_list = [rock, paper, scissors]

keep_going = True
while keep_going:
    player_input = input('Please select a pattern, rock, paper or scissors? \n')
    computer_input = random.choice(new_list)
    if computer_input == rock:
        print('com input')
        print(rock)
        if player_input == "rock":
            print('your input')
            print(rock)
            print('you draw')
        elif player_input == "paper":
            print('your input')
            print(paper)
            print('you win')
        elif player_input == "scissors":
            print('your input')
            print(scissors)
            print('you lose')
        else:
            print('Invalid input, you lose.')


    if computer_input == paper:
        print('com input')
        print(paper)
        if player_input == "rock":
            print('your input')
            print(rock)
            print('you lose')
        elif player_input == "paper":
            print('your input')
            print(paper)
            print('you draw')
        elif player_input == "scissors":
            print('your input')
            print(scissors)
            print('you win')
        else:
            print('Invalid input, you lose.')


    if computer_input == scissors:
        print('com input')
        print(scissors)
        if player_input == "rock":
            print('your input')
            print(rock)
            print('you win')
        elif player_input == "paper":
            print('your input')
            print(paper)
            print('you lose')
        elif player_input == "scissors":
            print('your input')
            print(scissors)
            print('you draw')
        else:
            print('Invalid input, you lose.')

    go_again = input('do you wish to go again? Y or N \n').lower()
    if go_again == 'n':
        keep_going = False
    elif go_again == 'y':
        print('smart decision')
        keep_going = True
    else:
        print('invalid input, try again')
