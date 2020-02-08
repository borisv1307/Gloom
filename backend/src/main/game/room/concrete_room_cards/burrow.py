from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Burrow(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Burrow")
        self.add_tile(UniqueDungeonCardValues.EXIT_B, -1, -4)
        self.add_tile(NumberedRoomTileValues.TWELVE, 0, -4)
        self.add_tile(NumberedRoomTileValues.ELEVEN, -1, -3)
        self.add_tile(NumberedRoomTileValues.TEN, 0, -3)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -2)
        self.add_tile(NumberedRoomTileValues.SEVEN, 0, -2)
        self.add_tile(NumberedRoomTileValues.SIX, -1, -1)
        self.add_tile(NumberedRoomTileValues.FIVE, 0, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 0)
        self.add_tile(NumberedRoomTileValues.TWO, -1, 1)
        self.add_tile(NumberedRoomTileValues.THREE, 0, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 2)
        self.add_tile(NumberedRoomTileValues.NINE, -1, 3)
        self.add_tile(NumberedRoomTileValues.EIGHT, 0, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(DungeonCardValues.EMPTY, -1, 5)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, -1, 6)
        self.add_tile(DungeonCardValues.EMPTY, 0, 4)
        self.add_tile(DungeonCardValues.EMPTY, 0, 5)
