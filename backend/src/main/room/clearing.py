"""This class is for Room Den tile mapping"""
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues
from backend.src.main.room.room import AbstractRoomCard


class Clearing(AbstractRoomCard):  # pylint: disable=too-few-public-methods
    """Clearing inherits RoomCard - Orient-Pointy"""

    def __init__(self):
        AbstractRoomCard.__init__(self, "Clearing")
        self.add_tile(DungeonCardValues.EMPTY, -1, -3)
        self.add_tile(NumberedRoomTileValues.FIVE, 0, -3)
        self.add_tile(NumberedRoomTileValues.FOUR, 1, -3)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, -3)
        self.add_tile(DungeonCardValues.EMPTY, 3, -3)
        self.add_tile(DungeonCardValues.EMPTY, -1, -2)
        self.add_tile(DungeonCardValues.EMPTY, 0, -2)
        self.add_tile(DungeonCardValues.EMPTY, 1, -2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 2, -2)
        self.add_tile(DungeonCardValues.EMPTY, -2, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(NumberedRoomTileValues.SIX, 0, -1)
        self.add_tile(DungeonCardValues.EMPTY, 1, -1)
        self.add_tile(NumberedRoomTileValues.TEN, 2, -1)
        self.add_tile(DungeonCardValues.ENTRANCE_B, -3, 0)
        self.add_tile(DungeonCardValues.EMPTY, -2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 0, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 0)
        self.add_tile(DungeonCardValues.EXIT_B, 2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -3, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 1)
        self.add_tile(NumberedRoomTileValues.THREE, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 1)
        self.add_tile(NumberedRoomTileValues.SEVEN, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -3, 2)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, -4, 3)
        self.add_tile(NumberedRoomTileValues.TWO, -3, 3)
        self.add_tile(NumberedRoomTileValues.ONE, -2, 3)
        self.add_tile(NumberedRoomTileValues.NINE, -1, 3)
        self.add_tile(DungeonCardValues.EMPTY, 0, 3)
