from backend.src.main.game.cards.card import Card
from backend.src.main.game.cards.cards import Cards


def test_cards_starts_empty():
    assert not Cards().cards


def test_add_card_to_card_deck():
    cards = Cards()
    card_one = Card("card1")
    cards.append(card_one)
    assert len(cards.cards) == 1
    assert cards.cards[0]


def test_remove_card_from_card_deck():
    cards = Cards()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    cards.append(card_one)
    cards.append(card_two)
    cards.append(card_three)

    cards.remove(card_two)
    assert len(cards.cards) == 2
    assert cards.cards[0] == card_one
    assert cards.cards[1] == card_three
