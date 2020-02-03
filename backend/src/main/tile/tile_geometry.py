# pylint: disable=too-many-public-methods
from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.room import AbstractRoomCard
from backend.src.main.tile.tile import Tile


class TileGeometry:
    def overlay_room_a_on_room_b_by_waypoint_a(self, room_a, room_b):
        current_room_b = room_b
        for i in range(6):
            new_room_b = self.center_room_a_on_room_b_by_waypoint_a(room_a, current_room_b)
            new_room_b = self.remove_tile_by_type(new_room_b, DungeonCardValues.ENTRANCE_A)
            if not self.do_rooms_overlap(room_a, new_room_b):
                return new_room_b
            current_room_b = current_room_b.rotate()
        raise AssertionError("TileGeometry algorithm failed")

    def overlay_room_a_on_room_b_by_waypoint_b(self, room_a, room_b):
        current_room_b = room_b
        for i in range(6):
            new_room_b = self.center_room_a_on_room_b_by_waypoint_b(room_a, current_room_b)
            new_room_b = self.remove_tile_by_type(new_room_b, DungeonCardValues.ENTRANCE_B)
            if not self.do_rooms_overlap(room_a, new_room_b):
                return new_room_b
            current_room_b = current_room_b.rotate()
        raise AssertionError("TileGeometry algorithm failed")

    @staticmethod
    def do_rooms_overlap(room_a: AbstractRoomCard, room_b: AbstractRoomCard) -> bool:
        for tile_a in room_a.get_tiles():
            for tile_b in room_b.get_tiles():
                if tile_a.has_same_coordinates(tile_b):
                    return True
        return False

    def center_room_a_on_room_b_by_waypoint_a(self, room_a, room_b):
        intermediate_room_b = self.center_on_entrance_a(room_b)
        room_a_exit = self.get_exit_a(room_a)
        new_room_b = self.shift_room_on_tile(intermediate_room_b, room_a_exit)
        return new_room_b

    def center_room_a_on_room_b_by_waypoint_b(self, room_a, room_b):
        intermediate_room_b = self.center_on_entrance_b(room_b)
        room_a_exit = self.get_exit_b(room_a)
        new_room_b = self.shift_room_on_tile(intermediate_room_b, room_a_exit)
        return new_room_b

    def center_on_entrance_a(self, room):
        return self.center_room_on_tile_type(room, DungeonCardValues.ENTRANCE_A)

    def center_on_entrance_b(self, room):
        return self.center_room_on_tile_type(room, DungeonCardValues.ENTRANCE_B)

    def center_room_on_tile_type(self, room, card_type):
        tile_to_recenter_around = self.get_tile_by_type(room, card_type)
        if not tile_to_recenter_around:
            raise ValueError("Room {} does not have tile with type {}".format(room, card_type))
        return self.center_room_on_tile(room, tile_to_recenter_around)

    def shift_room_on_tile(self, room, tile_to_be_shifted_round):
        room_tiles = room.get_tiles()
        new_tiles = self.shift_tile_list(room_tiles, tile_to_be_shifted_round)

        new_room = room.clone()
        new_room.set_tiles(new_tiles)

        return new_room

    def center_room_on_tile(self, room, tile_to_center_around):
        room_tiles = room.get_tiles()
        new_tiles = self.recenter_tile_list(room_tiles, tile_to_center_around)

        new_room = room.clone()
        new_room.set_tiles(new_tiles)

        return new_room

    def shift_tile_list(self, tiles_to_move, tile_to_shift_to):
        return [self.shift_tile(tile, tile_to_shift_to) for tile in tiles_to_move]

    @staticmethod
    def shift_tile(tile_to_move, tile_to_shift_to):
        new_x = tile_to_shift_to.get_x() + tile_to_move.get_x()
        new_y = tile_to_shift_to.get_y() + tile_to_move.get_y()
        character_number = tile_to_move.get_character_number()
        return Tile(new_x, new_y, character_number)

    def recenter_tile_list(self, tile_list, tile_to_recenter_around):
        return [self.recenter_tile(tile, tile_to_recenter_around) for tile in tile_list]

    @staticmethod
    def recenter_tile(tile_to_move, tile_to_center_around):
        new_x = tile_to_move.get_x() - tile_to_center_around.get_x()
        new_y = tile_to_move.get_y() - tile_to_center_around.get_y()
        character_number = tile_to_move.get_character_number()
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

    def get_exit_a(self, room):
        return self.get_tile_by_type(room, DungeonCardValues.EXIT_A)
    
    def get_exit_b(self, room):
        return self.get_tile_by_type(room, DungeonCardValues.EXIT_B)

    def remove_tile_by_type(self, room, card_type):
        tiles = room.get_tiles()
        tile_to_remove = self.get_tile_by_type(room, card_type)
        new_tiles = [tile for tile in tiles if tile != tile_to_remove]
        new_room = room.clone()
        new_room.set_tiles(new_tiles)
        return new_room

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
