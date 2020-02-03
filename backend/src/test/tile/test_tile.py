from backend.src.main.game.values import NumberedRoomTileValues
from backend.src.main.tile.tile import Tile


def test_tile_with_same_attributes_are_equal():
    tile_one = Tile(0, 1, None)
    tile_two = Tile(0, 1, None)
    assert tile_one == tile_two


def test_tile_and_dog_object_are_not_equal():
    tile = Tile(0, 0, None)

    class Dog:  # pylint: disable=too-few-public-methods
        pass

    assert Dog() != tile


def test_tiles_with_different_attributes_are_not_equal():
    tile_one = Tile(1, 2, 3)
    tile_two = Tile(4, 5, 6)
    assert tile_one != tile_two


def test_get_z_tile_0_0_returns_0():
    tile = Tile(0, 0, None)
    actual = tile.get_z()
    assert actual == 0


def test_get_z_tile_1_1_returns_minus_2():
    tile = Tile(1, 1, None)
    actual = tile.get_z()
    assert actual == -2


def test_rotate_tile_0_0_returns_0_0():
    tile = Tile(0, 0, None)
    actual = tile.rotate()

    assert actual == tile


def test_rotate_tile_returns_tile_with_same_character_number():
    attribute = NumberedRoomTileValues.ONE
    tile = Tile(0, 0, attribute)
    actual = tile.rotate()

    assert actual.get_character_number() == attribute


def test_rotate_tile_minus_2_1_returns_tile_minus_1_2():
    tile = Tile(-2, 1, None)
    actual = tile.rotate()

    assert actual == Tile(-1, 2, None)


def test_rotate_tile_1_0_returns_tile_0_minus_1():
    tile = Tile(1, 0, None)
    actual = tile.rotate()

    assert actual == Tile(1, -1, None)


def test_hash():
    actual = hash(Tile(0, 0, NumberedRoomTileValues.ONE))
    expected = hash((0, 0, NumberedRoomTileValues.ONE))
    assert actual == expected


def test_repr():
    tile = Tile(0, 0, NumberedRoomTileValues.ONE)
    expected = '{} {} {}'.format(0, 0, NumberedRoomTileValues.ONE)
    assert tile.__repr__() == expected
