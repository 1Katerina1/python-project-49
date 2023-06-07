#!/usr/bin/env python3
from brain_games.games.general_logic import welcome_user
from brain_games.games.general_logic import welcome
from brain_games.games.calc import calc


def main():
    welcome()
    name = welcome_user()
    calc(name)
