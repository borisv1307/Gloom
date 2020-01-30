from unittest.mock import MagicMock, call

from backend.src.main.dungeon.dungeon import RandomDungeonGenerator
from backend.src.main.game.random_monster_card import AbstractMonsterCard
from backend.src.main.room.constructed_room import ConstructedRoom
from backend.src.main.room.room import AbstractRoomCard
from backend.src.main.wrappers.random_wrapper import RandomWrapper


def test_dungeon_generator_has_20_monster_cards():
    dungeon_generator = RandomDungeonGenerator()
    assert len(dungeon_generator.monster_cards) == 20
    for item in dungeon_generator.monster_cards:
        assert isinstance(item, AbstractMonsterCard)


def test_dungeon_generator_has_20_room_cards():
    dungeon_generator = RandomDungeonGenerator()
    assert len(dungeon_generator.room_cards) == 20
    for item in dungeon_generator.room_cards:
        assert isinstance(item, AbstractRoomCard)


def test_dungeon_generator_has_no_rooms_initially():
    dungeon_generator = RandomDungeonGenerator()
    assert not dungeon_generator.constructed_rooms


def test_select_first_room_reduces_deck_sizes_by_one():
    dungeon_generator = RandomDungeonGenerator()
    dungeon_generator.select_first_room(RandomWrapper())
    assert len(dungeon_generator.room_cards) == 19
    assert len(dungeon_generator.monster_cards) == 19


def test_select_first_room_adds_constructed_room():
    dungeon_generator = RandomDungeonGenerator()
    dungeon_generator.select_first_room(RandomWrapper())
    assert len(dungeon_generator.constructed_rooms) == 1
    assert isinstance(dungeon_generator.constructed_rooms[0], ConstructedRoom)


def test_select_first_room_calls_random_choice_twice():
    dungeon_generator = RandomDungeonGenerator()

    # Note, we depend on the order of calls
    mock = MagicMock()
    mock.side_effect = [0, 0]

    random_wrapper = RandomWrapper()
    random_wrapper.randrange = mock

    expected_room_argument = 20
    expected_monster_argument = 20
    expected_calls = [call(expected_room_argument), call(expected_monster_argument)]

    dungeon_generator.select_first_room(random_wrapper)

    mock.assert_has_calls(expected_calls)
    assert mock.call_count == 2
