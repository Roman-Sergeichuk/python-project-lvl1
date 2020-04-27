"""This function creates random number and returns
tuple of string of this number and string 'yes' if
number is prime or 'no' if not"""


from random import randint


def is_prime(val):
    if val % 2 == 0:
        return False
    for i in range(3, val, 2):
        if val % i == 0:
            return False
    return True


def get_prime():
    val = randint(2, 100)
    if is_prime(val):
        answer = 'yes'
    else:
        answer = 'no'
    return str(val), answer
