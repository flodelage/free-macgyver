
#! /usr/bin/env python3.7
# coding: utf-8

class Labyrinth:
    """ Class which creates a map structure from a file """
    def __init__(self, map_file):
        with open(map_file) as file:
            self.labyrinth_structure = [[letter for letter in line if letter != "\n"]for line in file]
            """ Initializes map structure in nested lists """

    def draw_structure_sprites(self, wall_img, floor_img, window):
        for line_id, line in enumerate(self.labyrinth_structure):
            for sprite_id, sprite in enumerate(line):
                # Sets sprites' coords
                x = sprite_id * SPRITE_SIZE
                y = line_id * SPRITE_SIZE
                # Displays wall if sprite in labyrinth_structure
                # is equal to the WALL_LETTER constant
                if sprite in WALL_LETTER:
                    window.blit(wall_img, (x, y))
                # sets the floor sprite where there is no wall
                if sprite not in WALL_LETTER:
                    window.blit(floor_img, (x, y))

    def find_letter(self, letter):
        """ Finds a letter (str) in the map file and return its coordinates y, x (int) in (tuple) """
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
        """ Returns a letter from the map based on its coordinates """
        return self.labyrinth_structure[y][x]

    def list_letter(self, letter):
        """ Returns in a list the coordinates of each letter  """
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

    def replace_letter(self, y, x, letter):
        self.labyrinth_structure[y][x] = letter

    def display(self):
        """ Displays the map by removing unnecessary characters (, "" []) """
        for line in self.labyrinth_structure:
            print("".join(line))



