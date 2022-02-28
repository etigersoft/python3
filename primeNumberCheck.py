# Description: 
#   Given an integer n, return the number of prime numbers that are strictly less than n.
#   A prime number is a number which has just two factors: itself and 1. 
#   Or in other words it can be divided evenly only by itself and 1.
# Author: 
#   Elio Garcia
# Author GitHub profile: 
#   https://github.com/etigersoft/


def is_prime(number_to_check):
    # 0 and 1 are not prime numbers by definition >> O(1)
    if number_to_check == 0 or number_to_check == 1:
        return False

    # Get the square root but just the even part
    even_square_root = int(number_to_check**0.5)

    for i in range(2,even_square_root+1):
        if i != number_to_check and (number_to_check%i) == 0:
            return False

    return True


def run():
    while True:
        try:
            number_to_check = int(input('Give me a number (Ctr+c to quit): '))
        except ValueError:
            print('Please enter a valid number')
            continue
        else:
            if number_to_check < 1:
                print('Please enter a number greater than 0 only')
            else:
                if is_prime(number_to_check):
                    print(str(number_to_check) + ' is a prime number!')
                else:
                    print(str(number_to_check) + ' is NOT a prime number')

    

if __name__ == '__main__':
    run()