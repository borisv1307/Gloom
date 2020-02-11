from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Drowned(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.NINE:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.TEN:
                          [DungeonCardValues.TRAPS, TrapIndicators.STUN, TrapIndicators.DAMAGE],
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Drowned", map_values)
