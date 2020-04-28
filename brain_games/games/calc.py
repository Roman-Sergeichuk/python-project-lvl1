"""This function creates random math operation of two ranom numbers
and returns tuple of string of this operation and result"""


from random import randint, choice
from operator import add, sub, mul


GAME_RULES = 'What is the result of the expression?'


def get_game():
    a = randint(1, 20)
    b = randint(1, 20)
    operation = choice([('+', add(a, b)), ('-', sub(a, b)), ('*', mul(a, b))])
    (operator, result) = operation
    question = f'{a} {operator} {b}'
    return question, str(result)
