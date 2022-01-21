from flask import Flask
from .database import mongo
from .config import DevConfig
from .routes.random import blueprint as random
from .routes.author import blueprint as author


# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config.from_object(DevConfig)

# MongoDB
mongo.init_app(app)

# Importações das BluePrints
app.register_blueprint(random)
app.register_blueprint(author)
