
import datetime

from flask import Blueprint, jsonify, current_app
from sqlalchemy import exc

from project import db
from project.api.models import Temperature
from project.api.poll import poll

collector_blueprint = Blueprint('collector', __name__)


@collector_blueprint.route('/collector/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@collector_blueprint.route('/collector', methods=['GET'])
def collect():
    current_app.logger.info('Hello from the /collector route!')

    response_object = {
        'status': 'fail',
        'message': 'Could not read collector value...'
    }

    try:       
        current_app.logger.info('Polling the sensor...')
        value = poll()
        current_app.logger.info('Collected value is: {}'.format(value))
        db.session.add(Temperature(UTCDateTime = datetime.datetime.utcnow(), value = value))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully collected sensor value!'
        }
        return jsonify(response_object), 200

    except (exc.IntegrityError, ValueError) as e:
        db.session.rollback()
        return jsonify(response_object), 400