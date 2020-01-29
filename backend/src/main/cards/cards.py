from backend.src.main.cards.card import Card


class Cards(Card):

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        self.cards.remove(card)
