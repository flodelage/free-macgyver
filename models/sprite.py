
#! /usr/bin/env python3.7
# coding: utf-8

from constants import *

import pygame
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect()

    def move(self, new_pos):
        self.rect.x = new_pos[1] * SPRITE_SIZE 
        self.rect.y = new_pos[0] * SPRITE_SIZE