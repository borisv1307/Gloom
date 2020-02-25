from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Horrific(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.TWO: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.THREE: MonsterValues.LURKER,
            NumberedRoomTileValues.FOUR: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.FIVE: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.SIX: MonsterValues.DEEP_TERROR,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.EIGHT: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.NINE: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: MonsterValues.DEEP_TERROR,
            TrapIndicators.INDICATOR: [TrapIndicators.MUDDLE, TrapIndicators.DAMAGE]
        }
        AbstractMonsterCard.__init__(self, "Horrific", map_values)
