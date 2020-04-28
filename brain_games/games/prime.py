from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


"""this predicate function to check the prime number"""


def is_prime(val):
    if val % 2 == 0:
        return False
    for i in range(3, val, 2):
        return val % i != 0


"""This function creates random number and returns
tuple of string of this number and string 'yes' if
number is prime or 'no' if not"""


def get_game():
    val = randint(2, 100)
    if is_prime(val):
        answer = 'yes'
    else:
        answer = 'no'
    return str(val), answer
