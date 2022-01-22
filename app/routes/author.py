
import re
from ..database import *
from flask import Blueprint
from flask_restx import Resource, Namespace
from ..models.poem.PoemModel import model as PoemModel
from ..models.error.ErrorModel import error_model as ErrorModel
from ..models.error.AuthorNotFoundModel import author_not_found_model as AuthorNotFoundModel


blueprint = Blueprint('authors', __name__)
api = Namespace('authors', 'Routes for author requests.')

# Registro dos modelos;
api.add_model('Poem', PoemModel)
api.add_model('Error', ErrorModel)
api.add_model('AuthorNotFound', AuthorNotFoundModel)


@api.route('/<author>', doc={
    'params': {
        'author': 'A name of a poet who is registered in our database.'
    },
    'description': 'A random poem by an author who is previously registered in our database is returned through a GET request at this URL.'
})
class RandomPoemFromAuthor(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(404, 'Request failed. The author was not found in our database. A JSON with the error information was returned.', AuthorNotFoundModel)
    def get(self, author):
        '''Returns a random poem by a given author.'''
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


@api.route('/<author>/<name>', doc={
    'params': {
        'author': 'A name of a poet who is registered in our database.',
        'name': 'A name or abbreviation of the name of a poem by the previously informed author.'
    },
    'description': 'A specific poem by the author is returned if it is in our database.',
})
class GetPoemFromAuthor(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(404, 'Request failed. The author or poem was not found in our database. A JSON with the error information was returned.', AuthorNotFoundModel)
    def get(self, author, name):
        '''Returns a particular poem by the author.'''
        author = re.compile(f"^{author}", re.IGNORECASE)
        name = re.compile(f"^{name}", re.IGNORECASE)

        poem = list(mongo.db.poems.aggregate([
            {
                "$match": {
                    "author": author,
                    "title": name,
                }
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

        return {"error": {
            "message": "Poem or author not found.",
            "type": "NotFoundError",
            "code": 404,
        }}, 404


@api.route('/<author>/<int:quantity>', doc={
    'params': {
        'author': 'A name of a poet who is registered in our database.',
        'quantity': 'Returns a JSON object with an amount determined by the poetry request.'
    },
    'description': 'A specific poem by the author is returned if it is in our database.',
})
class GetPoemsFromAuthor(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(404, 'Request failed. The author or poem was not found in our database. A JSON with the error information was returned.', AuthorNotFoundModel)
    def get(self, author, quantity):
        '''Returns more than one poem when requested.'''
        dict_to_return = {}
        author = re.compile(f"^{author}", re.IGNORECASE)

        poems = list(mongo.db.poems.aggregate([
            {"$match": {"author": author}},
            {
                "$sample": {"size": quantity}
            }
        ]))

        for i in range(len(poems)):
            dict_to_return[i] = {
                "title": poems[i]["title"],
                "author": poems[i]["author"],
                "content": poems[i]["content"]
            }

        if dict_to_return:
            return {dict_to_return}, 200

        return {"error": {
            "message": "Poem or author not found.",
            "type": "NotFoundError",
            "code": 404,
        }}, 404
