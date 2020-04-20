from random import randint, choice


def get_calc():
    val1 = randint(1, 20)
    val2 = randint(1, 20)
    operator_list = (['+', '-', '*'])
    operator = choice(operator_list)
    if operator == '+':
        question = str(val1) + ' ' + operator + ' ' + str(val2)
        return question, val1 + val2
    if operator == '-':
        question = str(val1) + ' ' + operator + ' ' + str(val2)
        return question, val1 - val2
    if operator == '*':
        question = str(val1) + ' ' + operator + ' ' + str(val2)
        return question, val1 * val2
