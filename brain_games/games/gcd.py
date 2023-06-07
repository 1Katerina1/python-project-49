import math
import prompt
from random import randint
from brain_games.games.general_logic import wrong_answer
from brain_games.games.general_logic import win


def gcd(name):
    print("Find the greatest common divisor of given numbers.")
    step = 1
    ans = ''
    cor = ''
    cong = 0

    while step <= 3 and str(ans) == str(cor):
        step += 1
        x = randint(1, 100)
        y = randint(1, 100)
        print('Question:', x, y)
        ans = prompt.string('Your answer: ')
        cor = math.gcd(x, y)

        if str(cor) == str(ans):
            cong += 1
            print('Correct!')
        else:
            wrong_answer(cor, ans, name)

        win(name, cong)
        



