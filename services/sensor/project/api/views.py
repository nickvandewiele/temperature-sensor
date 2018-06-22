from flask import Blueprint, jsonify

from project import sensor

sensor_blueprint = Blueprint('sensor', __name__)


@sensor_blueprint.route('/sensor/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@sensor_blueprint.route('/sensor', methods=['GET'])
def read():

    response_object = {
        'status': 'fail',
        'message': 'Could not read sensor value...'
    }

    try:

        value = sensor.read()
        print('Reading value: {}'.format(value))

        if not value:
            print('value: {}'.format(value))
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'message': 'Sensor value successfully read!',
                'value': value,
            }
            return jsonify(response_object), 200
    except:
        return jsonify(response_object), 404