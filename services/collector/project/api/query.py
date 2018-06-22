import os
import requests

SENSOR_URL = os.environ['SENSOR_URL']

def poll():

	resp = requests.get(SENSOR_URL + '/sensor')
	data = resp.json()

	if data['status'] == 'success':
		return data['value']

	else:
		return 0.


