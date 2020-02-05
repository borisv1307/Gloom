# pylint: disable=duplicate-code
import pytest

from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.concrete_room_cards.burrow import Burrow
from backend.src.main.room.concrete_room_cards.hovel import Hovel
from backend.src.main.room.concrete_room_cards.trail import Trail
from backend.src.main.room.waypoint_pojo import WaypointPOJO
from backend.src.main.tile.tile import Tile


@pytest.fixture(name='waypoint_pojo_a')
def create_instance_of_waypoint_pojo_a():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_A, DungeonCardValues.EXIT_B)


@pytest.fixture(name='waypoint_pojo_b')
def create_instance_of_waypoint_pojo_b():
    return WaypointPOJO(DungeonCardValues.ENTRANCE_B, DungeonCardValues.EXIT_B)


def test_has_entrance_b_on_hovel_returns_true(waypoint_pojo_b):
    room = Hovel()
    actual = waypoint_pojo_b.has_entrance(room)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_trail_returns_true(waypoint_pojo_a):
    room = Trail()
    actual = waypoint_pojo_a.has_entrance(room)
    expected = True
    assert actual == expected


def test_is_entrance_b_on_tile_returns_true(waypoint_pojo_b):
    tile = Tile(0, 0, DungeonCardValues.ENTRANCE_B)
    actual = waypoint_pojo_b.is_entrance(tile)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_burrow_returns_false(waypoint_pojo_a):
    room = Burrow()
    actual = waypoint_pojo_a.has_entrance(room)
    expected = False
    assert actual == expected


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


def test_remove_tile_by_type(waypoint_pojo_b):
    room = Burrow()
    new_room = waypoint_pojo_b.remove_entrance(room)

    assert not waypoint_pojo_b.has_entrance(new_room)
    assert new_room.get_name() == room.get_name()
