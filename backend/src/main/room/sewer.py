"""This class is for Room Den tile mapping"""
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues
from backend.src.main.room.room import AbstractRoomCard


class Sewer(AbstractRoomCard):  # pylint: disable=too-few-public-methods
    """Sewer inherits RoomCard - Orient-Pointy"""

    def __init__(self):
        AbstractRoomCard.__init__(self, "Sewer")
        self.add_tile(DungeonCardValues.EXIT_A, 2, -4)
        self.add_tile(NumberedRoomTileValues.TWELVE, -1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 0, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 2, -3)
        self.add_tile(DungeonCardValues.EMPTY, 3, -3)
        self.add_tile(NumberedRoomTileValues.SEVEN, 4, -3)
        self.add_tile(NumberedRoomTileValues.TEN, -2, -2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, -1, -2)
        self.add_tile(DungeonCardValues.EMPTY, 0, -2)
        self.add_tile(NumberedRoomTileValues.ONE, 1, -2)
        self.add_tile(DungeonCardValues.EMPTY, 2, -2)
        self.add_tile(NumberedRoomTileValues.FIVE, 3, -2)
        self.add_tile(NumberedRoomTileValues.SIX, 4, -2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, -1)
        self.add_tile(NumberedRoomTileValues.NINE, 1, -1)
        self.add_tile(NumberedRoomTileValues.TWO, -1, 0)
        self.add_tile(NumberedRoomTileValues.THREE, 0, 0)
        self.add_tile(NumberedRoomTileValues.FOUR, 1, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, -2, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(DungeonCardValues.ENTRANCE_A, -2, 4)
