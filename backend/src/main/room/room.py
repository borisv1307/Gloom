from abc import ABC
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues
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

        if isinstance(character_number, NumberedRoomTileValues) \
                and character_number in attributes:
            raise DuplicateTileError
        if coordinates in coordinates_in_tile_list:
            raise DuplicateTileError
        self.tiles.append(new_tile)

    def get_tiles(self):
        return self.tiles

    def get_name(self):
        return self.name
