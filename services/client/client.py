import requests
import time

url = 'http://localhost:5001/collector'

SLEEP = 10.

def main():

	while True:
		
		print('Collecting sensor value!')
		resp = requests.get(url)
		data = resp.json()
		print(data)

		time.sleep(SLEEP)

if __name__ == '__main__':
	main()