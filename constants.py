
#! /usr/bin/env python3.7
# coding: utf-8

import pygame
from pygame.locals import *


"""
[Window params]
"""
# sets window size
SPRITE_SIZE = 30
SPRITES_QTY = 15
WINDOW_SIDE = SPRITE_SIZE * SPRITES_QTY

"""
[Images params]
"""
# sets wall image
WALL_IMG = "data/resources/wall.png"
# sets floor image
FLOOR_IMG = "data/resources/floor.png"
# sets player character image
PLAYER_CHARACTER_IMG = "data/resources/macgyver.png"
# # sets non player character image
NON_PLAYER_CHARACTER_IMG = "data/resources/guard.png"
NEEDLE_IMG = "data/resources/needle.png"
ETHER_IMG = "data/resources/ether.png"
TUBE_IMG = "data/resources/tube.png"

"""
[Labyrinth params]
"""
MAP_FILE = "data/labyrinth_sketch.txt"
WALL_LETTER = "x"
FLOOR_LETTER = " "

"""
[Items params]
"""
NEEDLE_LETTER = "n"
ETHER_LETTER = "e"
TUBE_LETTER = "t"

"""
[Personas params]
"""
MACGYVER_LETTER = "m"
GUARDIAN_LETTER = "g"


