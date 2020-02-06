import copy
from abc import ABC

from backend.src.main.game.values import UniqueTileValues
from backend.src.main.room.room_card_exceptions import DuplicateTileError
from backend.src.main.tile.tile import Tile


class AbstractRoomCard(ABC):  # pylint: disable=too-few-public-methods
    def __init__(self, name):
        self.name = name
        self.tiles = []

    def add_tile(self, character_number, x_value, y_value):
        new_tile = Tile(x_value, y_value, character_number)
        coordinates = (x_value, y_value)
        coordinates_in_tile_list = ((tile.get_x(), tile.get_y()) for tile in self.tiles)
        attributes = (tile.get_character_number() for tile in self.tiles)

        if isinstance(character_number, UniqueTileValues) \
                and character_number in attributes:
            raise DuplicateTileError
        if coordinates in coordinates_in_tile_list:
            raise DuplicateTileError
        self.tiles.append(new_tile)

    def rotate(self):
        new_tiles = [tile.rotate() for tile in self.get_tiles()]
        new_room = self.clone()
        new_room.set_tiles(new_tiles)
        return new_room

    def get_tiles(self) -> [Tile]:
        return self.tiles

    def get_name(self):
        return self.name

    def set_tiles(self, new_tiles):
        self.tiles = new_tiles

    def clone(self):
        return copy.deepcopy(self)
