from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Frigid(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.SEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.DISARM],
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.NINE:
                          [DungeonCardValues.TRAPS, TrapIndicators.DISARM],
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.DISARM],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Frigid", map_values)
