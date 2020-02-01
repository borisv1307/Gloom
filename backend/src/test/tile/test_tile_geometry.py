import pytest
from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.concrete_room_cards.burrow import Burrow
from backend.src.main.room.concrete_room_cards.hovel import Hovel
from backend.src.main.room.concrete_room_cards.trail import Trail
from backend.src.main.room.concrete_room_cards.tunnel import Tunnel
from backend.src.main.tile.tile import Tile
from backend.src.main.tile.tile_geometry import TileGeometry


@pytest.fixture
def tile_geometry():
    return TileGeometry()


def test_recentering_tile_0_0_returns_tile_with_coordinates_0_0(tile_geometry):
    x_coordinate = 0
    y_coordinate = 0
    tile_to_be_recentered = Tile(x_coordinate, y_coordinate, None)

    tile_to_recenter_around = Tile(x_coordinate, y_coordinate, None)

    actual = tile_geometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = 0

    assert isinstance(actual, Tile)
    assert expected_x == actual_x
    assert expected_y == actual_y


def test_recentering_tile0_0_around_0_1_has_coordinates_0_minus_1(tile_geometry):
    tile_to_be_recentered = Tile(0, 0, None)

    tile_to_recenter_around = Tile(0, 1, None)

    actual = tile_geometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = -1

    assert expected_x == actual_x
    assert expected_y == actual_y


def test_tile_character_attribute_does_not_change_after_being_recentered(tile_geometry):
    attribute = DungeonCardValues.MONSTER
    tile_to_be_recentered = Tile(0, 0, attribute)
    tile_to_recenter_around = Tile(0, 1, None)

    actual = tile_geometry.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    assert actual.get_character_number() == DungeonCardValues.MONSTER


def test_recenters_list_of_tiles_around_a_tile(tile_geometry):
    tile_one = Tile(0, 1, None)
    tile_two = Tile(1, 0, None)
    tile_list = [tile_one, tile_two]
    tile_to_be_recentered_around = Tile(-1, 1, None)

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


def test_is_entrance_a_on_tile_returns_true(tile_geometry):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    actual = tile_geometry.is_entrance_a(tile)
    expected = True
    assert actual == expected


def test_is_entrance_a_on_non_entrance_return_false(tile_geometry):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    actual = tile_geometry.is_entrance_a(tile)
    expected = False
    assert actual == expected


def test_is_entrance_b_on_tile_returns_true(tile_geometry):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    actual = tile_geometry.is_entrance_b(tile)
    expected = True
    assert actual == expected


def test_is_entrance_b_on_non_entrance_return_false(tile_geometry):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    actual = tile_geometry.is_entrance_b(tile)
    expected = False
    assert actual == expected


def test_has_entrance_b_on_trail_returns_false(tile_geometry):
    room = Trail()
    actual = tile_geometry.has_entrance_b(room)
    expected = False
    assert actual == expected


def test_has_entrance_b_on_hovel_returns_true(tile_geometry):
    room = Hovel()
    actual = tile_geometry.has_entrance_b(room)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_trail_returns_true(tile_geometry):
    room = Trail()
    actual = tile_geometry.has_entrance_a(room)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_burrow_returns_false(tile_geometry):
    room = Burrow()
    actual = tile_geometry.has_entrance_a(room)
    expected = False
    assert actual == expected


def test_get_entrance_a_on_trail_returns_entrance_tile(tile_geometry):
    room = Trail()
    actual = tile_geometry.get_entrance_a(room)
    expected = Tile(-2, 5, DungeonCardValues.ENTRANCE_A)
    assert actual == expected


def test_get_entrance_b_on_hovel_returns_entrance_tile(tile_geometry):
    room = Hovel()
    actual = tile_geometry.get_entrance_b(room)
    expected = Tile(0, 3, DungeonCardValues.ENTRANCE_B)
    assert actual == expected


def test_center_hovel_on_entrance_a(tile_geometry):
    room = Hovel()
    assert tile_geometry.has_entrance_a(room)
    actual = tile_geometry.center_on_entrance_a(room)
    tile = tile_geometry.get_entrance_a(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    assert isinstance(actual, Hovel)


def test_center_burrow_on_entrance_b(tile_geometry):
    room = Burrow()
    assert tile_geometry.has_entrance_b(room)
    actual = tile_geometry.center_on_entrance_b(room)
    tile = tile_geometry.get_entrance_b(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert isinstance(actual, Burrow)


def test_center_room_on_tile_type_that_room_does_not_have_raises_value_error(tile_geometry):
    room = Burrow()
    assert not tile_geometry.has_entrance_a(room)
    with pytest.raises(ValueError):
        tile_geometry.center_room_on_tile_type(room, DungeonCardValues.ENTRANCE_A)


def test_get_exit_b_on_burrow(tile_geometry):
    room = Burrow()
    actual = tile_geometry.get_exit_b(room)
    assert actual == Tile(-1, -4, DungeonCardValues.EXIT_B)


def test_recenter_room_on_tile(tile_geometry):
    room = Burrow()
    tile = tile_geometry.get_entrance_b(room)
    actual = tile_geometry.center_room_on_tile(room, tile)

    assert tile_geometry.get_entrance_b(actual) == Tile(0, 0, DungeonCardValues.ENTRANCE_B)


def test_center_on_entrance_b_causes_entrance_to_have_coordinate_0_0(tile_geometry):
    room = Tunnel()
    new_room = tile_geometry.center_on_entrance_b(room)
    actual = tile_geometry.get_entrance_b(new_room)

    assert actual == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert actual.get_x() == 0
    assert actual.get_y() == 0

# def test_center_tunnel_on_top_of_burrow_on_waypoint_a_causes_waypoint_to_match_coordinates(tile_geometry):
#     room_one = Burrow()
#     room_two = Tunnel()
#
#     moved_room = tile_geometry.center_room_a_on_room_b_by_waypoint_b(room_one, room_two)
#
#     exit_waypoint = tile_geometry.get_entrance_b(room_one)
#     entry_waypoint = tile_geometry.get_entrance_b(moved_room)
#
#     assert exit_waypoint.get_x() == entry_waypoint.get_x()
#     assert exit_waypoint.get_y() == entry_waypoint.get_y()
#
