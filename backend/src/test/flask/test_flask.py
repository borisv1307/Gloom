""" FILE: test_flask.py
    DESC: Contains tests for the application level items
"""

import unittest
from backend.src.main.flask.app import get_handler


class TestFlask(unittest.TestCase):
    """ Flask test class """

    def test_index(self):
        """ Test that index returns status_code 200 """
        handler = get_handler()
        tester = handler.app.test_client(self)
        response = tester.get('/', content_type='html/text')

        self.assertEqual(response.status_code, 200)
