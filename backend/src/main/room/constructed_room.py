from backend.src.main.game.monster.random_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.values import NumberedRoomTileValues
from backend.src.main.game.room.room import AbstractRoomCard
from backend.src.main.tile.tile import Tile


class ConstructedRoom(AbstractRoomCard):
    def __init__(self, room_card, monster_card):
        if not isinstance(room_card, AbstractRoomCard):
            raise ValueError("Bad Room Card input to ConstructedRoom")
        if not isinstance(monster_card, AbstractMonsterCard):
            raise ValueError("Bad Monster Card input to ConstructedRoom")
        AbstractRoomCard.__init__(self, room_card.get_name)
        self.room_card = room_card
        self.monster_card = monster_card
        self.tiles = self.transform_tiles()

    def transform_tiles(self):
        room_tiles = self.room_card.get_tiles()
        output_tiles = []

        for tile in room_tiles:
            if self.is_tile_numbered_tile(tile):
                tile = self.replace_generic_number_with_concrete_monster_value(tile)
            output_tiles.append(tile)
        return output_tiles

    def replace_generic_number_with_concrete_monster_value(self, tile):
        character_number = tile.character_number
        character_number = self.monster_card.get_designation_by_number(character_number)
        new_tile = Tile(tile.get_x(), tile.get_y(), character_number)
        return new_tile

    @staticmethod
    def is_tile_numbered_tile(tile):
        return isinstance(tile.character_number, NumberedRoomTileValues)
