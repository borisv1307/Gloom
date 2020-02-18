from backend.src.main.serializer.dungeon_serializer import DungeonSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer


class SerializerBuilder:
    @staticmethod
    def create_enum_serializer():
        return EnumSerializer()

    @staticmethod
    def create_tile_serializer():
        return TileSerializer(SerializerBuilder.create_enum_serializer())

    @staticmethod
    def create_room_serializer():
        enum = SerializerBuilder.create_enum_serializer()
        tile = SerializerBuilder.create_tile_serializer()
        return RoomSerializer(tile, enum)

    @staticmethod
    def create_dungeon_serializer():
        return DungeonSerializer(SerializerBuilder.create_room_serializer())
