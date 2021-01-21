from flask import jsonify
from flask import request
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import current_app

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from sqlalchemy import exc
from app.models import User

from app import db
from app import login

from datetime import datetime, timedelta
import jwt

user_bp = Blueprint("login", __name__)


@login.request_loader
def load_user(request):
    auth_header = request.headers.get("X-Auth", "")
    if auth_header == "":
        return None
    try:
        token = auth_header
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS512"])
        user = User.query.filter_by(username=data["sub"]).first_or_404()
        if user:
            return user
    except jwt.ExpiredSignatureError:
        print("token expired")
        return None
    except (jwt.InvalidTokenError, Exception) as e:
        print("token invalid")
        print(str(e))
        return None
    return None


@user_bp.route("/")
def index():
    return "user home page"


@user_bp.route("/all", methods=["GET"])
def list_users():
    """Returns all users in the database

    Returns:
        List<Dict>: - List containing dictionary each representing a user model
    """
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@user_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    """Get a user by their ID

    Args:
        user_id (int): unique ID of a user

    Returns:
        Dict: dictionary of user model or 404 if not found
    """
    user = User.query.filter_by(id=user_id).first_or_404()
    return jsonify(user.to_dict())


@user_bp.route("register", methods=["POST"])
def signup():
    # parse content from the body
    body = request.get_json()
    username = body.get("username", None)
    email = body.get("email", None)
    password = body.get("password", None)

    # bad request if username, email or password missing
    if not all([username, email, password]):
        return "Missing info", 400

    try:
        # add user to database
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return "signed up", 200
    except exc.IntegrityError:
        # unique contraint violated
        return "Error conflict", 409


@user_bp.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        print("already logged in")
        return redirect(url_for("index.index"))

    # parse content from the body
    body = request.get_json()
    username = body.get("username", None)
    password = body.get("password", None)
    remember_me = body.get("remember", False)

    # bad request if username or password missing
    if not all([username, password]):
        return "Missing info", 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return "Invalid username or password", 400

    login_user(user, remember=remember_me)
    token = jwt.encode(
        {
            "sub": user.username,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS512",
    )
    return jsonify({"token": token})


@user_bp.route("/logout", methods=["GET"])
def logout():
    if not current_user.is_authenticated:
        return "not logged in", 400
    logout_user()
    return redirect(url_for("index.index"))
