from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from ..models.user import UserModel, users

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument(
    "firstname", required=True, help="The firstname is  required", type=str
)

parser.add_argument(
    'lastname', required=True, help='Your lastname is required', type=str
)

parser.add_argument(
    'othername', required=True, help="Your surname/any other name is required", type=str
)

parser.add_argument(
    "email", required=True, help="Your email address is required", type=str
)

parser.add_argument(
    'phoneNumber', required=True, help='Your phone number is required', type=str
)

parser.add_argument(
    "username", type=str, required=True, help="A username is required"
)


class User(Resource):
    '''contains user endpoints for get and post'''


    def get(self):
        '''the get all users endpoint'''
        return {
            'status': 200,
            'data' : users
        }
    
    def post(self):
        '''creates a new user'''
        data = request.get_json()
        args = parser.parse_args()
        firstname = args.get('firstname')
        lastname = args.get('lastname')
        othername = args.get('othername')
        email = args.get('email')
        phone_number = args.get('phoneNumber')
        username = args.get('username')
        payload = ['id','firstname', 'lastname', 'othername', 
                    'email', 'phoneNumber', 'username', 'registered',
                    'isadmin']
        
        if not firstname or not lastname or not othername:
            return {'message': 'Your full name is required, at least 3 names'}, 400
        elif not email or not phone_number:
            return {'message': 'Your contact info (phone and email) are requuired'}, 400
        elif not username:
            return {'message': 'Username is required'}, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {
                        'message':'{} isnt required as user information'.format(item)},400

        try: 
            UserModel.create_user(
                firstname, lastname, othername, email, phone_number, username
            )
            return {
                'status': 201,
                'message': 'User created successfully',
                'data': users[-1]
            }, 201
        except Exception as e:
            return {
                'status': 500,
                'message': e
            }

class SingleUser(Resource):
    '''contains the get, put and delete requests for single user records'''

    def get(self, email):
        '''gets the user's data by id'''
        return UserModel.single_user(email)
    
    def put(self):
        '''updates existing user information''' 
        pass
    
    def delete(self, email):
        '''deletes an entire user record by id'''
        return UserModel.delete_user(email)


class Login(Resource):
    '''allows the user to log in'''
    pass

class Register(Resource):
    '''allows a user to register'''
    pass
    