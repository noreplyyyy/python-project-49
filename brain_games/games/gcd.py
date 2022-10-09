import math
from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."
START_NUM = 1
END_NUM = 101


def get_round():
    num1 = randint(START_NUM, END_NUM)
    num2 = randint(START_NUM, END_NUM)
    correct_answer = str(math.gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer