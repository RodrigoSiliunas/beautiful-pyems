from flask_restx import Model, fields

error_model = Model('Error', {
    'message': fields.String(description="The message that the server will return."),
    'type': fields.String(description="The type of error the server is returning."),
    'code': fields.Integer(description="The HTTP status code that the server is returning.")
})
