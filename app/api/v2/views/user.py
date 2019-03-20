
import datetime

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    JWTManager
)

from ..models.user import User

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    '''defines the get, post and delete user endpoints'''
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

    def post(self):
        '''creates a user account'''
        args = Users.parser.parse_args()
        firstname = args.get('firstname')
        lastname = args.get('lastname')
        othername = args.get('othername')
        email = args.get('email')
        phone_number = args.get('phoneNumber')
        username = args.get('username')
        password = args.get('password')

        if not firstname or not lastname or not othername:
            return {'message': 'Your full name is required, at least 3 names'}, 400
        elif not email or not phone_number:
            return {'message': 'Your contact info (phone and email) are required'}, 400
        elif not username or not password:
            return {'message': 'Username and Password are required'}, 400
        else:
            hash = User.generate_hash(password)

        fullname = firstname + ' ' + lastname + ' ' + othername
        contact = email + ', ' + phone_number

        try:
            User(fullname, hash, contact).save_user()
            return {
                'status': "Created",
                'message': "User created successfully",
            }, 201
            
        except Exception as e:
            e= str(e)
            return {
                'status':500,
                'message': e
            }, 500


class Getall(Resource):
    '''Gets all users'''
    def get(self):
        '''gets all users from the database'''
        return User.viewall(self)

class GetOne(Resource):
    '''Works to get, delete and/or manage a single user'''

    def get(self, email):
        '''gets a single user'''
        return User.veiwone(self, email)

    def delete(self, email):
        '''deletes a single user'''
        return User.delete_user(self, email)

    

    





    
