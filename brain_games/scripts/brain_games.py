from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def get_rules_even():
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')


def get_rules_calc():
    print('What is the result of the expression?', end='\n\n')


def main():
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
