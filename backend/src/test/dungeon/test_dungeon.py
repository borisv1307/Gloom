from backend.src.main.dungeon.dungeon import RandomDungeonGenerator
from backend.src.main.game.random_monster_card import AbstractMonsterCard
from backend.src.main.room.room import AbstractRoomCard


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
