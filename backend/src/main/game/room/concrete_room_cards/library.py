from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Library(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Library")
        self.add_tile(UniqueDungeonCardValues.EXIT_A, 2, -4)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -3)
        self.add_tile(DungeonCardValues.EMPTY, 1, -3)
        self.add_tile(DungeonCardValues.EMPTY, 2, -3)
        self.add_tile(DungeonCardValues.EMPTY, 3, -3)
        self.add_tile(DungeonCardValues.EMPTY, -1, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -2)
        self.add_tile(NumberedRoomTileValues.NINE, 1, -2)
        self.add_tile(NumberedRoomTileValues.EIGHT, 2, -2)
        self.add_tile(DungeonCardValues.EMPTY, 3, -2)
        self.add_tile(DungeonCardValues.EMPTY, -2, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -1)
        self.add_tile(NumberedRoomTileValues.SEVEN, 1, -1)
        self.add_tile(DungeonCardValues.EMPTY, 2, -1)
        self.add_tile(DungeonCardValues.EMPTY, 3, -1)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, -3, 0)
        self.add_tile(DungeonCardValues.EMPTY, -2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(NumberedRoomTileValues.TWO, 0, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, 2, 0)
        self.add_tile(DungeonCardValues.OBSTACLE, -3, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, -2, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, 1)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 1)
        self.add_tile(NumberedRoomTileValues.THREE, 1, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, 2, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, -3, 2)
        self.add_tile(NumberedRoomTileValues.FIVE, -2, 2)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, 2)
        self.add_tile(NumberedRoomTileValues.TEN, 0, 2)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 1, 2)
        self.add_tile(DungeonCardValues.EMPTY, -3, 3)
        self.add_tile(NumberedRoomTileValues.SIX, -2, 3)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, 3)
        self.add_tile(NumberedRoomTileValues.TWELVE, 0, 3)
