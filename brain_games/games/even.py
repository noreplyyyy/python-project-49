from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUM = 1
END_NUM = 101


def get_round():
    number = randint(START_NUM, END_NUM)
    question = f'{number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

def is_even(random_number):
    return random_number % 2 == 0