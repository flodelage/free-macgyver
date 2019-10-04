
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

    def move(self):
        event = input("utiliser z q s d pour se déplacer")
        if event == "z":
            return (self.x, self.y - 1)
        elif event == "q":
            return (self.x - 1, self.y)
        elif event == "s":
            return (self.x, self.y + 1)
        elif event == "d":
            return (self.x + 1, self.y)


class Guard(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)