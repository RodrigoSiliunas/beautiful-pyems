
import os
from flask_restx import Api, cors
from distutils.debug import DEBUG
from .routes.author import api as authors
from .routes.random import api as randoms
from .routes.poem import api as poems

# Área de configuração da aplicação;


class Config:
    JSON_SORT_KEYS = False
    THREADED = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    MONGO_URI = str(os.environ.get('MONGO_URI', None))
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    MONGO_URI = 'mongodb://localhost:27017/flask'
    TESTING = True
    DEBUG = True


# Área de configuração das informações da nossa API.
api = Api(
    version="1.0.0",
    title="Beautiful Pyems",
    description="Beautiful Pyems é uma aplicação desenvolvida em Python com o microframework Flask. Seu objetivo principal é fornecer poemas quando for requisitado. A base para sua criação foi uma aplicação ETL que acessa o site https://www.escritas.org/pt/ e efetua uma raspagem de dados obtendo grandes volumes de documentos que são armazenados no MongoDB.",

    contact="Rodrigo Siliunas",
    contact_email="rodrigo.siliunas98@outlook.com",
    contact_url="https://github.com/RodrigoSiliunas/beautiful-pyems",

    doc="/docs"
)

api.add_namespace(authors)
api.add_namespace(randoms)
api.add_namespace(poems)
