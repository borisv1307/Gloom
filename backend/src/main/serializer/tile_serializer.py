from backend.src.main.game.tile.tile import Tile
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer


class TileSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods
    def __init__(self, enum_serializer: EnumSerializer):
        self.enum_serializer = enum_serializer

    def serialize(self, serializable_object: Tile):
        return {
            'x': serializable_object.get_x(),
            'y': serializable_object.get_y(),
            'z': serializable_object.get_z(),
            'value': self.enum_serializer.serialize(serializable_object.get_character_number()),
        }
