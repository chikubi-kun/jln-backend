from os import getenv

from sanic import Sanic
from strawberry.sanic.views import GraphQLView


def init(app: Sanic) -> None:
    from .schema import auth_schema

    register_graphql_route(app, auth_schema, path="/api/graphql")


def register_graphql_route(app: Sanic, schema, path, auth=True) -> None:
    enable = getenv("FLASK_ENV") == "development"
    skip = enable and getenv("__UNSAFE_SKIP_AUTH__") == "yes"

    handler = GraphQLView.as_view(schema=schema, graphql_ide=True)

    if auth and not skip:
        pass

    app.add_route(handler, path)
