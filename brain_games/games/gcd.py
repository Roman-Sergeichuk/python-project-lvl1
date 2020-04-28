"""This function creates two random numbers and returns
tuple of string of these numbers and their great common divisor"""


from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_game():
    a = randint(1, 99)
    b = randint(1, 99)
    question = f'{a} {b}'
    while max(a, b) % min(a, b) != 0:
        result = max(a, b) % min(a, b)
        if a > b:
            a = result
        else:
            b = result
    else:
        return question, str(min(a, b))
