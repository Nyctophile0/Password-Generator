import random
import string
from sys import exit, platform
from time import sleep
import os
from termcolor import cprint
import pyperclip

# Logo


def logo():
    sleep(0.5)

    # Checking for system
    if platform == 'win32':
        os.system('cls')
    elif platform == 'linux':
        os.system('clear')
    cprint('\t\t\tCONSOLE PASSWORD GENERATOR', 'cyan', attrs=['bold'])


# Progress Bar


def progress():
    r = 80
    items = list(range(0, r))
    l = len(items)
    for i, item in enumerate(items):
        sleep(0.02)
        filled = int(r * (i + 1) // l)
        bar = '█' * filled + ' ' * (r - filled)
        print(f'\r{bar}', end='\r')


# Generate random password


def rand(length):
    password = ''
    while len(password) < length:
        password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

    return password


# Ensuring that the password must contain all required variables
# i.e, uppercase, lowercase letters
# digits and special symbols


def password_validator(password):
    upper = 0
    lower = 0
    digits = 0
    special = 0

    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isnumeric():
            digits += 1
        else:
            special += 1

    if (upper > 0 and lower > 0 and digits > 0 and special > 0):
        return True
    return False


def main():

    # Prompt for length of password
    # must be more than or equal to 4
    while True:
        try:
            length = int(input('+ Enter desired length of the password: '))

        except ValueError:
            continue

        if length >= 4:
            break

    password = rand(length)

    while not password_validator(password):
        password = rand(length)

    print(f"Strong Password generated: '{password}'")

    # Copying password to clipboard
    pyperclip.copy(password)

    print("Your password has been copied to clipboard!")


if __name__ == "__main__":

    # CUI
    logo()
    progress()
    cprint('\n\n\t\t\t\tWelcome!', 'blue', attrs=['bold'])
    cprint('\n\t*The Password will contain atleast one uppercase letter,', 'green')
    cprint('\t   lowercase letter, numeric digit and special characters.', 'green')
    cprint('\n\t*Minimum length of the password should be 4 to ensure', 'green')
    cprint('\t\t        strength of the password.\n', 'green')
    #####

    main()

