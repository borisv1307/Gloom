from backend.src.main.room.tile import Tile
from backend.src.main.room.concrete_room_cards.den import Den
from backend.src.main.game.values import NumberedRoomTileValues, DungeonCardValues
from backend.src.main.room.constructed_room import ConstructedRoom
from backend.src.main.game.cutthroat import Cutthroat


def test_numbered_tile_is_numbered_tile():
    numbered_five_tile = Tile(0, 0, NumberedRoomTileValues.FIVE)
    assert ConstructedRoom.is_tile_numbered_tile(numbered_five_tile) is True


def test_obstacle_tile_is_not_numbered_tile():
    obstacle_tile = Tile(0, 0, DungeonCardValues.OBSTACLE)
    assert ConstructedRoom.is_tile_numbered_tile(obstacle_tile) is False


def test_coin_tile_is_correctly_replaced():
    den = Den()
    cutthroat = Cutthroat()
    dungeon = ConstructedRoom(den, cutthroat)
    tile_of_interest = den.get_tiles()[1]

    # Sanity check the second tile is the numbered tile with value 2
    assert tile_of_interest.character_number == NumberedRoomTileValues.TWO

    # Update the tile to be replaced with concrete items from the monster card
    output_tile = dungeon.replace_generic_number_with_concrete_monster_value(tile_of_interest)

    # Sanity check
    two = NumberedRoomTileValues.TWO
    assert output_tile.character_number == cutthroat.get_designation_by_number(two)


def test_get_tiles_returns_no_instances_of_numbered_tiles():
    dungeon = ConstructedRoom(Den(), Cutthroat())
    tiles = dungeon.get_tiles()

    for tile in tiles:
        assert not isinstance(tile.character_number, NumberedRoomTileValues)
