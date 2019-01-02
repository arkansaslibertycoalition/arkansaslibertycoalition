from flask import Flask

from alc.models import db
from alc.assets import assets


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    assets.init_app(app)
    db.init_app(app)

    from alc.views import static
    app.register_blueprint(static.bp)

    return app
