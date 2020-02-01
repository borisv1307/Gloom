from backend.src.main.game.values import DungeonCardValues
from backend.src.main.tile.tile import Tile


class TileGeometry:
    @staticmethod
    def recenter_tile(tile_to_be_recentered, tile_to_recenter_around):
        new_x = tile_to_be_recentered.get_x() - tile_to_recenter_around.get_x()
        new_y = tile_to_be_recentered.get_y() - tile_to_recenter_around.get_y()
        character_number = tile_to_be_recentered.get_character_number()
        return Tile(new_x, new_y, character_number)

    def recenter_tile_list(self, tile_list, tile_to_recenter_around):
        return [self.recenter_tile(tile, tile_to_recenter_around) for tile in tile_list]

    def has_entrance_b(self, room):
        for current_tile in room.get_tiles():
            if self.is_entrance_b(current_tile):
                return True
        return False

    def has_entrance_a(self, room):
        for current_tile in room.get_tiles():
            if self.is_entrance_a(current_tile):
                return True
        return False

    def get_entrance_a(self, room):
        for current_tile in room.get_tiles():
            if self.is_entrance_a(current_tile):
                return current_tile
        return None

    def get_entrance_b(self, room):
        for current_tile in room.get_tiles():
            if self.is_entrance_b(current_tile):
                return current_tile
        return None

    @staticmethod
    def is_entrance_a(tile):
        return tile.get_character_number() == DungeonCardValues.ENTRANCE_A

    @staticmethod
    def is_entrance_b(tile):
        return tile.get_character_number() == DungeonCardValues.ENTRANCE_B

