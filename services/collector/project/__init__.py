
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instantiate db
db = SQLAlchemy()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    # app_settings = os.getenv('APP_SETTINGS')
    # app.config.from_object(app_settings)
    app.config.from_object('project.config.DevelopmentConfig')

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import collector_blueprint
    app.register_blueprint(collector_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    return app
    