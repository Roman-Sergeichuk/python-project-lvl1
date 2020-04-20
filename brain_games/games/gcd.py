"""This function creates two random numbers and returns
tuple of string of these numbers and their great common divisor"""


from random import randint
from math import gcd


def get_gcd():
    a = randint(1, 99)
    b = randint(1, 99)
    question = str(a) + ' ' + str(b)
    return question, gcd(a, b)
