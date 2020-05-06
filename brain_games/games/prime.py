import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_divided_by(val, divider):
    return val % divider


def is_prime(val):
    """this predicate function to check the prime number"""
    if val < 2 or (val > 2 and is_divided_by(val, 2) == 0):
        result = False
    elif val == 2:
        result = True
    for i in range(3, val, 2):
        if is_divided_by(val, 3) == 0:
            result = False
    result = True
    return result


def get_game():
    """This function creates random number and returns
tuple of string of this number and string 'yes' if
number is prime or 'no' if not"""
    val = random.randint(0, 100)
    if is_prime(val):
        answer = 'yes'
    else:
        answer = 'no'
    return str(val), answer
