from backend.src.main.cards.card import Card
from backend.src.main.cards.hand import Hand
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.lost import Lost


class Deck:
    def __init__(self):
        self.card_deck = []
        self.hand = Hand
        self.discard = Discard
        self.lost = Lost

    def hand_to_discard(self):
        self.hand.remove(Card.get_name)
        self.discard.add(Card.get_name)

    def discard_to_lost(self):
        self.discard.remove(Card.get_name)
        self.lost.add(Card.get_name)

    def discard_to_hand(self):
        self.discard.remove(Card.get_name)
        self.hand.add(Card.get_name)
