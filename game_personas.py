
#! /usr/bin/env python3.7
# coding: utf-8

class GamePersona:
    """
    Base class for all personas (PlayerCharacter, NonPlayerCharacter...) in the game
    """
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x


class PlayerCharacter(GamePersona):
    """
    Class which creates Player Character
    """
    def __init__(self, name, y, x):
        GamePersona.__init__(self, name, y, x)

    def move(self):
        """
        Defines the movement of the Player Character.
        Gets the event (str) and
        returns the requested coordinates (int, int)
        """
        event = input("Use Z, Q, S, or D to move your character: ")
        if event == "q":
            return (self.y, self.x -1)
        elif event == "d":
            return (self.y, self.x + 1)
        elif event == "z":
            return (self.y - 1, self.x)
        elif event == "s":
            return (self.y + 1, self.x)

    def set_position(self, y, x):
        self.x = x
        self.y = y


class NonPlayerCharacter(GamePersona):
    """
    Class which creates Non Player Character
    """
    def __init__(self, name, y, x):
        GamePersona.__init__(self, name, y, x)