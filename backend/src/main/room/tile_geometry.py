from backend.src.main.room.tile import Tile


class TileGeometry:
    @staticmethod
    def recenter_tile(tile_to_be_recentered, tile_to_recenter_around):
        new_x = tile_to_be_recentered.get_x() - tile_to_recenter_around.get_x()
        new_y = tile_to_be_recentered.get_y() - tile_to_recenter_around.get_y()
        character_number = tile_to_be_recentered.get_character_number()
        return Tile(new_x, new_y, character_number)

    def recenter_tile_list(self, tile_list, tile_to_recenter_around):
        return [self.recenter_tile(tile, tile_to_recenter_around) for tile in tile_list]
