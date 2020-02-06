import pytest
from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.concrete_room_cards.burrow import Burrow
from backend.src.main.room.concrete_room_cards.hovel import Hovel
from backend.src.main.room.concrete_room_cards.tunnel import Tunnel
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO
from backend.src.main.tile.center_tile import CenterTile
from backend.src.main.tile.tile import Tile


@pytest.fixture(name='waypoint_pojo_a', scope='function')
def create_instance_of_waypoint_pojo_a():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_A, DungeonCardValues.EXIT_B)


@pytest.fixture(name='waypoint_pojo_b', scope='function')
def create_instance_of_waypoint_pojo_b():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_B, DungeonCardValues.EXIT_B)


def test_recentering_tile_0_0_returns_tile_with_coordinates_0_0():
    x_coordinate = 0
    y_coordinate = 0
    tile_to_be_recentered = Tile(x_coordinate, y_coordinate, None)

    tile_to_recenter_around = Tile(x_coordinate, y_coordinate, None)

    actual = CenterTile.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

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

    actual = CenterTile.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

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

    actual = CenterTile.recenter_tile(tile_to_be_recentered, tile_to_recenter_around)

    assert actual.get_character_number() == DungeonCardValues.MONSTER


def test_recenters_list_of_tiles_around_a_tile():
    tile_one = Tile(0, 1, None)
    tile_two = Tile(1, 0, None)
    tile_list = [tile_one, tile_two]
    tile_to_be_recentered_around = Tile(-1, 1, None)

    actual = CenterTile.recenter_tile_list(tile_list, tile_to_be_recentered_around)
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


def test_recenter_room_on_tile(waypoint_pojo_b):
    room = Burrow()
    actual = CenterTile.center_on_entrance(room, waypoint_pojo_b)
    assert waypoint_pojo_b.get_entrance(actual) == Tile(0, 0, DungeonCardValues.ENTRANCE_B)


def test_center_on_entrance_b_causes_entrance_to_have_coordinate_0_0(waypoint_pojo_b):
    room = Tunnel()
    new_room = CenterTile.center_on_entrance(room, waypoint_pojo_b)
    actual = waypoint_pojo_b.get_entrance(new_room)

    assert actual == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert actual.get_x() == 0
    assert actual.get_y() == 0


def test_center_hovel_on_entrance_a(waypoint_pojo_a):
    room = Hovel()
    assert waypoint_pojo_a.has_entrance(room)
    actual = CenterTile.center_on_entrance(room, waypoint_pojo_a)
    tile = waypoint_pojo_a.get_entrance(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_A)
    assert isinstance(actual, Hovel)


def test_center_room_on_tile_type_that_room_does_not_have_raises_value_error(waypoint_pojo_a):
    room = Burrow()
    assert not waypoint_pojo_a.has_entrance(room)
    with pytest.raises(ValueError):
        CenterTile.center_on_entrance(room, waypoint_pojo_a)


def test_center_burrow_on_entrance_b(waypoint_pojo_b):
    room = Burrow()
    assert waypoint_pojo_b.has_entrance(room)
    actual = CenterTile.center_on_entrance(room, waypoint_pojo_b)
    tile = waypoint_pojo_b.get_entrance(actual)
    assert tile == Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    assert isinstance(actual, Burrow)
