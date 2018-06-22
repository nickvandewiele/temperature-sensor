import json
import unittest

from project import sensor
from project.tests.base import BaseTestCase

class TestSensorService(BaseTestCase):
    """Tests for the Sensor Service."""

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/sensor/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])
    

    def test_read(self):
        """Ensure read route behaves correctly."""
        
        with self.client:
            response = self.client.get('/sensor')
            data = json.loads(response.data.decode())
            print('data: {}'.format(data))
            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])