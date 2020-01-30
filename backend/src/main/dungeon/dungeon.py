from backend.src.main.game.cutthroat import Cutthroat
from backend.src.main.room.concrete_room_cards.den import Den


class RandomDungeonGenerator:
    def __init__(self):
        self.monster_cards = [Cutthroat() for _ in range(20)]
        self.room_cards = [Den() for _ in range(20)]

