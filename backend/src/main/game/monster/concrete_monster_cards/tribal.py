from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Tribal(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.INOX_GUARD,
            NumberedRoomTileValues.TWO: MonsterValues.INOX_GUARD,
            NumberedRoomTileValues.THREE: MonsterValues.INOX_SHAMAN,
            NumberedRoomTileValues.FOUR: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.FIVE: MonsterValues.INOX_ARCHER,
            NumberedRoomTileValues.SIX: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.SEVEN: MonsterValues.INOX_SHAMAN,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: MonsterValues.INOX_ARCHER,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.COIN,
            TrapIndicators.INDICATOR: [TrapIndicators.WOUND, TrapIndicators.DISARM]
        }
        AbstractMonsterCard.__init__(self, "Tribal", map_values)
