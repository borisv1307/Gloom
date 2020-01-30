from backend.src.main.game.cutthroat import Cutthroat
from backend.src.main.room.concrete_room_cards.den import Den
from backend.src.main.room.constructed_room import ConstructedRoom


class RandomDungeonGenerator: # pylint: disable=too-few-public-methods
    def __init__(self):
        self.monster_cards = [Cutthroat() for _ in range(20)]
        self.room_cards = [Den() for _ in range(20)]
        self.constructed_rooms = []

    def select_first_room(self, random_wrapper):
        chosen_monster_idx = random_wrapper.randrange(len(self.room_cards))
        chosen_room_idx = random_wrapper.randrange(len(self.monster_cards))

        chosen_monster = self.monster_cards.pop(chosen_monster_idx)
        chosen_room = self.room_cards.pop(chosen_room_idx)

        self.constructed_rooms.append(ConstructedRoom(chosen_room, chosen_monster))
