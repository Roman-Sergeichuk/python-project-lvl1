from random import randint


GAME_RULES = "Answer 'yes' if number even otherwise answer 'no'."


"""this predicate function to check the even number"""


def is_even(number):
    return number % 2 == 0


"""This function returns a tuple of any number and the string
'yes' if the number is even and 'no' if the number is odd"""


def get_game():
    number = randint(1, 99)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return str(number), answer
