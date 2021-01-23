from flask import jsonify
from flask import request
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import current_app
from flask_restful import Resource

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from sqlalchemy import exc
from app.models import User as UserModel

from app import db
from app import login

from datetime import datetime, timedelta
import jwt


@login.request_loader
def load_user(request):
    auth_header = request.headers.get("X-Auth", "")
    if auth_header == "":
        return None
    try:
        token = auth_header
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS512"])
        user = UserModel.query.filter_by(username=data["sub"]).first_or_404()
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


class Users(Resource):
    def get(self):
        """Returns all users in the database

        Returns:
            List<Dict>: - List containing dictionary each representing a user model
        """
        users = UserModel.query.all()
        return [u.to_dict() for u in users]


class User(Resource):
    def get(self, user_id):
        """Get a user by their ID

        Args:
            user_id (int): unique ID of a user

        Returns:
            Dict: dictionary of user model or 404 if not found
        """
        user = UserModel.query.filter_by(id=user_id).first_or_404()
        return user.to_dict()


class Register(Resource):
    def post(self):
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


class Login(Resource):
    def post(self):
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

        user = UserModel.query.filter_by(username=username).first()
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


class Logout(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return "not logged in", 400
        logout_user()
        return redirect(url_for("index.index"))
