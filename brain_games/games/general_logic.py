def wrong_answer(cor, ans, name):
    cong = "Let's try again,"
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
    print(cong, name, "!")

def win(name, cong):
    if cong == 3:
        print(f'Congratulations, {name}!')
