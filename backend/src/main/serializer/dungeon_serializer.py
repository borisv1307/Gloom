from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer


class DungeonSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods
    def __init__(self, room_serializer: RoomSerializer):
        self.room_serializer = room_serializer

    def serialize(self, serializable_object: RandomDungeonGenerator):
        return {
            idx: self.room_serializer.serialize(serializable_object.constructed_rooms[idx])
            for idx in range(len(serializable_object.constructed_rooms))
        }
