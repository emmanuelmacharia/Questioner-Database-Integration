import datetime

from flask import request
from flask_restful import Resource, reqparse

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
    def create_user(firstname,lastname,othername,email,phone_number,username):
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
            'registered': registered
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

