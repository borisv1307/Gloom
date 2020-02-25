from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Frigid(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.THREE: MonsterValues.SAVVAS_ICESTORM,
            NumberedRoomTileValues.FOUR: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.FIVE: MonsterValues.FROST_DEMON,
            NumberedRoomTileValues.SIX: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: MonsterValues.WIND_DEMON,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: MonsterValues.WIND_DEMON,
            TrapIndicators.INDICATOR: [TrapIndicators.DISARM]
        }
        AbstractMonsterCard.__init__(self, "Frigid", map_values)
