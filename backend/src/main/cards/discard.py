"""Discard class."""


class Discard:
    """Discard class for Discard card pile."""

    def __init__(self):
        self.cards = []

    def add(self, card):
        """Add cards to discard."""
        self.cards.append(card)

    def remove(self, card):
        """Remove cards from discard."""
        self.cards.remove(card)
