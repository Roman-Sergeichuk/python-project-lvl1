from random import randint, choice


def get_question():
    start = randint(0, 20)
    step = randint(1, 10)
    sequence = []
    question = ''
    for i in range(10):
        sequence.append(start)
        start += step
    val = choice(sequence)
    for i in sequence:
        if i == val:
            question += '..'
        else:
            question += str(i)
        if i != sequence[-1]:
            question += ' '
    return question, val
