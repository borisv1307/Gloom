import pytest

from backend.src.main.game.concrete_monster_cards.cutthroat import Cutthroat
from backend.src.main.game.values import DungeonCardValues, NumberedRoomTileValues


@pytest.fixture(autouse=True)
def cutthroat():
    cutthroat = Cutthroat()
    return cutthroat


def test_if_cutthroat_can_be_instantaited():
    cut_throat = Cutthroat()


def test_cutthroat_node_1_is_monster(cutthroat):
    assert cutthroat.map_values[NumberedRoomTileValues.ONE] == DungeonCardValues.MONSTER


def test_cutthroat_node_12_is_treasure(cutthroat):
    assert cutthroat.map_values[NumberedRoomTileValues.TWELVE] == DungeonCardValues.TREASURE


def test_cutthroat_node_13_raises_key_error(cutthroat):
    with pytest.raises(KeyError):
        cutthroat.map_values[13]


def test_cutthroat_node_0_raises_key_error(cutthroat):
    with pytest.raises(KeyError):
        cutthroat.map_values[0]
