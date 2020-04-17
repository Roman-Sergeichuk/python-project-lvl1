from random import randint


def get_question():
    question = randint(1, 99)
    if question % 2 == 0:
        return question, 'yes'
    return question, 'no'
