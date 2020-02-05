from backend.src.main.tile.tile_geometry_util import TileGeometryUtility


class WaypointPOJO:
    def __init__(self, entrance_tile_type, exit_tile_type):
        self.entrance_tile = entrance_tile_type
        self.exit_tile = exit_tile_type

    def has_entrance(self, room):
        return TileGeometryUtility.has_tile_of_type(room, self.entrance_tile)

    def get_entrance(self, room):
        return TileGeometryUtility.get_tile_by_type(room, self.entrance_tile)

    def get_exit(self, room):
        return TileGeometryUtility.get_tile_by_type(room, self.exit_tile)

    def is_entrance(self, tile):
        return TileGeometryUtility.is_tile_of_type(tile, self.entrance_tile)
