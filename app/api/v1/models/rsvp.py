import datetime

from flask import request
from flask_restful import Resource

rsvps = []

class RsvpModel:
    '''models for rsvps'''
    @staticmethod
    def create_rsvp(
        meetup, user, response
    ):
        '''creates the rsvps'''
        id = len(rsvps) + 1
        date = datetime.datetime.now()
        rsvpOn = date.strftime('%d/%m/%Y %H:%M:%S')
        rsvp = {
            'id': id,
            'meetup': meetup,
            'user': user,
            'response': response,
            'date_confirmed': rsvpOn
        }
        rsvps.append(rsvp)
        return rsvps

    @staticmethod
    def single_rsvp(id):
        '''gets a single rsvp record'''
        exist = next((rsvp for rsvp in rsvps if rsvp['id'] == id), False)
        if exist is False:
            return {
                'status': 404,
                'message': 'No rsvp by that id exists'
            }, 404
        return {
            'status': 200,
            'message': 'RSVP found',
            'data': exist
        }

    @staticmethod
    def delete(id):
        '''deletes rsvp record'''
        if len(rsvps) < 1:
            return {
                'status': 404,
                'message': 'There are no rsvps currently available'
            }, 404
        else:
            myRsvp = RsvpModel.single_rsvp(id)
            if myRsvp is False:
                return {
                    'status': 404,
                    'message': 'No rsvp by that id exists'
                }, 404
            else:
                index = int(id) - 1
                rsvps.pop(index)
                return {
                    'status': 204,
                    'message': 'RSVP successfully deleted'
                }, 200
