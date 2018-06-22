
class SensorExt(object):

  def __init__(self, app=None, test=True):
      self.app = app
      if app is not None:
          self.init_app(app)

      self.sensor = MockSensor() if test else get_real_sensor()

  def init_app(self, app):
      
      # Use the newstyle teardown_appcontext if it's available,
      # otherwise fall back to the request context
      if hasattr(app, 'teardown_appcontext'):
          app.teardown_appcontext(self.teardown)
      else:
          app.teardown_request(self.teardown)

  def teardown(self, exception):
      pass

  def begin(self):
    self.sensor.begin()

  def read(self):
    return self.sensor.readTempC()

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

