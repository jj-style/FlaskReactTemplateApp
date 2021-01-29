# Defines request and responses for marshalling/unmarshalling
from marshmallow import Schema, fields

default_user = {"username": "unknown", "id": 0}


class NewPostRequest(Schema):
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    draft = fields.Bool(required=False)
    created_at = fields.Date(required=False)


class PostResponse(NewPostRequest, Schema):
    id = fields.Int()
    slug = fields.Str()
    author = fields.Nested(
        "UserResponse", default=default_user, only=("id", "username")
    )


class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    posts = fields.Nested("PostResponse", only=("id", "title", "slug"), many=True)


new_post_request = NewPostRequest()
post_response = PostResponse()
posts_response = PostResponse(many=True)
user_response = UserResponse()
users_response = UserResponse(many=True)
