from backend.src.main.cards.discard import Discard
from backend.src.main.cards.card import Card


def test_discard_starts_empty():
    assert Discard().cards.__len__() == 0


def test_add_card_to_discard():
    discard = Discard()
    card = Card("Name")
    discard.add(card)
    assert discard.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card

