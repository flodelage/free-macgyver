
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from labyrinth import *
from character import Macgyver, Guard


class GameManager:
    def __init__(self):
        self.labyrinth = Labyrinth("labyrinth_sketch.txt")
        pos = self.labyrinth.find_character("g")
        self.guard = Guard(pos[0], pos[1])
        pos = self.labyrinth.find_character("m")
        self.macgyver = Macgyver(pos[0], pos[1])


    def start(self):
        while True:
    #afficher carte
            self.labyrinth.display()
    #demander user de se deplacer
            pos = self.macgyver.move()
    #mettre à jour map
