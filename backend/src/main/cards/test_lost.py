"""Test for Lost card adding and removing cards."""
from backend.src.main.cards.card import Card
from backend.src.main.cards.lost import Lost


def test_lost_starts_empty():
    assert Lost().cards.__len__() == 0


def test_add_card_to_lost():
    lost = Lost()
    card = Card("Name")
    lost.add(card)
    assert lost.cards.__len__() == 1
    assert lost.cards.__getitem__(0) == card


def test_remove_specific_card():
    lost = Lost()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    lost.add(card_one)
    lost.add(card_two)
    lost.add(card_three)

    lost.remove(card_two)
    assert lost.cards.__len__() == 2
    assert lost.cards.__getitem__(0) == card_one
    assert lost.cards.__getitem__(1) == card_three

    lost.remove(card_one)
    assert lost.cards.__len__() == 1
    assert lost.cards.__getitem__(0) == card_three
