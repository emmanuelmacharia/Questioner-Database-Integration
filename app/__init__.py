import os

from flask import Blueprint, Flask
from flask_restful import Api, Resource

from instance.config import app_configurations

v1 = Blueprint('v1',__name__,url_prefix='/api/v1')
api = Api(v1)

def createapp():
    '''runs the entire app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations['testing'])
    os.getenv("SECRET_KEY")

    app.register_blueprint(v1)
    return app
