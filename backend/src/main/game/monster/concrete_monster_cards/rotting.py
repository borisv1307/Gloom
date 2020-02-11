from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues,\
    TrapIndicators


class Rotting(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):

        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.COIN,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.POISON],
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.POISON],
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.POISON],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Rotting", map_values)
