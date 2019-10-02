"""
- ficher labyrinth.py --> la classe Labyrinth s'occupera de lire le fichier où est inscrit le labyrinth 
    et le stocker dans une structure python
- Dans le constructor de la classe (__init__), tu devras ouvrir le fichier, le lire puis stocker chaque charactere 
    du fichier dans un tableau (list en python) 
"""

#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class Labyrinth:

    with open("labyrinth_sketch.txt") as file:
        #Refacto
        labyrinth_structure = [[sprite for sprite in line if sprite != "\n"]for line in file]
        """
        labyrinth_structure = []
        for line in file:
            map_line = []
            for sprite in line:
                if sprite != '\n':
                    map_line.append(sprite)
            labyrinth_structure.append(map_line)
        """

