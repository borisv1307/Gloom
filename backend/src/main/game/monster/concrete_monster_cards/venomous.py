from backend.src.main.game.monster.random_monster_card import RandomMonsterCard
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues


class Venomous(RandomMonsterCard):  # pylint: disable=too-few-public-methods

    def __init__(self):
        map_values = {NumberedRoomTileValues.THREE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ONE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SIX: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.SEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.EIGHT: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.NINE: DungeonCardValues.TRAPS,
                      NumberedRoomTileValues.FOUR: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.FIVE: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.ELEVEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TEN: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWO: DungeonCardValues.MONSTER,
                      NumberedRoomTileValues.TWELVE: DungeonCardValues.TREASURE}
        RandomMonsterCard.__init__(self, "Venomous", map_values)
