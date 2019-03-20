import os
import unittest

from app import createapp
from ...api.v2.models import create_tables, drop_tables, create_admin

#urls for user endpoints
REGISTER_URL = 'api/v1/v2/user'
SINGLE_USER_URL = 'api/v1/v2/eminem@shadyrecords.com'
DELETE_USER_URL = 'api/v1/v2/eugenecrabs@bikinibottom.com'
USERS_URL = 'api/v1/v2/users'

class BaseTest(unittest.TestCase):
    '''initializes data and env for the test modules'''
    def setUp(self):
        '''sets up the test client'''
        self.app = createapp(os.getenv('APP_SETTINGS'))
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        with self.app.app_context():
            drop_tables()
            create_tables()
        # variables for the user endpoints;
        # including but not limited to: logging in and signing up

        self.valid_entry = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

    def tearDown(self):
        '''removes all the testing data created'''
        drop_tables()
        return "all clear"
