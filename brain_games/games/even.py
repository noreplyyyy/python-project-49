from random import randint


DESCRIPTION ='Answer "yes" if number is even otherwise answer "no".'


def get_round():
	random_number = randint(1, 101)
	if random_number % 2 == 0::
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	question = random_number
	return question, correct_answer