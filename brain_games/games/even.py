"""this function returns a tuple of any number and the string
'yes' if the number is even and 'no' if the number is odd"""


from random import randint


def get_even():
    number = randint(1, 99)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
