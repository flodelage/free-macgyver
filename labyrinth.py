
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class Labyrinth:
    """
    Class which creates a map structure from a file
    """
    def __init__(self, map_file):
        with open(map_file) as file:
            self.labyrinth_structure = [[sprite for sprite in line if sprite != "\n"]for line in file]

    def find_letter(self, letter):
        """
        Finds a letter in the map file and return its position in a tuple
        """
        x = 0
        y = 0
        for line in self.labyrinth_structure:
            x = 0
            for c in line:
                if c == letter:
                    return (x, y)
                x += 1
            y += 1

    def display(self):
        """
        Displays the map by removing unnecessary characters (, "" [])
        """
        for line in self.labyrinth_structure:
            print("".join(line))