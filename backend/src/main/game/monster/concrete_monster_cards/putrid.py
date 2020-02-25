from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Putrid(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.TWO: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.THREE: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.FOUR: MonsterValues.OOZE,
            NumberedRoomTileValues.FIVE: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.SIX: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.SEVEN: MonsterValues.OOZE,
            NumberedRoomTileValues.EIGHT: MonsterValues.OOZE,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.MUDDLE, TrapIndicators.DAMAGE]
        }
        AbstractMonsterCard.__init__(self, "Putrid", map_values)
