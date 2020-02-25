from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Corrupted(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.TWO: MonsterValues.LIVING_BONES,
            NumberedRoomTileValues.THREE: MonsterValues.NIGHT_DEMON,
            NumberedRoomTileValues.FOUR: MonsterValues.NIGHT_DEMON,
            NumberedRoomTileValues.FIVE: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.SIX: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.SEVEN: MonsterValues.LIVING_BONES,
            NumberedRoomTileValues.EIGHT: MonsterValues.CULTIST,
            NumberedRoomTileValues.NINE: MonsterValues.CULTIST,
            NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Corrupted", map_values)
