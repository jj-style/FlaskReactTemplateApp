from .post_manager import PostManager
from flask_login import current_user
from app.models import Post as PostModel
from app import db
from app.data import post_response, posts_response, new_post_request


class SQLPostManager(PostManager):
    def list_posts(self):
        posts = PostModel.query.all()
        return posts_response.dump(posts)

    def get_post_by_id(self, id):
        post = PostModel.query.filter_by(id=id).first_or_404()
        return post_response.dump(post), 200

    def create_post(self, req):
        post_req = new_post_request.load(req)
        post = PostModel(
            title=post_req["title"], body=post_req["body"], user=current_user
        )
        db.session.add(post)
        db.session.commit()
        return post_response.dump(post), 201

    def get_post_by_slug(self, slug: str):
        post = PostModel.query.filter_by(slug=slug).first_or_404()
        return post_response.dump(post), 200
