import os

class Configurations():
    '''contains all cnfigs of the app'''
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    


class Development(Configurations):
    '''configs the development environment'''
    DEBUG = True
    DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URI")

class Testing(Configurations):
    '''configs the testing environment'''
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.getenv("TESTING_DATABASE_URI")

class Production(Configurations):
    '''configs the production environment'''
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URI")

app_configurations = {
    'development': Development,
    'testing': Testing,
    'production': Production
}
