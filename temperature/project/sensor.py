sensor = None


class MockSensor(object):
   """docstring for MockSensor"""
   def __init__(self):
    super(MockSensor, self).__init__()

   def begin(self):
    pass
   def readTempC(self):
    return 25.

def get_real_sensor():
	import Adafruit_MCP9808.MCP9808 as MCP9808

	return MCP9808.MCP9808() 

def initialize(test=True):
	global sensor

	sensor = MockSensor() if test else get_real_sensor()
	sensor.begin()

def read():

	return sensor.readTempC()


