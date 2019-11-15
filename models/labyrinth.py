
class Labyrinth:
    """ Base class to create labyrinth in the game """
    def __init__(self, map_file):
        """ It initializes map structure in nested list.
        Each line is a list into Labyrinth list"""
        with open(map_file) as file:
            self.labyrinth_structure = [
                    [letter for letter in line if letter != "\n"]
                    for line in file
                ]

    def display(self):
        """ It displays the map by removing unnecessary
        characters (, "" []) """
        for line in self.labyrinth_structure:
            print("".join(line))

    def find_letter_position(self, letter):
        """ It finds a letter (str) in the map nested list and return its
        coordinates y, x (int) in (tuple) """
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
        """ It returns a letter from the map nested list based on
        its coordinates """
        return self.labyrinth_structure[y][x]

    def list_position_letter(self, letter):
        """ It returns in a list the coordinates of letter(s) from
        map nested list """
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
        """ It replaces the letter at given coordinates by the letter given """
        self.labyrinth_structure[y][x] = letter
