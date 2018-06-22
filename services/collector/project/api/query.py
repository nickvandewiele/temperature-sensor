import requests
import json

url = 'http://localhost:5000/sensor'

def poll():

	resp = requests.get(url)
	data = resp.json()

	if data['status'] == 'success':
		return data['value']

	else:
		return 0.


