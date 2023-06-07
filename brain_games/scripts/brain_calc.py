#!/usr/bin/env python3
from brain_games.games.game import *
from brain_games.games.calc import calc


def main():
    welcome()
    name = welcome_user()
    calc(name)
