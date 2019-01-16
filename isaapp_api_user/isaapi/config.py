"""
config.py
    - Factory settings for the flask app 
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

database_type = 'postgresql+psycopg2://'
database_base_format = database_type + '{dbuser}:{dbpass}@{dbhost}/{dbname}'

database_dev_uri = database_base_format.format(
    dbuser='isaapp_dev',
    dbpass='isaapp',
    dbhost='localhost',
    dbname='isaapp_dev'
)

database_prod_uri = database_base_format.format(
    dbuser='isaapp_prod',
    dbpass='isaapp',
    dbhost='localhost',
    dbname='isaapp_prod'
)


class BaseConfig:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_dev_uri
    SECRET_KEY = 'mysecretkey'


class DevelopmentConfig(BaseConfig):
    IS_LOCAL = True
    SECURITY_PASSWORD_SALT = '87ca286c08f4504981b1f8ee44988e77'


class ProductionConfig(BaseConfig):
    IS_LOCAL = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = database_prod_uri
    ECURITY_PASSWORD_SALT = '0a1234f3c6b54217c348857dbeba0578'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
