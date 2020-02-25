from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Mangy(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.VERMLING_SHAMAN,
            NumberedRoomTileValues.TWO: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.THREE: MonsterValues.CAVE_BEAR,
            NumberedRoomTileValues.FOUR: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.FIVE: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.SIX: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.SEVEN: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.EIGHT: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.NINE: MonsterValues.VERMLING_SCOUT,
            NumberedRoomTileValues.TEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Mangy", map_values)
