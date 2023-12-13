import random

print("This is a password generator")

while True:
    print("Do you want to add symbols? (Like: !@#$%^&*()+_-=)\nYes/no")
    symbols_choice = input("").lower()

    if symbols_choice == "yes":
        symbols = True
    else:
        symbols = False

    print("Do you want to add numbers? (Like: 1234567890)\nYes/no")
    numbers_choice = input("").lower()

    if numbers_choice == "yes":
        numbers = True
    else:
        numbers = False

    print("What will be lentgh of password??")
    length = int(input())

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if symbols:
        characters += '!@#$%^&*()+_-=~`|[]{}/?'
    if numbers:
        characters += '0123456789'

    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated password: {password}")
    print(f"Do you want to generate one more password?Yes/no")
    question = input("").lower()
    
    if question == "yes":
        continue;
    else:
        break
