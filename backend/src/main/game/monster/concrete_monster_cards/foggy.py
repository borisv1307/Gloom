from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Foggy(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.FROST_DEMON,
            NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.THREE: MonsterValues.FLAME_DEMON,
            NumberedRoomTileValues.FOUR: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.FIVE: MonsterValues.FROST_DEMON,
            NumberedRoomTileValues.SIX: MonsterValues.FLAME_DEMON,
            NumberedRoomTileValues.SEVEN: MonsterValues.FROST_DEMON,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.NINE: MonsterValues.FLAME_DEMON,
            NumberedRoomTileValues.TEN: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.COIN,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Foggy", map_values)
