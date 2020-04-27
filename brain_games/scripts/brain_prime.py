#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet, get_rules_prime
from brain_games.cli import welcome_user, request_answer
from brain_games.games.prime import get_prime


def main():
    counter = 0
    greet()
    get_rules_prime()
    name = welcome_user()
    while counter < 3:
        (question, true_answer) = get_prime()
        print(f'Question: {question}')
        user_answer = request_answer()
        if user_answer != true_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{true_answer}'."  # noqa: E501
                f"\nLet's try again, {name}!"
            )
            break
        print('Correct!')
        counter += 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
