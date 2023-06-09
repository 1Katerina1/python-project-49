import prompt
from sympy import *
from random import choice
from random import randint
from brain_games.games.general_logic import wrong_answer
from brain_games.games.general_logic import win


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    step = 1
    ans = ''
    cor = ''
    cong = 0

    while step <= 3 and str(ans) == str(cor):
        step += 1
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        y = choice(prime)
        x = randint(1, 150)
        z = choice([x, y])
        print('Question:', z)
        ans = prompt.string('Your answer: ')
        corr = isprime(z)

        if corr == True:
            cor = 'yes'
        else:
            cor = 'no'

        if str(cor) == str(ans):
            cong += 1
            print('Correct!')
        else:
            wrong_answer(cor, ans, name)

        win(name, cong)

