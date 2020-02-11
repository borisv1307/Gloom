from backend.src.main.game.monster.concrete_monster_cards.archaic import Archaic
from backend.src.main.game.monster.concrete_monster_cards.corrupted import Corrupted
from backend.src.main.game.monster.concrete_monster_cards.crushing import Crushing
from backend.src.main.game.monster.concrete_monster_cards.cutthroat import Cutthroat
from backend.src.main.game.monster.concrete_monster_cards.defied import Defied
from backend.src.main.game.monster.concrete_monster_cards.drowned import Drowned
from backend.src.main.game.monster.concrete_monster_cards.foggy import Foggy
from backend.src.main.game.monster.concrete_monster_cards.fortified import Fortified
from backend.src.main.game.monster.concrete_monster_cards.frigid import Frigid
from backend.src.main.game.monster.concrete_monster_cards.hopeless import Hopeless
from backend.src.main.game.monster.concrete_monster_cards.horrific import Horrific
from backend.src.main.game.monster.concrete_monster_cards.infected import Infected
from backend.src.main.game.monster.concrete_monster_cards.mangy import Mangy
from backend.src.main.game.monster.concrete_monster_cards.putrid import Putrid
from backend.src.main.game.monster.concrete_monster_cards.rotting import Rotting
from backend.src.main.game.monster.concrete_monster_cards.scaled import Scaled
from backend.src.main.game.monster.concrete_monster_cards.tribal import Tribal
from backend.src.main.game.monster.concrete_monster_cards.unstable import Unstable
from backend.src.main.game.monster.concrete_monster_cards.venomous import Venomous
from backend.src.main.game.monster.concrete_monster_cards.wild import Wild


def get_all_monsters():
    return [
        Archaic(),
        Corrupted(),
        Crushing(),
        Cutthroat(),
        Defied(),
        Drowned(),
        Foggy(),
        Fortified(),
        Frigid(),
        Hopeless(),
        Horrific(),
        Infected(),
        Mangy(),
        Putrid(),
        Rotting(),
        Scaled(),
        Tribal(),
        Unstable(),
        Venomous(),
        Wild()
    ]
