import unittest

from app import createapp

#urls for user endpoints
REGISTER_URL = 'api/v1/v2/user'
SINGLE_USER_URL = 'api/v1/v2/eminem@shadyrecords.com'
DELETE_USER_URL = 'api/v1/v2/eugenecrabs@bikinibottom.com'
USERS_URL = 'api/v1/v2/users'

class BaseTest(unittest.TestCase):
    '''initializes data and env for the test modules'''
    def setUp(self):
        '''sets up the test client'''
        self.app = createapp('testing').test_client()