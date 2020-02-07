
class PlayableCardLogic:
    def __init__(self, hand):
        self.hand = hand
        self.discard = []
        self.lost = []

    def hand_to_discard(self, card_name):
        for card in self.hand:
            if card.name == card_name:
                self.hand.remove(card)
                self.discard.append(card)
                break

    def hand_to_lost(self, card_name):
        for card in self.hand:
            if card.name == card_name:
                self.hand.remove(card)
                self.lost.append(card)
                break

    def discard_to_lost(self, card_name):
        for card in self.discard:
            if card.name == card_name:
                self.discard.remove(card)
                self.lost.append(card)
                break

    def discard_to_hand(self, card_name):
        for card in self.discard:
            if card.name == card_name:
                self.discard.remove(card)
                self.hand.append(card)
                break

    def lost_to_discard(self, card_name):
        for card in self.lost:
            if card.name == card_name:
                self.lost.remove(card)
                self.discard.append(card)
                break

    def lost_to_hand(self, card_name):
        for card in self.lost:
            if card.name == card_name:
                self.lost.remove(card)
                self.hand.append(card)
                break
