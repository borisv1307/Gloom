"""Test case for Cutthroat Class:
Test cases for Cutthroat Monster Card
"""
import pytest

from game.cutthroat import Cutthroat
from game.values import RandomEnemyCardValues


@pytest.fixture(autouse=True)
def cutthroat():
    """Getting Cutthroat object"""
    return Cutthroat()


def test_cutthroat_node_1_is_monster(cutthroat):
    """Testing if node 1 is Monster"""
    assert cutthroat.map_values[1] == RandomEnemyCardValues.MONSTER


def test_cutthroat_node_12_is_treasure(cutthroat):
    """Testing if node 12 is Treasure"""
    assert cutthroat.map_values[12] == RandomEnemyCardValues.TREASURE


def test_cutthroat_node_13_raises_key_error(cutthroat):
    """Testing if node 13 Raises Error"""
    with pytest.raises(KeyError):
        cutthroat.map_values[13]


def test_cutthroat_node_0_raises_key_error(cutthroat):
    """Testing if node 0 Raises Error"""
    with pytest.raises(KeyError):
        cutthroat.map_values[0]
