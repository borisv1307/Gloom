from backend.src.main.game.room.room import AbstractRoomCard
from backend.src.main.game.room.waypoint.waypoint_pojo import WaypointPOJO
from backend.src.main.game.tile.center_tile import CenterTile
from backend.src.main.game.tile.shift_tile import ShiftTile


class TileGeometry:
    MAX_ROTATIONS = 6

    @staticmethod
    def overlay_room_a_on_room_b(room_a, room_b, waypoint_pojo: WaypointPOJO):
        current_room_b = room_b
        for _ in range(TileGeometry.MAX_ROTATIONS):
            new_room_b = TileGeometry \
                .center_room_a_on_room_b_by_waypoint(room_a, current_room_b, waypoint_pojo)
            new_room_b = waypoint_pojo.remove_entrance(new_room_b)
            if not TileGeometry.do_rooms_overlap(room_a, new_room_b):
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

    @staticmethod
    def center_room_a_on_room_b_by_waypoint(room_a, room_b, waypoint_pojo):
        intermediate_room_b = CenterTile.center_on_entrance(room_b, waypoint_pojo)
        room_a_exit = waypoint_pojo.get_exit(room_a)
        new_room_b = ShiftTile.shift_room_on_tile(intermediate_room_b, room_a_exit)
        return new_room_b
