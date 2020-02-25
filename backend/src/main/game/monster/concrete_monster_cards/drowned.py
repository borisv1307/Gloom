from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Drowned(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.LURKER,
            NumberedRoomTileValues.TWO: MonsterValues.LURKER,
            NumberedRoomTileValues.THREE: MonsterValues.LURKER,
            NumberedRoomTileValues.FOUR: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.FIVE: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.SIX: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.SEVEN: MonsterValues.LIVING_SPIRIT,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.DIFFICULT_TERRAIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.STUN, TrapIndicators.DAMAGE]
        }
        AbstractMonsterCard.__init__(self, "Drowned", map_values)
