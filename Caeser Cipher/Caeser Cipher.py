alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!','@','#','$','%','ˆ','&','*','(',')','_','+','-','=']

keep_going = True
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        encoded_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            encoded_text += alphabet[new_position]
        print(encoded_text)

    def decrypt(encryt_text, shift_amount):
        decoded_text = ""
        for letter in encryt_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            decoded_text += alphabet[new_position]
        print(decoded_text)

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input, please input either 'encode' or ' decode'")

    result = input('do you wish to continue? yes or no?\n').lower()
    if result == "yes":
        keep_going = True
    elif result == "no":
        keep_going = False
        print('it was fun while it lasted, Goodbye')


# #alternate solution
# keep_going = True
# while keep_going:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     new_shift = (shift % 26)
#
#     def caeser(input_text, shift_amount):
#         final_text = ""
#         for letter in input_text:
#             position = alphabet.index(letter)
#             if direction == "encode":
#                 new_position = position + shift_amount
#                 final_text += alphabet[new_position]
#             elif direction == "decode":
#                 new_position = position - shift_amount
#                 final_text += alphabet[new_position]
#         print(f'your {direction}d code is {final_text}')
#
#     caeser(text, new_shift)
#
#     result = input('do you wish to continue? yes or no?\n').lower()
#     if result == "yes":
#         keep_going = True
#     elif result == "no":
#         keep_going = False
#         print('it was fun while it lasted, Goodbye')