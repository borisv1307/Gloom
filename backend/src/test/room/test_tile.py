from backend.src.main.room.tile import Tile


def test_tile_with_same_attributes_are_equal():
    tile_one = Tile(0, 1, None)
    tile_two = Tile(0, 1, None)
    assert tile_one == tile_two


def test_tile_and_dog_object_are_not_equal():
    tile = Tile(0, 0, None)

    class Dog:
        pass

    assert Dog() != tile


def test_tiles_with_different_attributes_are_not_equal():
    tile_one = Tile(1, 2, 3)
    tile_two = Tile(4, 5, 6)
    assert tile_one != tile_two


