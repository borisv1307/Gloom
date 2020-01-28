"""Deck class."""

from backend.src.main.cards.card import Card
from backend.src.main.cards.hand import Hand
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.lost import Lost


class Deck:
    """Deck class to handle the Hand, Discard, and Lost plies."""
    def __init__(self):
        self.card_deck = []
        self.hand = Hand.Card = []
        self.discard = Discard.Card = []
        self.lost = Lost.Card = []

    def hand_to_discard(self, card: Card):
        """Move cards from hand to discard."""
        self.hand.remove(card.name)
        self.discard.append(card.name)

    def discard_to_lost(self, card: Card):
        """Move cards from discard to lost."""
        self.discard.remove(card.name)
        self.lost.append(card.name)

    def discard_to_hand(self, card: Card):
        """Move cards from discard to lost."""
        self.discard.remove(card.name)
        self.hand.append(card.name)
