from .factory import Database

db = Database()

def init(app):
    db.init_db(app)
