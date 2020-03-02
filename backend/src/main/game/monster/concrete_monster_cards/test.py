from backend.src.main.game.monster.values import MonsterValues

dictionary = {}

def toImage(string):
    title_string = string.title()
    split_title_string = title_string.split()
    hyphened_string = "-".join(split_title_string)
    return hyphened_string


for monster in MonsterValues:
    key = monster.value
    value = "../Images/{}.png".format(toImage(monster.value))
    dictionary[key] = value

import json
output = json.dumps(dictionary)
print(output)