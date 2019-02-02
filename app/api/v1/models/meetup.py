import datetime

from flask import request
from flask_restful import Resource

meetup = [
    {
        'id': 1,
        'createdOn': 1/1/2019,
        "location": "Andela",
        "images": "1.jpeg",
        "topic": "AR and Education",
        "happeningOn": "1/2/2019",
        "tags": ["#AR&Education, #AR"]
    }
]

class MeetupModel:
    '''models for the meetup information'''
    @staticmethod
    def create_meetup(
        location, images, topic, happeningon, tags 
       ):
        id = len(meetup)+1
        date_created = datetime.datetime.now()
        createdOn = date_created.strftime('%d/%m/%Y')
        new_meetup = {
            'id': id,
            'createdOn': createdOn,
            'location': location,
            'images': images,
            'topic': topic,
            "happeningon": happeningon,
            "Tags": tags
        }

        meetup.append(new_meetup)
        return meetup

    @staticmethod
    def single_meetup(id):
        '''finds a single meetup record'''
        exists = next((meet for meet in meetup if meet['id'] == id), False)
        if exists is False:
            return {
                'status': 404,
                'message': 'Meetup record is doesn\'t exist'
            }, 404

        return {
            'status': 200,
            "message": 'Meetup found',
            "data": exists
        }, 200

    @staticmethod
    def delete(id):
        '''deletes a meetup record'''
        if len(meetup) < 1:
            return {
                'status': 404,
                'message': 'There are no meetups currently available'
            }, 404
        else:
            result = MeetupModel.single_meetup(id)
            if result [-1] == 404:
                return {
                    'status': 404,
                    'message': 'Meetup record is doesn\'t exist'
                }, 404
            else:
                index = int(id) - 1
                meetup.pop(index)
                return {
                    'status': 204,
                    'message': 'Meetup deleted successfully'
                }, 200


        
