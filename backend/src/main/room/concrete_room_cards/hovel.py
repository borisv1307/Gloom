from backend.src.main.game.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.room.room import AbstractRoomCard


class Hovel(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Hovel")
        self.add_tile(DungeonCardValues.EMPTY, 1, -4)
        self.add_tile(DungeonCardValues.EMPTY, 2, -4)
        self.add_tile(UniqueDungeonCardValues.EXIT_A, -1, -3)
        self.add_tile(NumberedRoomTileValues.TEN, 0, -3)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -3)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, -3)
        self.add_tile(NumberedRoomTileValues.EIGHT, -1, -2)
        self.add_tile(NumberedRoomTileValues.ONE, 0, -2)
        self.add_tile(NumberedRoomTileValues.TWO, 1, -2)
        self.add_tile(NumberedRoomTileValues.NINE, 2, -2)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(DungeonCardValues.EMPTY, 1, -1)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, 0)
        self.add_tile(NumberedRoomTileValues.SIX, 0, 0)
        self.add_tile(NumberedRoomTileValues.THREE, -2, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, -3, 2)
        self.add_tile(DungeonCardValues.OBSTACLE, -2, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 2)
        self.add_tile(NumberedRoomTileValues.FIVE, -3, 3)
        self.add_tile(DungeonCardValues.EMPTY, -2, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, 0, 3)
        self.add_tile(NumberedRoomTileValues.ELEVEN, -4, 4)
        self.add_tile(DungeonCardValues.EMPTY, -3, 4)
        self.add_tile(DungeonCardValues.EMPTY, -2, 4)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, -3, 5)
