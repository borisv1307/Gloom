from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer


class DungeonSerializer(AbstractSerializer):
    def __init__(self, room_serializer: RoomSerializer):
        self.room_serializer = room_serializer

    def serialize(self, dungeon: RandomDungeonGenerator):
        return {
            idx: self.room_serializer.serialize(dungeon.constructed_rooms[idx])
            for idx in range(len(dungeon.constructed_rooms))
        }
