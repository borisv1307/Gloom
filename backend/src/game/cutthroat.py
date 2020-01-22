from game.random_monster_card import RandomMonsterCard
from game.values import RandomEnemyCardValues


class Cutthroat(RandomMonsterCard):
    def __init__(self):
        map_values = {1: RandomEnemyCardValues.MONSTER,
                      2: RandomEnemyCardValues.COIN,
                      3: RandomEnemyCardValues.MONSTER,
                      4: RandomEnemyCardValues.MONSTER,
                      5: RandomEnemyCardValues.TRAPS,
                      6: RandomEnemyCardValues.MONSTER,
                      7: RandomEnemyCardValues.MONSTER,
                      8: RandomEnemyCardValues.MONSTER,
                      9: RandomEnemyCardValues.TRAPS,
                      10: RandomEnemyCardValues.MONSTER,
                      11: RandomEnemyCardValues.TRAPS,
                      12: RandomEnemyCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Cutthroat", map_values)
