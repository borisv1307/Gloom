from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.room import AbstractRoomCard


class Corridor(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Corridor")
        self.add_tile(DungeonCardValues.EMPTY, 1, -4)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 2, -4)
        self.add_tile(NumberedRoomTileValues.TWELVE, 3, -4)
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 0, -3)
        self.add_tile(NumberedRoomTileValues.NINE, 1, -3)
        self.add_tile(NumberedRoomTileValues.TEN, 2, -3)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, -2)
        self.add_tile(NumberedRoomTileValues.SEVEN, 1, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 2, -2)
        self.add_tile(NumberedRoomTileValues.TWO, 0, -1)
        self.add_tile(NumberedRoomTileValues.ONE, 1, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 0, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 2)
        self.add_tile(NumberedRoomTileValues.FOUR, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 3)
        self.add_tile(NumberedRoomTileValues.THREE, 0, 1)
        self.add_tile(NumberedRoomTileValues.SIX, -2, 2)
        self.add_tile(NumberedRoomTileValues.FIVE, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, -3, 4)
        self.add_tile(DungeonCardValues.EMPTY, -2, 4)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, -2, 5)
