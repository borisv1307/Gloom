from enum import Enum


class DungeonCardValues(Enum):
    CHARACTER = 'character'
    WALL = 'wall'
    OBSTACLE = 'obstacle'
    TRAPS = 'trap'
    HAZARDOUS_TERRAIN = 'hazardous terrain'
    DIFFICULT_TERRAIN = 'dangerous terrain'
    WALL_LINE = 'wall line'
    EMPTY = 'empty'
    COIN = 'coin'
    TREASURE = '5 gold'


class MonsterValues(Enum):
    ANCIENT_ARTILLERY = 'ancient artillery'
    BANDIT_ARCHER = 'bandit archer'
    BANDIT_GUARD = 'bandit guard'
    BLACK_IMP = 'black imp'
    CAVE_BEAR = 'cave bear'
    CITY_ARCHER = 'city archer'
    CITY_GUARD = 'city guard'
    CULTIST = 'cultist'
    DEEP_TERROR = 'deep terror'
    EARTH_DEMON = 'earth demon'
    FLAME_DEMON = 'flame demon'
    FROST_DEMON = 'frost demon'
    FOREST_IMP = 'forest imp'
    GIANT_VIPER = 'giant viper'
    HARROWER_INFESTER = 'harrower infester'
    HOUND = 'hound'
    INOX_ARCHER = 'inox archer'
    INOX_GUARD = 'inox guard'
    INOX_SHAMAN = 'inox shaman'
    LIVING_BONES = 'living bones'
    LIVING_CORPSE = 'living corpse'
    LIVING_SPIRIT = 'living spirit'
    LURKER = 'lurker'
    OOZE = 'ooze'
    NIGHT_DEMON = 'night demon'
    RENDING_DRAKE = 'rending drake'
    SAVVAS_ICESTORM = 'savvas icestorm'
    SAVVAS_LAVAFLOW = 'savvas lavaflow'
    SPITTING_DRAKE = 'spitting drake'
    STONE_GOLEM = 'stone golem'
    SUN_DEMON = 'sun demon'
    VERMLING_SCOUT = 'vermling scout'
    VERMLING_SHAMAN = 'vermling shaman'
    WIND_DEMON = 'wind demon'


class UniqueTileValues(Enum):
    pass


class UniqueDungeonCardValues(DungeonCardValues, UniqueTileValues):
    ENTRANCE_A = 'entrance a'
    ENTRANCE_B = 'entrance b'
    EXIT_A = 'exit a'
    EXIT_B = 'exit b'


class NumberedRoomTileValues(UniqueTileValues):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'


class TrapIndicators(Enum):
    POISON = 'poison'
    WOUND = 'wound'
    IMMOBILIZE = 'immobilize'
    DISARM = 'disarm'
    STUN = 'stun'
    MUDDLE = 'muddle'
    CURSE = 'curse'
    DAMAGE = 'damage'
    INDICATOR = 'Trap_Indicators'
