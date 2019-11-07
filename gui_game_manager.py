
# ! /usr/bin/env python3.7
# coding: utf-8


import pygame

import random

from models.game_personas import PlayerCharacter
from models.item import Item
from models.sprite import MySprite
from models.labyrinth import Labyrinth
from settings import *


class GuiGameManager:
    def __init__(self):
        """ initialize pygame """
        pygame.init()
        """ set Labyrinth instance """
        self.labyrinth = Labyrinth(MAP_FILE)
        """ set game window """
        self.window = pygame.display.set_mode((WINDOW_SIDE + 160, WINDOW_SIDE))
        """ set attributes images """ 
        self.macgyver_img = pygame.image.load(PLAYER_IMG).convert_alpha()
        self.guardian_img = pygame.image.load(NON_PLAYER_IMG).convert_alpha()
        self.wall_img = pygame.image.load(WALL_IMG).convert_alpha()
        self.floor_img = pygame.image.load(FLOOR_IMG).convert_alpha()
        self.needle_img = pygame.image.load(NEEDLE_IMG).convert_alpha()
        self.ether_img = pygame.image.load(ETHER_IMG).convert_alpha()
        self.tube_img = pygame.image.load(TUBE_IMG).convert_alpha()
        self.win_img = pygame.image.load(WIN_IMG).convert_alpha()
        self.lose_img = pygame.image.load(LOSE_IMG).convert_alpha()
        """ set Sprite instances """
        self.player_sprite = MySprite(self.macgyver_img)
        self.non_player_sprite = MySprite(self.guardian_img)
        self.needle_sprite = MySprite(self.needle_img)
        self.ether_sprite = MySprite(self.ether_img)
        self.tube_sprite = MySprite(self.tube_img)
        """ set Sprite instances in sprite Group() class """
        self.wall_sprites_list = pygame.sprite.Group()
        self.floor_sprites_list = pygame.sprite.Group()
        self.characters_sprites_list = pygame.sprite.Group()
        self.items_sprites_list = pygame.sprite.Group()
        """ set pygame time Clock() """
        self.clock = pygame.time.Clock()
        """ set pygame text surface for inventory information  """
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text_surface = self.font.render("Inventory:", True, (255, 255, 255))
        self.window.blit(text_surface, dest=(WINDOW_SIDE + 20, 30))

    def set_characters(self):
        """ set Player and Non Player Character positions from map file """
        macgyver_pos = self.labyrinth.find_letter_position(MACGYVER_LETTER)
        guardian_pos = self.labyrinth.find_letter_position(GUARDIAN_LETTER)
        """ set PlayerCharacter instance: macgyver """
        self.macgyver = PlayerCharacter("MacGyver", macgyver_pos[0],
                                        macgyver_pos[1], [])
        """ set characters Sprite instances and their rect positions """
        self.player_sprite.rect.x = macgyver_pos[1] * SPRITE_SIZE
        self.player_sprite.rect.y = macgyver_pos[0] * SPRITE_SIZE
        self.non_player_sprite.rect.x = guardian_pos[1] * SPRITE_SIZE
        self.non_player_sprite.rect.y = guardian_pos[0] * SPRITE_SIZE
        """ Then add them into sprite group """
        self.characters_sprites_list.add(self.player_sprite,
                                         self.non_player_sprite)

    def set_walls(self):
        """ set walls positions from map file and assign
        them to Sprite rect positions """
        walls = self.labyrinth.list_position_letter(WALL_LETTER)
        for wall in walls:
            wall_sprite = MySprite(self.wall_img)
            wall_sprite.rect.x = wall[1] * SPRITE_SIZE
            wall_sprite.rect.y = wall[0] * SPRITE_SIZE
            """ Then add them into sprite group """
            self.wall_sprites_list.add(wall_sprite)
        
    def set_floor(self):
        """ set floors positions from map file and assign
        them to Sprite rect positions.
        Macgyver and guardian images being transparent, we need to draw
        floors at their positions """
        floors = self.labyrinth.list_position_letter(FLOOR_LETTER)
        macgyver = self.labyrinth.list_position_letter(MACGYVER_LETTER)
        guardian = self.labyrinth.list_position_letter(GUARDIAN_LETTER)
        floors += macgyver + guardian
        for floor in floors:
            floor_sprite = MySprite(self.floor_img)
            floor_sprite.rect.x = floor[1] * SPRITE_SIZE
            floor_sprite.rect.y = floor[0] * SPRITE_SIZE
            """ Then add them into sprite group """
            self.floor_sprites_list.add(floor_sprite)

    def set_items(self):
        self.items = [Item("needle", "n", -1, -1), Item("ether", "e", -1, -1),
                      Item("tube", "t", -1, -1)]
        self.items_sprites_list.add(self.needle_sprite, self.ether_sprite,
                                    self.tube_sprite)
        """ Set floors from map file letter, list of
        coordinates y x (int, int) """
        floor_squares = self.labyrinth.list_position_letter(FLOOR_LETTER)
        """ For each object, a random position picken from
        the floors positions list will be chosen.
        This random position will be assigned to the item position.
        The labyrinth is updated: item letter added to the position.
        The position is removed from the list of available floors in order
        to no longer be selected and to prevent that two objects from being
        in the same position """
        for item in self.items:
            random_position = random.choice(floor_squares)
            item.set_position(random_position[0], random_position[1])
            self.labyrinth.replace_letter(item.y, item.x, item.letter)
            floor_squares.remove(random_position)
        """ assign positions to Sprite rect """
        for sprite_id, sprite, in enumerate(self.items_sprites_list):
            item = self.items[sprite_id]
            sprite.rect.x = item.x * SPRITE_SIZE
            sprite.rect.y = item.y * SPRITE_SIZE

    def launch_game(self):
        """ Run the game """

        """ set Sprite instances positions """
        self.set_walls()
        self.set_floor()
        self.set_items()
        self.set_characters()

        while True:
            """ initialize necessary movement variables """
            requested_position = None
            position_before_movement = (self.macgyver.y, self.macgyver.x) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    """ The user wants to move Macgyver.
                    Store requested coordinates (int, int) """
                    requested_position = self.macgyver.move_gui(event.key)

                    if requested_position is not None:
                        """ Store which letter is at the requested position
                        and compare this letter to wall letter """
                        requested_map_letter = \
                            self.labyrinth.retrieve_letter(requested_position[0], 
                                                           requested_position[1])
                        """ If the letter present at the requested position
                        is not a wall letter: """
                        if requested_map_letter != WALL_LETTER:
                            """ the letter present at the requested position
                            is replaced by macgyver letter """
                            self.labyrinth.replace_letter(requested_position[0], 
                                                          requested_position[1],
                                                          MACGYVER_LETTER)
                            """ the old Macgyver position is replaced by
                            a floor letter """
                            self.labyrinth.replace_letter(position_before_movement[0],
                                                          position_before_movement[1],
                                                          FLOOR_LETTER)
                            """ Character Sprite instance is moved
                            to the requested position """
                            self.player_sprite.move(requested_position)
                            """ the new macgyver coordinates position
                            are redefined """
                            self.macgyver.set_position(requested_position[0],
                                                       requested_position[1])

                        """ If the letter present at the requested position
                        is one of items letter:
                        item name is added to Macgyver's inventory.
                        Item name is added to the inventory pygame text surface
                        Item Sprite instance is deleted so that
                        it is not redrawn """
                        if requested_map_letter == NEEDLE_LETTER or \
                            requested_map_letter == ETHER_LETTER or \
                                requested_map_letter == TUBE_LETTER:
                            for item in self.items:
                                if item.letter == requested_map_letter:
                                    item_name = item.name
                                    self.macgyver.loot_item(item_name)
                                    text_surface = self.font.render(item_name,
                                                                    True,
                                                                    (255, 255, 255))
                                    self.window.blit(text_surface, dest=(WINDOW_SIDE + 20,
                                                                         60 + (len(self.macgyver.inventory) * 30)))
                                    for sprite in self.items_sprites_list:
                                        if sprite.rect.x == item.x * SPRITE_SIZE and \
                                            sprite.rect.y == item.y * SPRITE_SIZE:
                                            sprite.kill()
                        elif requested_map_letter == GUARDIAN_LETTER:
                            """ If the letter present at the requested position
                            is the Guardian letter:
                            - User win if he looted all items
                            - User lose if he looted all items
                            All Sprite groups are emptied so that they are 
                            no longer displayed and make room for 
                            the end game message """
                            if self.macgyver.is_inventory_full(self.items):
                                self.wall_sprites_list.empty()
                                self.floor_sprites_list.empty()
                                self.items_sprites_list.empty()
                                self.characters_sprites_list.empty()
                                self.window.blit(self.win_img, (0, 0))
                            elif not self.macgyver.is_inventory_full(self.items):
                                self.wall_sprites_list.empty()
                                self.floor_sprites_list.empty()
                                self.items_sprites_list.empty()
                                self.characters_sprites_list.empty()
                                self.window.blit(self.lose_img, (0, 0))

                """ draw Sprite images to their positions """
                self.wall_sprites_list.draw(self.window)
                self.floor_sprites_list.draw(self.window)
                self.items_sprites_list.draw(self.window)
                self.characters_sprites_list.draw(self.window)

                """ Refresh window """
                pygame.display.flip()
                self.clock.tick(60)
