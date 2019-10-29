
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
        self.clock = pygame.time.Clock()
        self.player = MySprite(self.macgyver_img)
        self.non_player = MySprite(self.guardian_img)
        self.wall_sprites_list = pygame.sprite.Group()
        self.floor_sprites_list = pygame.sprite.Group()
        self.characters_sprites_list = pygame.sprite.Group()

    def draw_characters(self):
        macgyver_position = self.labyrinth.find_letter(MACGYVER_LETTER)
        guardian_position = self.labyrinth.find_letter(GUARDIAN_LETTER)
        macgyver = PlayerCharacter("MacGyver", macgyver_position[0], macgyver_position[1], [])
        self.player.rect.x = macgyver_position[1] * SPRITE_SIZE
        self.player.rect.y = macgyver_position[0] * SPRITE_SIZE
        self.non_player.rect.x = guardian_position[1] * SPRITE_SIZE
        self.non_player.rect.y = guardian_position[0] * SPRITE_SIZE
        self.characters_sprites_list.add(self.player, self.non_player)

    def draw_walls(self):
        walls = self.labyrinth.list_letter(WALL_LETTER)
        for wall in walls:
            wall_sprite = MySprite(self.wall_img)
            wall_sprite.rect.x = wall[1] * SPRITE_SIZE
            wall_sprite.rect.y = wall[0] * SPRITE_SIZE
            self.wall_sprites_list.add(wall_sprite)
        
    def draw_floor(self):
        floors = self.labyrinth.list_letter(FLOOR_LETTER)
        for floor in floors:
            floor_sprite = MySprite(self.floor_img)
            floor_sprite.rect.x = floor[1] * SPRITE_SIZE
            floor_sprite.rect.y = floor[0] * SPRITE_SIZE
            self.floor_sprites_list.add(floor_sprite)

    def launch_game(self):
        self.draw_walls()
        self.draw_floor()
        self.draw_characters()
        while True:
            requested_position = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


            self.wall_sprites_list.draw(self.window)
            self.floor_sprites_list.draw(self.window)
            self.characters_sprites_list.draw(self.window)
            
            #Refresh window
            pygame.display.flip()
            self.clock.tick(60)
            


            