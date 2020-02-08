from backend.src.main.game.monster.values import UniqueDungeonCardValues
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO


class WaypointB(WaypointPOJO):
    def __init__(self):
        super(WaypointB, self).__init__(
            UniqueDungeonCardValues.ENTRANCE_B,
            UniqueDungeonCardValues.EXIT_B
        )
