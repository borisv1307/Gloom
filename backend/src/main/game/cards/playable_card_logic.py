class PlayableCardLogic:
    def __init__(self, hand):
        self.hand = hand
        self.discard = []
        self.lost = []
        if not self.hand:
            raise ValueError('non card type')

    def hand_to_discard(self, card_name):
        self.move_card_by_name(card_name, self.hand, self.discard)

    def hand_to_lost(self, card_name):
        self.move_card_by_name(card_name, self.hand, self.lost)

    def discard_to_lost(self, card_name):
        self.move_card_by_name(card_name, self.discard, self.lost)

    def discard_to_hand(self, card_name):
        self.move_card_by_name(card_name, self.discard, self.hand)

    def lost_to_discard(self, card_name):
        self.move_card_by_name(card_name, self.lost, self.discard)

    def lost_to_hand(self, card_name):
        self.move_card_by_name(card_name, self.lost, self.hand)

    def move_card_by_name(self, card_name, source, destination):
        for card in source:
            if self.does_card_have_name(card, card_name):
                self.move_card(card, source, destination)
                break

    @staticmethod
    def does_card_have_name(card, name):
        return card.name == name

    @staticmethod
    def move_card(card, source, destination):
        source.remove(card)
        destination.append(card)
