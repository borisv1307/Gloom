from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Wild(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.COIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.COIN,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.IMMOBILIZE,
                           TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE:
                          [DungeonCardValues.TRAPS,
                           TrapIndicators.IMMOBILIZE,
                           TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Wild", map_values)
