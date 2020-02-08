import pytest
from backend.src.main.game.monster.abstract_monster_card import AbstractMonsterCard
from backend.src.main.game.monster.concrete_monster_cards.cutthroat import Cutthroat
from backend.src.main.game.monster.values import DungeonCardValues, NumberedRoomTileValues


def test_if_cutthroat_can_be_instantiated(cutthroat):
    assert isinstance(cutthroat, Cutthroat)
    assert isinstance(cutthroat, AbstractMonsterCard)


def test_cutthroat_node_1_is_monster(cutthroat):
    assert cutthroat.map_values[NumberedRoomTileValues.ONE] == DungeonCardValues.MONSTER


def test_cutthroat_node_12_is_treasure(cutthroat):
    assert cutthroat.map_values[NumberedRoomTileValues.TWELVE] == DungeonCardValues.TREASURE


# pylint: disable=pointless-statement
def test_cutthroat_node_13_raises_key_error(cutthroat):
    with pytest.raises(KeyError):
        cutthroat.map_values[13]


def test_cutthroat_node_0_raises_key_error(cutthroat):
    with pytest.raises(KeyError):
        cutthroat.map_values[0]
