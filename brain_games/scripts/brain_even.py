#!/usr/bin/env python3
import prompt
from random import randint

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, { name }!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step = 1
    ans = ''
    cor = ''
    cong = 1

    while step <= 3 and ans == cor: 
        cong += 1
        x = randint(1,100)
        step += 1
        print('Question:', x)
        ans = prompt.string('Your answer: ')
    
        if x % 2 == 0:
            cor = 'yes'
        else:
            cor = 'no'


        if (x % 2 == 0 and ans == 'yes') or (x % 2 != 0 and ans == 'no'):
            print('Correct!')

        else:
            cong = "Let's try again,"
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(cong, name, "!")
            # print(f"Let's try again, {name}!")

        if cong == 4:
            print(f'Congratulations, {name}!')

    




    
    




