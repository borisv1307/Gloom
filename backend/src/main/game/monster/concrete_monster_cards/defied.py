from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Defied(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.POISON,
                           TrapIndicators.IMMOBILIZE],
                      NumberedRoomTileValues.NINE:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.POISON,
                           TrapIndicators.IMMOBILIZE],
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.POISON,
                           TrapIndicators.IMMOBILIZE],
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Defied", map_values)
