import datetime

from flask import request
from flask_restful import Resource, reqparse

questions = []

class QuestionModel:
    '''model for the questions model'''
    @staticmethod
    def create_question(
        createdBy, meetup, title, body, votes
    ):
        '''creates the questions'''
        id = len(questions)+1
        time_created = datetime.datetime.now()
        createdOn = time_created.strftime('%d/%m/%Y %H:%M:%S')
        new_question = {
            'id': id,
            'createdOn': createdOn,
            'createdBy': createdBy,
            'meetup': meetup,
            'title': title,
            'body': body,
            'votes': votes
        }

        questions.append(new_question)
        return questions

    @staticmethod
    def single_question(id):
        '''gets a question by id'''
        exist = next((question for question in questions if question['id']==id), False)
        if exist is False:
            return {
                'status': 404,
                'message': 'No question by that id exists'
            }, 404
        return {
            'status': 200,
            'message': 'Question found',
            'data': exist
        }
    
    @staticmethod
    def delete_question(id):
        '''deletes a question by id'''
        if len(questions) < 1:
            return {
                'status': 404,
                'message': 'There are no questions currently available'
            }, 404
        else: 
            myQuestion = QuestionModel.single_question(id)
            if myQuestion is False:
                return {
                    'status': 404,
                    'message': 'No question by that id exists'
                }, 404
            else:
                index = int(id) - 1
                questions.pop(index)
                return {
                    'status': 204,
                    'message': 'Question successfully deleted'
                }, 200


