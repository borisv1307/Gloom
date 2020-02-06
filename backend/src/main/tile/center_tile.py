from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO
from backend.src.main.tile.tile import Tile


class CenterTile:
    @staticmethod
    def center_on_entrance(room, waypoint_pojo: WaypointPOJO):
        entrance = waypoint_pojo.get_entrance(room)
        if not entrance:
            raise ValueError
        return CenterTile.center_room_on_tile(room, entrance)

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
