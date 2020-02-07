from backend.src.main.game.random_monster_card import RandomMonsterCard
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


class Mangy(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {
            NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.EIGHT: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.NINE: DungeonCardValues.MONSTER,
            NumberedRoomTileValues.TEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.ELEVEN: DungeonCardValues.COIN,
            NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE,
            NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER}
        RandomMonsterCard.__init__(self, "Mangy", map_values)
