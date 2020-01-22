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

