from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Crossroads(AbstractRoomCard):

    def __init__(self):
        AbstractRoomCard.__init__(self, "Crossroads")
        self.add_tile('EntranceB', -2, -3)
        self.add_tile(DungeonCardValues.EMPTY, -1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 0, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -3)
        self.add_tile(NumberedRoomTileValues.NINE, 2, -3)
        self.add_tile(DungeonCardValues.EMPTY, 3, -3)
        self.add_tile(NumberedRoomTileValues.SEVEN, 4, -3)
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 5, -3)
        self.add_tile(DungeonCardValues.EMPTY, -2, -2)
        self.add_tile(DungeonCardValues.EMPTY, -1, -2)
        self.add_tile(NumberedRoomTileValues.FOUR, 0, -2)
        self.add_tile(NumberedRoomTileValues.FIVE, 1, -2)
        self.add_tile(DungeonCardValues.EMPTY, 2, -2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 3, -2)
        self.add_tile(NumberedRoomTileValues.SIX, 4, -2)
        self.add_tile(NumberedRoomTileValues.THREE, 0, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 0, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 1)
        self.add_tile(NumberedRoomTileValues.TEN, 0, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(NumberedRoomTileValues.ONE, -1, 2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 0, 2)
        self.add_tile(NumberedRoomTileValues.TWO, -2, 3)
        self.add_tile(NumberedRoomTileValues.TWELVE, -1, 3)
