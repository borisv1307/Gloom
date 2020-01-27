"""Creating Random Monster Card Class:
Cutthroat
"""
from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues


class Cutthroat(RandomMonsterCard):  # pylint: disable=too-few-public-methods
    """ Class for Cutthroat Random Monster Card """

    def __init__(self):
        map_values = {1: DungeonCardValues.MONSTER,
                      2: DungeonCardValues.COIN,
                      3: DungeonCardValues.MONSTER,
                      4: DungeonCardValues.MONSTER,
                      5: DungeonCardValues.TRAPS,
                      6: DungeonCardValues.MONSTER,
                      7: DungeonCardValues.MONSTER,
                      8: DungeonCardValues.MONSTER,
                      9: DungeonCardValues.TRAPS,
                      10: DungeonCardValues.MONSTER,
                      11: DungeonCardValues.TRAPS,
                      12: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Cutthroat", map_values)
