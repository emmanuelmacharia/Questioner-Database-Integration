import os

class Configurations():
    '''contains all cnfigs of the app'''
    DEBUG = False
    TESTING = False


class Development(Configurations):
    '''configs the development environment'''
    DEBUG = True

class Testing(Configurations):
    '''configs the testing environment'''
    DEBUG = True
    TESTING = True

class Production(Configurations):
    '''configs the production environment'''
    DEBUG = False
    TESTING = False

app_configurations = {
    'development': Development,
    'testing': Testing,
    'production': Production
}