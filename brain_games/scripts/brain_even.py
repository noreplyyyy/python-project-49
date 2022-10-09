from random import randint
import prompt

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
def get_round_data():
	random_number = randint(1, 200)
	if random_number % 2 == 0:
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	question = random_number
	return question, correct_answer

def main():
	print("Welcome to the Brain Games!")
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	print(DESCRIPTION)
	index = 0
	score = 3
	while index < score:
		question, correct_answer = get_round_data()
		print(f'Question: {question}')
		answer = prompt.string('Your answer: ')
		if answer == correct_answer:
			print('Correct!')
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
			print(f'Let\'s try again, {name}!')
			return
		index = index + 1
	print(f'Congratulations, {name}!')
def is_even(random_number):
    return random_number % 2 == 0

if __name__ == '__main__':
    brain_even()



