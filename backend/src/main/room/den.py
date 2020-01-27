"""This class is for Room Den tile mapping"""
from backend.src.main.room.room import AbstractRoomCard
from backend.src.main.game.values import NumberedRoomTileValues


class Den(AbstractRoomCard):  # pylint: disable=too-few-public-methods
    """Den inherits RoomCard"""

    def __init__(self):
        AbstractRoomCard.__init__(self, "Den")
        self.add_tile(self.EMPTY_TILE, 0, 2)
        self.add_tile(NumberedRoomTileValues.TWO, 0, 4)
        self.add_tile(NumberedRoomTileValues.THREE, 0, 6)
        self.add_tile(self.EMPTY_TILE, 1, 1)
        self.add_tile(self.EMPTY_TILE, 1, 3)
        self.add_tile(NumberedRoomTileValues.NINE, 1, 5)
        self.add_tile(NumberedRoomTileValues.ELEVEN, 1, 7)
        self.add_tile(self.EMPTY_TILE, 2, 0)
        self.add_tile(self.EMPTY_TILE, 2, 2)
        self.add_tile(NumberedRoomTileValues.SIX, 2, 4)
        self.add_tile(NumberedRoomTileValues.TEN, 2, 6)
        self.add_tile(NumberedRoomTileValues.TWELVE, 2, 8)
        self.add_tile(NumberedRoomTileValues.EIGHT, 3, 1)
        self.add_tile(NumberedRoomTileValues.SEVEN, 3, 3)
        self.add_tile(self.COIN_TILE, 3, 5)
        self.add_tile(NumberedRoomTileValues.ONE, 3, 7)
        self.add_tile(self.EMPTY_TILE, 4, 2)
        self.add_tile(NumberedRoomTileValues.FOUR, 4, 4)
        self.add_tile(NumberedRoomTileValues.FIVE, 4, 6)
