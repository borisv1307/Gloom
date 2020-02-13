from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer


class RoomSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods
    def __init__(self, tile_serializer: TileSerializer, enum_serializer: EnumSerializer):
        self.tile_serializer = tile_serializer
        self.enum_serializer = enum_serializer

    def serialize(self, serializable_object: AbstractRoomCard):
        tiles = serializable_object.get_tiles()
        tile_dict = {
            idx: self.tile_serializer.serialize(tiles[idx])
            for idx in range(len(tiles))
        }
        indicators = [
            self.enum_serializer.serialize(indicator)
            for indicator in serializable_object.get_trap_indicators()
        ]
        return {
            'name': serializable_object.get_name(),
            'tiles': tile_dict,
            'indicators': indicators
        }
