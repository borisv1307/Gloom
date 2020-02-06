"""Creating Random Monster Card Class:
Cutthroat
"""
from backend.src.main.game.random_monster_card import AbstractMonsterCard
from backend.src.main.game.values import (
    DungeonCardValues,
    NumberedRoomTileValues
)


class Cutthroat(AbstractMonsterCard):  # pylint: disable=too-few-public-methods
    """ Class for Cutthroat Random Monster Card """

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.COIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        AbstractMonsterCard.__init__(self, "Cutthroat", map_values)
