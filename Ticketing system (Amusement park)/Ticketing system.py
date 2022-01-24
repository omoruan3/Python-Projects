print("Welcome to Emmanuel's fun ride park")

height = int(input('How tall are you? (cm) \n'))
bill = 0
if height >= 120:
    print('You are eligible for a ride')
    age = int(input('How old are you? \n'))
    if age <= 12:
        bill = 5
        print('Kiddie price $5.')
    elif age <= 18:
        bill = 7
        print('Teen price $7.')
    else:
        bill = 12
        print('Adult price $12.')

    ride_with_pics = input('Do you want a photo with your ride? y or n \n')
    if ride_with_pics == "y":
        bill += 3

    print(f'Your final bill is ${bill}')
else:
    print('You are not eligible for a ride')