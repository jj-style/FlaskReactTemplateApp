import os
from app.config.sql_alchemy import SqlAlchemyFactory

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    sql_fact = SqlAlchemyFactory()
    sql_fact.set_db_name(os.path.join(basedir, "app.db"))
    SQLALCHEMY_DATABASE_URI = sql_fact.URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True
    SECRET_KEY = "my secret key"
