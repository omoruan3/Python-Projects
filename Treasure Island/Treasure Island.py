from art import logo, win, lose
from replit import clear

play_again = True
while play_again:
    print(logo)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    stage1 = input('you are at a cross road, which direction are you taking? left or right?\n').lower()
    if stage1 == "left":
        print('What a smart choice, you can proceed!')
        stage2 = input('You have encountered a river, do you swim or you wait? swim or wait?\n').lower()
        if stage2 == "wait":
            print('Lucky you, a boat just arrived. Get in!')
            stage3 = input("You are almost there. Now you encounter 3 colored doors, choose wisely. Red, yellow or blue?\n").lower()
            if stage3 == "red":
                print("Oh no! you got flamed.")
                print(lose)
            elif stage3 == "yellow":
                print("Congratulations! you are victorious!")
                print(win)
            elif stage3 == "blue":
                print("Such bad luck, you got eaten by beasts.")
                print(lose)
            else:
                print('invalid selection')
                print(lose)
        else:
            print('You unlucky bastard, you got attacked by trouts. GAME OVER!')
            print(lose)
    else:
        print('Oh no! you fell into a hole.')
        print(lose)

    should_continue = input("Do you wish to play again? 'yes' or 'no'\n")
    if should_continue == "yes":
        clear()
    else:
        play_again = False