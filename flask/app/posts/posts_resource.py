from flask_restful import Resource, marshal_with
from flask_login import login_required
from flask import current_app as app
from flask import request

from app.models import Post as PostModel

from app.data import new_post_request


class Posts(Resource):
    @login_required
    def get(self):
        return app.config["POST_MANAGER"].list_posts()


class Post(Resource):
    @login_required
    def get(self, id):
        return app.config["POST_MANAGER"].get_post_by_id(id)

    @login_required
    def put(self):
        data = request.get_json()
        errors = new_post_request.validate(data)
        if errors:
            print(errors)
            return "bad request", 400
        return app.config["POST_MANAGER"].create_post(data)


class PostSlug(Resource):
    @login_required
    def get(self, slug):
        return app.config["POST_MANAGER"].get_post_by_slug(slug)
