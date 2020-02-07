"""Test case for Cutthroat Monster Card Class:
Test cases for Cutthroat Monster Card
"""
import pytest

from backend.src.main.game.cutthroat import Cutthroat
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


@pytest.fixture(name='cutthroat', autouse=True)
def create_cutthroat():
    """Getting Cutthroat object"""
    cutthroat = Cutthroat()
    return cutthroat


def test_if_cutthroat_can_be_instantaited():
    """ ABC """
    cut_throat = Cutthroat()


def test_cutthroat_node_1_is_monster(cutthroat):
    """Testing if node 1 is Monster"""
    assert cutthroat.map_values[NumberedRoomTileValues.ONE] == DungeonCardValues.MONSTER


def test_cutthroat_node_12_is_treasure(cutthroat):
    """Testing if node 12 is Treasure"""
    assert cutthroat.map_values[NumberedRoomTileValues.TWELVE] == DungeonCardValues.TREASURE


def test_cutthroat_node_13_raises_key_error(cutthroat):
    """Testing if node 13 Raises Error"""
    with pytest.raises(KeyError):
        cutthroat.map_values[13]


def test_cutthroat_node_0_raises_key_error(cutthroat):
    """Testing if node 0 Raises Error"""
    with pytest.raises(KeyError):
        cutthroat.map_values[0]
