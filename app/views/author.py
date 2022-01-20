import re
from flask import Blueprint, jsonify
from ..database import *

blueprint = Blueprint('authors', __name__)


@blueprint.route('/authors/<author>')
def get_random_poem_from_author(author):
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
        return jsonify({
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }), 200
    else:
        return jsonify({"error": {
            "message": "Author not found.",
            "type": "NotFoundError",
            "code": 404,
        }}), 404


@blueprint.route('/authors/<author>/<int:quantity>')
def get_poems_from_author(author, quantity):
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
        return jsonify(dict_to_return), 200
    else:
        return jsonify({"error": {
            "message": "Poem or author not found.",
            "type": "NotFoundError",
            "code": 404,
        }}), 404


@blueprint.route('/authors/<author>/<name>')
def get_poem_from_author(author, name):
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
        return jsonify({
            "title": poem[0]["title"],
            "author": poem[0]["author"],
            "content": poem[0]["content"]
        }), 200
    else:
        return jsonify({"error": {
            "message": "Poem or author not found.",
            "type": "NotFoundError",
            "code": 404,
        }}), 404
