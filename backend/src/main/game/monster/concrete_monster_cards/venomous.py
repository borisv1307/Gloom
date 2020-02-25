from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Venomous(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.HARROWER_INFESTER,
            NumberedRoomTileValues.TWO: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.THREE: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.FOUR: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.FIVE: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.SIX: MonsterValues.HARROWER_INFESTER,
            NumberedRoomTileValues.SEVEN: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.ELEVEN: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.POISON, TrapIndicators.STUN]
        }
        AbstractMonsterCard.__init__(self, "Venomous", map_values)
