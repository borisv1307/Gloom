from backend.src.main.game.values import DungeonCardValues
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO


class WaypointB(WaypointPOJO):
    def __init__(self):
        super(WaypointB, self).__init__(
            DungeonCardValues.ENTRANCE_B,
            DungeonCardValues.EXIT_B
        )
