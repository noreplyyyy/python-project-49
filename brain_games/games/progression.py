from random import randint


DESCRIPTION = "What number is missing in the progression?"
START_MIN = 1
START_MAX = 101
COUNT_MIN = 5
COUNT_MAX = 10
STEP_MIN = 2
STEP_MAX = 5


def get_round():
    start = randint(START_MIN, START_MAX)
    count = randint(COUNT_MIN, COUNT_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    end_progression = start + step * count
    progression = list(range(start, end_progression, step))
    random_number = randint(0, count - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    question = ""
    for number in progression:
        question = question + str(number) + " "
    question = str(question.strip())
    return question, correct_answer
