"""This is game engine for Brain Games"""


from brain_games import cli


def run(game):
    cli.greet()
    cli.show_rules(game.GAME_RULES)
    name = cli.welcome_user()
    counter = 0
    while counter < 3:
        question, true_answer = game.get_game()
        user_answer = cli.request_answer(question)
        if user_answer != true_answer:
            cli.show_wrong_answer_message(user_answer, true_answer, name)
            break
        cli.show_right_answer_message()
        counter += 1
    else:
        cli.show_win_game_message(name)
