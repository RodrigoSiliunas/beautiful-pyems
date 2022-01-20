from flask import Blueprint, jsonify
from ..database import *

blueprint = Blueprint('random', __name__)


@blueprint.route('/')
def get_random_poem():
    poem = list(mongo.db.poems.aggregate([
        {
            "$sample": {"size": 1}
        }
    ]))

    return jsonify({
        "title": poem[0]["title"],
        "author": poem[0]["author"],
        "content": poem[0]["content"]
    }), 200
