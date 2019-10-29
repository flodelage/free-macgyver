
#! /usr/bin/env python3.7
# coding: utf-8

from models.game_personas import PlayerCharacter, NonPlayerCharacter

from models.sprite import MySprite
from models.labyrinth import Labyrinth
from constants import *

import pygame
from pygame.locals import *


class Gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.labyrinth = Labyrinth(MAP_FILE)
        self.window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
        self.window_title = pygame.display.set_caption(WINDOW_TITLE)
        self.window_icon = pygame.image.load(ICON_IMG).convert_alpha()
        self.wall_img = pygame.image.load(WALL_IMG).convert_alpha()
        self.floor_img = pygame.image.load(FLOOR_IMG).convert_alpha()
        self.macgyver_img = pygame.image.load(PLAYER_CHARACTER_IMG).convert_alpha()
        self.guardian_img = pygame.image.load(NON_PLAYER_CHARACTER_IMG).convert_alpha()


            