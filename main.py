
# ! /usr/bin/env python3.7
# coding: utf-8

import argparse

from game_terminal_manager import TerminalGameManager
from game_gui_manager import GuiGameManager


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action="store_true")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parse()
    if args.gui:
        gui = GuiGameManager()
        gui.launch_game()
    else:
        terminal = TerminalGameManager()
        terminal.launch_game()
