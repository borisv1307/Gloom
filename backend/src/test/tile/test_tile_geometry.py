# pylint: disable=line-too-long,duplicate-code
import itertools

import pytest

from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.concrete_room_cards.burrow import Burrow
from backend.src.main.room.concrete_room_cards.hovel import Hovel
from backend.src.main.room.concrete_room_cards.trail import Trail
from backend.src.main.room.concrete_room_cards.tunnel import Tunnel
from backend.src.main.room.waypoint_pojo import WaypointPOJO
from backend.src.main.tile.tile import Tile
from backend.src.main.tile.tile_geometry import WaypointATileGeometry, WaypointBTileGeometry


@pytest.fixture(name='tile_geometry_a')
def create_instance_of_tile_geometry_a():
    return WaypointATileGeometry()


@pytest.fixture(name='tile_geometry_b')
def create_instance_of_tile_geometry_b():
    return WaypointBTileGeometry()


@pytest.fixture(name='waypoint_pojo_a')
def create_instance_of_waypoint_pojo_a():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_A, DungeonCardValues.EXIT_B)


@pytest.fixture(name='waypoint_pojo_b')
def create_instance_of_waypoint_pojo_b():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_B, DungeonCardValues.EXIT_B)


def test_recentering_tile_0_0_returns_tile_with_coordinates_0_0(tile_geometry_a):
    x_coordinate = 0
    y_coordinate = 0
    tile_to_be_recentered = Tile(x_coordinate, y_coordinate, None)

    tile_to_recenter_around = Tile(x_coordinate, y_coordinate, None)

    actual = tile_geometry_a.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = 0

    assert isinstance(actual, Tile)
    assert expected_x == actual_x
    assert expected_y == actual_y


def test_recentering_tile0_0_around_0_1_has_coordinates_0_minus_1(tile_geometry_a):
    tile_to_be_recentered = Tile(0, 0, None)

    tile_to_recenter_around = Tile(0, 1, None)

    actual = tile_geometry_a.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    actual_x = actual.get_x()
    actual_y = actual.get_y()

    expected_x = 0
    expected_y = -1

    assert expected_x == actual_x
    assert expected_y == actual_y


def test_tile_character_attribute_does_not_change_after_being_recentered(tile_geometry_a):
    attribute = DungeonCardValues.MONSTER
    tile_to_be_recentered = Tile(0, 0, attribute)
    tile_to_recenter_around = Tile(0, 1, None)

    actual = tile_geometry_a.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    assert actual.get_character_number() == DungeonCardValues.MONSTER


def test_recenters_list_of_tiles_around_a_tile(tile_geometry_a):
    tile_one = Tile(0, 1, None)
    tile_two = Tile(1, 0, None)
    tile_list = [tile_one, tile_two]
    tile_to_be_recentered_around = Tile(-1, 1, None)

    actual = tile_geometry_a.recenter_tile_list(tile_list, tile_to_be_recentered_around)
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


def test_is_entrance_a_on_tile_returns_true(waypoint_pojo_a):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    actual = waypoint_pojo_a.is_entrance(tile)
    expected = True
    assert actual == expected


def test_is_entrance_a_on_non_entrance_return_false(waypoint_pojo_a):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    actual = waypoint_pojo_a.is_entrance(tile)
    expected = False
    assert actual == expected


def test_is_entrance_b_on_non_entrance_return_false(waypoint_pojo_b):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    actual = waypoint_pojo_b.is_entrance(tile)
    expected = False
    assert actual == expected


def test_has_entrance_b_on_trail_returns_false(waypoint_pojo_b):
    room = Trail()
    actual = waypoint_pojo_b.has_entrance(room)
    expected = False
    assert actual == expected


def test_get_entrance_a_on_trail_returns_entrance_tile(waypoint_pojo_a):
    room = Trail()
    actual = waypoint_pojo_a.get_entrance(room)
    expected = Tile(-2, 5, DungeonCardValues.ENTRANCE_A)
    assert actual == expected


def test_get_entrance_b_on_hovel_returns_entrance_tile(waypoint_pojo_b):
    room = Hovel()
    actual = waypoint_pojo_b.get_entrance(room)
    expected = Tile(0, 3, DungeonCardValues.ENTRANCE_B)
    assert actual == expected


