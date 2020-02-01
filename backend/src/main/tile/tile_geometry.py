import copy

from backend.src.main.game.values import DungeonCardValues
from backend.src.main.tile.tile import Tile


class TileGeometry:
    def center_on_entrance_a(self, room):
        return self.center_room_on_tile_type(room, DungeonCardValues.ENTRANCE_A)

    def center_on_entrance_b(self, room):
        return self.center_room_on_tile_type(room, DungeonCardValues.ENTRANCE_B)

    def center_room_on_tile_type(self, room, card_type):
        room_tiles = room.get_tiles()
        tile_to_recenter_around = self.get_tile_by_type(room, card_type)
        new_tiles = self.recenter_tile_list(room_tiles, tile_to_recenter_around)

        new_room = copy.deepcopy(room)
        new_room.set_tiles(new_tiles)

        return new_room

    def recenter_tile_list(self, tile_list, tile_to_recenter_around):
        return [self.recenter_tile(tile, tile_to_recenter_around) for tile in tile_list]

    @staticmethod
    def recenter_tile(tile_to_be_recentered, tile_to_recenter_around):
        new_x = tile_to_be_recentered.get_x() - tile_to_recenter_around.get_x()
        new_y = tile_to_be_recentered.get_y() - tile_to_recenter_around.get_y()
        character_number = tile_to_be_recentered.get_character_number()
        return Tile(new_x, new_y, character_number)

    def has_entrance_a(self, room):
        return self.has_tile_of_type(room, DungeonCardValues.ENTRANCE_A)

    def has_entrance_b(self, room):
        return self.has_tile_of_type(room, DungeonCardValues.ENTRANCE_B)

    def has_tile_of_type(self, room, card_type):
        for tile in room.get_tiles():
            if self.is_tile_of_type(tile, card_type):
                return True
        return False

    def get_entrance_a(self, room):
        return self.get_tile_by_type(room, DungeonCardValues.ENTRANCE_A)

    def get_entrance_b(self, room):
        return self.get_tile_by_type(room, DungeonCardValues.ENTRANCE_B)

    def get_tile_by_type(self, room, card_type):
        for tile in room.get_tiles():
            if self.is_tile_of_type(tile, card_type):
                return tile
        return None

    def is_entrance_a(self, tile):
        return self.is_tile_of_type(tile, DungeonCardValues.ENTRANCE_A)

    def is_entrance_b(self, tile):
        return self.is_tile_of_type(tile, DungeonCardValues.ENTRANCE_B)

    @staticmethod
    def is_tile_of_type(tile, card_type):
        return tile.get_character_number() == card_type
