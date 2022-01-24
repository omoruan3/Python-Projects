print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
    else:
        price += 0
    print(f'Your final bill is: ${price}.')
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
    else:
        price += 0
    print(f'Your final bill is: ${price}.')
elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
    else:
        price += 0
    print(f'Your final bill is: ${price}.')



# alternate solution
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
#
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f'Your total bill is ${bill}.')


