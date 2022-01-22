import re
from ..database import *
from flask import Blueprint
from flask_restx import Resource, Namespace

from ..models.poem.PoemModel import model as PoemModel
from ..models.error.ErrorModel import error_model as ErrorModel


blueprint = Blueprint('poems', __name__)
api = Namespace(
    name='poems', description='Route to get poems by name without needing to inform the author.')

# Registro dos modelos;
api.add_model('Poem', PoemModel)
api.add_model('Error', ErrorModel)


@api.route('/poems/<poem>', doc={
    'params': {
        'poem': 'Name of the poem to be returned.'
    },
    'description': 'Returns a poem by name if it is registered in the database.'
})
class GetPoemByName(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(404, 'Request failed. Poem not found.', ErrorModel)
    def gef(self, name):
        '''If exists return a poem by name.'''
        name = re.compile(f"^{name}", re.IGNORECASE)

        try:
            poem = list(mongo.db.poems.aggregate([
                {
                    "$match": {"name": name}
                },
                {
                    "$sample": {"size": 1}
                }
            ]))


            return {
                "title": poem[0]["title"],
                "author": poem[0]["author"],
                "content": poem[0]["content"]
            }, 200
        except:
            return {
                "error": {
                    "message": "Something have wrong with us.",
                    "type": "ServerError",
                    "code": 503,
                    "retryAfter": "60m"
                }}, 503
