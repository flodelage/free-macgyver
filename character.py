
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Macgyver(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)


class Guard(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)