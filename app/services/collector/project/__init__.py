import logging
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask.logging import default_handler

class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)


# instantiate db
db = SQLAlchemy()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import collector_blueprint
    app.register_blueprint(collector_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    app.logger.setLevel(logging.DEBUG)

    return app
    