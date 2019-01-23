from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from ..models.rsvp import RsvpModel, rsvps

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument(
    'meetup', required=True, type=int, help='MeetupId is an integer and is required'
)

parser.add_argument(
    'user', required=True, type=int, help='UserId is an integer and is required'
)
parser.add_argument(
    'response', required=True, type=str, help='MeetupId is an integer and is required'
)

class Rsvp(Resource):
    '''contains rsvp endpoints'''
    def get(self):
        '''gets all rsvps'''
        return {
            'status': 200,
            'data': rsvps
        }, 200

    def post(self):
        '''creates n rsvp record'''
        data = request.get_json()
        args = parser.parse_args()
        meetup = args.get('meetup')
        user = args.get('user')
        response = args.get('response')
        payload = [
            'id', 'meetup', 'user', 'response', 'date_confirmed'
        ]
        if not meetup or not user or not response:
            return {'message': 'Your id and meetup id  and response is required'}, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {
                        'message': '{} isnt required as user information'.format(item)}, 400
        
        try:
            RsvpModel.create_rsvp(
                meetup, user, response
            )
            return {
                'status': 201,
                'message': 'RSVP created',
                'data' : rsvps[-1]
            },201

        except Exception as e:
            return {
                'status': 500,
                'message': e
            }, 500


class Single_Rsvp(Resource):
    '''contains endpoints for a single rsvp record'''
    def patch(self):
        '''updates rsvp record'''
        pass
    
    def get(self, id):
        '''gets a single rsvp record'''
        return RsvpModel.single_rsvp(id)

    def delete(self, id):
        '''deletes rsvp record'''
        return RsvpModel.delete(id)




