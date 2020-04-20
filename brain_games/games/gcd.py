from random import randint
from math import gcd


def get_gcd():
    a = randint(1, 99)
    b = randint(1, 99)
    question = str(a) + ' ' + str(b)
    return question, gcd(a, b)
