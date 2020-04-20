"""This function creates random number and returns
tuple of string of this number and string 'yes' if
number is prime or 'no' if not"""


from random import randint


def get_prime():
    val = randint(2, 100)
    if val > 2 and val % 2 == 0:
        return val, 'no'
    for i in range(3, val):
        if val % i == 0:
            return val, 'no'
    return val, 'yes'