def test_center_hovel_on_entrance_a(tile_geometry_a, waypoint_pojo_a):
    room = Hovel()
    assert waypoint_pojo_a.has_entrance(room)
    actual = tile_geometry_a.center_on_entrance(room)
    tile = waypoint_pojo_a.get_entrance(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    assert isinstance(actual, Hovel)


def test_center_burrow_on_entrance_b(tile_geometry_b, waypoint_pojo_b):
    room = Burrow()
    assert waypoint_pojo_b.has_entrance(room)
    actual = tile_geometry_b.center_on_entrance(room)
    tile = waypoint_pojo_b.get_entrance(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert isinstance(actual, Burrow)


def test_center_room_on_tile_type_that_room_does_not_have_raises_value_error(tile_geometry_a, waypoint_pojo_a):
    room = Burrow()
    assert not waypoint_pojo_a.has_entrance(room)
    with pytest.raises(ValueError):
        tile_geometry_a.center_on_entrance(room)


def test_get_exit_b_on_burrow(waypoint_pojo_b):
    room = Burrow()
    actual = waypoint_pojo_b.get_exit(room)
    assert actual == Tile(-1, -4, DungeonCardValues.EXIT_B)


def test_recenter_room_on_tile(tile_geometry_b, waypoint_pojo_b):
    room = Burrow()
    actual = tile_geometry_b.center_on_entrance(room)
    assert waypoint_pojo_b.get_entrance(actual) == Tile(0, 0, DungeonCardValues.ENTRANCE_B)


def test_center_on_entrance_b_causes_entrance_to_have_coordinate_0_0(tile_geometry_b, waypoint_pojo_b):
    room = Tunnel()
    new_room = tile_geometry_b.center_on_entrance(room)
    actual = waypoint_pojo_b.get_entrance(new_room)

    assert actual == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert actual.get_x() == 0
    assert actual.get_y() == 0


def test_shift_tile_0_0_to_1_2_returns_1_2(tile_geometry_a):
    tile_to_move = Tile(0, 0, None)
    tile_to_shift_to = Tile(1, 2, None)
    actual = tile_geometry_a.shift_tile(tile_to_move, tile_to_shift_to)
    assert actual == tile_to_shift_to


def test_shift_tile_list_0_0_and_0_1_to_1_0_returns_1_0_and_1_1(tile_geometry_a):
    tiles_to_move = [Tile(0, 0, None), Tile(0, 1, None)]
    tile_to_shift_to = Tile(1, 0, None)

    actual = tile_geometry_a.shift_tile_list(tiles_to_move, tile_to_shift_to)

    expected = [Tile(1, 0, None), Tile(1, 1, None)]
    assert actual == expected


def test_center_tunnel_on_top_of_burrow_on_waypoint_a_causes_waypoints_to_match_coordinates(tile_geometry_b,
                                                                                            waypoint_pojo_b):
    room_one = Burrow()
    room_two = Tunnel()

    moved_room = tile_geometry_b.center_room_a_on_room_b_by_waypoint(room_one, room_two)

    exit_waypoint = waypoint_pojo_b.get_exit(room_one)
    entry_waypoint = waypoint_pojo_b.get_entrance(moved_room)

    assert exit_waypoint.get_x() == entry_waypoint.get_x()
    assert exit_waypoint.get_y() == entry_waypoint.get_y()


def test_do_rooms_overlap_with_non_overlapping_tiles_returns_false(tile_geometry_a):
    room_one = Burrow()
    room_two = Burrow()
    room_one.set_tiles([Tile(0, 0, None), Tile(1, 1, None)])
    room_two.set_tiles([Tile(2, 2, None), Tile(3, 3, None)])

    assert not tile_geometry_a.do_rooms_overlap(room_one, room_two)


def test_do_rooms_overlap_with_overlapping_tiles_returns_true(tile_geometry_a):
    room_one = Burrow()
    room_two = Burrow()
    room_one.set_tiles([Tile(0, 0, None), Tile(1, 1, None)])
    room_two.set_tiles([Tile(1, 1, None), Tile(3, 3, None)])

    assert tile_geometry_a.do_rooms_overlap(room_one, room_two)


def test_remove_tile_by_type(tile_geometry_b, waypoint_pojo_b):
    room = Burrow()
    new_room = tile_geometry_b.remove_entrance(room)

    assert not waypoint_pojo_b.has_entrance(new_room)
    assert new_room.get_name() == room.get_name()


def test_overlay_room_b_on_room_a_returns_room_b_after_rotation(tile_geometry_b):
    room_one = Burrow()
    room_two = Tunnel()

    moved_room = tile_geometry_b.overlay_room_a_on_room_b(room_one, room_two)

    assert moved_room is not None


def test_rotation_algorithm_fails_on_arbitrary_edge_case(tile_geometry_b):
    room_one = Burrow()
    room_two = Tunnel()

    tile_coordinate_list = list(itertools.permutations([-1, 0, 1], 2))
    tiles_surrounding_origin = [Tile(coord[0], coord[1], None) for coord in tile_coordinate_list]
    origin_tile = Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    tiles_surrounding_origin.append(origin_tile)

    room_two.set_tiles(tiles_surrounding_origin)

    with pytest.raises(AssertionError, match="TileGeometry algorithm failed"):
        tile_geometry_b.overlay_room_a_on_room_b(room_one, room_two)
