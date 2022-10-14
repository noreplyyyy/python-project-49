from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
END_NUM = 15


def get_round():
    num1 = randint(START_NUM, END_NUM)
    question = num1
    if is_prime(num1):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = num1
    return question, correct_answer

def is_prime(num1):
    for i in range(2, (num1//2)+1):
        if num1 % i == 0:
            return False
    return True
