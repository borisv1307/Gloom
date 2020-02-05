from backend.src.main.tile.tile import Tile
from backend.src.main.tile.tile_geometry_util import TileGeometryUtility


class CenterTile:
    @staticmethod
    def center_on_entrance(room, tile_type):
        return CenterTile.center_room_on_tile_type(room, tile_type)

    @staticmethod
    def center_room_on_tile_type(room, card_type):
        tile_to_recenter_around = TileGeometryUtility.get_tile_by_type(room, card_type)
        if not tile_to_recenter_around:
            raise ValueError("Room {} does not have tile with type {}".format(room, card_type))
        return CenterTile.center_room_on_tile(room, tile_to_recenter_around)

    @staticmethod
    def center_room_on_tile(room, tile_to_center_around):
        room_tiles = room.get_tiles()
        new_tiles = CenterTile.recenter_tile_list(room_tiles, tile_to_center_around)

        new_room = room.clone()
        new_room.set_tiles(new_tiles)

        return new_room

    @staticmethod
    def recenter_tile_list(tile_list, tile_to_recenter_around):
        return [CenterTile.recenter_tile(tile, tile_to_recenter_around) for tile in tile_list]

    @staticmethod
    def recenter_tile(tile_to_move, tile_to_center_around):
        new_x = tile_to_move.get_x() - tile_to_center_around.get_x()
        new_y = tile_to_move.get_y() - tile_to_center_around.get_y()
        character_number = tile_to_move.get_character_number()
        return Tile(new_x, new_y, character_number)
