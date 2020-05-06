"""This is game engine for Brain Games"""


from brain_games import cli


def run(game, rounds=3):
    cli.greet()
    name = cli.welcome_user(game.RULES)
    counter = 0
    while counter < rounds:
        question, true_answer = game.get_game()
        user_answer = cli.request_answer(question)
        if user_answer != true_answer:
            cli.show_wrong_answer_message(user_answer, true_answer, name)
            break
        cli.show_right_answer_message()
        counter += 1
    else:
        cli.show_win_game_message(name)
