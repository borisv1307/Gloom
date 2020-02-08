class Cards:
    def __init__(self):
        self.card_deck = []

    def append(self, card):
        self.card_deck.append(card)

    def remove(self, card):
        self.card_deck.remove(card)
