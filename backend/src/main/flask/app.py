""" FILE: foo.py
    DESC: Flask routing file. Contains the flask application object
"""

from flask import Flask


class Handler:  # pylint: disable=too-few-public-methods
    """ Class for flask app object """
    app = Flask(__name__)

    @staticmethod
    def index():
        """ Returns index page """
        return "Hello, world!"


def get_handler():
    """ Initializes the handler and adds endpoint mappings """
    handler = Handler()

    # URL Routes
    handler.app.add_url_rule('/', 'index', handler.index)

    return handler


if __name__ == "__main__":
    HANDLER = get_handler()

    # App Config
    HANDLER.app.run(host='0.0.0.0', port=5000, debug=True)
