"""Lost class."""


class Lost:
    """Lost class for Lost card pile."""

    def __init__(self):
        self.cards = []

    def add(self, card):
        """Add cards to lost."""
        self.cards.append(card)

    def remove(self, card):
        """Remove cards from lost."""
        self.cards.remove(card)
