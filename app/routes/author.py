import re
from ..database import *
from flask import Blueprint
from flask_restx import Api, Resource, fields

blueprint = Blueprint('authors', __name__)
api = Api(
    blueprint,
    version="1.0.0",
    title="Beautiful Pyems",
    description="Beautiful Pyems é uma aplicação desenvolvida em Python com o microframework Flask. Seu objetivo principal é fornecer poemas quando for requisitado. A base para sua criação foi uma aplicação ETL que acessa o site https://www.escritas.org/pt/ e efetua uma raspagem de dados obtendo grandes volumes de documentos que são armazenados no MongoDB.",

    contact="Rodrigo Siliunas",
    contact_email="rodrigo.siliunas98@outlook.com",
    contact_url="https://github.com/RodrigoSiliunas/beautiful-pyems",

    doc="/docs")


poem_model = api.model('Poem', {
    'title': fields.String(description="The title of poems."),
    'author': fields.String(description="The name of author of poem."),
    'content': fields.String(description="The poem.")
})

error_model = api.model('Fail', {
    'message': fields.String(description="The message that the server will return."),
    'type': fields.String(description="The type of error the server is returning."),
    'code': fields.Integer(description="The HTTP status code that the server is returning.")
})

error_model_v2 = api.model('AuthorNotFound', {
    'error': fields.Nested(error_model)
})


@api.route('/authors/<author>', doc={
    'params': {
        'author': 'A name of a poet who is registered in our database.'
    },
    'description': 'Filha da puta de rota',
})
@api.param('id', 'The task identifier')
class RandomPoemFromAuthor(Resource):
    @api.response(200, 'Success.', poem_model)
    @api.response(404, 'Author Not Found.', error_model_v2)
    def get(self, author):
        '''Retorna uma poesia aleatória de um determinado autor.'''
        author = re.compile(f"^{author}", re.IGNORECASE)

        poem = list(mongo.db.poems.aggregate([
            {
                "$match": {"author": author}
            },
            {
                "$sample": {"size": 1}
            }
        ]))

        if poem:
            return {
                "title": poem[0]["title"],
                "author": poem[0]["author"],
                "content": poem[0]["content"]
            }, 200

        return {
            "error": {
                "message": "Author not found.",
                "type": "NotFoundError",
                "code": 404,
            }}, 404


# @blueprint.route('/authors/<author>/<name>')
# def get_poem_from_author(author, name):
#     author = re.compile(f"^{author}", re.IGNORECASE)
#     name = re.compile(f"^{name}", re.IGNORECASE)

#     poem = list(mongo.db.poems.aggregate([
#         {
#             "$match": {
#                 "author": author,
#                 "title": name,
#             }
#         },
#         {
#             "$sample": {"size": 1}
#         }
#     ]))

#     if poem:
#         return jsonify({
#             "title": poem[0]["title"],
#             "author": poem[0]["author"],
#             "content": poem[0]["content"]
#         }), 200
#     else:
#         return jsonify({"error": {
#             "message": "Poem or author not found.",
#             "type": "NotFoundError",
#             "code": 404,
#         }}), 404


# @blueprint.route('/authors/<author>/<int:quantity>')
# def get_poems_from_author(author, quantity):
#     dict_to_return = {}
#     author = re.compile(f"^{author}", re.IGNORECASE)

#     poems = list(mongo.db.poems.aggregate([
#         {"$match": {"author": author}},
#         {
#             "$sample": {"size": quantity}
#         }
#     ]))

#     for i in range(len(poems)):
#         dict_to_return[i] = {
#             "title": poems[i]["title"],
#             "author": poems[i]["author"],
#             "content": poems[i]["content"]
#         }

#     if dict_to_return:
#         return jsonify(dict_to_return), 200
#     else:
#         return jsonify({"error": {
#             "message": "Poem or author not found.",
#             "type": "NotFoundError",
#             "code": 404,
#         }}), 404


# @api.route('/authors/<author>')
# @api.doc(params={'author': 'an author'})
# class Author(Resource):
#     def get(self, author):
#         return 202
