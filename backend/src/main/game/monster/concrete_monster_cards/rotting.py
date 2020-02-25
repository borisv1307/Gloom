from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Rotting(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.TWO: MonsterValues.LIVING_BONES,
            NumberedRoomTileValues.THREE: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.FOUR: MonsterValues.LIVING_CORPSE,
            NumberedRoomTileValues.FIVE: MonsterValues.LIVING_BONES,
            NumberedRoomTileValues.SIX: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.STUN, TrapIndicators.POISON]
        }
        AbstractMonsterCard.__init__(self, "Rotting", map_values)
