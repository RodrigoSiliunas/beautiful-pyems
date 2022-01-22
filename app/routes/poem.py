import re
from ..database import *
from flask import Blueprint
from flask_restx import Resource, Namespace, cors

from ..models.poem.PoemModel import model as PoemModel
from ..models.error.ErrorModel import error_model as ErrorModel


blueprint = Blueprint('poems', __name__)
api = Namespace(
    name='poems', description='Route to get poems by name without needing to inform the author.',
    decorators=[cors.crossdomain(origin="*")])

# Registro dos modelos;
api.add_model('Poem', PoemModel)
api.add_model('Error', ErrorModel)


@api.route('/<title>', doc={
    'params': {
        'title': 'Title of the poem to be returned.'
    },
    'description': 'Returns a poem by name if it is registered in the database.'
})
class GetPoemByName(Resource):
    @api.response(200, 'Success. Your request was accepted and a JSON with the format specified below was returned.', PoemModel)
    @api.response(404, 'Request failed. Poem not found.', ErrorModel)
    def get(self, title):
        '''If exists return a poem by name.'''
        name = re.compile(f"^{title}", re.IGNORECASE)

        try:
            poem = list(mongo.db.poems.aggregate([
                {
                    "$match": {"title": name}
                },
                {
                    "$sample": {"size": 1}
                }
            ]))
        except:
            return {
                "error": {
                    "message": "Poem not found.",
                    "type": "NotFoundError",
                    "code": 404
                }}, 404

        return {
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }, 200
