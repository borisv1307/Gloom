from backend.src.main.cards.card import Card
from backend.src.main.cards.cards import Cards


class PlayableCardLogic(Cards):
    def __init__(self):
        self.hand = []
        self.discard = []
        self.lost = []

    def hand_to_discard(self, card: Card):
        self.hand.remove(card.name)
        self.discard.add(card.name)

    def discard_to_lost(self, card: Card):
        self.discard.remove(card.name)
        self.lost.add(card.name)

    def discard_to_hand(self, card: Card):
        self.discard.remove(card.name)
        self.hand.add(card.name)
