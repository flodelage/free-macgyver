
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from labyrinth import *
from character import Macgyver, Guard


class GameManager:
    def __init__(self):
        self.labyrinth = Labyrinth("labyrinth_sketch.txt")


    def start(self):
        pass
