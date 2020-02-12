from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer


class RoomSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods
    def __init__(self, tile_serializer: TileSerializer):
        self.tile_serializer = tile_serializer

    def serialize(self, serializable_object: AbstractRoomCard):
        tiles = serializable_object.get_tiles()
        tile_dict = {
            idx: self.tile_serializer.serialize(tiles[idx])
            for idx in range(len(tiles))
        }
        return {
            'name': serializable_object.get_name(),
            'tiles': tile_dict
        }
