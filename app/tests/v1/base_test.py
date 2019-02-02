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
NO_MEETUP_URL = 'api/v1/meetups/100'

# urls for question endpoints
BASE_QUESTION_URL = 'api/v1/question'
SINGLE_QUESTION_URL = 'api/v1/question/1'
NO_QUESTION_URL = 'api/v1/question/100'

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
        self.valid_meetup_entry = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_without_location = {
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_without_images = {
            "location": "Andela",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_without_topic = {
            "location": "Andela",
            "images": "1.jpeg",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_without_date = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_without_tags = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019"
            }
        
        self.meetup_with_empty_images = {
            "location": "Andela",
            "images": "",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_with_empty_location = {
            "location": "",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_with_empty_topic = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "",
            "happeningOn": "1/2/2019",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_with_empty_date = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "",
            "tags": ["#AR&Education, #AR"]
            }

        self.meetup_with_empty_tags = {
            "location": "Andela",
            "images": "1.jpeg",
            "topic": "AR and Education",
            "happeningOn": "1/2/2019",
            "tags": ""
            }

        #variables for the questions endpoints
        self.valid_question_entry = {
                "createdBy": 2,
                "meetup": 1,
                "title": "Snack Time",
                "body": "Will there be lunch?",
                "votes": 5
            }

        self.question_without_name = {
                "meetup": 1,
                "title": "Snack Time",
                "body": "Will there be lunch?",
                "votes": 5
            }

        self.question_without_meetup = {
                "createdBy": 2,
                "title": "Snack Time",
                "body": "Will there be lunch?",
                "votes": 5
            }

        self.question_without_title = {
                "createdBy": 2,
                "meetup": 1,
                "body": "Will there be lunch?",
                "votes": 5
            }

        self.question_without_body = {
                "createdBy": 2,
                "meetup": 1,
                "title": "Snack Time",
                "votes": 5
            }


        self.question_without_votes = {
                "createdBy": 2,
                "meetup": 1,
                "title": "Snack Time",
                "body": "Will there be lunch?"
            }

        self.empty_user = {
            "createdBy": None,
            "meetup": 1,
            "title": "Snack Time",
            "body": "Will there be lunch?",
            "votes": 5
        }

        self.empty_meetup = {
            "createdBy": 2,
            "meetup": None,
            "title": "Snack Time",
            "body": "Will there be lunch?",
            "votes": 5
        }

        self.empty_title = {
            "createdBy": 2,
            "meetup": 1,
            "title": "",
            "body": "Will there be lunch?",
            "votes": 5
        }

        self.empty_body = {
            "createdBy": 2,
            "meetup": 1,
            "title": "Snack Time",
            "body": "",
            "votes": 5
        }

        self.empty_votes = {
            "createdBy": 2,
            "meetup": 1,
            "title": "Snack Time",
            "body": "Will there be lunch?",
            "votes": None
        }

    # methods for user registration and login
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


    # methods for meetup creation
    def create_meetup(self):
        '''creates a meetup record'''
        meetup = self.app.post(
            CREATE_MEETUP_URL,
            headers = dict(Authorization = "Bearer " + self.login()),
            data = json.dumps(self.valid_meetup_entry),
            content_type = 'application/json'
            )
        return meetup


    #method for creating a question
    def create_question(self):
        '''creates a question'''
        question = self.app.post(
            BASE_QUESTION_URL,
            headers = dict(
                Authorization= 'Bearer ' + self.login()
            ),
            data = json.dumps(self.valid_question_entry),
            content_type = 'application/json'
        )
        return question
