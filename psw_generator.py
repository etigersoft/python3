# Description: 
#   Game: Simple Password Generator
# Author: 
#   Elio Garcia
# Author GitHub profile: 
#   https://github.com/etigersoft/


import random
import string


def psw_generator(size):
    seed = string.punctuation + string.hexdigits
    password = ""
    
    while len(password) < size:
        password += random.choice(seed)
    
    return password


def run():
    while True:
        try:
            size = int(input("How many characters for your password: "))
        except ValueError:
            print('Please enter a valid number')
            continue
        break

    print("Your new password is: " + psw_generator(size))


if __name__ == "__main__":
    run()