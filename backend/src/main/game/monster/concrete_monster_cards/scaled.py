from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Scaled(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE:
                          [DungeonCardValues.TRAPS, TrapIndicators.WOUND, TrapIndicators.POISON],
                      NumberedRoomTileValues.TWO:
                          [DungeonCardValues.TRAPS, TrapIndicators.WOUND, TrapIndicators.POISON],
                      NumberedRoomTileValues.THREE:
                          [DungeonCardValues.TRAPS, TrapIndicators.WOUND, TrapIndicators.POISON],
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Scaled", map_values)
