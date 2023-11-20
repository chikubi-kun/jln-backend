import os
from alembic.config import Config

class Migration:
    def __init__(
        self,
        app=None,
        *,
        directory="migrations",
        **kwargs,
    ):
        if app is not None:
            self.init_app(app)
        self.directory = str(directory)

    def init_app(self, app, directory=None):        
        if directory:
            self.directory = str(directory)
            
        config = Config(os.path.join(directory, "alembic.ini"))
        config.set_main_option("script_location", directory)
        config.set_main_option("sqlalchemy.url", app.config.get("DB_URI"))
        