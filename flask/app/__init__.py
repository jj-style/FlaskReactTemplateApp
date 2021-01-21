from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():

        from app.index.index import index_bp
        from app.user.user import user_bp
        from app.posts.posts import posts_bp

        app.register_blueprint(index_bp, url_prefix="/")
        app.register_blueprint(user_bp, url_prefix="/user")
        app.register_blueprint(posts_bp, url_prefix="/posts")
    return app


# from app import models
