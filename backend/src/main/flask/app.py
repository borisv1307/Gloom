# pylint:disable=wrong-import-order,line-too-long
import json

from backend.src.main.game.dungeon.random_dungeon_generator import RandomDungeonGenerator
from backend.src.main.serializer.dungeon_serializer import DungeonSerializer
from backend.src.main.serializer.enum_serializer import EnumSerializer
from backend.src.main.serializer.room_serializer import RoomSerializer
from backend.src.main.serializer.tile_serializer import TileSerializer
from backend.src.main.wrappers.random_wrapper import RandomWrapper
from flask import Flask


class Handler:
    app = Flask(__name__)

    @staticmethod
    def index():
        return "Hello, world!"

    @staticmethod
    def start():
        rdg = RandomDungeonGenerator(RandomWrapper())
        rdg.select_first_room()
        output = DungeonSerializer(RoomSerializer(TileSerializer(EnumSerializer()), EnumSerializer())).serialize(rdg)

        return json.dumps(output)


def get_handler():
    handler = Handler()

    handler.app.add_url_rule('/', 'index', handler.index)
    handler.app.add_url_rule('/start', 'start', handler.start)

    return handler


if __name__ == "__main__":
    HANDLER = get_handler()
    HANDLER.app.run(host='0.0.0.0', port=5000, debug=True)
