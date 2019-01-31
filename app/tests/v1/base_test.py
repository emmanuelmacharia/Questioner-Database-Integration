import unittest
import json

from app import createapp

# urls for user endpoints
REGISTER_URL = 'api/v1/register'
LOGIN_URL = 'api/v1/login'
SINGLE_USER_URL = 'api/v1/user/spongebobsquarepants@bikinibottom.sea'
NO_SINGLE_USER_URL = 'api/v1/user/spongebobsquarepants@bikin.sea'
DELETE_URL = 'api/v1/user/solera@knowerwe.com'
USERS_URL = 'api/v1/users'

# urls for meetup endpoints
CREATE_MEETUP_URL = 'api/v1/meetups'
ALL_MEETUPS_URL = 'api/v1/meetups/upcoming'
SINGLE_MEETUP_URL = 'api/v1/meetups/1'

# urls for question endpoints
BASE_QUESTION_URL = 'api/v1/question'
SINGLE_QUESTION_URL = 'api/v1/question/1'

# urls for rsvp endpoints
BASE_RSVP_URL = 'api/v1/rsvp'
SINGLE_RSVP_URL = 'api/v1/rsvp/1'


class BaseTest(unittest.TestCase):
    '''initializes the data for the test modules'''

    def setUp(self):
        '''sets up the testclient'''
        self.app = createapp('testing').test_client()

        # variables for the user endpoints; 
        # including but limited to: logging in and signing up 

        self.valid_entry = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_firstname = {
            "firstname": "",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_lastname = {
            "firstname": "solo",
            "lastname": "",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_othername = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_email = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_phoneNumber = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "",
            "username": "capriereceor",
            "password": "despacito"
        }

        self.missing_username = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "",
            "password": "despacito"
        }

        self.missing_password = {
            "firstname": "solo",
            "lastname": "compredo",
            "othername": "nyakahia",
            "email": "solera@knowerwe.com",
            "phoneNumber": "0723143761",
            "username": "capriereceor",
            "password": ""
        }

        self.login_user_without_username = {
            'email': "spongebobsquarepants@bikinibottom.sea",
            'username': "",
            "password": "CrustyKr1abs"
        }

        self.login_user_without_email = {
            'email': "",
            'username': "Spongebob",
            "password": "CrustyKr1abs"
        }

        self.login_user_without_password = {
            'email': "spongebobsquarepants@bikinibottom.sea",
            'username': "Spongebob",
            "password": ""
        }

        self.login_user = {
            'email': "spongebobsquarepants@bikinibottom.sea",
            'username': "Spongebob",
            "password": "CrustyKr1abs"
        }

        self.unexisting_login = {
            'email': "username@email.com",
            'username': "username",
            "password": "password"
        }

        self.login_wrong_password = {
            'email': "spongebobsquarepants@bikinibottom.sea",
            'username': "Spongebob",
            "password": "password"
        }

        # variables for the meetup endpoints;
        

    def register(self):
        '''registers the test client'''
        register = self.app.post(
            REGISTER_URL, 
            data = json.dumps(self.valid_entry),
            content_type = 'application/json'
        )
        return register

    def login(self):
        '''logs in the test client'''
        login = self.app.post(
            LOGIN_URL,
            data = json.dumps(self.login_user),
            content_type = 'application/json'
        )
        return json.loads(login.data.decode())["access_token"]
