from backend.src.main.game.tile.tile import Tile
from backend.src.main.serializer.abstract_serializer import AbstractSerializer


class TileSerializer(AbstractSerializer):
    def __init__(self, enum_serializer):
        self.enum_serializer = enum_serializer

    def serialize(self, tile: Tile):
        return {
            'x': tile.get_x(),
            'y': tile.get_y(),
            'z': tile.get_z(),
            'value': self.enum_serializer.serialize(tile.get_character_number()),
        }
