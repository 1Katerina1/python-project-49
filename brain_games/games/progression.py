import prompt
from random import randint
from brain_games.games.general_logic import wrong_answer
from brain_games.games.general_logic import win


def progression(name):
    print("What number is missing in the progression?")
    step = 1
    ans = ''
    cor = ''
    cong = 0

    while step <= 3 and str(ans) == str(cor):
        step += 1
        start = randint(1, 9)
        stepp = randint(2, 20)
        arr = []
        i = 0

        while i < 10:
            x = start + stepp * i
            arr.append(x)
            i += 1

        y = randint(0,9)
        cor = arr[y]
        arr[y] = '..'
        s = ' '.join(map(str, arr))
        
        print('Question:', s)
        ans = prompt.string('Your answer: ')
        
        if str(cor) == str(ans):
            cong += 1
            print('Correct!')
        else:
            wrong_answer(cor, ans, name)

        win(name, cong)


