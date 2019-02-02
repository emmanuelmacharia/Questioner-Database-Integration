from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required

from ..models.question import QuestionModel, questions

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument(
    'createdBy', required=True, type=int, help='Createdby userid is an integer and is required'
)

parser.add_argument(
    'meetup', required=True, type=int, help='Meetup-id is an integer and is required'
)

parser.add_argument(
    'title', required=True, type=str, help='The question title is required'
)

parser.add_argument(
    'body', required=True, type=str, help='The question body is required'
)

parser.add_argument(
    'votes', required=True, type=int, help='The question\'s votes is required and is an integer'
)

class Question(Resource):
    '''contains endpoints for creating the questions'''

    @jwt_required
    def get(self):
        '''gets all questions'''
        return {
            'status': 200,
            'data': questions
        }, 200

    @jwt_required
    def post(self):
        '''creates a new question'''
        data = request.get_json()
        args = parser.parse_args()
        createdBy = args.get('createdBy')
        meetup = args.get('meetup')
        title = args.get('title')
        body = args.get('body')
        votes = args.get('votes')

        payload = [
            'id', 'createdBy', 'meetup',
            'title', 'body', 'votes'
        ]

        if not createdBy or not meetup:
            return {'message': 'Your id and meetup id is required'}, 400
        elif not title or not body:
            return {'message': 'Your question information is required'}, 400
        elif not votes:
            return {'message': 'upvote numbers are required'}, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {
                        'message': '{} isnt required as user information'.format(item)}, 400

        try:
            QuestionModel.create_question(
                createdBy, meetup, title, body, votes
            )
            return {
                'status':201,
                'message': 'Question created',
                'data': questions[-1]
                }, 201

        except Exception as e:
            return {
                'status': 500,
                'message': e
            }, 500



class Single_Question(Resource):
    '''contains endpoints for a single question'''
    @jwt_required
    def patch(self):
        '''updates the question- i think'''
        pass

    @jwt_required
    def get(self, id):
        '''gets a single question'''
        return QuestionModel.single_question(id)

    @jwt_required
    def delete(self,id):
        '''deletes a question'''
        return QuestionModel.delete_question(id)


