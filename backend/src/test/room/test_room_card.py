""" FILE: test_flask.py
    DESC: Contains tests for the application level items
"""

import pytest

from backend.src.main.room import room, den
from backend.src.main.room.room import DuplicateTileError


@pytest.fixture
def test_room():
    return room.AbstractRoomCard("Den")


def test_add_tile(test_room):
    current_tile = (5, 10)
    test_room.add_tile(0, 5, 10)
    assert current_tile in test_room.hexes


def test_can_have_multiple_empty_tiles(test_room):
    tile_one = (5, 11)
    tile_two = (5, 12)
    test_room.add_tile(0, 5, 11)
    test_room.add_tile(0, 5, 12)
    assert tile_one in test_room.hexes
    assert tile_two in test_room.hexes


def test_no_duplicate_character_number_in_room_hexes(test_room):
    test_room.add_tile(1, 5, 13)
    with pytest.raises(DuplicateTileError):
        # Both tiles have character_number 1
        # this is not valid
        test_room.add_tile(1, 5, 14)


def test_no_duplicate_coordinates_in_room(test_room):
    test_room.add_tile(0, 5, 15)
    with pytest.raises(DuplicateTileError):
        test_room.add_tile(1, 5, 15)


def test_den_can_be_instantiate():
    current_room = den.Den()
    assert current_room.name == "Den"
