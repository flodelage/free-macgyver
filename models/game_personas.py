
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from pygame.locals import *
from pygame import K_RIGHT, K_LEFT, K_DOWN, K_UP

class GamePersona:
    """ Base class for all personas (PlayerCharacter, NonPlayerCharacter...) in the game """
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x


class PlayerCharacter(GamePersona):
    """ Class which creates Player Character """
    def __init__(self, name, y, x, inventory):
        GamePersona.__init__(self, name, y, x)
        self.inventory = []

    def set_position(self, y, x):
        self.y = y
        self.x = x

    def move_gui(self, key):
        if key == K_RIGHT:
            return (self.y, self.x + 1)
        if key == K_LEFT:
            return (self.y, self.x -1)
        if key == K_UP:
            return (self.y - 1, self.x)
        if key == K_DOWN:
            return (self.y + 1, self.x)

    def move(self):
        """ Defines the movement of the Player Character.
        Gets the event (str) and
        returns the requested coordinates (int, int) """
        while True:
            event = input("Use z, q, s, or d to move your character:")
            if event == "q":
                return (self.y, self.x -1)
            elif event == "d":
                return (self.y, self.x + 1)
            elif event == "z":
                return (self.y - 1, self.x)
            elif event == "s":
                return (self.y + 1, self.x)
            else:
                next
        
    def loot_item(self, item_name):
        self.inventory.append(item_name)

    def display_inventory(self, inventory):
        print("Inventory:")
        for item in inventory:
            print("".join(item))

    def is_inventory_full(self, items):
        if len(self.inventory) == len(items):
            return True
        else:
            return False


class NonPlayerCharacter(GamePersona):
    """ Class which creates Non Player Character """
    def __init__(self, name, y, x):
        GamePersona.__init__(self, name, y, x)