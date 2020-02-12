from backend.src.main.game.monster.values import DungeonCardValues
from backend.src.main.serializer.dungeon_serializer import DungeonSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer


def test_enum_serializer_on_trap_returns_trap_value():
    serializer = EnumSerializer()

    input_enum = DungeonCardValues.COIN

    actual = serializer.serialize(input_enum)
    expected = DungeonCardValues.COIN.value

    assert actual == expected


def test_serialize_tile(tile_a, enum_serializer):
    serializer = TileSerializer(enum_serializer)

    actual = serializer.serialize(tile_a)
    expected = {'x': 0, 'y': 0, 'z': 0, 'value': 'coin'}
    assert actual == expected


def test_serialize_test_room_with_mocked_tile_serializer(test_room, tile_serializer):
    serializer = RoomSerializer(tile_serializer)
    actual = serializer.serialize(test_room)
    expected = {
        'name': 'foo',
        'tiles': {}
    }

    assert actual == expected


def test_serialize_test_room_with_tiles(test_room, tile_serializer, tile_a, tile_b):
    serializer = RoomSerializer(tile_serializer)
    test_room.set_tiles([tile_a, tile_b])
    actual = serializer.serialize(test_room)
    mocked_tile_value = {
        'x': 0,
        'y': 0,
        'z': 0,
        'value': 'coin'}

    expected = {
        'name': 'foo',
        'tiles': {
            0: mocked_tile_value,
            1: mocked_tile_value
        }
    }

    assert actual == expected


def test_serialize_dungeon_with_no_room(room_serializer, dungeon_generator):
    serializer = DungeonSerializer(room_serializer)
    actual = serializer.serialize(dungeon_generator)
    expected = {}
    assert actual == expected


def test_serialize_dungeon_with_one_room(room_serializer, dungeon_generator):
    serializer = DungeonSerializer(room_serializer)
    dungeon_generator.select_first_room()
    actual = serializer.serialize(dungeon_generator)
    expected = {
        0: 'mocked_room'
    }
    assert actual == expected
