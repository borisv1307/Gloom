from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import (
    DungeonCardValues,
    MonsterValues,
    NumberedRoomTileValues,
    TrapIndicators
)


class Hopeless(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.ONE: MonsterValues.NIGHT_DEMON,
            NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
            NumberedRoomTileValues.THREE: MonsterValues.NIGHT_DEMON,
            NumberedRoomTileValues.FOUR: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.SIX: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.FIVE: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.SEVEN: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.COIN,
            NumberedRoomTileValues.NINE: DungeonCardValues.COIN,
            NumberedRoomTileValues.TEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.ELEVEN: MonsterValues.BLACK_IMP,
            NumberedRoomTileValues.TWELVE: MonsterValues.BLACK_IMP,
            TrapIndicators.INDICATOR: []
        }
        AbstractMonsterCard.__init__(self, "Hopeless", map_values)
