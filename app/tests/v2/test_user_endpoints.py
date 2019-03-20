import json 

from app import createapp
from .base_test import (
    BaseTest,
    REGISTER_URL,
    SINGLE_USER_URL,
    DELETE_USER_URL,
    USERS_URL
)

class TestUser(BaseTest):
    '''tests the user endpoints'''
    def test_register_success(self):
        '''tests successful user registration'''
        response = self.client.post(
            REGISTER_URL,
            data = json.dumps(self.valid_entry),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 201)
