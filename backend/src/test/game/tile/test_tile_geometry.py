# pylint: disable=line-too-long,duplicate-code
import itertools

import pytest

from backend.src.main.game.monster.values import UniqueDungeonCardValues
from backend.src.main.game.room.concrete_room_cards.burrow import Burrow
from backend.src.main.game.room.concrete_room_cards.tunnel import Tunnel
from backend.src.main.game.room.waypoint.waypoint_b_pojo import WaypointB
from backend.src.main.game.tile.tile import Tile
from backend.src.main.game.tile.tile_geometry import TileGeometry


@pytest.fixture(name='waypoint_pojo_b', scope='module')
def create_instance_of_waypoint_pojo_b():
    return WaypointB()


def test_get_exit_b_on_burrow(waypoint_pojo_b):
    room = Burrow()
    actual = waypoint_pojo_b.get_exit(room)
    assert actual == Tile(-1, -4, UniqueDungeonCardValues.EXIT_B)


def test_center_tunnel_on_top_of_burrow_on_waypoint_a_causes_waypoints_to_match_coordinates(waypoint_pojo_b):
    room_one = Burrow()
    room_two = Tunnel()

    moved_room = TileGeometry.center_room_a_on_room_b_by_waypoint(room_one, room_two, waypoint_pojo_b)

    exit_waypoint = waypoint_pojo_b.get_exit(room_one)
    entry_waypoint = waypoint_pojo_b.get_entrance(moved_room)

    assert exit_waypoint.get_x() == entry_waypoint.get_x()
    assert exit_waypoint.get_y() == entry_waypoint.get_y()


def test_do_rooms_overlap_with_non_overlapping_tiles_returns_false():
    room_one = Burrow()
    room_two = Burrow()
    room_one.set_tiles([Tile(0, 0, None), Tile(1, 1, None)])
    room_two.set_tiles([Tile(2, 2, None), Tile(3, 3, None)])

    assert not TileGeometry.do_rooms_overlap(room_one, room_two)


def test_do_rooms_overlap_with_overlapping_tiles_returns_true():
    room_one = Burrow()
    room_two = Burrow()
    room_one.set_tiles([Tile(0, 0, None), Tile(1, 1, None)])
    room_two.set_tiles([Tile(1, 1, None), Tile(3, 3, None)])

    assert TileGeometry.do_rooms_overlap(room_one, room_two)


def test_overlay_room_b_on_room_a_returns_room_b_after_rotation(waypoint_pojo_b):
    room_one = Burrow()
    room_two = Tunnel()

    moved_room = TileGeometry.overlay_room_a_on_room_b(room_one, room_two, waypoint_pojo_b)

    assert moved_room is not None


def test_rotation_algorithm_fails_on_arbitrary_edge_case(waypoint_pojo_b):
    room_one = Burrow()
    room_two = Tunnel()

    tile_coordinate_list = list(itertools.permutations([-1, 0, 1], 2))
    tiles_surrounding_origin = [Tile(coord[0], coord[1], None) for coord in tile_coordinate_list]
    origin_tile = Tile(0, 0, UniqueDungeonCardValues.ENTRANCE_B)
    tiles_surrounding_origin.append(origin_tile)

    room_two.set_tiles(tiles_surrounding_origin)

    with pytest.raises(AssertionError, match="TileGeometry algorithm failed"):
        TileGeometry.overlay_room_a_on_room_b(room_one, room_two, waypoint_pojo_b)
