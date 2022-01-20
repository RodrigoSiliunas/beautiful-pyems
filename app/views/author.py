from flask import Blueprint, jsonify
from ..database import *

blueprint = Blueprint('authors', __name__)


@blueprint.route('/authors/<author>')
def get_random_poem_from_author(author):
    poem = list(mongo.db.poems.aggregate([
        {
            "$match": {"author": author.title()}
        },
        {
            "$sample": {"size": 1}
        }
    ]))

    if poem:
        return jsonify({
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }), 200
    else:
        return jsonify({"message": "author não encontrado"}), 404


@blueprint.route('/authors/<author>/<name>')
def get_poem_from_author(author, name):
    pass
