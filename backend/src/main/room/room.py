"""FILE: room.py
DESCRIPTION: Abstract class for Random Rooms
"""
from backend.src.main.room.room_card_exceptions import DuplicateTileError


class AbstractRoomCard:  # pylint: disable=too-few-public-methods
    """This class outlines basic Room Card    """
    EMPTY_TILE = 0
    COIN_TILE = 99

    def __init__(self, name):
        self.name = name
        self.hexes = {}

    def add_tile(self, character_number, x_value, y_value):
        """This method adds tile to the room
        Inputs: Value, coordinates (x,y) of the tile
        """
        coordinates = (x_value, y_value)
        if character_number in self.hexes.values() and character_number is not self.EMPTY_TILE:
            raise DuplicateTileError
        if coordinates in self.hexes:
            raise DuplicateTileError
        self.hexes[coordinates] = character_number
