from backend.src.main.tile.tile import Tile


class ShiftTile:
    @staticmethod
    def shift_room_on_tile(room, tile_to_be_shifted_round):
        room_tiles = room.get_tiles()
        new_tiles = ShiftTile.shift_tile_list(room_tiles, tile_to_be_shifted_round)

        new_room = room.clone()
        new_room.set_tiles(new_tiles)

        return new_room

    @staticmethod
    def shift_tile_list(tiles_to_move, tile_to_shift_to):
        return [ShiftTile.shift_tile(tile, tile_to_shift_to) for tile in tiles_to_move]

    @staticmethod
    def shift_tile(tile_to_move, tile_to_shift_to):
        new_x = tile_to_shift_to.get_x() + tile_to_move.get_x()
        new_y = tile_to_shift_to.get_y() + tile_to_move.get_y()
        character_number = tile_to_move.get_character_number()
        return Tile(new_x, new_y, character_number)
