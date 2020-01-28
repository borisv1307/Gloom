""" FILE: dungeon.py
    DESC: Connects the AbstractRoomCard to AbstractMonsterCard
    to produce one third of the DungeonCard (consists of three
    monster-room card pairs).
"""

from backend.src.main.game.values import NumberedRoomTileValues


class Dungeon:
    """ Represents room card paired with monster card """
    def __init__(self, room_card, monster_card):
        self.room_card = room_card
        self.monster_card = monster_card

    def get_tiles(self):
        """ Returns a list of tiles with the monster cards substituted in """
        room_tiles = self.room_card.get_tiles()
        output_tiles = []

        for tile in room_tiles:
            if self.is_tile_numbered_tile(tile):
                tile = self.replace_generic_number_with_concrete_monster_value(tile)
            output_tiles.append(tile)
        return output_tiles

    def replace_generic_number_with_concrete_monster_value(self, tile):
        """ Returns a tile with the NumberedTileValue replaced with
            the corresponding DungeonCardValue """
        character_number = tile.character_number
        tile.character_number = self.monster_card.get_designation_by_number(character_number)
        return tile

    @staticmethod
    def is_tile_numbered_tile(tile):
        """ Returns T/F if a tile a numbered tile (1-12) """
        return tile.character_number in NumberedRoomTileValues
