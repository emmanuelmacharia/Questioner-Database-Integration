import unittest
import json

from app import createapp
#from ...api.v1.views import user

REGISTER_URL = 'api/v1/users'
LOGIN_URL = 'api/v1/login'
SINGLE_USER_URL = 'api/v1/user/1'

class TestUser(unittest.TestCase):
    '''tests all user endpoints'''
    def setUp(self):
        '''sets up the testclient'''
        self.app = createapp('testing').test_client()
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



    def test_register_success(self):
        '''tests successful registration'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.valid_entry),
            content_type = 'application/json'
        )
        # json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)
                        ["message"], "User created successfully")

    def test_missing_firstname(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_firstname), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Your full name is required, at least 3 names"
                         )

    def test_missing_lastname(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_lastname),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                            ["message"], "Your full name is required, at least 3 names"
                            )

    def test_missing_othername(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_lastname),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                            ["message"], "Your full name is required, at least 3 names"
                            )
            
    def test_missing_email(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_email),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Your contact info (phone and email) are required"
                            )

    def test_missing_phone(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_phoneNumber),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Your contact info (phone and email) are required"
                            )

    def test_missing_username(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Username and Password are required"
                         )

    def test_missing_password(self):
        '''tests failure due to missing username'''
        response = self.app.post(
            REGISTER_URL, data=json.dumps(self.missing_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Username and Password are required"
                         )

