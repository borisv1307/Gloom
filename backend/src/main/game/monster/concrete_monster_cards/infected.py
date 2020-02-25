from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Infected(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.TWO: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.THREE: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.FOUR: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.FIVE: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.SIX: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.SEVEN: MonsterValues.OOZE,
            NumberedRoomTileValues.EIGHT: MonsterValues.GIANT_VIPER,
            NumberedRoomTileValues.NINE: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.TEN: MonsterValues.OOZE,
            NumberedRoomTileValues.ELEVEN: MonsterValues.OOZE,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.COIN,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Infected", map_values)
