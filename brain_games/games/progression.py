"""This function creates random arithmetic progression and
returns tuple of string of progression and thought number in it"""


from random import randint


GAME_RULES = 'What number is missing in the progression?'


def get_game():
    start = randint(0, 20)
    step = randint(1, 10)
    hidden_index = randint(0, 9)
    sequence = ''
    for i in range(10):
        if hidden_index == i:
            sequence += '..'
            val = start
        else:
            sequence += str(start)
        start += step
        if i < 9:
            sequence += ' '
    return sequence, str(val)
