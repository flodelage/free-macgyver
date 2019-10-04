
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from labyrinth import Labyrinth
from game_personas import PlayerCharacter, NonPlayerCharacter


class GameManager:
    def __init__(self):
        self.labyrinth = Labyrinth("labyrinth_sketch.txt")
        pos = self.labyrinth.find_character("m")
        self.macgyver = PlayerCharacter(pos[0], pos[1])
        pos = self.labyrinth.find_character("g")
        self.guard = NonPlayerCharacter(pos[0], pos[1])



    def start(self):
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