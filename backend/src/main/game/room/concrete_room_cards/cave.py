from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Cave(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Cave")
        self.add_tile(NumberedRoomTileValues.ELEVEN, -1, -2)
        self.add_tile(NumberedRoomTileValues.NINE, 0, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 1, -2)
        self.add_tile(NumberedRoomTileValues.TEN, 2, -2)
        self.add_tile(NumberedRoomTileValues.FOUR, -2, -1)
        self.add_tile(NumberedRoomTileValues.ONE, -1, -1)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, -1)
        self.add_tile(NumberedRoomTileValues.SIX, 1, -1)
        self.add_tile(DungeonCardValues.EMPTY, 2, -1)
        self.add_tile(DungeonCardValues.OBSTACLE, -2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 0, 0)
        self.add_tile(NumberedRoomTileValues.FIVE, 1, 0)
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -3, 1)
        self.add_tile(NumberedRoomTileValues.THREE, -2, 1)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 1)
        self.add_tile(NumberedRoomTileValues.TWO, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -3, 2)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(NumberedRoomTileValues.TWELVE, 0, 2)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, -3, 3)
