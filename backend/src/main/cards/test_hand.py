from backend.src.main.cards.hand import Hand
from backend.src.main.cards.card import Card


def test_hand_starts_empty():
    assert Hand().cards.__len__() == 0


def test_add_card_to_hand():
    hand = Hand()
    card = Card("Name")
    hand.add(card)
    assert hand.cards.__len__() == 1
    assert hand.cards.__getitem__(0) == card


def test_remove_specific_card():
    hand = Hand()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    hand.add(card_one)
    hand.add(card_two)
    hand.add(card_three)

    hand.remove("card2")
    assert hand.cards.__len__() == 2
    assert hand.cards.__getitem__(0) == card_one
    assert hand.cards.__getitem__(1) == card_three
