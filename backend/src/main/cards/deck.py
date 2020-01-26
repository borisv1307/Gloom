from backend.src.main.cards import card
from backend.src.main.cards.hand import Hand
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.lost import Lost


class Deck:
    def __init__(self):
        self.card_deck = []

    def hand_to_discard(self):
        self.hand.remove(card.name)
        self.discard.add(card.name)

    def discard_to_lost(self):
        self.discard.remove(card.name)
        self.lost.add(card.name)

    def discard_to_hand(self):
        self.discard.remove(card.name)
        self.hand.add(card.name)
