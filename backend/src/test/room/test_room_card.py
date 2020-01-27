""" FILE: test_room_card.py
    DESC: Contains tests for the Room Card
"""

import pytest

from backend.src.main.room import room, den
from backend.src.main.room.room_card_exceptions import DuplicateTileError


@pytest.fixture
def _test_room():
    """Fixture for an object of Room Card"""
    return room.AbstractRoomCard("Den")


def test_add_tile(_test_room):
    """Tests the add_tile method of AbstractRoomCard
    """
    current_tile = (5, 10)
    _test_room.add_tile(0, 5, 10)
    assert current_tile in _test_room.hexes


def test_can_have_multiple_empty_tiles(_test_room):
    """This test ensures we can have multiple empty tiles in a Room
    """
    tile_one = (5, 11)
    tile_two = (5, 12)
    _test_room.add_tile(0, 5, 11)
    _test_room.add_tile(0, 5, 12)
    assert tile_one in _test_room.hexes
    assert tile_two in _test_room.hexes


def test_no_duplicate_character_number_in_room_hexes(_test_room):
    """No tile can have same character_number
    """
    _test_room.add_tile(1, 5, 13)
    with pytest.raises(DuplicateTileError):
        # Both tiles have character_number 1
        # this is not valid
        _test_room.add_tile(1, 5, 14)


def test_no_duplicate_coordinates_in_room(_test_room):
    """No duplicate coordinates can be added for a room"""
    _test_room.add_tile(0, 5, 15)
    with pytest.raises(DuplicateTileError):
        _test_room.add_tile(1, 5, 15)


def test_den_can_be_instantiate():
    """A room Den can be instantiated"""
    current_room = den.Den()
    assert current_room.name == "Den"
