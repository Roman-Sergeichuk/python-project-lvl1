import random
from even import is_even


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_divided_by(val, divider):
    return val % divider


def is_prime(val):
    """this predicate function to check the prime number"""
    if val < 2 or (val > 2 and is_even(val)):
        return False
    elif val == 2:
        return True
    for i in range(3, val, 2):
        if is_divided_by(val, i) == 0:
            return False
    return True


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
