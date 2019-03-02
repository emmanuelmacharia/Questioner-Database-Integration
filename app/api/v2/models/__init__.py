'''creates a connection with the databases'''
import os
import psycopg2
from .database import queries, deleters
from instance.config import Configurations, Testing, Development, Production, app_configurations

environment = os.getenv('APP_SETTINGS')
development_url = os.getenv('DEVELOPMENT_DATABASE_URI')
testing_url = os.getenv('TESTING_DATABASE_URI')
production_url = os.getenv('PRODUCTION_DATABASE_URI')

def dbconnect():
    '''connects to the databases'''
    try:
        '''try connecting to one of the three environments set'''
        if environment == 'testing':
            conn = psycopg2.connect(testing_url)
        if environment == 'production':
            conn = psycopg2.connect(production_url)
        if environment == 'development':
            conn = psycopg2.connect(development_url)
    except Exception as e:
        print (e, "No connection")

    print(environment)
    return conn, environment


conn = dbconnect()
print(conn)

