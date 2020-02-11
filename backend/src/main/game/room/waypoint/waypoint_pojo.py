from abc import ABC

from backend.src.main.game.tile.tile_util import TileUtility


class WaypointPOJO(ABC):
    def __init__(self, entrance_tile_type, exit_tile_type):
        self.entrance_tile = entrance_tile_type
        self.exit_tile = exit_tile_type

    def remove_entrance(self, room):
        return TileUtility.remove_tile_by_type(room, self.entrance_tile)

    def has_entrance(self, room):
        return TileUtility.has_tile_of_type(room, self.entrance_tile)

    def has_exit(self, room):
        return TileUtility.has_tile_of_type(room, self.exit_tile)

    def get_entrance(self, room):
        return TileUtility.get_tile_by_type(room, self.entrance_tile)

    def get_exit(self, room):
        return TileUtility.get_tile_by_type(room, self.exit_tile)

    def is_entrance(self, tile):
        return TileUtility.is_tile_of_type(tile, self.entrance_tile)
