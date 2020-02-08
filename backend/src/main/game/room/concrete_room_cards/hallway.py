from backend.src.main.game.monster.values import (
    DungeonCardValues,
    NumberedRoomTileValues,
    UniqueDungeonCardValues)
from backend.src.main.game.room.abstract_room_card import AbstractRoomCard


class Hallway(AbstractRoomCard):

    def __init__(self):
        AbstractRoomCard.__init__(self, "Hallway")
        self.add_tile(NumberedRoomTileValues.EIGHT, -1, -2)
        self.add_tile(NumberedRoomTileValues.SEVEN, -1, -1)
        self.add_tile(NumberedRoomTileValues.FIVE, -1, 0)
        self.add_tile(NumberedRoomTileValues.TWO, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(UniqueDungeonCardValues.EXIT_B, 0, -4)
        self.add_tile(DungeonCardValues.EMPTY, 0, -3)
        self.add_tile(NumberedRoomTileValues.NINE, 0, -2)
        self.add_tile(DungeonCardValues.EMPTY, 0, -1)
        self.add_tile(NumberedRoomTileValues.FOUR, 0, 0)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 1)
        self.add_tile(DungeonCardValues.EMPTY, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 3)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_B, 0, 4)
        self.add_tile(NumberedRoomTileValues.TWELVE, 1, -4)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 1, -3)
        self.add_tile(NumberedRoomTileValues.TEN, 1, -2)
        self.add_tile(DungeonCardValues.EMPTY, 1, -1)
        self.add_tile(NumberedRoomTileValues.SIX, 1, 0)
        self.add_tile(NumberedRoomTileValues.THREE, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 1, 2)
        self.add_tile(DungeonCardValues.EMPTY, 1, 3)
        self.add_tile(UniqueDungeonCardValues.ENTRANCE_A, 2, 2)
