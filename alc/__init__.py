from flask import Flask

from alc.models import db
from alc.models import migrate
from alc.assets import assets


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(config)

    assets.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from alc.views import static
    app.register_blueprint(static.bp)

    return app
