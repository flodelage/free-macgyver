
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
        self.macgyver = PlayerCharacter("MacGyver", position[0], position[1], [])
        """
        Creates PlayerCharacter instance and assigns its coordinates x, y (int) from var position
        """
        position = self.labyrinth.find_letter("g")
        """
        Finds the Guardian, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple)
        """
        self.guardian = NonPlayerCharacter("Guardian", position[0], position[1])
        """
        Creates NonPlayerCharacter instance and assigns its coordinates x, y (int) from var position
        """
        empty_squares = self.labyrinth.list_letter(" ")
        """
        Defines labyrinth empty squares
        """
        items = [Item("needle", "n", 0, 0), Item("ether", "e", 0, 0), Item("tube", "t", 0, 0)]
        """
        Creates the 3 items instances
        """
        for item in items:
            new_position = random.choice(empty_squares)
            item.set_position(new_position[0], new_position[1])
            self.labyrinth.replace_letter(item.y, item.x, item.letter)
        """
        Defines items random positions at the launch of the game
        """

    def start(self):
        """
        Runs the game 
        """
      
        while True:
            print(self.macgyver.inventory)
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
            elif requested_map_letter == "n" or requested_map_letter == "e" or requested_map_letter == "t":
                self.labyrinth.replace_letter(requested_position[0], requested_position[1], "m")
                self.labyrinth.replace_letter(position_before_movement[0], position_before_movement[1], " ")
                self.macgyver.set_position(requested_position[0], requested_position[1])
                self.macgyver.loot_item(requested_map_letter)
            else:
                pass

        