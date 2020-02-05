from backend.src.main.tile.shift_tile import ShiftTile
from backend.src.main.tile.tile import Tile


def test_shift_tile_0_0_to_1_2_returns_1_2():
    tile_to_move = Tile(0, 0, None)
    tile_to_shift_to = Tile(1, 2, None)
    actual = ShiftTile.shift_tile(tile_to_move, tile_to_shift_to)
    assert actual == tile_to_shift_to


def test_shift_tile_list_0_0_and_0_1_to_1_0_returns_1_0_and_1_1():
    tiles_to_move = [Tile(0, 0, None), Tile(0, 1, None)]
    tile_to_shift_to = Tile(1, 0, None)

    actual = ShiftTile.shift_tile_list(tiles_to_move, tile_to_shift_to)

    expected = [Tile(1, 0, None), Tile(1, 1, None)]
    assert actual == expected
