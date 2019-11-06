
# ! /usr/bin/env python3.7
# coding: utf-8

import random

from models.labyrinth import Labyrinth
from models.game_personas import PlayerCharacter, NonPlayerCharacter
from models.item import Item
from settings import MAP_FILE, MACGYVER_LETTER, GUARDIAN_LETTER, WALL_LETTER, FLOOR_LETTER, NEEDLE_LETTER, ETHER_LETTER, TUBE_LETTER


class TerminalGameManager:
    """ Class which manages the terminal version of the game """
    def __init__(self):
        """ Create Labyrinth instance """
        self.labyrinth = Labyrinth(MAP_FILE)
        """ Find macgyver, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple) """
        position = self.labyrinth.find_letter_position(MACGYVER_LETTER)
        """ Create PlayerCharacter instance and assigns
        its coordinates x, y (int) from var position """
        self.macgyver = PlayerCharacter("MacGyver", position[0],
                                        position[1], [])
        """ Find the Guardian, represented by a letter (str)
        and return its coordinates y, x (int) in a (tuple) """
        position = self.labyrinth.find_letter_position(GUARDIAN_LETTER)
        """ Create NonPlayerCharacter instance and assigns
        its coordinates x, y (int) from var position """
        self.guardian = NonPlayerCharacter("Guardian", position[0],
                                           position[1])
        """ Create Item instances """
        self.items = [Item("needle", "n", -1, -1), Item("ether", "e", -1, -1),
                      Item("tube", "t", -1, -1)]

        """ Set floors from map file letter, list of coordinates y x (int, int) """
        floor_squares = self.labyrinth.list_position_letter(FLOOR_LETTER)
        """ For each object, a random position picken from the floors positions list will be chosen.
        This random position will be assigned to the item position.
        The labyrinth is updated: item letter added to the position
        The position is removed from the list of available floors in order to no longer be selected and to prevent that two objects from being in the same position"""
        for item in self.items:
            random_position = random.choice(floor_squares)
            item.set_position(random_position[0], random_position[1])
            self.labyrinth.replace_letter(item.y, item.x, item.letter)
            floor_squares.remove(random_position)

    def launch_game(self):
        """ Run the game """
        run = True
        while run:
            """ Display Macgyver inventory to user """
            self.macgyver.display_inventory(self.macgyver.inventory)
            """ Display map to user """
            self.labyrinth.display()

            """ Store macgyver current position """
            position_before_movement = (self.macgyver.y, self.macgyver.x)
            """ The user wants to move Macgyver.
            Store requested coordinates (int, int) """
            requested_position = self.macgyver.move()
            """ Store which letter is at the requested position
            and compare this letter to wall letter """
            requested_map_letter = self.labyrinth.retrieve_letter(requested_position[0], requested_position[1])

            """ If the letter present at the requested position
            is not a wall letter: """
            if requested_map_letter != WALL_LETTER:
                """ the letter present at the requested position
                is replaced by macgyver letter """
                self.labyrinth.replace_letter(requested_position[0],
                                              requested_position[1],
                                              MACGYVER_LETTER)
                """ the old Macgyver position is replaced by a floor letter """
                self.labyrinth.replace_letter(position_before_movement[0],
                                              position_before_movement[1],
                                              FLOOR_LETTER)
                """ the new macgyver coordinates position are redefined """
                self.macgyver.set_position(requested_position[0],
                                           requested_position[1])

            """ If the letter present at the requested position is one of items letter:
            item name is added to Macgyver's inventory  """
            if requested_map_letter == NEEDLE_LETTER or requested_map_letter == ETHER_LETTER or requested_map_letter == TUBE_LETTER:
                for item in self.items:
                    if item.letter == requested_map_letter:
                        item_name = item.name
                        self.macgyver.loot_item(item_name)
            elif requested_map_letter == GUARDIAN_LETTER:
                """ If the letter present at the requested position
                is the Guardian letter:
                - User win if he looted all items
                - User lose if he looted all items """
                if self.macgyver.is_inventory_full(self.items):
                    print("*** You slept the Guardian ! ***")
                    print("*** YOU WIN ! ***")
                elif not self.macgyver.is_inventory_full(self.items):
                    print("*** The Guardian is still awake ! ***")
                    print("*** YOU LOSE ! ***")
                """ the loop game ends """
                run = False
