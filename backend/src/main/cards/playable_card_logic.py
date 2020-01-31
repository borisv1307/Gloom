from backend.src.main.cards.card import Card


class PlayableCardLogic:
    def __init__(self):
        self.card = Card
        self.hand = []
        self.discard = []
        self.lost = []

    def hand_to_discard(self, card):
        self.hand.remove(card.name)
        self.discard.append(card.name)

    def discard_to_lost(self, card):
        self.discard.remove(card.name)
        self.lost.append(card.name)

    def discard_to_hand(self, card):
        self.discard.remove(card.name)
        self.hand.append(card.name)
