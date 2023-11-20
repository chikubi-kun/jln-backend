from .factory import Database
from .factory import Migration

db = Database()
migrate = Migration()

def init(app):
    db.init_app(app)
    migrate.init_app(app, directory=app.config.get("DB_MIGRATIONS_DIR"))
