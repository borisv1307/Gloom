from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Fortified(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.CITY_GUARD,
            NumberedRoomTileValues.TWO: MonsterValues.CITY_GUARD,
            NumberedRoomTileValues.THREE: DungeonCardValues.COIN,
            NumberedRoomTileValues.FOUR: DungeonCardValues.COIN,
            NumberedRoomTileValues.FIVE: MonsterValues.CITY_ARCHER,
            NumberedRoomTileValues.SIX: MonsterValues.CITY_ARCHER,
            NumberedRoomTileValues.SEVEN: MonsterValues.CITY_ARCHER,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: MonsterValues.ANCIENT_ARTILLERY,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: MonsterValues.ANCIENT_ARTILLERY,
            TrapIndicators.INDICATOR: [TrapIndicators.DAMAGE]
        }
        AbstractMonsterCard.__init__(self, "Fortified", map_values)
