# pylint: disable=line-too-long
import pytest
from backend.src.main.game.monster.values import DungeonCardValues
from backend.src.main.serializer.abstract_serializer import AbstractSerializer
from backend.src.main.serializer.dungeon_serializer import DungeonSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.serializer_builder import SerializerBuilder
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


def test_serialize_test_room_with_mocked_tile_serializer(test_constructed_room, tile_serializer, enum_serializer):
    serializer = RoomSerializer(tile_serializer, enum_serializer)
    actual = serializer.serialize(test_constructed_room)
    expected = {
        'name': 'foo',
        'tiles': {},
        'monsterCardName': 'Frigid',
        'indicators': ['coin']
    }

    assert actual == expected


def test_serialize_test_room_with_tiles(test_constructed_room, tile_serializer, enum_serializer, tile_a, tile_b):
    serializer = RoomSerializer(tile_serializer, enum_serializer)
    test_constructed_room.set_tiles([tile_a, tile_b])
    actual = serializer.serialize(test_constructed_room)
    mocked_tile_value = tile_serializer.serialize.return_value

    expected = {
        'name': 'foo',
        'indicators': ['coin'],
        'monsterCardName': 'Frigid',
        'tiles': {
            0: mocked_tile_value,
            1: mocked_tile_value
        }
    }

    assert actual == expected


def test_serialize_room_with_trap_indicators(tile_serializer, enum_serializer, test_constructed_room):
    serializer = RoomSerializer(tile_serializer, enum_serializer)
    mocked_enum_value = enum_serializer.serialize.return_value
    # test_constructed_room = ConstructedRoom(test_room, Frigid())

    actual = serializer.serialize(test_constructed_room)

    expected = {
        'name': 'foo',
        'indicators': [mocked_enum_value],
        'monsterCardName': 'Frigid',
        'tiles': {}
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


def test_serialize_child_classes_raise_unimplement_error_when_method_not_implemented():
    class FooSerializer(AbstractSerializer):  # pylint: disable=too-few-public-methods,abstract-method
        pass

    with pytest.raises(NotImplementedError):
        FooSerializer().serialize(None)

    with pytest.raises(NotImplementedError):
        FooSerializer().create()


def test_create_dungeon_serializer():
    actual = DungeonSerializer.create()
    util_is_dungeon_serializer_concrete(actual)


def test_create_dungeon_serializer_using_builder():
    actual = SerializerBuilder.create_dungeon_serializer()
    util_is_dungeon_serializer_concrete(actual)


def util_is_dungeon_serializer_concrete(concrete_dungeon_serializer):
    assert isinstance(concrete_dungeon_serializer, DungeonSerializer)

    room_serializer = concrete_dungeon_serializer.room_serializer
    assert isinstance(room_serializer, RoomSerializer)

    enum_serializer_in_room = room_serializer.enum_serializer
    tile_serializer = room_serializer.tile_serializer
    assert isinstance(enum_serializer_in_room, EnumSerializer)
    assert isinstance(tile_serializer, TileSerializer)

    enum_serializer_in_tile = tile_serializer.enum_serializer
    assert isinstance(enum_serializer_in_tile, EnumSerializer)
