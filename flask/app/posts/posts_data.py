from flask_restful import fields
from app.user.user_data import user_response

post_response = {
    "title": fields.String,
    "body": fields.String,
    "timestamp": fields.DateTime,
    "author": fields.Nested(user_response),
    # "uri": fields.Url("post_ep"),
}