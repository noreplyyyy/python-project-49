from random import randint


DESCRIPTION ='Answer "yes" if number is even otherwise answer "no".'
START_NUM = 1
END_NUM = 101

def get_round():
	random_number = randint(START_NUM, END_NUM)
	if random_number % 2 == 0:
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	question = random_number
	return question, correct_answer
