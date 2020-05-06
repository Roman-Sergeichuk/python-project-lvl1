"""This function creates random math operation of two ranom numbers
and returns tuple of string of this operation and result"""


import random
import operator


RULES = 'What is the result of the expression?'


def get_game():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    OPERATIONS = [
        ('+', operator.add(a, b)),
        ('-', operator.sub(a, b)),
        ('*', operator.mul(a, b))
    ]
    operation = random.choice(OPERATIONS)
    symbol, result = operation
    question = f'{a} {symbol} {b}'
    return question, str(result)
