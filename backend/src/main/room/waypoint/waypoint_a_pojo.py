from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO


class WaypointA(WaypointPOJO):
    def __init__(self):
        super(WaypointA, self).__init__(
            DungeonCardValues.ENTRANCE_A,
            DungeonCardValues.EXIT_A
        )
