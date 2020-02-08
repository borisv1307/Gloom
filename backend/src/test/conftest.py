import pytest
from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.game.monster.concrete_monster_cards.cutthroat import Cutthroat
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard
from backend.src.main.game.room.waypoint.waypoint_a import WaypointA
from backend.src.main.game.room.waypoint.waypoint_b import WaypointB
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
    return AbstractRoomCard("Den")


@pytest.fixture(name='cutthroat')
def create_cutthroat():
    return Cutthroat()
