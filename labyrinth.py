
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class Labyrinth:
    def __init__(self, file_map):
        with open(file_map) as file:
            self.labyrinth_structure = [[sprite for sprite in line if sprite != "\n"]for line in file]

    def find_character(self, char):
        x = 0
        y = 0
        for line in self.labyrinth_structure:
            x = 0
            for c in line:
                if c == char:
                    return (x, y)
                x += 1
            y += 1

    def display(self):
        for line in self.labyrinth_structure:
            print("".join(line))