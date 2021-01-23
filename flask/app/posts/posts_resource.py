from flask_restful import Resource
from flask_login import login_required

from app.models import Post


class Posts(Resource):
    @login_required
    def get(self):
        posts = Post.query.all()
        return [p.to_dict() for p in posts]
