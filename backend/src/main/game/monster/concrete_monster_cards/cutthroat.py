from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Cutthroat(AbstractMonsterCard):  # pylint: disable=too-few-public-methods
    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.BANDIT_GUARD,
            NumberedRoomTileValues.TWO: DungeonCardValues.COIN,
            NumberedRoomTileValues.THREE: MonsterValues.BANDIT_ARCHER,
            NumberedRoomTileValues.FOUR: MonsterValues.BANDIT_ARCHER,
            NumberedRoomTileValues.FIVE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.SIX: MonsterValues.HOUND,
            NumberedRoomTileValues.SEVEN: MonsterValues.BANDIT_GUARD,
            NumberedRoomTileValues.EIGHT: MonsterValues.HOUND,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: MonsterValues.BANDIT_ARCHER,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.DAMAGE, TrapIndicators.POISON]
        }
        AbstractMonsterCard.__init__(self, "Cutthroat", map_values)
