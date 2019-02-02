import json

from .base_test import (
    BaseTest,
    CREATE_MEETUP_URL,
    ALL_MEETUPS_URL,
    SINGLE_MEETUP_URL,
    NO_MEETUP_URL
)


class TestMeetUps(BaseTest):
    '''tests all meetup endpoint'''
    def test_create_meetup(self):
        '''tests the create new event endpoint'''
        meetup = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data = json.dumps(self.valid_meetup_entry),
            content_type = 'application/json'
            )
        response_data = json.loads(meetup.data.decode())
        self.assertEqual(meetup.status_code, 201)
        self.assertEqual(json.loads(meetup.data)
                        ['message'], 'Meetup created successfully'
                        )
        self.assertTrue(response_data["data"])
        #self.create_meetup()
        #response_data = json.loads(self.create_meetup.data.decode())
        #self.assertequal(self.create_meetup.status_code, 201)
        #self.assertequal(json.loads(self.create_meetup.data)
        #                ['message'], 'meetup created successfully'
        #                )
        #self.asserttrue(response_data["data"])
    
    def test_missing_location(self):
        '''tests whether the location is an empty string'''
        response = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data=json.dumps(
                self.meetup_with_empty_location
                ), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Information on the location, event-invite-image and date must be provided")

    def test_missing_images(self):
        '''tests whether the images record is an empty string'''
        response = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data=json.dumps(
                self.meetup_with_empty_images
                ), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Information on the location, event-invite-image and date must be provided")

    def test_missing_topic(self):
        '''tests whether the topic record is an empty string'''
        response = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data=json.dumps(
                self.meetup_with_empty_topic
                ), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "the subject of the meetup must be provided (topic and tags)"
                         )

    def test_missing_date(self):
        '''tests whether the topic record is an empty string'''
        response = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data=json.dumps(
                self.meetup_with_empty_date
                ), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "Information on the location, event-invite-image and date must be provided")

    def test_missing_tags(self):
        '''tests whether the topic record is an empty string'''
        response = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data=json.dumps(
                self.meetup_with_empty_tags
                ), 
            content_type= 'application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)
                         ["message"], "the subject of the meetup must be provided (topic and tags)"
                         )


    def test_get_all_meetups(self):
            '''tests the get all meetups endpoint'''
            self.create_meetup()
            response = self.app.get(
                ALL_MEETUPS_URL,
                headers=dict(
                    Authorization="Bearer " + self.login()
                ),
                content_type='application/json'
            )
            response_data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response_data["data"])

    # def test_get_single_meetup(self):
    #     '''tests the get-single meetup  endpoint'''
    #     self.create_meetup()
    #     response = self.app.get(
    #         SINGLE_MEETUP_URL,
    #         headers = dict(
    #             Authorization = "Bearer " + self.login()
    #             ),
    #         data=json.dumps(self.valid_meetup_entry),
    #         content_type = 'application/json'
    #         )
    #     response_data = json.loads(response.data.decode())
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(response_data['data'])

    def test_no_meetup_found(self):
        '''tests the get meeetup endpoint where it doesnt exist'''
        response = self.app.get(
            NO_MEETUP_URL,
            headers = dict(
                Authorization = "Bearer " + self.login()
                ),
            content_type = 'application/json'
            )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data['message'],
                         'Meetup record is doesn\'t exist')

    def test_delete_meetup_success(self):
        '''tests the delete meetup endpoint'''
        response = self.app.delete(
            SINGLE_MEETUP_URL,
            headers=dict(Authorization="Bearer " + self.login()),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data["message"])
        self.assertEqual(response_data["message"], "Meetup deleted successfully")

    def test_delete_meetup_not_exist(self):
        '''tests whether you can delete a meetup that doesnt exist'''
        self.create_meetup()
        response = self.app.delete(
            NO_MEETUP_URL,
            headers=dict(Authorization="Bearer " + self.login()),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data['message'], 
                            'Meetup record is doesn\'t exist')


