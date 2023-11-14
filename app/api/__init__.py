from sanic import Sanic


def init(app: Sanic) -> None:
    from . import gql
    gql.init(app)
