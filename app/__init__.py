from flask import Flask, redirect
from .database import mongo
from .config import ProdConfig, api
from .routes.author import blueprint as author
from .routes.random import blueprint as random
from .routes.poem import blueprint as poem

# Instanciando a aplicação Flask
app = Flask(__name__)

# Configurações do Flask
app.config.from_object(ProdConfig)

# Instanciando o MongoDB com a nossa aplicação.
mongo.init_app(app)

# Importações dos BluePrints
app.register_blueprint(random)
app.register_blueprint(author)
app.register_blueprint(poem)


@app.route('/')
def index():
    return redirect('/docs', 302)


# Instanciando as configurações do APP com a API
api.init_app(app)
