from enum import Enum


class RandomEnemyCardValues(Enum):
    MONSTER = 'monster'
    CHARACTER = 'character'
    WALL = 'wall'
    OBSTACLE = 'obstacle'
    TRAPS = 'trap'
    HAZARDOUS_TERRAIN = 'hazardous terrain'
    DIFFICULT_TERRAIN = 'difficult terrain'
    WALL_LINE = 'wall line'
    EMPTY = 'empty'
    COIN = '1'
    TREASURE = '5 gold'
