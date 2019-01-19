from flask import Flask
from flask_migrate import Migrate
from flask_user import UserManager

from alc import models
from alc.assets import assets


db = models.db
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(config)

    assets.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # available as app.user_manager
    UserManager(app, db, models.User)

    from alc.views import static
    app.register_blueprint(static.bp)

    return app
