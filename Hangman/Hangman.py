import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_bank = ["davido", "wizkid", "burna", "luckysings", "tems", "buju"]

ran_word = random.choice(word_bank)
len_ran_word = len(ran_word)

lives = 6

blanks = []
for _ in ran_word:
    blanks += "_"
print(blanks)


end_of_game = True
while end_of_game:
    user_guess = input("guess a letter: \n")
# replace the correct guesses in the blank variable
    for index_position in range(len_ran_word):
        letter = ran_word[index_position]
        if letter == user_guess:
            blanks[index_position] = user_guess
    print(stages[lives])
    print(blanks)

    if user_guess not in ran_word:
        lives -= 1
        print(stages[lives])
        print('wrong letter')
        if lives == 0:
            end_of_game = False
            print(stages[lives])
            print('you lose')
    # elif user_guess in blanks:
    #     print(stages[lives])
    #     print('you already guessed that letter')
    if "_" not in blanks:
        end_of_game = False
        print(stages[lives])
        print('you win, congratulations!')

