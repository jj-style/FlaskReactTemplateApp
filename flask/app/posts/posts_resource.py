from flask_restful import Resource, marshal_with
from flask_login import login_required

from app.models import Post as PostModel

from app.posts.posts_data import post_response


class Posts(Resource):
    @marshal_with(post_response)
    @login_required
    def get(self):
        posts = PostModel.query.all()
        return posts


class Post(Resource):
    @marshal_with(post_response)
    @login_required
    def get(self, id):
        post = PostModel.query.filter_by(id=id).first_or_404()
        return post


class PostSlug(Resource):
    @marshal_with(post_response)
    @login_required
    def get(self, slug):
        post = PostModel.query.filter_by(slug=slug).first_or_404()
        return post
