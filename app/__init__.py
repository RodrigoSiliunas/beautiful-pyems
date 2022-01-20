from flask import Flask
from .database import mongo
from .config import DevConfig
from .views.random_poem import blueprint as randomPoem
from .views.author import blueprint as author

# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config.from_object(DevConfig)

# MongoDB
mongo.init_app(app)

# Importações das BluePrints
app.register_blueprint(randomPoem)
app.register_blueprint(author)
