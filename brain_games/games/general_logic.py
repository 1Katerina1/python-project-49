import prompt


def welcome():
    print('Welcome to the Brain Games!')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, { name }!')
    return name

def wrong_answer(cor, ans, name):
    cong = "Let's try again,"
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
    print(f'{cong} {name}!')

def win(name, cong):
    if cong == 3:
        print(f'Congratulations, {name}!')
