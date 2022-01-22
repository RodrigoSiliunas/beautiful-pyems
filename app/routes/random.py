from ..database import *
from flask import Blueprint
from flask_restx import Resource, Namespace, cors

from ..models.poem.PoemModel import model as PoemModel
from ..models.error.ErrorModel import error_model as ErrorModel
from ..models.error.AuthorNotFoundModel import author_not_found_model as AuthorNotFoundModel

blueprint = Blueprint('randoms', __name__)
api = Namespace(
    name='randoms', description='Routes to obtain poems by random authors.',
    decorators=[cors.crossdomain(origin="*")])

# Registrando os modelos desse NameSpace;
api.add_model('Poem', PoemModel)
api.add_model('Error', ErrorModel)
api.add_model('AuthorNotFound', AuthorNotFoundModel)


@api.route('/', doc={
    'description': 'A random poem by an author who is previously registered in our database is returned through a GET request at this URL.'
})
class GetRandomPoem(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(503, 'Something is wrong with us. A JSON with information about the request is sent.', AuthorNotFoundModel)
    def get(self):
        '''Returns a random poem by a random author.'''
        try:
            poem = list(mongo.db.poems.aggregate([
                {
                    "$sample": {"size": 1}
                }
            ]))
        except:
            return {
                "error": {
                    "message": "Something have wrong with us.",
                    "type": "ServerError",
                    "code": 503,
                    "retryAfter": "60m"
                }}, 503

        return {
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }, 200


@api.route('/<int:quantity>', doc={
    'params': {
        'quantity': 'Number of poems to be returned.'
    },
    'description': 'A random poem by an author who is previously registered in our database is returned through a GET request at this URL.'
})
class GetRandomPoems(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(503, 'Something is wrong with us. A JSON with information about the request is sent.', AuthorNotFoundModel)
    def get(self, quantity):
        '''Returns several different poems.'''
        try:
            poems = list(mongo.db.poems.aggregate([
                {
                    "$sample": {"size": quantity}
                }
            ]))

            poems_to_return = {}

            for i in range(len(poems)):
                poems_to_return[i] = {
                    "title": poems[i]["title"],
                    "author": poems[i]["author"],
                    "content": poems[i]["content"]
                }
        except:
            return {
                "error": {
                    "message": "Something have wrong with us.",
                    "type": "ServerError",
                    "code": 503,
                    "retryAfter": "60m"
                }}, 503

        return poems_to_return, 200
