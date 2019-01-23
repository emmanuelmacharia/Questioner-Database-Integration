import os

from flask import Blueprint, Flask
from flask_restful import Api, Resource

from instance.config import app_configurations

from .api.v1.views.user import User, SingleUser
from .api.v1.views.meetup import Meetup, SingleMeetup, AllMeetups
from .api.v1.views.question import Question, Single_Question

v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)

def createapp():
    '''runs the entire app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations['testing'])
    os.getenv("SECRET_KEY")

    app.register_blueprint(v1)
    return app


api.add_resource(User, '/users')
api.add_resource(SingleUser, '/user/<string:email>')
api.add_resource(Meetup, '/meetups')
api.add_resource(AllMeetups, '/meetups/upcoming')
api.add_resource(SingleMeetup, '/meetups/<int:id>')
api.add_resource(Question, '/question')
api.add_resource(Single_Question, '/question/<int:id>')

