from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

from app.index.index_resource import Index, Health
from app.posts.posts_resource import Posts
from app.user.user_resource import User, Users, Login, Logout, Register

api = Api()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(
        app,
        resources={r"/*": {"origins": r".*"}},
        allow_headers=["Content-Type", "X-Auth"],
    )
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    api.add_resource(Index, "/")
    api.add_resource(Health, "/health")
    api.add_resource(Posts, "/posts")
    api.add_resource(Users, "/users")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(Login, "/login")
    api.add_resource(Logout, "/logout")
    api.add_resource(Register, "/register")
    api.init_app(app)

    return app