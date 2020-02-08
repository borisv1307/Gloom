from backend.src.main.game.monster.values import (
    NumberedRoomTileValues,
    DungeonCardValues,
    UniqueDungeonCardValues
)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Den(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Den")
        self.add_tile(DungeonCardValues.EMPTY, 0, -2)
        self.add_tile(NumberedRoomTileValues.TWO, 1, -2)
        self.add_tile(NumberedRoomTileValues.THREE, 2, -2)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, -2, -1)
        self.add_tile(DungeonCardValues.EMPTY, -1, -1)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(NumberedRoomTileValues.NINE, 1, -1)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 2, -1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 0)
        self.add_tile(DungeonCardValues.EMPTY, -1, 0)
        self.add_tile(NumberedRoomTileValues.SIX, 0, 0)
        self.add_tile(NumberedRoomTileValues.TEN, 1, 0)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, 0)
        self.add_tile(NumberedRoomTileValues.EIGHT, -2, 1)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, 1)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, 1)
        self.add_tile(NumberedRoomTileValues.ONE, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -2, 2)
        self.add_tile(NumberedRoomTileValues.FOUR, -1, 2)
        self.add_tile(NumberedRoomTileValues.FIVE, 0, 2)
        self.add_tile(UniqueDungeonCardValues.EXIT_A, -2, 3)
