import random
import string

password_lenght = int(input("enter lenght of passward: "))

include_letters = input("include letters? (yes/no): ").lower()
include_number = input("include number? (yes/no): ").lower()
include_symbol = input("include symbol? (yes/no): ").lower()

characters = ""

if include_letters == "yes":
    characters += string.ascii_letters

if include_number == "yes":
    characters += string.digits

if include_symbol == "yes":
    characters += string.punctuation

if characters == "":
    print("Please select at least one character type.")
else:
    password = ""

    for _ in range(password_lenght):
        password += random.choice(characters)

    print(f"Generated password: {password}")
