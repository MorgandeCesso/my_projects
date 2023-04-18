import random

def _numRand():
    number = random.randint(0, 10)
    return number

def _try_to_guess():
    while (True):
        number = _numRand()
        a = input()
        if a == '.':
            break
        if a != str(number):
            print(f'Wrong, AI guessed: {number}\n')
        else:
            print('Amazing! Try again!\n')
    print("See ya!\n")

print("To exit this app press '.' + Enter\n")
_try_to_guess()