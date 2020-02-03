from unittest.mock import MagicMock, call

import pytest
from backend.src.main.dungeon.dungeon import RandomDungeonGenerator
from backend.src.main.game.random_monster_card import AbstractMonsterCard
from backend.src.main.room.constructed_room import ConstructedRoom
from backend.src.main.room.room import AbstractRoomCard
from backend.src.main.tile.tile_geometry import TileGeometry
from backend.src.main.wrappers.random_wrapper import RandomWrapper


@pytest.fixture(name='dungeon_generator')
def create_dungeon_generator():
    return RandomDungeonGenerator(RandomWrapper(), TileGeometry())


def test_dungeon_generator_has_20_monster_cards(dungeon_generator):
    assert len(dungeon_generator.monster_cards) == 20
    for item in dungeon_generator.monster_cards:
        assert isinstance(item, AbstractMonsterCard)


def test_dungeon_generator_has_20_room_cards(dungeon_generator):
    assert len(dungeon_generator.room_cards) == 20
    for item in dungeon_generator.room_cards:
        assert isinstance(item, AbstractRoomCard)


def test_dungeon_generator_has_no_rooms_initially(dungeon_generator):
    assert not dungeon_generator.constructed_rooms


def test_select_first_room_reduces_deck_sizes_by_one(dungeon_generator):
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.room_cards) == 19
    assert len(dungeon_generator.monster_cards) == 19


def test_select_first_room_adds_constructed_room(dungeon_generator):
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.constructed_rooms) == 1
    assert isinstance(dungeon_generator.constructed_rooms[0], ConstructedRoom)


def test_select_first_room_calls_random_choice_twice(dungeon_generator):
    # Note, we depend on the order of calls
    mock = MagicMock()
    mock.side_effect = [0, 0]

    random_wrapper = RandomWrapper()
    random_wrapper.randrange = mock

    expected_room_argument = 20
    expected_monster_argument = 20
    expected_calls = [call(expected_room_argument), call(expected_monster_argument)]

    dungeon_generator.random_wrapper = random_wrapper
    dungeon_generator.select_first_room()

    mock.assert_has_calls(expected_calls)
    assert mock.call_count == 2


def test_select_room_waypoint_a_checks_if_drawn_card_has_entrance_a(dungeon_generator):
    mock = MagicMock()
    dungeon_generator.tile_geometry.has_entrance_a = mock
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.constructed_rooms) == 1
    dungeon_generator.select_room_waypoint_a()
    assert mock.call_count >= 1


def test_select_room_waypoint_a_calls_overlay_room(dungeon_generator):
    mock = MagicMock()
    dungeon_generator.tile_geometry.overlay_room_a_on_room_b_by_waypoint_a = mock

    dungeon_generator.select_first_room()
    assert len(dungeon_generator.constructed_rooms) == 1
    dungeon_generator.select_room_waypoint_a()

    assert mock.call_count == 1


def test_select_room_waypoint_a_causes_two_constructed_rooms_to_be_in_list(dungeon_generator):
    dungeon_generator.select_first_room()
    dungeon_generator.select_room_waypoint_a()
    assert len(dungeon_generator.constructed_rooms) == 2


def test_select_room_waypoint_a_causes_monster_cards_to_be_length_18(dungeon_generator):
    dungeon_generator.select_first_room()
    assert len(dungeon_generator.room_cards) == 19
    assert len(dungeon_generator.monster_cards) == 19
    dungeon_generator.select_room_waypoint_a()
    assert len(dungeon_generator.room_cards) == 18
    assert len(dungeon_generator.monster_cards) == 18
