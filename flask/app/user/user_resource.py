from flask import request
from flask import redirect
from flask import url_for
from flask import current_app
from flask_restful import Resource, marshal_with, reqparse

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from sqlalchemy import exc
from app.models import User as UserModel

from app import db
from app import login
from app.user.user_data import user_response, password_t

from datetime import datetime, timedelta
import jwt


@login.request_loader
def load_user(req):
    auth_header = req.headers.get("X-Auth", "")
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
    @marshal_with(user_response)
    def get(self):
        """Returns all users in the database

        Returns:
            List<Dict>: - List containing dictionary each representing a user model
        """
        users = UserModel.query.all()
        return users


class User(Resource):
    @marshal_with(user_response)
    def get(self, id):
        """Get a user by their ID

        Args:
            id (int): unique ID of a user

        Returns:
            Dict: dictionary of user model or 404 if not found
        """
        user = UserModel.query.filter_by(id=id).first_or_404()
        return user


class Register(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "username", type=str, location="json", required=True, nullable=False
        )
        self.reqparse.add_argument(
            "email", type=str, location="json", required=True, nullable=False
        )
        self.reqparse.add_argument(
            "password", type=password_t, location="json", required=True, nullable=False
        )
        super(Register, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        print(args)
        try:
            # add user to database
            user = UserModel(username=args.username, email=args.email)
            user.set_password(args.password)
            db.session.add(user)
            db.session.commit()
            return "signed up", 200
        except exc.IntegrityError:
            # unique contraint violated
            return "Error conflict", 409


class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str, location="json", required=True)
        self.reqparse.add_argument("password", type=str, location="json", required=True)
        self.reqparse.add_argument(
            "remember", type=bool, location="json", default=False
        )
        super(Login, self).__init__()

    def post(self):
        if current_user.is_authenticated:
            print("already logged in")
            return redirect(url_for("api.index"))

        args = self.reqparse.parse_args()

        user = UserModel.query.filter_by(username=args.username).first()
        if user is None or not user.check_password(args.password):
            return "Invalid username or password", 400

        login_user(user, remember=args.remember)
        token = jwt.encode(
            {
                "sub": user.username,
                "iat": datetime.utcnow(),
                "exp": datetime.utcnow() + timedelta(minutes=30),
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS512",
        )
        return {"token": token}


class Logout(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return "not logged in", 400
        logout_user()
        return redirect(url_for("api.index"))
