"""This class is for Room Den tile mapping"""
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues
from backend.src.main.room.room import AbstractRoomCard


class Cabin(AbstractRoomCard):  # pylint: disable=too-few-public-methods
    """Cabin inherits RoomCard - Orient-Flat"""

    def __init__(self):
        AbstractRoomCard.__init__(self, "Cabin")
        self.add_tile(DungeonCardValues.ENTRANCE_A, -3, 1)
        self.add_tile(NumberedRoomTileValues.THREE, -2, -2)
        self.add_tile(NumberedRoomTileValues.TWO, -2, -1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -2, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(DungeonCardValues.EMPTY, -2, 3)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -2)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, 0)
        self.add_tile(NumberedRoomTileValues.EIGHT, -1, 1)
        self.add_tile(NumberedRoomTileValues.NINE, -1, 2)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -3)
        self.add_tile(NumberedRoomTileValues.ONE, 0, -2)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(NumberedRoomTileValues.SIX, 0, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 1)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, -4)
        self.add_tile(NumberedRoomTileValues.TEN, 2, -3)
        self.add_tile(NumberedRoomTileValues.FIVE, 2, -2)
        self.add_tile(NumberedRoomTileValues.FOUR, 2, -1)
        self.add_tile(DungeonCardValues.EMPTY, 2, 0)
        self.add_tile(DungeonCardValues.EMPTY, 2, 1)
        self.add_tile(DungeonCardValues.EXIT_A, 3, -2)
