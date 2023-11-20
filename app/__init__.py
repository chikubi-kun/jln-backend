from sanic import Sanic


def create_app() -> Sanic:
    from . import api, config, db

    app = Sanic(__name__)

    # Load config
    config.init(app)

    # Load database
    db.init(app)

    # # Load API
    api.init(app)

    return app
