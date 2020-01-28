"""Test for deck card adding and removing cards between decks."""
from backend.src.main.cards.hand import Hand
from backend.src.main.cards.discard import Discard
from backend.src.main.cards.lost import Lost
from backend.src.main.cards.card import Card
from backend.src.main.cards.deck import Deck


def test_deck_starts_empty():
    assert Deck().card_deck.__len__() == 0


def test_hand_moves_to_discard():
    hand = Hand()
    discard = Discard()
    card_one = Card("card1")
    hand.add(card_one)
    assert hand.cards.__len__() == 1

    hand.remove(card_one)
    discard.add(card_one)
    assert hand.cards.__len__() == 0
    assert discard.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card_one


def test_discard_moves_to_lost():
    lost = Lost()
    discard = Discard()
    card_one = Card("card1")
    card_two = Card("card2")
    discard.add(card_two)
    discard.add(card_one)
    assert discard.cards.__len__() == 2

    discard.remove(card_one)
    lost.add(card_one)
    assert discard.cards.__len__() == 1
    assert lost.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card_two
    assert lost.cards.__getitem__(0) == card_one

    discard.remove(card_two)
    lost.add(card_two)
    assert discard.cards.__len__() == 0
    assert lost.cards.__len__() == 2
    assert lost.cards.__getitem__(1) == card_two


def test_discard_moves_to_hand():
    hand = Hand()
    discard = Discard()
    card_one = Card("card1")
    card_two = Card("card2")
    card_three = Card("card3")
    discard.add(card_two)
    discard.add(card_one)
    discard.add(card_three)
    assert discard.cards.__len__() == 3

    discard.remove(card_one)
    hand.add(card_one)
    assert discard.cards.__len__() == 2
    assert hand.cards.__len__() == 1
    assert discard.cards.__getitem__(0) == card_two
    assert discard.cards.__getitem__(1) == card_three
    assert hand.cards.__getitem__(0) == card_one
