import random
import time

from sensor import initialize, read
from write import write

def main():

	test = False
	initialize(test=test)

	while True:
		# value = random.uniform(0, 1) * 100
		value = read()

		print('Reading a temperature of {} degrees C.'.format(value))

		write(value)
		time.sleep(10.)



if __name__ == '__main__':
	main()