# Área de configuração da aplicação

from distutils.debug import DEBUG


class Config:
    JSON_SORT_KEYS = False
    THREADED = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    MONGO_URI = 'mongodb://localhost:27017/flask'
    TESTING = True
    DEBUG = True
