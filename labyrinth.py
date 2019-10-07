
#! /usr/bin/env python3.7
# coding: utf-8

class Labyrinth:
    """
    Class which creates a map structure from a file
    """
    def __init__(self, map_file):
        with open(map_file) as file:
            self.labyrinth_structure = [[sprite for sprite in line if sprite != "\n"]for line in file]
            """
            Initializes map structure in nested lists
            """

    def find_letter(self, letter):
        """
        Finds a letter (str) in the map file and return its coordinates y, x (int) in (tuple)
        """
        y = 0
        x = 0
        for line in self.labyrinth_structure:
            x = 0
            for c in line:
                if c == letter:
                    return (y, x)
                x += 1
            y += 1

    def retrieve_letter(self, y, x):
        """
        Returns a letter from the map based on its coordinates
        """
        return self.labyrinth_structure[y][x]

    def replace_letter(self, y, x, letter):
        self.labyrinth_structure[y][x] = letter

    def display(self):
        """
        Displays the map by removing unnecessary characters (, "" [])
        """
        for line in self.labyrinth_structure:
            print("".join(line))

    def list_letter(self, letter):
        position_list = []
        y = 0
        x = 0
        for line in self.labyrinth_structure:
            x = 0
            for c in line:
                if c == letter:
                    position_list.append((y, x))
                x += 1
            y += 1
        return position_list


