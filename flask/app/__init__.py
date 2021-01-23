from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

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

    from app.index.index_resource import Index, Health
    from app.posts.posts_resource import Posts, Post, PostSlug
    from app.user.user_resource import User, Users, Login, Logout, Register

    api.add_resource(Index, "/")
    api.add_resource(Health, "/health")
    api.add_resource(Posts, "/posts", endpoint="posts_ep")
    api.add_resource(Post, "/post/<int:id>", endpoint="post_ep")
    api.add_resource(PostSlug, "/post/s/<slug>", endpoint="post_slug_ep")
    api.add_resource(Users, "/users")
    api.add_resource(User, "/user/<int:id>", endpoint="user_ep")
    api.add_resource(Login, "/login")
    api.add_resource(Logout, "/logout")
    api.add_resource(Register, "/register")
    api.init_app(app)

    with app.app_context():
        from app.blueprints.admin.admin import admin_bp

        app.register_blueprint(admin_bp)

    return app