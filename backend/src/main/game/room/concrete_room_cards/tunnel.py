from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.room import AbstractRoomCard


class Tunnel(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Tunnel")
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 0, -4)
        self.add_tile(NumberedRoomTileValues.TEN, 0, -3)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -2)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 1)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, -3)
        self.add_tile(NumberedRoomTileValues.TWELVE, -1, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -1)
        self.add_tile(NumberedRoomTileValues.NINE, -1, 0)
        self.add_tile(NumberedRoomTileValues.ONE, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, 3)
        self.add_tile(NumberedRoomTileValues.FIVE, -2, 2)
        self.add_tile(NumberedRoomTileValues.SEVEN, -2, 3)
        self.add_tile(NumberedRoomTileValues.THREE, -2, 4)
        self.add_tile(DungeonCardValues.EMPTY, -3, 3)
        self.add_tile(NumberedRoomTileValues.TWO, -3, 4)
        self.add_tile(DungeonCardValues.EMPTY, -3, 5)
        self.add_tile(DungeonCardValues.OBSTACLE, -4, 4)
        self.add_tile(DungeonCardValues.EMPTY, -4, 5)
        self.add_tile(DungeonCardValues.EMPTY, -4, 6)
        self.add_tile(DungeonCardValues.EMPTY, -5, 5)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, -5, 6)
        self.add_tile(NumberedRoomTileValues.FOUR, 1, -4)
        self.add_tile(DungeonCardValues.EMPTY, 1, -3)
        self.add_tile(NumberedRoomTileValues.SIX, 1, -2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 1, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, 0)
        self.add_tile(UniqueDungeonCardValues.EXIT_A, 2, -3)
