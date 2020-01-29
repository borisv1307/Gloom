from backend.src.main.cards.card import Card
from backend.src.main.cards.cards import Cards


def test_cards_starts_empty():
    assert Cards().cards.__len__() == 0


def test_add_card_to_card_deck():
    cards = Cards()
    card_one = Card("card1")
    cards.add(card_one)
    assert cards.cards.__len__() == 1
    assert cards.cards.__getitem__(0) == card_one


def test_remove_card_from_card_deck():
    cards = Cards()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    cards.add(card_one)
    cards.add(card_two)
    cards.add(card_three)

    cards.remove(card_two)
    assert cards.cards.__len__() == 2
    assert cards.cards.__getitem__(0) == card_one
    assert cards.cards.__getitem__(1) == card_three
