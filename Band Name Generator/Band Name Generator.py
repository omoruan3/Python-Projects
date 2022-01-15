from replit import clear
from art import logo
#This program will combine both information (city and pet_name)from the user into a band name.

#use a while loop to rerun the program until the user wishes to stop
keep_going = True
while keep_going:
    print(logo)

    print('Hello, welcome to the band name generator')
    city = input("Which city did you grow up in? \n").lower()
    pet_name = input("What is the name of your pet?\n").lower()

    #combine both variables
    band_name = (f"{city} {pet_name}")
    print(band_name)

    generate_again = input("Do you wish to generate another band name? 'yes' or 'no'\n").lower()
    if generate_again == 'yes':
        clear()
        #to be able to use the clear function, you need to have the REPLIT package installed and the clear function imported
    else:
        keep_going = False


