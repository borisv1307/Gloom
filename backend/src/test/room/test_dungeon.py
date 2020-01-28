""" FILE: test_room_card.py
    DESC: Contains tests for the Room Card
"""

from backend.src.main.room.room import Tile
from backend.src.main.room.den import Den
from backend.src.main.game.values import NumberedRoomTileValues, DungeonCardValues
from backend.src.main.room.dungeon import Dungeon
from backend.src.main.game.cutthroat import Cutthroat


def test_numbered_tile_is_numbered_tile():
    """ Check that a numbered tile returns true """
    numbered_five_tile = Tile(0, 0, NumberedRoomTileValues.FIVE)
    assert Dungeon.is_tile_numbered_tile(numbered_five_tile) is True


def test_obstactle_tile_is_not_numbered_tile():
    """ Check obstactle does not return true """
    obstacle_tile = Tile(0, 0, DungeonCardValues.OBSTACLE)
    assert Dungeon.is_tile_numbered_tile(obstacle_tile) is False


def test_coin_tile_is_correctly_replaced():
    """ Check that we have correctly paired two cards """
    den = Den()
    cutthroat = Cutthroat()
    dungeon = Dungeon(den, cutthroat)
    tile_of_interest = den.get_tiles()[1]

    # Sanity check the second tile is the numbered tile with value 2
    assert tile_of_interest.character_number == NumberedRoomTileValues.TWO

    # Update the tile to be replaced with concrete items from the monster card
    output_tile = dungeon.replace_generic_number_with_concrete_monster_value(tile_of_interest)

    # Sanity check
    two = NumberedRoomTileValues.TWO
    assert output_tile.character_number == cutthroat.get_designation_by_number(two)


def test_get_tiles_returns_no_instances_of_numbered_tiles():
    """ There should be no more instances of NumberedRoomTileValues """
    dungeon = Dungeon(Den(), Cutthroat())
    tiles = dungeon.get_tiles()

    for tile in tiles:
        assert tile.character_number not in NumberedRoomTileValues
