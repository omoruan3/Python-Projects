import random
from replit import clear
from art import blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """This returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(com_score, user_score):
    """This compares the scores to determine teh winner of the game"""
    if user_score > 21 and com_score > 21:
        return "you went over, you lose"


    if user_score == com_score:
        return "draw"
    elif user_score == 0:
        return "BlackJack, you win"
    elif com_score == 0:
        return "BlackJack, computer wins! you lose"
    elif user_score > 21:
        return "you lose"
    elif com_score > 21:
        return "computer loses, you win"
    elif user_score > com_score:
        return "you win"
    else:
        return "you lose"

def calculate_score(cards):
    """This function takes a list of cards and return teh score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():

    print(blackjack)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for item in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards)
    print(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'your hand: {user_cards}, current score: {user_score}')
        print(f'computers hand: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_new_card = input("Do you want to draw another card? 'yes' or 'no'?\n")
            if draw_new_card == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'your final hand {user_cards}, final score: {user_score}')
    print(f'computers final hand {computer_cards}, final score: {computer_score}')
    print(compare(computer_score, user_score))

    while input("do you wish to keep on playing? yes or no?\n") == "yes":
        clear()
        play_game()

play_game()