from flask import Flask

from .database import mongo
from .config import DevConfig, api

from .routes.author import blueprint as author
from .routes.random import blueprint as random
from .routes.poem import blueprint as poem

# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config.from_object(DevConfig)

# Instanciando o MongoDB com a nossa aplicação.
mongo.init_app(app)

# Importações dos BluePrints
app.register_blueprint(random)
app.register_blueprint(author)
app.register_blueprint(poem)

# Instanciando as configurações do APP com a API
api.init_app(app)
