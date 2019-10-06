
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class GamePersona:
    """
    Base class for all personas (PlayerCharacter, NonPlayerCharacter...) in the game
    """
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class PlayerCharacter(GamePersona):
    """
    Class which creates Player Character
    """
    def __init__(self, name, x, y):
        GamePersona.__init__(self, name, x, y)

    def move(self):
        """
        Defines the movement of the Player Character.
        Gets the event (str) and
        return the desired position (tuple)
        """
        event = input("Use Z, Q, S, or D to move your character")
        if event == "q":
            return (self.x - 1, self.y)
        elif event == "d":
            return (self.x + 1, self.y)
        elif event == "z":
            return (self.x, self.y - 1)
        elif event == "s":
            return (self.x, self.y + 1)


class NonPlayerCharacter(GamePersona):
    """
    Class which creates Non Player Character
    """
    def __init__(self, name, pos_x, pos_y):
        GamePersona.__init__(self, name, pos_x, pos_y)