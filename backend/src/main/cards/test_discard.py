"""Test for Discard card adding and removing cards."""
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.card import Card


def test_discard_starts_empty():
    """Test if discard starts empty."""
    assert Discard().cards.__len__() == 0


def test_add_card_to_discard():
    """Test adding cards to discard."""
    discard = Discard()
    card = Card("Name")
    discard.add(card)
    assert discard.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card


def test_remove_specific_card():
    """Test removing cards."""
    discard = Discard()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    discard.add(card_one)
    discard.add(card_two)
    discard.add(card_three)

    discard.remove(card_two)
    assert discard.cards.__len__() == 2
    assert discard.cards.__getitem__(0) == card_one
    assert discard.cards.__getitem__(1) == card_three

    discard.remove(card_one)
    assert discard.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card_three
