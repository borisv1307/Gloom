"""Values for Enemy Card Values:
Card Values
"""
from enum import Enum


class RandomEnemyCardValues(Enum):
    """ Class for Random Enemy Card Values"""
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
