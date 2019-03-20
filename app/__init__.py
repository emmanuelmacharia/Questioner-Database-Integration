import os

from flask import Blueprint, Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from instance.config import app_configurations

from .api.v2.models import dbconnect, create_tables, drop_tables, check_admin
# from .api.v2.views.user import Users, Getall, GetOne

v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)

JWT = JWTManager()

def createapp(config_name):
    '''runs the entire app'''
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_configurations[config_name])
    CORS(app)
    
    app.config.from_pyfile('config.py')
    os.getenv("SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = 'practice'
    app.register_blueprint(v1)

    with app.app_context():
        from .api.v2.views.user import (
            Users, Getall, GetOne
        )
    JWT.init_app(app)

    # with app.app_context():
    #     from .api.v1.views.meetup import Meetup, SingleMeetup, AllMeetups
    #     from .api.v1.views.user import User, SingleUser, Login
    #     from .api.v1.views.question import Question, Single_Question
    #     from .api.v1.views.rsvp import Rsvp, Single_Rsvp

    dbconnect()
    create_tables()
    check_admin()

    api.add_resource(Users, '/v2/user')
    api.add_resource(Getall, '/v2/users')
    api.add_resource(GetOne, '/v2/user/<string:email>')
    return app


