import pytest

from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues
)
from backend.src.main.game.room import room, concrete_rooms
from backend.src.main.game.room.concrete_room_cards import den
from backend.src.main.game.room.room_card_exceptions import DuplicateTileError
from backend.src.main.game.tile.tile import Tile


@pytest.fixture
def _test_room():
    return room.AbstractRoomCard("Den")


def test_add_tile(_test_room):
    current_tile = Tile(5, 10, DungeonCardValues.EMPTY)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 10)
    assert current_tile in _test_room.get_tiles()


def test_can_have_multiple_empty_tiles(_test_room):
    tile_one = Tile(5, 11, DungeonCardValues.EMPTY)
    tile_two = Tile(5, 12, DungeonCardValues.EMPTY)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 11)
    _test_room.add_tile(DungeonCardValues.EMPTY, 5, 12)
    assert tile_one in _test_room.get_tiles()
    assert tile_two in _test_room.get_tiles()


def test_cannot_add_second_exit(_test_room):
    _test_room.add_tile(UniqueDungeonCardValues.EXIT_A, 101, 101)
    with pytest.raises(DuplicateTileError):
        _test_room.add_tile(UniqueDungeonCardValues.EXIT_A, 102, 102)


def test_cannot_add_second_entrance(_test_room):
    _test_room.add_tile(UniqueDungeonCardValues.ENTRANCE_A, 103, 103)
    with pytest.raises(DuplicateTileError):
        _test_room.add_tile(UniqueDungeonCardValues.ENTRANCE_A, 104, 104)


def test_no_duplicate_character_number_in_room_tiles(_test_room):
    character_number = NumberedRoomTileValues.TWELVE
    _test_room.add_tile(character_number, 5, 13)
    with pytest.raises(DuplicateTileError):
        # Both tiles have character_number 1
        # this is not valid
        _test_room.add_tile(character_number, 5, 14)


def test_no_duplicate_coordinates_in_room(_test_room):
    _test_room.add_tile(0, 5, 15)
    with pytest.raises(DuplicateTileError):
        _test_room.add_tile(1, 5, 15)


def test_den_can_be_instantiate():
    current_room = den.Den()
    assert current_room.get_name() == "Den"


def test_get_tiles_on_den_returns_list_of_tiles():
    current_room = den.Den()
    expected = current_room.get_tiles()
    assert isinstance(expected, list)


def test_can_instantiate_all_rooms():
    rooms = concrete_rooms.get_all_rooms()
    assert len(rooms) == 20
