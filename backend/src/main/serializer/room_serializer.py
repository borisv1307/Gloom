from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.serializer.abstract_serializer import AbstractSerializer


class RoomSerializer(AbstractSerializer):
    def __init__(self, tile_serializer):
        self.tile_serializer = tile_serializer

    def serialize(self, room: AbstractRoomCard):
        tiles = room.get_tiles()
        tile_dict = {
            idx: self.tile_serializer.serialize(tiles[idx])
            for idx in range(len(tiles))
        }
        return {
            'name': room.get_name(),
            'tiles': tile_dict
        }
