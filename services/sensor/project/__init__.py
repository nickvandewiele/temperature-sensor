
import os
from flask import Flask

from project.api.sensor import SensorExt

sensor = SensorExt(test=True)

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    sensor.init_app(app)

    # register blueprints
    from project.api.views import sensor_blueprint
    app.register_blueprint(sensor_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})

    return app
    