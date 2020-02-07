from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


class Hopeless(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.EMPTY,
                      NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.COIN,
                      NumberedRoomTileValues.NINE: DungeonCardValues.COIN,
                      NumberedRoomTileValues.TEN: DungeonCardValues.COIN,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Hopeless", map_values)
