from flask_restx import Model, fields
from .ErrorModel import error_model

author_not_found_model = Model('AuthorNotFound', {
    'error': fields.Nested(error_model)
})
