from flask import Blueprint, jsonify
from ..database import *

blueprint = Blueprint('random', __name__)


@blueprint.route('/')
def get_random_poem():
    try:
        poem = list(mongo.db.poems.aggregate([
            {
                "$sample": {"size": 1}
            }
        ]))
    except:
        return jsonify({"error": {
            "message": "Something have wrong with us.",
            "type": "ServerError",
            "code": 503,
            "retryAfter": "60m"
        }}), 503
    else:
        return jsonify({
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }), 200


@blueprint.route('/<int:quantity>')
def get_random_poems(quantity):
    try:
        poems = list(mongo.db.poems.aggregate([
            {
                "$sample": {"size": quantity }
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
        return jsonify({"error": {
            "message": "Something have wrong with us.",
            "type": "ServerError",
            "code": 503,
            "retryAfter": "60m"
        }}), 503
    else:
        return jsonify(poems_to_return), 200