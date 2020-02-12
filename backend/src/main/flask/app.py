""" FILE: foo.py
    DESC: Flask routing file. Contains the flask application object
"""
import json

from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.serializer.dungeon_serializer import DungeonSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer
from backend.src.main.wrappers.random_wrapper import RandomWrapper
from flask import Flask


class Handler:  # pylint: disable=too-few-public-methods
    """ Class for flask app object """
    app = Flask(__name__)

    @staticmethod
    def index():
        """ Returns index page """
        return "Hello, world!"

    @staticmethod
    def start():
        rdg = RandomDungeonGenerator(RandomWrapper())
        rdg.select_first_room()
        output = DungeonSerializer(RoomSerializer(TileSerializer(EnumSerializer()))).serialize(rdg)

        return json.dumps(output)


def get_handler():
    """ Initializes the handler and adds endpoint mappings """
    handler = Handler()

    # URL Routes
    handler.app.add_url_rule('/', 'index', handler.index)
    handler.app.add_url_rule('/start', 'start', handler.start)

    return handler


if __name__ == "__main__":
    HANDLER = get_handler()

    # App Config
    HANDLER.app.run(host='0.0.0.0', port=5000, debug=True)
