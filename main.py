#!/usr/bin/env python

import os

from wecs import boilerplate


def run_game():
    boilerplate.run_game(
        module_name='game',
        console=True,
        # open_console=True,
        keybindings=True,
    )


if __name__ == '__main__':
    run_game()
