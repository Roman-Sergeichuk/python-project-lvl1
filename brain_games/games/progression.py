"""This function creates random arithmetic progression and
returns tuple of string of progression and thought number in it"""


import random


RULES = 'What number is missing in the progression?'


def get_game():
    start = random.randint(0, 20)
    step = random.randint(1, 10)
    hidden_index = random.randint(0, 9)
    sequence = ''
    for i in range(10):
        if hidden_index == i:
            sequence += '.. '
            val = start
        else:
            sequence += f'{start} '
        start += step
    return sequence[:-1], str(val)
