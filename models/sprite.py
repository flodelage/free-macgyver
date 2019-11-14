
# ! /usr/bin/env python3.7
# coding: utf-8

import pygame


from settings import SPRITE_SIZE


class MySprite(pygame.sprite.Sprite):
    """ Class which inherit from pygame Sprite class """
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def move_sprite(self, new_pos):
        """ It defines image rect x and y position from
        a position tuple (y, x)  """
        self.rect.x = new_pos[1] * SPRITE_SIZE
        self.rect.y = new_pos[0] * SPRITE_SIZE
