#!/usr/bin/env python3
from brain_games.games.general_logic import welcome_user
from brain_games.games.general_logic import welcome
from brain_games.games.progression import progression


def main():
    welcome()
    name = welcome_user()
    progression(name)