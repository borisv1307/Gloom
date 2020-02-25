from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Crushing(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.STONE_GOLEM,
            NumberedRoomTileValues.TWO: MonsterValues.WIND_DEMON,
            NumberedRoomTileValues.THREE: MonsterValues.WIND_DEMON,
            NumberedRoomTileValues.FOUR: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.FIVE: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.SIX: MonsterValues.STONE_GOLEM,
            NumberedRoomTileValues.SEVEN: MonsterValues.WIND_DEMON,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.NINE: MonsterValues.WIND_DEMON,
            NumberedRoomTileValues.TEN: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TREASURE,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Crushing", map_values)
