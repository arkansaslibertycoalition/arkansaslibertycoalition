import flask_assets

assets = flask_assets.Environment()

assets.register(
    'site_css',
    flask_assets.Bundle(

    ),
)
