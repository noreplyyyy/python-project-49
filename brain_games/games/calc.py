from random import randint, choice

DESCRIPTION = ("What is the result of the expression?")
START_NUM = 1
END_NUM = 101


def get_round():
    num1 = randint(START_NUM, END_NUM)
    num2 = randint(START_NUM, END_NUM)
    operation = choice(['*', '+', '-'])
    correct_answer = str(sum_counter(num1, operation, num2))
    question = f"{num1}{operation}{num2}"
    return question, correct_answer


def sum_counter(num1, operation, num2):
    if operation == '*':
        result = num1 * num2
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    return result
