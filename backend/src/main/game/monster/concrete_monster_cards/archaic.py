from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Archaic(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.TWO: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
                      TrapIndicators.INDICATOR: []}
        AbstractMonsterCard.__init__(self, "Archaic", map_values)
