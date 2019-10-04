
#! /usr/bin/env python3.7
# coding: utf-8

import pygame


class Labyrinth:
    def __init__(self, file_map):
        with open(file_map) as file:
            self.labyrinth_structure = [[sprite for sprite in line if sprite != "\n"]for line in file]

