import pymongo
from flask import Blueprint, jsonify

random_poem = Blueprint('random_poem', __name__)

@random_poem.route('/random')
def random_poem():
    pass