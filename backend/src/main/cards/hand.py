"""Hand class."""


class Hand:
    """Hand class for Hand card pile."""

    def __init__(self):
        self.cards = []

    def add(self, card):
        """Add cards to hand."""
        self.cards.append(card)

    def remove(self, card):
        """Remove cards from hand."""
        self.cards.remove(card)
