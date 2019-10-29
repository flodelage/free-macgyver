
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


            