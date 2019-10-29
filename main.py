
#! /usr/bin/env python3.7
# coding: utf-8

import argparse

from game_manager import GameManager
from gui import Gui

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action="store_true")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = arg_parse()
    if args.gui:
        gui = Gui()
        gui.launch_game()
    else:
        game = GameManager()
        game.start()







    




