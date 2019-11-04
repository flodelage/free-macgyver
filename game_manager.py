
#! /usr/bin/env python3.7
# coding: utf-8



import random

from models.labyrinth import Labyrinth
from models.game_personas import PlayerCharacter, NonPlayerCharacter
from models.item import Item
from constants import *


class GameManager:
    """ Class which manages the game """
    def __init__(self):
        self.labyrinth = Labyrinth(MAP_FILE)
        """ Creates Map instance """
        position = self.labyrinth.find_letter(MACGYVER_LETTER)
        """ Finds macgyver, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple) """
        self.macgyver = PlayerCharacter("MacGyver", position[0], position[1], [])
        """ Creates PlayerCharacter instance and assigns its coordinates x, y (int) from var position """
        position = self.labyrinth.find_letter(GUARDIAN_LETTER)
        """ Finds the Guardian, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple) """
        self.guardian = NonPlayerCharacter("Guardian", position[0], position[1])
        """ Creates NonPlayerCharacter instance and assigns its coordinates x, y (int) from var position """
        self.items = [Item("needle", "n", -1, -1), Item("ether", "e", -1, -1), Item("tube", "t", -1, -1)]
        floor_squares = self.labyrinth.list_letter(FLOOR_LETTER)
        items_positions = []
        while len(items_positions) != len(self.items):
            for item in self.items:
                random_position = random.choice(floor_squares)
                item.set_position(random_position[0], random_position[1])
                self.labyrinth.replace_letter(item.y, item.x, item.letter)
                new_item_position = (item.y, item.x)
                if new_item_position not in items_positions : items_positions.append(new_item_position)
     

    def start(self):
        """ Runs the game """
        run = True
        while run:
            print(self.macgyver.inventory)
            self.labyrinth.display()
            """ Displays map to user """
            position_before_movement = (self.macgyver.y, self.macgyver.x)
            requested_position = self.macgyver.move()
            """ The user tries to move the Player Character
            Returns the requested coordinates (int, int) """
            requested_map_letter = self.labyrinth.retrieve_letter(requested_position[0], requested_position[1])
            if requested_map_letter != WALL_LETTER:
                self.labyrinth.replace_letter(requested_position[0], requested_position[1], MACGYVER_LETTER)
                self.labyrinth.replace_letter(position_before_movement[0], position_before_movement[1], FLOOR_LETTER)
                self.macgyver.set_position(requested_position[0], requested_position[1])
            if requested_map_letter == NEEDLE_LETTER or requested_map_letter == ETHER_LETTER or requested_map_letter == TUBE_LETTER:
                for item in self.items:
                    if item.letter == requested_map_letter:
                        item_name = item.name
                        self.macgyver.loot_item(item_name)
            elif requested_map_letter == GUARDIAN_LETTER:
                if self.macgyver.is_inventory_full(self.items) == True:
                    print("You slept the Guardian !")
                    print("YOU WIN !")
                elif self.macgyver.is_inventory_full(self.items) == False:
                    print("The Guardian is still awake !")
                    print("YOU LOSE !")
                run = False

        