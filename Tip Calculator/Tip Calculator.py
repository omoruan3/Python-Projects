#This program will help calculate the amount of tip to be paid by individuals based on the % of tip they are willing to offer, number of individuals and the total bill.
from art import logo
from replit import clear

run_again = True
while run_again:
    print(logo)
    print("welcome to the tip calculator")


    #NOTE - all inputs were converted to integers or floats so they can be used for calculations.
    total_bill = float(input("Please input the total bill\n$"))
    no_of_guests = int(input("How many people will the bill be split between?\n"))
    tip = int(input("What percentage of tip are you willing to offer? 5, 10 or 15\n"))

    #here we calculate the amount of tip by dividing the tip by 100 and then multiplying it by the total bill.
    calculated_tip = (total_bill * (tip/100))
    print(f"The total amount of tip is: ${round(calculated_tip, 2)}")

    #here we add the calculated tip to total bill to get the new bill
    new_bill = total_bill + calculated_tip
    print(f"The total bill with the tip is: ${new_bill}")

    #here we divide the new bill by the number of guests to obtain the final bill
    final_bill = (new_bill / no_of_guests)
    rounded_bill = round(final_bill, 2)
    print(f"The amount to be paid by each person is: ${rounded_bill}")

    should_continue = input("Do you wish to run the program again? 'y' or 'n'\n")
    if should_continue == "y":
        clear()
    else:
        print("Have a good day")
        run_again = False

