
from pygame import K_RIGHT, K_LEFT, K_DOWN, K_UP


class GamePersona:
    """ Base class for all personas (PlayerCharacter,
    NonPlayerCharacter...) in the game """
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x


class PlayerCharacter(GamePersona):
    """ Class which creates Player Character, inherit from
    Game Persona class """
    def __init__(self, name, y, x, inventory):
        GamePersona.__init__(self, name, y, x)
        self.inventory = []

    def set_position(self, y, x):
        """ It defines Player Character position from its
        coordinates y and x  """
        self.y = y
        self.x = x

    def move(self):
        """ [Terminal version method]
        Prompts the user to enter a letter to define the direction that the
        Player Character should take.
        Gets the event (str) and returns the requested
        coordinates (int, int) """
        while True:
            event = input("Use z, q, s, or d to move your character:")
            if event == "q":
                return (self.y, self.x - 1)
            elif event == "d":
                return (self.y, self.x + 1)
            elif event == "z":
                return (self.y - 1, self.x)
            elif event == "s":
                return (self.y + 1, self.x)
            else:
                next

    def move_gui(self, key):
        """ [Gui version method]
        It defines the movement of the Player Character.
        Gets the event (str) and returns the requested
        coordinates (int, int) """
        if key == K_RIGHT:
            return (self.y, self.x + 1)
        if key == K_LEFT:
            return (self.y, self.x - 1)
        if key == K_UP:
            return (self.y - 1, self.x)
        if key == K_DOWN:
            return (self.y + 1, self.x)

    def loot_item(self, item_name):
        """ It adds an item name in Player Character's inventory """
        self.inventory.append(item_name)

    def display_inventory(self, inventory):
        """ It displays the current content of Player Character's inventory """
        print("Inventory:")
        for item in inventory:
            print("".join(item))

    def is_inventory_full(self, items):
        """ It checks if all items are in Player Character's inventory.
        It compares the size of the Player Character's inventory to
        the number of object instances. It returns True if both identical """
        if len(self.inventory) == len(items):
            return True
        else:
            return False


class NonPlayerCharacter(GamePersona):
    """ Class which creates Non Player Character, inherit from
    Game Persona class """
    def __init__(self, name, y, x):
        GamePersona.__init__(self, name, y, x)
