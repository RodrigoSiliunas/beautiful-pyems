from flask import Flask

from .database import mongo
from .views.random_poem import blueprint as random

# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask'
app.config['JSON_SORT_KEYS'] = False

# MongoDB
mongo.init_app(app)

# Importações das BluePrints
app.register_blueprint(random)
