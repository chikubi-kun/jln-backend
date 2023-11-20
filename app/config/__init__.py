import os

from dotenv import load_dotenv
from sanic import Sanic


appdir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dotenv = os.path.join(appdir, "config", "development.env")
load_dotenv(dotenv)


def db_conn_string(host, port, user, password, database):
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"


class Config:
    # DB Configs
    DB_HOST = str(os.getenv("DB_HOST"))
    DB_PORT = str(os.getenv("DB_PORT"))
    DB_USER = str(os.getenv("DB_USER"))
    DB_PASS = str(os.getenv("DB_PASS"))
    DB_NAME = str(os.getenv("DB_NAME"))

    DB_URI = db_conn_string(DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME)


def init(app: Sanic) -> None:
    app.update_config(Config)
