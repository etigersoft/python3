# Description: 
#   Game: Guess the number
# Author: 
#   Elio Garcia
# Author GitHub profile: 
#   https://github.com/etigersoft/

from random import randint

def run():
    seed_number = randint(1,50)
    guess_number = int(input("Guess the number from 1 to 50 in 5 tries max: "))
    tries = 1

    while seed_number != guess_number and tries < 5:
        if guess_number < seed_number:
            print("Hint: Try a bigger number")
        else:
            print("Hint: Try a smaller number")
        
        if tries == 4: 
            print("(You have one try left)")

        guess_number = int(input("Guess a diferent number: "))
        tries += 1

    if seed_number == guess_number:
        print("Congratulations, you got the number in " + str(tries) + " tries")
    else:
        print("You have reached the max number of tries!")
        print("The right answer is >> " + str(seed_number))

if __name__ == "__main__":
    run()