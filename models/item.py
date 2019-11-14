
class Item:
    """ Base class for all items in the game """
    def __init__(self, name, letter, y, x):
        self.name = name
        self.letter = letter
        self.y = y
        self.x = x

    def set_position(self, y, x):
        """ It defines Item position from its
        coordinates y and x  """
        self.y = y
        self.x = x
