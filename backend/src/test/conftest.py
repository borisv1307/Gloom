from unittest.mock import Mock

import pytest
from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.game.monster.concrete_monster_cards.cutthroat import Cutthroat
from backend.src.main.game.monster.values import DungeonCardValues
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.game.room.waypoint.waypoint_a import WaypointA
from backend.src.main.game.room.waypoint.waypoint_b import WaypointB
from backend.src.main.game.tile.tile import Tile
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer
from backend.src.main.wrappers.random_wrapper import RandomWrapper


@pytest.fixture(name='waypoint_a')
def create_waypoint_a():
    return WaypointA()


@pytest.fixture(name='waypoint_b')
def create_waypoint_b():
    return WaypointB()


@pytest.fixture(name='dungeon_generator')
def create_dungeon_generator():
    return RandomDungeonGenerator(RandomWrapper())


@pytest.fixture(name='test_room')
def create_test_room():
    return AbstractRoomCard("foo")


@pytest.fixture(name='tile_a')
def create_tile_a():
    return Tile(0, 0, DungeonCardValues.COIN)


@pytest.fixture(name='tile_b')
def create_tile_b():
    return Tile(0, 0, DungeonCardValues.COIN)


@pytest.fixture(name='cutthroat')
def create_cutthroat():
    return Cutthroat()


@pytest.fixture(name='enum_serializer')
def create_enum_serializer():
    enum_serializer = EnumSerializer()
    mock = Mock(return_value='coin')
    enum_serializer.serialize = mock
    return enum_serializer


@pytest.fixture(name='tile_serializer')
def create_tile_serializer():
    tile_serializer = TileSerializer(None)
    mock = Mock(return_value={
        'x': 0,
        'y': 0,
        'z': 0,
        'value': 'coin'}
    )
    tile_serializer.serialize = mock
    return tile_serializer


@pytest.fixture(name='room_serializer')
def create_room_serializer():
    serializer = RoomSerializer(None)
    mock = Mock(return_value='mocked_room')
    serializer.serialize = mock
    return serializer
