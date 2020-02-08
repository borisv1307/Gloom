import pytest
from backend.src.main.cards.card import Card
from backend.src.main.cards.playable_card_logic import PlayableCardLogic


@pytest.fixture(name='card')
def create_card():
    card = Card("1")
    return card


@pytest.fixture(name='playable_card_logic')
def create_playable_card_logic(card):
    hand = [card]
    playable_card_logic_hand = PlayableCardLogic(hand)
    return playable_card_logic_hand


def test_starts_with_hand(playable_card_logic):
    assert playable_card_logic.hand.__len__() == 1


def test_discard_starts_empty(playable_card_logic):
    assert playable_card_logic.discard.__len__() == 0


def test_lost_starts_empty(playable_card_logic):
    assert playable_card_logic.lost.__len__() == 0


def test_hand_moves_to_discard(playable_card_logic, card):
    playable_card_logic.hand_to_discard("1")
    assert playable_card_logic.hand.__len__() == 0
    assert playable_card_logic.discard.__len__() == 1
    assert playable_card_logic.discard.__getitem__(0) == card


def test_lost_moves_to_discard(playable_card_logic, card):
    playable_card_logic.hand_to_lost("1")
    playable_card_logic.lost_to_discard("1")
    assert playable_card_logic.lost.__len__() == 0
    assert playable_card_logic.discard.__len__() == 1
    assert playable_card_logic.discard.__getitem__(0) == card


def test_hand_moves_to_discard_with_many_cards():
    card_one = Card("1")
    card_two = Card("2")
    card_three = Card("3")
    card_four = Card("4")
    card_five = Card("5")
    hand = [card_one, card_two, card_three, card_four, card_five]
    playable_card_logic = PlayableCardLogic(hand)
    playable_card_logic.hand_to_discard("3")
    assert playable_card_logic.hand.__len__() == 4
    assert playable_card_logic.discard.__len__() == 1
    assert playable_card_logic.discard.__getitem__(0) == card_three


def test_discard_moves_to_lost(playable_card_logic, card):
    playable_card_logic.hand_to_discard("1")
    playable_card_logic.discard_to_lost("1")
    assert playable_card_logic.discard.__len__() == 0
    assert playable_card_logic.lost.__len__() == 1
    assert playable_card_logic.lost.__getitem__(0) == card


def test_discard_moves_to_hand(playable_card_logic, card):
    playable_card_logic.discard_to_hand("1")
    assert playable_card_logic.discard.__len__() == 0
    assert playable_card_logic.hand.__len__() == 1
    assert playable_card_logic.hand.__getitem__(0) == card


def test_lost_moves_to_hand(playable_card_logic, card):
    playable_card_logic.lost_to_hand("1")
    assert playable_card_logic.lost.__len__() == 0
    assert playable_card_logic.hand.__len__() == 1
    assert playable_card_logic.hand.__getitem__(0) == card


def test_hand_moves_to_lost():
    hand = []
    playable_card_logic = PlayableCardLogic(hand)
    card = Card("4")
    hand.append(card)
    playable_card_logic.hand_to_lost("4")
    assert playable_card_logic.hand.__len__() == 0
    assert playable_card_logic.lost.__len__() == 1
    assert playable_card_logic.lost.__getitem__(0) == card
