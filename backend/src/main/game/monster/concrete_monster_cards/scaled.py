from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Scaled(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWO: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.THREE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.FOUR: MonsterValues.RENDING_DRAKE,
            NumberedRoomTileValues.FIVE: MonsterValues.RENDING_DRAKE,
            NumberedRoomTileValues.SIX: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.EIGHT: MonsterValues.SPITTING_DRAKE,
            NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TEN: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.ELEVEN: MonsterValues.SPITTING_DRAKE,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.COIN,
            TrapIndicators.INDICATOR: [TrapIndicators.WOUND, TrapIndicators.POISON]
        }
        AbstractMonsterCard.__init__(self, "Scaled", map_values)
