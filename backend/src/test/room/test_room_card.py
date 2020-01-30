
import pytest

from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room import room
from backend.src.main.room.concrete_room_cards import den
from backend.src.main.room.room_card_exceptions import DuplicateTileError


@pytest.fixture
def _test_room():
    return room.AbstractRoomCard("Den")


def test_add_tile(_test_room):
    current_tile = (5, 10)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 10)
    assert current_tile in _test_room.tiles


def test_can_have_multiple_empty_tiles(_test_room):
    tile_one = (5, 11)
    tile_two = (5, 12)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 11)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 12)
    assert tile_one in _test_room.tiles
    assert tile_two in _test_room.tiles


def test_no_duplicate_character_number_in_room_tiles(_test_room):
    _test_room.add_tile(1, 5, 13)
    with pytest.raises(DuplicateTileError):
        # Both tiles have character_number 1
        # this is not valid
        _test_room.add_tile(1, 5, 14)


def test_no_duplicate_coordinates_in_room(_test_room):
    _test_room.add_tile(0, 5, 15)
    with pytest.raises(DuplicateTileError):
        _test_room.add_tile(1, 5, 15)


def test_den_can_be_instantiate():
    current_room = den.Den()
    assert current_room.name == "Den"


def test_get_tiles_on_den_returns_list_of_tiles():
    current_room = den.Den()
    expected = current_room.get_tiles()
    assert isinstance(expected, list)
