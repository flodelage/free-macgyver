
#! /usr/bin/env python3.7
# coding: utf-8

import pygame

class Item:
    def __init__(self, name, letter, y, x):
        self.name = name
        self.letter = letter
        self.y = y
        self.x = x

    def set_position(self, y, x):
        self.y = y
        self.x = x
