import unittest
from api import Bauart
from api import api
import os

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_DATABASE'),
}
class BauartTests(unittest.TestCase):
    def test_createBauart(self):
        connection = api.get_db_connection(**db_config)
        bauart = Bauart.create(connection)
        self.assertEquals(True, True)