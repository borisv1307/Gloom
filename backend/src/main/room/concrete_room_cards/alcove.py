from backend.src.main.game.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.room.room import AbstractRoomCard


class Alcove(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Alcove")
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 0, -5)
        self.add_tile(DungeonCardValues.EMPTY, -1, -4)
        self.add_tile(DungeonCardValues.EMPTY, 0, -4)
        self.add_tile(DungeonCardValues.EMPTY, 1, -5)
        self.add_tile(NumberedRoomTileValues.EIGHT, -1, -3)
        self.add_tile(NumberedRoomTileValues.SEVEN, 0, -3)
        self.add_tile(NumberedRoomTileValues.NINE, 1, -4)
        self.add_tile(NumberedRoomTileValues.SIX, -1, -2)
        self.add_tile(NumberedRoomTileValues.ONE, 0, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(DungeonCardValues.EMPTY, 1, -2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 0, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, -1)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 1)
        self.add_tile(NumberedRoomTileValues.TWO, 1, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, 1)
        self.add_tile(NumberedRoomTileValues.THREE, 2, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 2, 0)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, 3, -1)
        self.add_tile(NumberedRoomTileValues.TEN, 3, 0)
        self.add_tile(DungeonCardValues.EMPTY, 3, 1)
        self.add_tile(NumberedRoomTileValues.FIVE, 4, -1)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 4, 0)
        self.add_tile(DungeonCardValues.EMPTY, 4, 1)
        self.add_tile(DungeonCardValues.EMPTY, 5, -1)
