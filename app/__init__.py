import os

from flask import Blueprint, Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from instance.config import app_configurations

from .api.v1.views.user import User, SingleUser, Login
from .api.v1.views.meetup import Meetup, SingleMeetup, AllMeetups
from .api.v1.views.question import Question, Single_Question
from .api.v1.views.rsvp import Rsvp, Single_Rsvp
from .api.v2.models import dbconnect

v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)

def createapp(config_name):
    '''runs the entire app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations[config_name])
    # app.config.from_pyfile('config.py')
    os.getenv("SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = 'practice'
    app.register_blueprint(v1)
    CORS(app)
    JWTManager(app)

    # with app.app_context():
    #     from .api.v1.views.meetup import Meetup, SingleMeetup, AllMeetups
    #     from .api.v1.views.user import User, SingleUser, Login
    #     from .api.v1.views.question import Question, Single_Question
    #     from .api.v1.views.rsvp import Rsvp, Single_Rsvp


    dbconnect()

    api.add_resource(User, '/users', '/register')
    api.add_resource(SingleUser, '/user/<string:email>')
    api.add_resource(Login, '/login')
    api.add_resource(Meetup, '/meetups')
    api.add_resource(AllMeetups, '/meetups/upcoming')
    api.add_resource(SingleMeetup, '/meetups/<int:id>')
    api.add_resource(Question, '/question')
    api.add_resource(Single_Question, '/question/<int:id>')
    api.add_resource(Rsvp, '/rsvp')
    api.add_resource(Single_Rsvp, '/rsvp/<int:id>')

    return app


