import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name), end='\n\n')
    return name


def request_answer():
    answer = prompt.string('Your answer: ')
    return answer
