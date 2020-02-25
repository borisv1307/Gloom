from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues, \
    TrapIndicators


class Defiled(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
                      TrapIndicators.INDICATOR: [TrapIndicators.POISON, TrapIndicators.IMMOBILIZE]}
        AbstractMonsterCard.__init__(self, "Defiled", map_values)
