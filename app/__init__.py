from sanic import Sanic


def create_app() -> Sanic:
    from . import api

    app = Sanic(__name__)

    api.init(app)

    return app
