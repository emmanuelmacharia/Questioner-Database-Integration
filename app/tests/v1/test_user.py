import json

from app import createapp
from .base_test import (
    REGISTER_URL,
    LOGIN_URL,
    SINGLE_USER_URL,
    NO_SINGLE_USER_URL,
    DELETE_URL,
    USERS_URL,
    BaseTest
)

class TestUser(BaseTest):
    '''tests all user endpoints'''

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

    def test_get_all_users(self):
        '''tests the get all users endpoint'''
        response = self.app.get(
            USERS_URL, 
            headers = dict(Authorization="Bearer " + self.login()), 
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data["data"])

    def test_get_single_user(self):
        '''tests single user endpoint'''
        response  = self.app.get(
            SINGLE_USER_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data["data"])

    def test_no_user_found(self):
        '''tests the get user by email where the email doesnt exist'''
        response = self.app.get(
            NO_SINGLE_USER_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertTrue(response_data["message"])
        self.assertEqual(response_data["message"], "No user by that email exists")

    def test_successful_login(self):
        '''tests successful logins by the user'''
        response = self.app.post(
            LOGIN_URL,
            data= json.dumps(self.login_user),
            content_type = 'application/json'
            )
        response_data = json.loads(response.data.decode())
        self.assertTrue(response_data['access_token'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['message'], "Successful login")

    def test_unregistered_user_login(self):
        '''tests login endpoint where the email doesnt exist'''
        response = self.app.post(
            LOGIN_URL,
            data = json.dumps(self.unexisting_login),
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response_data['message'],
            "email- {} doesnt seem to exist".format(self.unexisting_login['email']
            ))

    # def test_login_without_username(self):
    #     '''tests user login without username'''
    #     response = self.app.post(
    #         LOGIN_URL,
    #         data=json.dumps(self.login_user_without_username),
    #         content_type='application/json'
    #     )
    #     response_data = json.loads(response.data.decode())
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(
    #         response_data['message'],
    #         "username is required as user information"
    #     )

    def test_login_without_email(self):
        '''tests user login without username'''
        response = self.app.post(
            LOGIN_URL,
            data=json.dumps(self.login_user_without_email),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response_data['message'],
            "email- {} doesnt seem to exist".format(
                self.login_user_without_email['email'])
        )

    def test_login_without_password(self):
        '''tests user login without username'''
        response = self.app.post(
            LOGIN_URL,
            data=json.dumps(self.login_user_without_password),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response_data['message'],
            "username and/or password do not match"
        )

    def test_wrong_password(self):
        '''tests for wrong password entries'''
        response = self.app.post(
            LOGIN_URL,
            data=json.dumps(self.login_wrong_password),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response_data['message'])
        self.assertEqual(response_data['message'],
                         "username and/or password do not match")

    def test_delete_user_success(self):
        '''tests successful deletion of a users account'''
        self.register()
        response = self.app.delete(
            DELETE_URL,
            headers=dict(Authorization="Bearer " + self.login()),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data["message"])
        self.assertEqual(response_data["message"], "User deleted successfully")
        
