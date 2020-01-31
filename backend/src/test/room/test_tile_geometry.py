from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.tile import Tile
from backend.src.main.room.tile_geometry import TileGeometry


def test_recentering_tile_0_0_returns_tile_with_coordinates_0_0():
    x_coordinate = 0
    y_coordinate = 0
    tile_to_be_recentered = Tile(x_coordinate, y_coordinate, None)

    tile_to_recenter_around = Tile(x_coordinate, y_coordinate, None)

    actual = TileGeometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = 0

    assert isinstance(actual, Tile)
    assert expected_x == actual_x
    assert expected_y == actual_y


def test_recentering_tile0_0_around_0_1_has_coordinates_0_minus_1():
    tile_to_be_recentered = Tile(0, 0, None)

    tile_to_recenter_around = Tile(0, 1, None)

    actual = TileGeometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = -1

    assert expected_x == actual_x
    assert expected_y == actual_y


def test_tile_character_attribute_does_not_change_after_being_recentered():
    attribute = DungeonCardValues.MONSTER
    tile_to_be_recentered = Tile(0, 0, attribute)
    tile_to_recenter_around = Tile(0, 1, None)

    actual = TileGeometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    assert actual.get_character_number() == DungeonCardValues.MONSTER


def test_recenters_list_of_tiles_around_a_tile():
    tile_one = Tile(0, 1, None)
    tile_two = Tile(1, 0, None)
    tile_list = [tile_one, tile_two]
    tile_to_be_recentered_around = Tile(-1, 1, None)

    tile_geometry = TileGeometry()
    actual = tile_geometry.recenter_tile_list(tile_list, tile_to_be_recentered_around)
    new_tile_one = actual[0]
    new_tile_two = actual[1]
    expected_tile_one_x = 1
    expected_tile_one_y = 0
    expected_tile_two_x = 2
    expected_tile_two_y = -1

    assert new_tile_one.get_x() == expected_tile_one_x
    assert new_tile_one.get_y() == expected_tile_one_y
    assert new_tile_two.get_x() == expected_tile_two_x
    assert new_tile_two.get_y() == expected_tile_two_y
