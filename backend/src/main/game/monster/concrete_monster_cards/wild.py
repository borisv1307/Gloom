from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Wild(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.CAVE_BEAR,
            NumberedRoomTileValues.TWO: DungeonCardValues.COIN,
            NumberedRoomTileValues.THREE: DungeonCardValues.COIN,
            NumberedRoomTileValues.FOUR: MonsterValues.HOUND,
            NumberedRoomTileValues.FIVE: MonsterValues.HOUND,
            NumberedRoomTileValues.SIX: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.SEVEN: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: MonsterValues.CAVE_BEAR,
            NumberedRoomTileValues.ELEVEN: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.IMMOBILIZE, TrapIndicators.DAMAGE]
        }
        AbstractMonsterCard.__init__(self, "Wild", map_values)
