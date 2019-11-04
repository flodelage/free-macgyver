
#! /usr/bin/env python3.7
# coding: utf-8

import random

import pygame
from pygame.locals import *

from models.game_personas import PlayerCharacter, NonPlayerCharacter
from models.item import Item
from models.sprite import MySprite
from models.labyrinth import Labyrinth
from constants import *


class Gui:
    def __init__(self):
        pygame.init()
        # set Labyrinth instance
        self.labyrinth = Labyrinth(MAP_FILE)
        # set game window
        self.window = pygame.display.set_mode((WINDOW_SIDE + 200, WINDOW_SIDE))
        # set images 
        self.macgyver_img = pygame.image.load(PLAYER_CHARACTER_IMG).convert_alpha()
        self.guardian_img = pygame.image.load(NON_PLAYER_CHARACTER_IMG).convert_alpha()
        self.wall_img = pygame.image.load(WALL_IMG).convert_alpha()
        self.floor_img = pygame.image.load(FLOOR_IMG).convert_alpha()
        self.needle_img = pygame.image.load(NEEDLE_IMG).convert_alpha()
        self.ether_img = pygame.image.load(ETHER_IMG).convert_alpha()
        self.tube_img = pygame.image.load(TUBE_IMG).convert_alpha()
        # set Sprite instances
        self.player_sprite = MySprite(self.macgyver_img)
        self.non_player_sprite = MySprite(self.guardian_img)
        self.needle_sprite = MySprite(self.needle_img)
        self.ether_sprite = MySprite(self.ether_img)
        self.tube_sprite = MySprite(self.tube_img)
        # set Sprite instances in sprite Group() class
        self.wall_sprites_list = pygame.sprite.Group()
        self.floor_sprites_list = pygame.sprite.Group()
        self.characters_sprites_list = pygame.sprite.Group()
        self.items_sprites_list = pygame.sprite.Group()
        # set pygame time Clock()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text_surface = self.font.render("Inventory:", True, (255, 255, 255))
        self.window.blit(text_surface, dest=(WINDOW_SIDE + 20, 30))


    def set_characters(self):
        macgyver_position = self.labyrinth.find_letter(MACGYVER_LETTER)
        guardian_position = self.labyrinth.find_letter(GUARDIAN_LETTER)
        self.macgyver = PlayerCharacter("MacGyver", macgyver_position[0], macgyver_position[1], [])
        self.player_sprite.rect.x = macgyver_position[1] * SPRITE_SIZE
        self.player_sprite.rect.y = macgyver_position[0] * SPRITE_SIZE
        self.non_player_sprite.rect.x = guardian_position[1] * SPRITE_SIZE
        self.non_player_sprite.rect.y = guardian_position[0] * SPRITE_SIZE
        self.characters_sprites_list.add(self.player_sprite, self.non_player_sprite)

    def set_walls(self):
        walls = self.labyrinth.list_letter(WALL_LETTER)
        for wall in walls:
            wall_sprite = MySprite(self.wall_img)
            wall_sprite.rect.x = wall[1] * SPRITE_SIZE
            wall_sprite.rect.y = wall[0] * SPRITE_SIZE
            self.wall_sprites_list.add(wall_sprite)
        
    def set_floor(self):
        floors = self.labyrinth.list_letter(FLOOR_LETTER)
        macgyver = self.labyrinth.list_letter(MACGYVER_LETTER)
        guardian = self.labyrinth.list_letter(GUARDIAN_LETTER)
        floors += macgyver + guardian
        for floor in floors:
            floor_sprite = MySprite(self.floor_img)
            floor_sprite.rect.x = floor[1] * SPRITE_SIZE
            floor_sprite.rect.y = floor[0] * SPRITE_SIZE
            self.floor_sprites_list.add(floor_sprite)

    def set_items(self):
        self.items = [Item("needle", "n", -1, -1), Item("ether", "e", -1, -1), Item("tube", "t", -1, -1)]
        self.items_sprites_list.add(self.needle_sprite, self.ether_sprite, self.tube_sprite)
        floor_squares = self.labyrinth.list_letter(FLOOR_LETTER)
        for item in self.items:
            random_position = random.choice(floor_squares)
            item.set_position(random_position[0], random_position[1])
            self.labyrinth.replace_letter(item.y, item.x, item.letter)
            floor_squares.remove(random_position)
        for sprite_id, sprite, in enumerate(self.items_sprites_list):
            item = self.items[sprite_id]
            sprite.rect.x = item.x * SPRITE_SIZE
            sprite.rect.y = item.y * SPRITE_SIZE

    def launch_game(self):
        self.set_walls()
        self.set_floor()
        self.set_items()
        self.set_characters()

        while True:
            requested_position = None
            position_before_movement = (self.macgyver.y, self.macgyver.x) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    #retourne un tuple de coordonnées
                    requested_position = self.macgyver.move_gui(event.key)

                    if requested_position is not None:
                        requested_map_letter = self.labyrinth.retrieve_letter(requested_position[0], requested_position[1])
                        if requested_map_letter != WALL_LETTER:
                            self.labyrinth.replace_letter(requested_position[0], requested_position[1], MACGYVER_LETTER)
                            self.labyrinth.replace_letter(position_before_movement[0], position_before_movement[1], FLOOR_LETTER)
                            self.player_sprite.move(requested_position)
                            self.macgyver.set_position(requested_position[0], requested_position[1])
                        if requested_map_letter == NEEDLE_LETTER or requested_map_letter == ETHER_LETTER or requested_map_letter == TUBE_LETTER:
                            for item in self.items:
                                if item.letter == requested_map_letter:
                                    item_name = item.name
                                    self.macgyver.loot_item(item_name)
                                    text_surface = self.font.render(item_name, True, (255, 255, 255))
                                    self.window.blit(text_surface, dest=(WINDOW_SIDE + 20, 60 + (len(self.macgyver.inventory) * 30)))
                                    for sprite in self.items_sprites_list:
                                        if sprite.rect.x == item.x * SPRITE_SIZE and sprite.rect.y == item.y * SPRITE_SIZE:
                                            sprite.kill()
                                            break
                        elif requested_map_letter == GUARDIAN_LETTER:
                            if self.macgyver.is_inventory_full(self.items) == True:
                                print("You slept the Guardian !")
                                print("YOU WIN !")
                                return
                            elif self.macgyver.is_inventory_full(self.items) == False:
                                print("The Guardian is still awake !")
                                print("YOU LOSE !")
                                return
                        self.items_sprites_list.update()
                        self.characters_sprites_list.update()

                self.wall_sprites_list.draw(self.window)
                self.floor_sprites_list.draw(self.window)
                self.items_sprites_list.draw(self.window)
                self.characters_sprites_list.draw(self.window)
                
                #Refresh window
                pygame.display.flip()
                self.clock.tick(60)
            