import json
from .base_test import (
    BaseTest,
    BASE_RSVP_URL,
    SINGLE_RSVP_URL
)

class TestRsvp(BaseTest):
    '''contains tests for all the rsvp endpoints'''
    def test_create_rsvp(self):
        '''tests the create rsvp endpoint'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers = dict(
                Authorization = "Bearer " + self.login()
            ),
            data=json.dumps(self.valid_rsvp_entry),
            content_type = 'application/json'
        ) 
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response_data['data'])
        self.assertEqual(response_data['message'], 'RSVP created')

    def test_missing_meetup(self):
        '''tests create rsvp where meetup is missing'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.rsvp_without_meetup),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['meetup'],
                         'MeetupId is an integer and is required')

    def test_missing_user(self):
        '''tests create rsvp where userid is missing'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.rsvp_without_user),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['user'],
                         'UserId is an integer and is required')

    def test_missing_response(self):
        '''tests create rsvp where response is missing'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.rsvp_without_response),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['response'],
                         'Your response is required')

    def test_empty_rsvp_user(self):
        '''tests create rsvp where user field is None'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_rsvp_user),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your id and meetup id  and response are required')

    def test_empty_rsvp_meetup(self):
        '''tests create rsvp where user field is None'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_rsvp_user),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your id and meetup id  and response are required')

    def test_empty_response(self):
        '''tests create rsvp where user field is None'''
        response = self.app.post(
            BASE_RSVP_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_rsvp_user),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your id and meetup id  and response are required')

    def test_get_all_rsvps(self):
        '''tests the get all rsvp endpoint'''
        self.create_rsvp()
        response = self.app.get(
            BASE_RSVP_URL,
            headers= dict(
                Authorization = "Bearer " + self.login()
            ),
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data['data'])

    def test_delete_rsvp(self):
        '''tests the delete rsvp endpoint'''
        self.create_rsvp()
        response = self.app.delete(
            SINGLE_RSVP_URL,
            headers = dict(
                Authorization = "Bearer " + self.login()
            ),
            content_type = 'application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['message'],
                         'RSVP successfully deleted'
                         )
