from backend.src.main.cards.card import Card
from backend.src.main.cards.hand import Hand
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.lost import Lost


class Deck:
    def __init__(self):
        self.card_deck = []
        self.hand = Hand.Card = []
        self.discard = Discard.Card = []
        self.lost = Lost.Card = []

    def hand_to_discard(self, card: Card):
        self.hand.remove(card.name)
        self.discard.add(card.name)

    def discard_to_lost(self, card: Card):
        self.discard.remove(card.name)
        self.lost.add(card.name)

    def discard_to_hand(self, card: Card):
        self.discard.remove(card.name)
        self.hand.add(card.name)
