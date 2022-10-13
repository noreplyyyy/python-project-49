from random import randint


DESCRIPTION = "What number is missing in the progression?"
START_LOW = 1
START_LIMIT = 101
COUNT_LOW = 5
COUNT_LIMIT = 10
STEP_LOW = 2
STEP_LIMIT = 5
START_RANDOM = 0


def get_round():
    start = randint(START_LOW, START_LIMIT)
    count = randint(COUNT_LOW, COUNT_LIMIT)
    step = randint(STEP_LOW, STEP_LIMIT)
    end_progression = start + step * count
    progression = list(range(start, end_progression, step))
    random_number = randint(START_RANDOM, count - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    question = ""
    for number in progression:
        question = question + str(number) + " "
    question = str(question.strip())
    return question, correct_answer
