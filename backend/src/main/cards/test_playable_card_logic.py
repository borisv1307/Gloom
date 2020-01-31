from backend.src.main.cards.cards import Cards
from backend.src.main.cards.card import Card
from backend.src.main.cards.playable_card_logic import PlayableCardLogic


def test_hand_discard_lost_starts_empty():
    assert PlayableCardLogic().hand.__len__() == 0
    assert PlayableCardLogic().discard.__len__() == 0
    assert PlayableCardLogic().lost.__len__() == 0


def test_hand_moves_to_discard():
    card = Card
    PlayableCardLogic.hand = Cards()
    PlayableCardLogic.discard = Cards()
    card_one = card("card1")
    PlayableCardLogic.hand.append(card_one)
    assert PlayableCardLogic.hand.cards.__len__() == 1

    PlayableCardLogic.hand.remove(card_one)
    PlayableCardLogic.discard.append(card_one)
    assert PlayableCardLogic.hand.cards.__len__() == 0
    assert PlayableCardLogic.discard.cards.__len__() == 1
    assert PlayableCardLogic.discard.cards.__getitem__(0) == card_one


def test_discard_moves_to_lost():
    card = Card
    PlayableCardLogic.lost = Cards()
    PlayableCardLogic.discard = Cards()
    card_one = card("card1")
    card_two = card("card2")
    PlayableCardLogic.discard.append(card_two)
    PlayableCardLogic.discard.append(card_one)
    assert PlayableCardLogic.discard.cards.__len__() == 2

    PlayableCardLogic.discard.remove(card_one)
    PlayableCardLogic.lost.append(card_one)
    assert PlayableCardLogic.discard.cards.__len__() == 1
    assert PlayableCardLogic.lost.cards.__len__() == 1
    assert PlayableCardLogic.discard.cards.__getitem__(0) == card_two
    assert PlayableCardLogic.lost.cards.__getitem__(0) == card_one

    PlayableCardLogic.discard.remove(card_two)
    PlayableCardLogic.lost.append(card_two)
    assert PlayableCardLogic.discard.cards.__len__() == 0
    assert PlayableCardLogic.lost.cards.__len__() == 2
    assert PlayableCardLogic.lost.cards.__getitem__(1) == card_two


def test_discard_moves_to_hand():
    card = Card
    PlayableCardLogic.hand = Cards()
    PlayableCardLogic.discard = Cards()
    card_one = card("card1")
    card_two = card("card2")
    card_three = card("card3")
    PlayableCardLogic.discard.append(card_two)
    PlayableCardLogic.discard.append(card_one)
    PlayableCardLogic.discard.append(card_three)
    assert PlayableCardLogic.discard.cards.__len__() == 3

    PlayableCardLogic.discard.remove(card_one)
    PlayableCardLogic.hand.append(card_one)
    assert PlayableCardLogic.discard.cards.__len__() == 2
    assert PlayableCardLogic.hand.cards.__len__() == 1
    assert PlayableCardLogic.discard.cards.__getitem__(0) == card_two
    assert PlayableCardLogic.discard.cards.__getitem__(1) == card_three
    assert PlayableCardLogic.hand.cards.__getitem__(0) == card_one
