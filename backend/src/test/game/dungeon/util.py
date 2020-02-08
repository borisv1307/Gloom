# pylint: disable=inconsistent-return-statements
from backend.src.main.game.room.waypoint.waypoint_a_pojo import WaypointA


def get_room_with_exit_a(dungeon):
    waypoint_a = WaypointA()
    for room in dungeon.room_cards:
        if waypoint_a.has_exit(room):
            return room
