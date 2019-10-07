
#! /usr/bin/env python3.7
# coding: utf-8

import random

from labyrinth import Labyrinth
from game_personas import PlayerCharacter, NonPlayerCharacter
from item import Item


class GameManager:
    """
    Class which manages the functioning of the game
    """
    def __init__(self):
        self.labyrinth = Labyrinth("labyrinth_sketch.txt")
        """
        Creates Map instance
        """
        position = self.labyrinth.find_letter("m")
        """
        Finds macgyver, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple)
        """
        self.macgyver = PlayerCharacter("MacGyver", position[0], position[1])
        """
        Creates PlayerCharacter instance and assigns its coordinates x, y (int) from var position
        """
        position = self.labyrinth.find_letter("g")
        self.guardian = NonPlayerCharacter("Guardian", position[0], position[1])

    def start(self):
        """
        Runs the game 
        """
      
        while True:
        
            self.labyrinth.display()
            """
            Displays map to user
            """
            position_before_movement = (self.macgyver.y, self.macgyver.x)
            requested_position = self.macgyver.move()
            """
            The user tries to move the Player Character
            Returns the requested coordinates (int, int)
            """
            requested_map_letter = self.labyrinth.retrieve_letter(requested_position[0], requested_position[1])
            if requested_map_letter == " ":
                self.labyrinth.replace_letter(requested_position[0], requested_position[1], "m")
                self.labyrinth.replace_letter(position_before_movement[0], position_before_movement[1], " ")
                self.macgyver.set_position(requested_position[0], requested_position[1])
            else:
                pass

        