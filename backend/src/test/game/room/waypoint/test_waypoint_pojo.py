from backend.src.main.game.monster.values import UniqueDungeonCardValues
from backend.src.main.game.room.concrete_room_cards.burrow import Burrow
from backend.src.main.game.room.concrete_room_cards.den import Den
from backend.src.main.game.room.concrete_room_cards.hovel import Hovel
from backend.src.main.game.room.concrete_room_cards.trail import Trail
from backend.src.main.game.tile.tile import Tile


def test_has_entrance_b_on_hovel_returns_true(waypoint_b):
    room = Hovel()
    actual = waypoint_b.has_entrance(room)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_trail_returns_true(waypoint_a):
    room = Trail()
    actual = waypoint_a.has_entrance(room)
    expected = True
    assert actual == expected


def test_is_entrance_b_on_tile_returns_true(waypoint_b):
    tile = Tile(0, 0, UniqueDungeonCardValues.ENTRANCE_B)
    actual = waypoint_b.is_entrance(tile)
    expected = True
    assert actual == expected


def test_has_entrance_a_on_burrow_returns_false(waypoint_a):
    room = Burrow()
    actual = waypoint_a.has_entrance(room)
    expected = False
    assert actual == expected


def test_is_entrance_a_on_tile_returns_true(waypoint_a):
    tile = Tile(0, 0, UniqueDungeonCardValues.ENTRANCE_A)
    actual = waypoint_a.is_entrance(tile)
    expected = True
    assert actual == expected


def test_is_entrance_a_on_non_entrance_return_false(waypoint_a):
    tile = Tile(0, 0, UniqueDungeonCardValues.ENTRANCE_B)
    actual = waypoint_a.is_entrance(tile)
    expected = False
    assert actual == expected


def test_is_entrance_b_on_non_entrance_return_false(waypoint_b):
    tile = Tile(0, 0, UniqueDungeonCardValues.ENTRANCE_A)
    actual = waypoint_b.is_entrance(tile)
    expected = False
    assert actual == expected


def test_has_entrance_b_on_trail_returns_false(waypoint_b):
    room = Trail()
    actual = waypoint_b.has_entrance(room)
    expected = False
    assert actual == expected


def test_get_entrance_a_on_trail_returns_entrance_tile(waypoint_a):
    room = Trail()
    actual = waypoint_a.get_entrance(room)
    expected = Tile(-2, 5, UniqueDungeonCardValues.ENTRANCE_A)
    assert actual == expected


def test_get_entrance_b_on_hovel_returns_entrance_tile(waypoint_b):
    room = Hovel()
    actual = waypoint_b.get_entrance(room)
    expected = Tile(0, 3, UniqueDungeonCardValues.ENTRANCE_B)
    assert actual == expected


def test_remove_tile_by_type(waypoint_b):
    room = Burrow()
    new_room = waypoint_b.remove_entrance(room)

    assert not waypoint_b.has_entrance(new_room)
    assert new_room.get_name() == room.get_name()


def test_has_exit_b_on_den_returns_false(waypoint_b):
    room = Den()
    assert not waypoint_b.has_exit(room)


def test_has_exit_a_on_den_returns_true(waypoint_a):
    room = Den()
    assert waypoint_a.has_exit(room)
