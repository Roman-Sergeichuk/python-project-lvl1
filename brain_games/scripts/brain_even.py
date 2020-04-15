from brain_games.scripts.brain_games import greet
from random import randint
from brain_games.cli import welcome_user
import prompt


answers = ['yes', 'no']


def is_even(number):
    return number % 2 == 0


def correct_answer(answer):
    for i in answers:
        if i != answer:
            return i
        continue


def main():
    counter = 0
    greet()
    print('Answer "yes" if number even otherwise answer "no".', end = '\n\n')
    name = welcome_user()
    while counter < 3:
        number = randint(1, 99)
        print('Question: ', number)
        answer = prompt.string('Your answer ')
        if is_even(number) and answer == 'yes':
            print('Correct!')
            counter += 1
            answer = ''
        elif not is_even(number) and answer == 'no':
            print('Correct!')
            counter += 1
            answer = ''
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. Let\'s try again, {}!".format(answer, correct_answer(answer), name))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
