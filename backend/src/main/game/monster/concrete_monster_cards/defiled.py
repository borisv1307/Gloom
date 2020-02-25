from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Defiled(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.SUN_DEMON,
            NumberedRoomTileValues.TWO: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.THREE: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.FOUR: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.FIVE: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.SIX: MonsterValues.SUN_DEMON,
            NumberedRoomTileValues.SEVEN: MonsterValues.FOREST_IMP,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TEN: MonsterValues.SUN_DEMON,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            TrapIndicators.INDICATOR: [TrapIndicators.POISON, TrapIndicators.IMMOBILIZE]
        }
        AbstractMonsterCard.__init__(self, "Defiled", map_values)
