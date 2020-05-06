from random import randint


RULES = "Answer 'yes' if number even otherwise answer 'no'."


def is_even(number):
    """this predicate function to check the even number"""
    return number % 2 == 0


def get_game():
    """This function returns a tuple of any number and the string
'yes' if the number is even and 'no' if the number is odd"""
    number = randint(1, 99)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return str(number), answer
