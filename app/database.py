from flask_pymongo import PyMongo
"""
    Observação:
        Esse arquívo existe para que não ocorra o erro de circular imports.
        Não deleta-lo e tentar mover o código para o __init__.py do app, isso
        não vai funcionar, acredite.
"""

mongo = PyMongo()
