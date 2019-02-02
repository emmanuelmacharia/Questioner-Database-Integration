import json

from .base_test import (
    BaseTest,
    BASE_QUESTION_URL,
    SINGLE_QUESTION_URL,
    NO_QUESTION_URL
)

class TestQuestions(BaseTest):
    '''tests all question endpoints'''

    def test_create_question(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers = dict(
                Authorization = "Bearer " + self.login()
            ),
            data = json.dumps(self.valid_question_entry),
            content_type = 'application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 201)
        self.assertEqual(response_data['message'],
            'Question created'
            )

    def test_missing_user(self):
        '''tests whether the user id is present'''
        response = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.question_without_name),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['createdBy'],
                         'Createdby userid is an integer and is required'
                         )


    def test_missing_meetup(self):
        '''tests whether the meetup id is present'''
        response = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.question_without_meetup),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['meetup'],
                         'Meetup-id is an integer and is required'
                         )

    def test_missing_title(self):
        '''tests whether the title is present'''
        response = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.question_without_title),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['title'],
                         'The question title is required'
                         )

    def test_missing_body(self):
        '''tests whether the title is present'''
        response = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.question_without_body),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['body'],
                         'The question body is required'
                         )

    def test_missing_votes(self):
        '''tests whether the title is present'''
        response = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.question_without_votes),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message']['votes'],
                         'The question\'s votes is required and is an integer'
                         )

    def test_empty_user(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_user),
            content_type='application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your id and meetup id is required'
                         )

    def test_empty_meetup(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_meetup),
            content_type='application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your id and meetup id is required'
                         )

    def test_empty_title(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_title),
            content_type='application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your question information is required'
                         )
                
    def test_empty_body(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_body),
            content_type='application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 400)
        self.assertEqual(response_data['message'],
                         'Your question information is required'
                         )

    def test_empty_votes(self):
        '''tests the post question endpoint'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            data=json.dumps(self.empty_votes),
            content_type='application/json'
        )
        response_data = json.loads(question.data.decode())
        self.assertEqual(question.status_code, 400)
        self.assertEqual(response_data['message'],
                         'upvote numbers are required'
                         )


    def test_get_all_questions(self):
        '''tests the get every question endpoint'''
        self.create_question()
        response = self.app.get(
            BASE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            content_type='application/json'
        )

        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_data['data'])


    def test_no_question_found(self):
        '''tests the get single questions endpoint'''
        response = self.app.get(
            NO_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data['message'],
                        'No question by that id exists'
            )

    def test_delete_question(self):
        '''tests the delete question endpoint'''
        response = self.app.delete(
            SINGLE_QUESTION_URL,
            headers=dict(
                Authorization="Bearer " + self.login()
            ),
            content_type='application/json'
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['message'],
                         'Question successfully deleted'
                         )

 