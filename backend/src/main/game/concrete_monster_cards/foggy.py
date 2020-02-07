from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


class Foggy(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN: DungeonCardValues.DIFFICULT_TERRAIN,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.HAZARDOUS_TERRAIN,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Foggy", map_values)
