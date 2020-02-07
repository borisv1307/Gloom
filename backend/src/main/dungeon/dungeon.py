from backend.src.main.game.cutthroat import Cutthroat
from backend.src.main.room import concrete_rooms
from backend.src.main.room.constructed_room import ConstructedRoom
from backend.src.main.room.waypoint.waypoint_pojo import WaypointPOJO
from backend.src.main.tile.tile_geometry import TileGeometry


class RandomDungeonGenerator:
    def __init__(self, random_wrapper):
        self.random_wrapper = random_wrapper
        self.monster_cards = [Cutthroat() for _ in range(20)]
        self.room_cards = concrete_rooms.get_all_rooms()
        self.constructed_rooms = []

    def select_first_room(self):
        chosen_monster = self.select_monster_card()
        chosen_room = self.select_room_card()
        new_constructed_room = self.construct_room(chosen_room, chosen_monster)
        self.constructed_rooms.append(new_constructed_room)

    def select_room_by_waypoint(self, waypoint: WaypointPOJO):
        if not waypoint.has_exit(self.constructed_rooms[-1]):
            raise ValueError(
                "Cannot use provided waypoint as room does not have corresponding exit."
            )
        chosen_room = self.select_room_card()
        while not waypoint.has_entrance(chosen_room):
            chosen_room = self.select_room_card()

        chosen_monster = self.select_monster_card()

        new_constructed_room = self.construct_room(chosen_room, chosen_monster)
        new_constructed_room = TileGeometry.overlay_room_a_on_room_b(self.constructed_rooms[-1],
                                                                     new_constructed_room,
                                                                     waypoint)
        self.constructed_rooms.append(new_constructed_room)

    def construct_room(self, room, monster):
        self.pop_room_card(room)
        self.pop_monster_card(monster)

        return ConstructedRoom(room, monster)

    def select_room_card(self):
        chosen_room_idx = self.random_wrapper.randrange(len(self.room_cards))
        return self.room_cards[chosen_room_idx]

    def select_monster_card(self):
        chosen_monster_idx = self.random_wrapper.randrange(len(self.monster_cards))
        return self.monster_cards[chosen_monster_idx]

    def pop_room_card(self, room):
        return self.room_cards.pop(self.room_cards.index(room))

    def pop_monster_card(self, monster):
        return self.monster_cards.pop(self.monster_cards.index(monster))
