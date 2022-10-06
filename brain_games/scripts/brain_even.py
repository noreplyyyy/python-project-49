from brain_games.cli import welcome_user
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    nice()
    return name

def Question():
	random_number = randint(1, 100)
	print("Question:"+ str(random_number))
	answer1=input('Your answer: ')
	if answer1 == "yes" and random_number % 2 == 0 or answer1 == 'no' and random_number % 2 != 0:
		print('Correct!')
		return True
	else:
		if random_number % 2 != 0:
			correct = "no"
		else:
			correct = "yes"
		print (f"'{answer1}' is wrong answer ;(. Correct answer was '{correct}'.")
		print(f"Let's try again, {name}!")
def nice():
	if Question() == True:
		Question()
	if Question() == True:
		print(f'Congratulations, {name}!')

if __name__ == '__main__':
    brain_even()


