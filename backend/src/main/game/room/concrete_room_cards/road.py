from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues
from backend.src.main.game.room.room import AbstractRoomCard


class Road(AbstractRoomCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        AbstractRoomCard.__init__(self, "Road")
        self.add_tile(DungeonCardValues.ENTRANCE_A, -2, 4)
        self.add_tile(NumberedRoomTileValues.TWELVE, -1, -3)
        self.add_tile(NumberedRoomTileValues.TEN, -1, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, -1, -1)
        self.add_tile(NumberedRoomTileValues.NINE, -1, 0)
        self.add_tile(NumberedRoomTileValues.SIX, -1, 1)
        self.add_tile(DungeonCardValues.EMPTY, -1, 2)
        self.add_tile(DungeonCardValues.EMPTY, -1, 3)
        self.add_tile(DungeonCardValues.EMPTY, -1, 4)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 0, -3)
        self.add_tile(DungeonCardValues.EMPTY, 0, -2)
        self.add_tile(DungeonCardValues.OBSTACLE, 0, -1)
        self.add_tile(NumberedRoomTileValues.ONE, 0, 0)
        self.add_tile(NumberedRoomTileValues.FIVE, 0, 1)
        self.add_tile(NumberedRoomTileValues.FOUR, 0, 2)
        self.add_tile(DungeonCardValues.EMPTY, 0, 3)
        self.add_tile(DungeonCardValues.ENTRANCE_B, 0, 4)
        self.add_tile(DungeonCardValues.EMPTY, 1, -4)
        self.add_tile(NumberedRoomTileValues.SEVEN, 1, -3)
        self.add_tile(NumberedRoomTileValues.EIGHT, 1, -2)
        self.add_tile(NumberedRoomTileValues.THREE, 1, -1)
        self.add_tile(NumberedRoomTileValues.TWO, 1, 0)
        self.add_tile(DungeonCardValues.EMPTY, 1, 1)
        self.add_tile(DungeonCardValues.EMPTY, 1, 2)
        self.add_tile(DungeonCardValues.EMPTY, 1, 3)
        self.add_tile(DungeonCardValues.EXIT_A, 2, -1)
