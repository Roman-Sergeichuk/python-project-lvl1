#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet, get_rules_even
from brain_games.games.even import get_even
from brain_games.cli import welcome_user, request_answer


def main():
    counter = 0
    greet()
    get_rules_even()
    name = welcome_user()
    while counter < 3:
        task = get_even()
        question = task[0]
        true_answer = str(task[1])
        print(f'Question: {question}')
        user_answer = request_answer()
        if user_answer == true_answer:
            print('Correct!')
            counter += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{true_answer}'."  # noqa: E501
                f"\nLet's try again, {name}!"
            )
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
