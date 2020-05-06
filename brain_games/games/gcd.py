"""This function creates two random numbers and returns
tuple of string of these numbers and their great common divisor"""


from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while max(num1, num2) % min(num1, num2) != 0:
        result = max(num1, num2) % min(num1, num2)
        if num1 > num2:
            num1 = result
        else:
            num2 = result
    return min(num1, num2)


def get_game():
    a = randint(1, 99)
    b = randint(1, 99)
    question = f'{a} {b}'
    answer = gcd(a, b)
    return question, str(answer)
