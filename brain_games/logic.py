from prompt import string


index = 0
score = 3


def logic(game):
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    index = 0
    score = 3
    while index < score:
        question, correct_answer = game.get_round()
        print(f'Question: {question}')
        answer = string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        index = index + 1
        print(f'Congratulations, {name}!')