from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from ..models.meetup import MeetupModel, meetup

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument(
    'location', required=True, type=str, help='The location for your  meetup is required'
)

parser.add_argument(
    'images', required=True, type=str, help='Image invite for your  meetup is required'
)

parser.add_argument(
    'topic', required=True, type=str, help='The topic for your  meetup is required'
)

parser.add_argument(
    'happeningOn', required=True, type=str, help='The date for your  meetup is required'
)

parser.add_argument(
    'tags', required=True, type=str, help='Tags for your  meetup is required'
)

class Meetup(Resource):
    '''handles the meetup endpoints for creating and viewing multiple meetup records'''

    def post(self):
        '''creates a new meetup event'''
        data = request.get_json()
        args = parser.parse_args()
        location = args.get('location')
        images = args.get('images')
        topic = args.get('topic')
        happeningOn = args.get('happeningOn')
        tags = args.get('tags')

        payload = [
            'id', 'createdOn', 'location',
            'images', 'topic', 'happeningOn',
            'tags' 
        ]

        if not location or not images or not happeningOn:
            return {'message': 'Information on the location, event-invite-image and date must be provided'}, 400
        elif not topic or not tags:
            return {'message': 'the subject of the meetup must be provided (topic and tags)'}, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {
                        'message': '{} isnt required as user information'.format(item)}, 400
                
        try:
            MeetupModel.create_meetup(
                location, images, topic, happeningOn, tags
            )
            return {
                'status': 201,
                'message': 'Meetup created successfully',
                'data': meetup[-1]
            },201

        except Exception as e:
            return {
                'status': 500,
                'message': e
            }



class SingleMeetup(Resource):
    '''handles single meetup endpoints'''

    def get(self, id):
        '''gets a single meetup record'''
        return MeetupModel.single_meetup(id)


    def put(self, id):
        '''updates a meetup record'''
        pass
    
    def delete(self, id):
        '''deletes a meetup record'''
        return MeetupModel.delete(id)


class AllMeetups(Resource):
    '''handles all meetups'''

    def get(self):
        '''gets all the meetups created'''
        return {
            'status': 200,
            'data': meetup
        }, 200
