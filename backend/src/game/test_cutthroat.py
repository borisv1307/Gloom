import pytest

from game.cutthroat import Cutthroat
from game.values import RandomEnemyCardValues


@pytest.fixture(autouse=True)
def cutthroat():
    cutthroat = Cutthroat()
    return cutthroat


def test_cutthroat_node_1_is_monster(cutthroat):
    assert cutthroat.map_values[1] == RandomEnemyCardValues.MONSTER


def test_cutthroat_node_12_is_treasure(cutthroat):
    assert cutthroat.map_values[12] == RandomEnemyCardValues.TREASURE


def test_cutthroat_node_13_raises_key_error(cutthroat):
    with pytest.raises(KeyError) as key_error:
        cutthroat.map_values[13]


def test_cutthroat_node_0_raises_key_error(cutthroat):
    with pytest.raises(KeyError) as key_error:
        cutthroat.map_values[0]
