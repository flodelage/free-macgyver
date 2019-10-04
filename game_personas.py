
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class GamePersona:
    """
    Base class for all personas (PlayerCharacter, NonPlayerCharacter...) in the game
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PlayerCharacter(GamePersona):
    def __init__(self, x, y):
        GamePersona.__init__(self, x, y)

    def move(self):
        event = input("utiliser z q s d pour se déplacer")
        if event == "q":
            return (self.x - 1, self.y)
        elif event == "d":
            return (self.x + 1, self.y)
        elif event == "z":
            return (self.x, self.y - 1)
        elif event == "s":
            return (self.x, self.y + 1)


class NonPlayerCharacter(GamePersona):
    def __init__(self, pos_x, pos_y):
        GamePersona.__init__(self, pos_x, pos_y)