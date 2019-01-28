import datetime

from flask import request
from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256 as sha256

users = [{
    'id': 1,
    'firstname': "emmanuel",
    'lastname': "kiangai",
    'othername': "macharia",
    'email': "samuelmarsha@outlook.com",
    'phoneNumber': "0707143761",
    'username': "emmanuelmacharia",
    'isAdmin': True,
    'registered': "19/1/2019"}
    ]

class UserModel:
    '''model for the user information'''
    @staticmethod
    def create_user(firstname,lastname,othername,email,phone_number,username,hash):
        '''creates the user'''
        isadmin = False
        id = len(users)+1
        register_time = datetime.datetime.now()
        registered = register_time.strftime('%d/%m/%Y')
        new_user = {
            'id': id,
            'firstname': firstname,
            'lastname': lastname,
            'othername': othername,
            'email': email,
            'phoneNumber': phone_number,
            'username': username,
            'isAdmin': isadmin,
            'registered': registered,
            'password': hash
        }

        users.append(new_user)
        return users

    @staticmethod
    def single_user(email):
        '''finds a single users record'''
        exists = next((user for user in users if user['email'] == email), False)
        if exists is False:
            return {
                'status': 404,
                'message': 'No user by that email exists'
            }, 404
        return {
            'status': 200,
            'message': 'User found',
            'data': exists
        }

    @staticmethod
    def delete_user(email):
        '''deletes the specified user'''
        if len(users) < 1:
            return {
                'status': 404,
                'message': 'There are no meetups currently available'
            }, 404
        else:   
            result = UserModel.single_user(email)
            if result is False:
                return {
                    'status': 404,
                    'message': 'No user by that email exists'
                }, 404    
            #indexed the position of the record in the list through its id
            index = int(result['data']['id'])-1 #subracted one because python starts counting from 0
            users.pop(index) #used pop- you can use del,but pop gets the job done 
            return {
                'status': 204,
                'message': 'User deleted successfully'
            }, 200 #cant give it a status of 204 because 204 returns no content

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)


    @staticmethod
    def verify_password(password,email):
        '''verifies that the password's right'''
        result = UserModel.single_user(email)
        return sha256.verify(password, result['data']['password'])