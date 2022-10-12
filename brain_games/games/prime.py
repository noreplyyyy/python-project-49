from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
END_NUM = 15


def get_round():
    num1 = randint(START_NUM, END_NUM)
    question = num1
    if num1 < 2:
        correct_answer = "no"
        return question,correct_answer
    for i in range(2, int(num1 ** 0.5 + 1)):
        if num1 % i == 0:
            correct_answer = "no"
            return question,correct_answer
    else:
        correct_answer = "yes"
        return question,correct_answer

#def is_prime(a):
    #if a < 2:
        #return False
    #for i in range(2, int(a ** 0.5 + 1)):
        #if a % i == 0:
            #return False
    #else:
        #return True



    #for i in range(2, (num1//2)+1):
        #if num1 % i == 0:
            #correct_answer = "no"
        #else:
            #correct_answer = "yes"
    #question = num1