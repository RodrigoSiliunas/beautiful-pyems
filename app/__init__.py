from flask import Flask
from .database import mongo
from .config import DevConfig, api
from .routes.author import blueprint as author
from .routes.random import blueprint as random

# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config.from_object(DevConfig)

# MongoDB
mongo.init_app(app)

# Importações dos BluePrints
app.register_blueprint(random)
app.register_blueprint(author)

# Instanciando as configurações do APP com a API
api.init_app(app)
