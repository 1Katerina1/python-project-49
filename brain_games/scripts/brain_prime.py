#!/usr/bin/env python3
from brain_games.games.general_logic import welcome_user
from brain_games.games.general_logic import welcome
from brain_games.games.prime import prime


def main():
    welcome()
    name = welcome_user()
    prime(name)
