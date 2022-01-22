from flask_restx import Model, fields

model = Model('Poem', {
    'title': fields.String(description="The title of poems."),
    'author': fields.String(description="The name of author of poem."),
    'content': fields.String(description="The poem.")
})
