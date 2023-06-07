from random import randint
from random import choice
import prompt
from brain_games.games.general_logic import *

def calc(name):
    print('What is the result of the expression?')
    step = 1
    ans = ''
    cor = ''
    cong = 0
    operations = '+-*'

    while step <= 3 and str(ans) == str(cor): 
        step += 1
        x = randint(30, 100)
        y = randint(1, 30)
        oper = choice(operations)
        print('Question:', x, oper, y)
        ans = prompt.string('Your answer: ')
    
        if oper == '+':
            cor = x + y
        if oper == '-':
            cor = x - y
        if oper == '*':
            cor = x * y


        if str(cor) == str(ans):
            cong += 1
            print('Correct!')

        else:
            wrong_answer(cor, ans, name)

        win(name, cong)

