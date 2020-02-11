from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Fortified(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.COIN,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.COIN,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.TEN:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Fortified", map_values)
