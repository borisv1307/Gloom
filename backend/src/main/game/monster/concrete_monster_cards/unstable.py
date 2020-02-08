from backend.src.main.game.monster.random_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues


class Unstable(AbstractMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.SIX: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.NINE: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        AbstractMonsterCard.__init__(self, "Unstable", map_values)
