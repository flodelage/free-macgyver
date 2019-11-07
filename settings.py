
# ! /usr/bin/env python3.7
# coding: utf-8


"""
[Window params]
"""
""" sets window size """
SPRITE_SIZE = 30
SPRITES_QTY = 15
WINDOW_SIDE = SPRITE_SIZE * SPRITES_QTY

"""
[Images params]
"""
""" sets wall image """
WALL_IMG = "data/images/wall.png"
""" sets floor image """
FLOOR_IMG = "data/images/floor.png"
""" sets player character image """
PLAYER_IMG = "data/images/macgyver.png"
""" sets non player character image """
NON_PLAYER_IMG = "data/images/guard.png"
""" sets items images """
NEEDLE_IMG = "data/images/needle.png"
ETHER_IMG = "data/images/ether.png"
TUBE_IMG = "data/images/tube.png"
""" sets end game images """
WIN_IMG = "data/images/youwin.png"
LOSE_IMG = "data/images/youdied.png"

"""
[Labyrinth params]
"""
""" sets map file """
MAP_FILE = "data/map/labyrinth_sketch.txt"
""" sets walls letter from map file """
WALL_LETTER = "x"
""" sets floors letter from map file """
FLOOR_LETTER = " "

"""
[Personas params]
"""
""" sets characters letters """
MACGYVER_LETTER = "m"
GUARDIAN_LETTER = "g"

"""
[Items params]
"""
""" sets items letter """
NEEDLE_LETTER = "n"
ETHER_LETTER = "e"
TUBE_LETTER = "t"
