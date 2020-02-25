from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Archaic(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.TWO: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.THREE: MonsterValues.STONE_GOLEM,
            NumberedRoomTileValues.FOUR: MonsterValues.STONE_GOLEM,
            NumberedRoomTileValues.FIVE: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.SIX: MonsterValues.ANCIENT_ARTILLERY,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.EIGHT: MonsterValues.ANCIENT_ARTILLERY,
            NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.ELEVEN: MonsterValues.ANCIENT_ARTILLERY,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Archaic", map_values)
