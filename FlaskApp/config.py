import os

class Config(object):
    SECRET_KEY = 'poiuytrewqasdfghjklñlkmnbvcxz'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'