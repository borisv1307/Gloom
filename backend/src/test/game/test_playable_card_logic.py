import pytest
from backend.src.main.game.cards.card import Card
from backend.src.main.game.cards.playable_card_logic import PlayableCardLogic


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
    assert len(playable_card_logic.hand) == 1


def test_discard_starts_empty(playable_card_logic):
    assert len(playable_card_logic.discard) == 0


def test_lost_starts_empty(playable_card_logic):
    assert len(playable_card_logic.lost) == 0


def test_hand_moves_to_discard(playable_card_logic):
    playable_card_logic.hand_to_discard("1")
    assert len(playable_card_logic.hand) == 0
    assert len(playable_card_logic.discard) == 1
    assert playable_card_logic.discard[0]


def test_lost_moves_to_discard(playable_card_logic):
    playable_card_logic.hand_to_lost("1")
    playable_card_logic.lost_to_discard("1")
    assert len(playable_card_logic.lost) == 0
    assert len(playable_card_logic.discard) == 1
    assert playable_card_logic.discard[0]


def test_hand_moves_to_discard_with_many_cards():
    card_one = Card("1")
    card_two = Card("2")
    card_three = Card("3")
    card_four = Card("4")
    card_five = Card("5")
    hand = [card_one, card_two, card_three, card_four, card_five]
    playable_card_logic = PlayableCardLogic(hand)
    playable_card_logic.hand_to_discard("3")
    assert len(playable_card_logic.hand) == 4
    assert len(playable_card_logic.discard) == 1
    assert playable_card_logic.discard.__getitem__(0) == card_three


def test_discard_moves_to_lost(playable_card_logic):
    playable_card_logic.hand_to_discard("1")
    playable_card_logic.discard_to_lost("1")
    assert len(playable_card_logic.discard) == 0
    assert len(playable_card_logic.lost) == 1
    assert playable_card_logic.lost[0]


def test_discard_moves_to_hand(playable_card_logic):
    playable_card_logic.hand_to_discard("1")
    assert len(playable_card_logic.discard) == 1
    playable_card_logic.discard_to_hand("1")
    assert len(playable_card_logic.discard) == 0
    assert len(playable_card_logic.hand) == 1
    assert playable_card_logic.hand[0]


def test_lost_moves_to_hand(playable_card_logic):
    playable_card_logic.hand_to_lost("1")
    assert len(playable_card_logic.lost) == 1
    playable_card_logic.lost_to_hand("1")
    assert len(playable_card_logic.lost) == 0
    assert len(playable_card_logic.hand) == 1
    assert playable_card_logic.hand[0]


def test_hand_moves_to_lost(playable_card_logic):
    playable_card_logic.hand_to_lost("1")
    assert len(playable_card_logic.hand) == 0
    assert len(playable_card_logic.lost) == 1
    assert playable_card_logic.lost[0]


def test_create_playable_card_logic_with_non_card_type_raises_value_error():
    with pytest.raises(ValueError, match='wrong input value'):
        PlayableCardLogic(None)
