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
    def get(self, post_id):
        post = PostModel.query.filter_by(id=post_id).first_or_404()
        return post
