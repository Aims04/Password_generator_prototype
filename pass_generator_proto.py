import random
import string

def generate_pwd(size, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(size))
    return password

def get_bool_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

length = int(input("Enter length of key required:"))
uppercase = get_bool_input("Include uppercase letters? (yes/no): ")
lowercase = get_bool_input("Include lowercase letters? (yes/no): ")
digits = get_bool_input("Include digits? (yes/no): ")
special_chars = get_bool_input("Include special characters? (yes/no): ")

pwd = generate_pwd(length, uppercase, lowercase, digits, special_chars)
print(pwd)
