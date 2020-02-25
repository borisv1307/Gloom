from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Unstable(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.SAVVAS_LAVAFLOW,
            NumberedRoomTileValues.TWO: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.THREE: MonsterValues.EARTH_DEMON,
            NumberedRoomTileValues.FOUR: MonsterValues.EARTH_DEMON,
            NumberedRoomTileValues.FIVE: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.SIX: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.SEVEN: MonsterValues.FLAME_DEMON,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TWELVE: MonsterValues.FLAME_DEMON,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Unstable", map_values)
