from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Tribal(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS, TrapIndicators.WOUND, TrapIndicators.DISARM],
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.WOUND, TrapIndicators.DISARM],
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.COIN,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.COIN}
        RandomMonsterCard.__init__(self, "Tribal", map_values)
