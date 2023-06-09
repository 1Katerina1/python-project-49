from random import randint
import prompt
from brain_games.games.general_logic import win
from brain_games.games.general_logic import wrong_answer


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step = 1
    ans = ''
    cor = ''
    cong = 0

    while step <= 3 and ans == cor:
        x = randint(1, 100)
        step += 1
        print('Question:', x)
        ans = prompt.string('Your answer: ')

        if x % 2 == 0:
            cor = 'yes'
        else:
            cor = 'no'

        if (x % 2 == 0 and ans == 'yes') or (x % 2 != 0 and ans == 'no'):
            cong += 1
            print('Correct!')

        else:
            wrong_answer(cor, ans, name)

        win(name, cong)
