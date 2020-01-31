from abc import ABC
from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.room_card_exceptions import DuplicateTileError
from backend.src.main.room.tile import Tile


class AbstractRoomCard(ABC):  # pylint: disable=too-few-public-methods
    def __init__(self, name):
        self.name = name
        self.tiles = {}

    def add_tile(self, character_number, x_value, y_value):
        coordinates = (x_value, y_value)
        if character_number in self.tiles.values() \
                and character_number is not DungeonCardValues.EMPTY:
            raise DuplicateTileError
        if coordinates in self.tiles:
            raise DuplicateTileError
        self.tiles[coordinates] = character_number

    def get_tiles(self):
        output_tiles = []
        for coordinate in self.tiles:
            value = self.tiles[coordinate]
            current_tile = Tile(coordinate[0], coordinate[1], value)
            output_tiles.append(current_tile)
        return output_tiles
