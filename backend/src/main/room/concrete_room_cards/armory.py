from backend.src.main.game.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.room.room import AbstractRoomCard


class Armory(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Armory")
        self.add_tile(NumberedRoomTileValues.TWELVE, -2, -2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, -2, -1)
        self.add_tile(NumberedRoomTileValues.TEN, -2, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -3)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -2)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, -1)
        self.add_tile(NumberedRoomTileValues.TWO, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(DungeonCardValues.EMPTY, -1, 5)
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 0, -4)
        self.add_tile(DungeonCardValues.EMPTY, 0, -3)
        self.add_tile(NumberedRoomTileValues.NINE, 0, -2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, -1)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 0)
        self.add_tile(NumberedRoomTileValues.SIX, 0, 1)
        self.add_tile(NumberedRoomTileValues.FIVE, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 3)
        self.add_tile(DungeonCardValues.EMPTY, 0, 4)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, 0, 5)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -4)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -2)
        self.add_tile(NumberedRoomTileValues.THREE, 1, -1)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, 1, 4)
