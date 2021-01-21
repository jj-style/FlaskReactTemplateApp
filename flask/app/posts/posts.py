from flask import Blueprint
from flask import jsonify
from app.models import Post

from flask_login import login_required

posts_bp = Blueprint("posts", __name__)


@posts_bp.route("/all", methods=["GET"])
@login_required
def listPosts():
    users = Post.query.all()
    return jsonify([u.to_dict() for u in users])
