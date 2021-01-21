from os import environ
from enum import Enum


class SqlDriver(Enum):
    SQLITE = "sqlite"
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"


class SqlAlchemyFactory:
    """Builds connection URI for flask-sqlalchemy
    URI Format: dialect+driver://username:password@host:port/database
    """

    def __init__(self):
        self.driver = environ.get("SQL_DRIVER", "sqlite")
        self.username = environ.get("SQL_USERNAME", "")
        self.password = environ.get("SQL_PASSWORD", "")
        self.host = environ.get("SQL_HOST", "")
        self.port = environ.get("SQL_PORT", "")
        self.db_name = environ.get("SQL_DB_NAME", "app.db")

    def set_driver(self, new_driver: SqlDriver):
        self.driver = new_driver
        return self

    def set_username(self, new_username: str):
        self.username = new_username
        return self

    def set_password(self, new_pwd: str):
        self.password = new_pwd
        return self

    def set_host(self, new_host: str):
        self.host = new_host
        return self

    def set_port(self, new_port: int):
        self.port = new_port
        return self

    def set_db_name(self, new_name: str):
        self.db_name = new_name
        return self

    @property
    def URI(self):
        user_part = f"{self.username}:{self.password}"
        host_part = f"{self.host}:{self.port}"

        user_part = "" if len(user_part) == 1 else user_part
        host_part = "" if len(host_part) == 1 else host_part

        full_user_host = f"{user_part}@{host_part}"
        full_user_host = "" if len(full_user_host) == 1 else full_user_host

        return f"{self.driver}://{full_user_host}/{self.db_name}"
