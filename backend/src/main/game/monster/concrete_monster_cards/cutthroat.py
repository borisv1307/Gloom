from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Cutthroat(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.COIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE:
                          [DungeonCardValues.TRAPS, TrapIndicators.DAMAGE, TrapIndicators.POISON],
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE:
                          [DungeonCardValues.TRAPS, TrapIndicators.DAMAGE, TrapIndicators.POISON],
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.DAMAGE, TrapIndicators.POISON],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Cutthroat", map_values)
