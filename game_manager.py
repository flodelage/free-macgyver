
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from labyrinth import Labyrinth
from game_personas import PlayerCharacter, NonPlayerCharacter


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
        and return its coordinates x, y (tuple)
        """
        self.macgyver = PlayerCharacter("MacGyver", position[0], position[1])
        """
        Creates MacGyver instance and assigns its coordinates x, y from var position (tuple)
        """
        position = self.labyrinth.find_letter("g")
        self.guardian = NonPlayerCharacter("Guardian", position[0], position[1])



    def start(self):
        """
        Runs the game 
        """
        while True:
    #afficher carte
            self.labyrinth.display()
    #demander user de se deplacer
            pos = self.macgyver.move() #retourne un tuple (x, y)
                
    #mettre à jour map

""" 
- Verifier si McGyver peut se déplacer à la position récuperée par la methode move()
- Creer une methode dans Labyrinth qui renvoie un character de la map en fonction d'une position: retrieve_character(self, x, y)
- Vérifier que ce character est un espace vide
    - si oui modifier les coordonnées du joueur
    - si non ne rien faire 
"""