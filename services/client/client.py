import os
import time
import requests
import logging

COLLECTOR_URL = os.environ['COLLECTOR_URL']
SLEEP = float(os.environ['SLEEP'])

def main():

	while True:
		
		logging.info('Collecting sensor value!')
		resp = requests.get(COLLECTOR_URL + '/collector')
		data = resp.json()
		logging.info(data)

		logging.info('Sleeping for {} seconds...'.format(SLEEP))
		time.sleep(SLEEP)

if __name__ == '__main__':
	main()