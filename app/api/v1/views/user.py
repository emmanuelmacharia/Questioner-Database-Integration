import re, datetime

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
    create_access_token, jwt_required, 
    create_refresh_token, jwt_refresh_token_required,
    get_jwt_identity
)

from ..models.user import UserModel, users

app = Flask(__name__)
api = Api(app)



class User(Resource):
    '''contains user endpoints for get and post'''
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

    parser.add_argument(
        "password", type=str, required=True, help="A username is required"
    )

    def get(self):
        '''the get all users endpoint'''
        return {
            'status': 200,
            'data' : users
        }
    
    def post(self):
        '''creates a new user'''
        data = request.get_json()
        args = User.parser.parse_args()
        firstname = args.get('firstname')
        lastname = args.get('lastname')
        othername = args.get('othername')
        email = args.get('email')
        phone_number = args.get('phoneNumber')
        username = args.get('username')
        password = args.get('password')
        payload = ['id','firstname', 'lastname', 'othername', 
                    'email', 'phoneNumber', 'username', 'registered',
                    'isadmin', 'password']
        
        if not firstname or not lastname or not othername:
            return {'message': 'Your full name is required, at least 3 names'}, 400
        elif not email or not phone_number:
            return {'message': 'Your contact info (phone and email) are requuired'}, 400
        elif not username or not password:
            return {'message': 'Username is required'}, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {
                        'message':'{} isnt required as user information'.format(item)},400
            hash = UserModel.generate_hash(password)
        try: 
            UserModel.create_user(
                firstname, lastname, othername, email, phone_number, username, hash
            )
            return {
                'status': 201,
                'message': 'User created successfully',
                'data': users[-1]
            }, 201
        except Exception as e:
            e = str(e)
            return {
                'status': 500,
                'message': e
            }

class SingleUser(Resource):
    '''contains the get, put and delete requests for single user records'''
    @jwt_required
    def get(self, email):
        '''gets the user's data by id'''
        return UserModel.single_user(email)

    @jwt_required
    def put(self):
        '''updates existing user information''' 
        pass

    @jwt_required
    def delete(self, email):
        '''deletes an entire user record by id'''
        return UserModel.delete_user(email)


class Login(Resource):
    '''allows the user to log in'''
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email", required=True, help="Your email address is required", type=str
    )
    parser.add_argument(
        "username", type=str, required=True, help="A username is required"
    )

    parser.add_argument(
        "password", type=str, required=True, help="A username is required"
    )
    def post(self):
        data = request.get_json()
        args = Login.parser.parse_args()
        username = args.get('firstname')
        email = args.get('email')
        password = args.get('password')
        payload = ['username', 'email', 'password']

        for item in data.keys():
            if item not in payload:
                return {
                    'status': 400,
                    'message':'{} is required as user information'.format(item)
                    },400

        UserModel.generate_hash(password)
        session = UserModel.single_user(email)
        if session is False:
            return {'message': 'Username, {}, email, {} or password dont seem to exist'.format(username, email)}, 400
        if UserModel.verify_password(password, email) is True:
            try:
                ac_token = create_access_token(identity=email, expires_delta=datetime.timedelta(days=2))
                return {
                    'status': 200,
                    'message': 'Successful login',
                    'access_token': ac_token
                }
            except Exception as e:
                e = str(e)
                return {
                    'status': 400,
                    'message': 'Bad request',
                    'error': e
                }, 400


    
