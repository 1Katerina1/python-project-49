from brain_games.games.general_logic import welcome_user
from brain_games.games.general_logic import welcome
from brain_games.games.gcd import gcd


def main():
    welcome()
    name = welcome_user()
    gcd(name)