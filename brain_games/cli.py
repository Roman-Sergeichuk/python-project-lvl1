import prompt


def greet():
    print('Welcome to the Brain Games!')


def show_rules(GAME_RULES):
    print(GAME_RULES, end='\n\n')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name), end='\n\n')
    return name


def request_answer(question):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def show_wrong_answer_message(user_answer, true_answer, name):
    print(
        f"'{user_answer}' is wrong answer ;(. Correct answer was '{true_answer}'."  # noqa: E501
        f"\nLet's try again, {name}!"
    )


def show_right_answer_message():
    print('Correct!')


def show_win_game_message(name):
    print(f'Congratulations, {name}!')
